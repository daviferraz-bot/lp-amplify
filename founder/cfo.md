# CFO: social media para médicos

**Leia assim:** a ferramenta escreve `$`, mas os valores são em R$. "A day" significa clientes ativos no mês (a unidade é cliente-mês). Os custos são estimativas (veja `cfo-sources.md`). O **lucro aqui é antes de pagar a própria social media**: é a renda dela.

- **Margem:** cada cliente do plano Completo (R$ 2.200) deixa cerca de R$ 2.023 depois de imposto e ferramentas (92%). Com 8 clientes, a margem é de 88% e o faturamento de R$ 17.600/mês.
- **Ano 1:** cerca de R$ 107 mil de lucro antes da remuneração dela, com a rampa de 0 a 8 clientes em 11 meses. O caixa inicial é pequeno (cerca de R$ 1.850).
- **O número que mais pesa é a rampa, não o custo.** O painel mostrou 0% de compra direta do mensal; a rampa supõe que **1 em cada 3 médicos que compram a entrada vira mensal** (estimativa a confirmar). Com volume 20% menor, o lucro do ano cai para cerca de R$ 84 mil.
- **O limite é o tempo.** 40 h/semana dão cerca de 170 h/mês. Com 15 h por cliente Completo e uns 30% do tempo para prospectar, cabem **cerca de 8 clientes**. Mais que isso exige baixar as horas por cliente (IA, modelos) ou contratar.
- **Três formas de melhorar:**
  1. Preço do Completo a R$ 2.500: margem de 90% (ferramenta, `--price 2500`).
  2. Reduzir de 15 h para 10 h por cliente com o fluxo de IA do sócio: a capacidade sobe de 8 para cerca de 12 clientes.
  3. Vender a entrada (R$ 497) com frequência: ela não está na conta acima e é receita extra que paga a prospecção.
- **Condições do conselho:** a margem está ok; o que falta provar é a conversão (casos e funil medido).

Não é aconselhamento contábil: um contador deve confirmar o regime tributário (Simples Nacional, Anexo III ou V conforme o fator R) e a alíquota real.

# Unit economics: Social media para médicos (gestão mensal de Instagram)

Every number below comes from the input file. Nothing is looked up or guessed.

## One cliente-mês

| line | per cliente-mês |
| --- | ---: |
| Price | $2,200.00 |
| Imposto sobre a nota (Simples Nacional, estimativa 6%) | -$132.00 |
| Taxa de cobrança (boleto/Pix recorrente, estimativa) | -$5.00 |
| Banco de imagens e ferramentas por cliente (estimativa) | -$40.00 |
| **Contribution** (what each cliente-mês leaves to pay the fixed costs) | **$2,023.00** (92%) |

## The margin that matters

Fixed costs: $650 a month (Ferramentas: Canva, agendador, IA, edição de vídeo (estimativa) $350, Contador (estimativa) $300).

- **Break-even: 1 cliente-mêss a day.** Below that you lose money every month.
- **Profit margin at your plan** (8 a day): **88%** of every sale, after every cost.
- Capacity: 8 a day.

## Year 1, month by month

| month | cliente-mêss a day | revenue | profit | cumulative (after $1,200 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$650 | -$1,850 |
| 2 | 1 | $2,200 | $1,373 | -$477 |
| 3 | 2 | $4,400 | $3,396 | $2,919 |
| 4 | 3 | $6,600 | $5,419 | $8,338 |
| 5 | 4 | $8,800 | $7,442 | $15,780 |
| 6 | 5 | $11,000 | $9,465 | $25,245 |
| 7 | 6 | $13,200 | $11,488 | $36,733 |
| 8 | 6 | $13,200 | $11,488 | $48,221 |
| 9 | 7 | $15,400 | $13,511 | $61,732 |
| 10 | 7 | $15,400 | $13,511 | $75,243 |
| 11 | 8 | $17,600 | $15,534 | $90,777 |
| 12 | 8 | $17,600 | $15,534 | $106,311 |

- **Year 1 operating profit: $107,511** on $125,400 of revenue.
- After the $1,200 startup spend: $106,311.
- Startup money earned back: month 3.
- Cash you need before it pays for itself: **$1,850**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 88% | 1 | $107,511 |
| Price -10% | 87% | 1 | $94,971 |
| Volume -20% | 87% | 1 | $84,449 |
| Unit costs +15% | 87% | 1 | $105,998 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
