"""Simulação de funil: 400 médicos abordados na Grande Vitória.

Monte Carlo sobre 400 perfis sorteados do mesmo customer.json dos painéis.
Etapas: (1) a mensagem chega a quem decide, (2) responde e aceita o vídeo,
(3) compra a entrada depois de ver o vídeo e a oferta, (4) vira mensal em 30 dias.
As taxas das etapas 1, 2 e 4 são premissas (cenários); a etapa 3 vem do painel
simulado da entrada "paga depois de aprovar", por grupo, com desconto porque
compradores simulados tendem a concordar demais.
"""
import json, os, random, statistics, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("panel", "/root/.claude/skills/founder-consumer/panel.py")
panel = importlib.util.module_from_spec(spec); spec.loader.exec_module(panel)

customer = json.load(open(os.path.join(ROOT, "customer.json")))
doctors = panel.deal(customer, n=400, seed=2026)

# Etapa 3: compra da entrada por grupo (painel-entrada-b), suavizada: (compras+1)/(n+2)
answers = {json.load(open(os.path.join(ROOT, "panel-entrada-b/answers", f)))["id"]: json.load(open(os.path.join(ROOT, "panel-entrada-b/answers", f)))
           for f in os.listdir(os.path.join(ROOT, "panel-entrada-b/answers"))}
cards = {c["id"]: c for c in json.load(open(os.path.join(ROOT, "panel-entrada-b/personas.json")))}
seg_stats = {}
for pid, a in answers.items():
    s = cards[pid]["segment"]
    k, n = seg_stats.get(s, (0, 0))
    seg_stats[s] = (k + int(a["buys"]), n + 1)
seg_buy = {s: (k + 1) / (n + 2) for s, (k, n) in seg_stats.items()}

# Etapas 1 e 2: multiplicadores por comportamento (premissas)
REACH = {"Secretária cuida do Instagram": 0.5}          # metade das secretárias repassa
REPLY_MULT = {"Posta sozinho quando dá": 1.3, "Quer crescer no particular": 1.5,
              "Medo do conselho": 1.3, "Já se decepcionou com agência": 0.6,
              "Agenda cheia": 0.5, "Desconfiado de abordagem comercial": 0.4}
BUY_MULT = {"Agenda cheia": 0.5, "Desconfiado de abordagem comercial": 0.5, "Já se decepcionou com agência": 0.7,
            "Quer crescer no particular": 1.3, "Posta sozinho quando dá": 1.2}

SCENARIOS = {
    #            resposta base, ganho dos follow-ups, desconto do painel, entrada->mensal
    "pessimista": dict(reply=0.05, followup=1.25, deflate=0.30, monthly=0.20),
    "base":       dict(reply=0.09, followup=1.40, deflate=0.50, monthly=0.33),
    "otimista":   dict(reply=0.14, followup=1.50, deflate=0.80, monthly=0.45),
}
MESSAGES = {"A: gancho CFM + portfólio": 1.0, "B: análise genérica": 0.6}

def run(sc, msg_mult, focus=False, runs=4000, rng=random.Random(7)):
    pool = doctors
    if focus:  # só especialidades clínicas e donos de clínica, sem agenda cheia/desconfiados
        pool = [d for d in doctors if ("clínica" in d["segment"]) and d["behaviour"] not in ("Agenda cheia", "Desconfiado de abordagem comercial")]
        pool = (pool * (400 // len(pool) + 1))[:400]
    out = {k: [] for k in ("chega", "responde", "entrada", "mensal", "receita_entrada", "mrr")}
    for _ in range(runs):
        ch = rp = en = me = 0
        for d in pool:
            if rng.random() > REACH.get(d["behaviour"], 0.9): continue
            ch += 1
            p = sc["reply"] * sc["followup"] * msg_mult * REPLY_MULT.get(d["behaviour"], 1.0)
            if rng.random() > min(p, 0.95): continue
            rp += 1
            q = seg_buy[d["segment"]] * sc["deflate"] * BUY_MULT.get(d["behaviour"], 1.0)
            if rng.random() > min(q, 0.95): continue
            en += 1
            if rng.random() < sc["monthly"]: me += 1
        for k, v in zip(out, (ch, rp, en, me, en * 497, me * 1500)):
            out[k].append(v)
    q = lambda xs, p: sorted(xs)[int(p * (len(xs) - 1))]
    return {k: (statistics.mean(v), q(v, 0.1), q(v, 0.9)) for k, v in out.items()}

if __name__ == "__main__":
    print("Compra da entrada por grupo (painel, suavizada):")
    for s, v in seg_buy.items(): print(f"  {v:.0%}  {s.split(';')[0]}")
    for msg, mm in MESSAGES.items():
        for focus in (False, True):
            print(f"\n=== Mensagem {msg} | {'lista focada' if focus else 'lista geral'} ===")
            for name, sc in SCENARIOS.items():
                r = run(sc, mm, focus)
                print(f"{name:10s} " + " | ".join(f"{k} {m:.0f} ({lo}-{hi})" for k, (m, lo, hi) in r.items()))
