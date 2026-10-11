# CFO: social media para médicos (versão da oferta final)

**Como ler:** a ferramenta escreve `$`, mas os valores são em R$. "A day" quer dizer clientes mensais ativos (a unidade é cliente-mês). Os custos são estimativas (`cfo-sources.md`). O **lucro mostrado é antes de pagar a própria social media**: é a renda dela.

- **Mix mensal:** preço médio de R$ 1.700, uma mistura de Essencial (R$ 1.500, cerca de 8 h por cliente) e Completo (R$ 2.200, cerca de 15 h). Com cerca de 10 h por cliente em média e 70% do tempo para entregar, cabem **11 clientes**.
- **Margem:** cada cliente deixa R$ 1.553 (91%). Com 11 clientes, a margem é de 88% e o faturamento de **R$ 18.700/mês**.
- **Ano 1, só mensalidades:** cerca de **R$ 158 mil de lucro** sobre R$ 182 mil de faturamento. A rampa vem da simulação (cenário base): 400 abordagens no mês 1 e cerca de 200 por mês depois.
- **Entradas, que não estão na conta acima:** no cenário base, cerca de R$ 12,6 mil no mês 1 (15 entradas) e cerca de R$ 6 mil por mês depois, com 200 abordagens. Elas pagam a prospecção e alimentam o mensal.
- **O que mais pesa:** a conversão da entrada em mensal (premissa de 1 em 3). Com volume 20% menor, o lucro do ano cai cerca de 20%.
- **O limite é o tempo:** passando de 11 clientes, é preciso reduzir as horas com IA ou contratar uma assistente.
- **Caixa inicial:** cerca de R$ 1.850.

Um contador deve confirmar o regime tributário e a alíquota. Não é aconselhamento contábil.

---
# Unit economics: Social media para médicos (gestão mensal, mix Essencial R$ 1.500 e Completo R$ 2.200)

Every number below comes from the input file. Nothing is looked up or guessed.

## One cliente-mês

| line | per cliente-mês |
| --- | ---: |
| Price | $1,700.00 |
| Imposto sobre a nota (Simples Nacional, estimativa 6%) | -$102.00 |
| Taxa de cobrança (boleto/Pix recorrente, estimativa) | -$5.00 |
| Banco de imagens e ferramentas por cliente (estimativa) | -$40.00 |
| **Contribution** (what each cliente-mês leaves to pay the fixed costs) | **$1,553.00** (91%) |

## The margin that matters

Fixed costs: $650 a month (Ferramentas: Canva, agendador, IA, edição de vídeo (estimativa) $350, Contador (estimativa) $300).

- **Break-even: 1 cliente-mêss a day.** Below that you lose money every month.
- **Profit margin at your plan** (11 a day): **88%** of every sale, after every cost.
- Capacity: 11 a day.

## Year 1, month by month

| month | cliente-mêss a day | revenue | profit | cumulative (after $1,200 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$650 | -$1,850 |
| 2 | 4 | $6,800 | $5,562 | $3,712 |
| 3 | 7 | $11,900 | $10,221 | $13,933 |
| 4 | 9 | $15,300 | $13,327 | $27,260 |
| 5 | 10 | $17,000 | $14,880 | $42,140 |
| 6 | 11 | $18,700 | $16,433 | $58,573 |
| 7 | 11 | $18,700 | $16,433 | $75,006 |
| 8 | 11 | $18,700 | $16,433 | $91,439 |
| 9 | 11 | $18,700 | $16,433 | $107,872 |
| 10 | 11 | $18,700 | $16,433 | $124,305 |
| 11 | 11 | $18,700 | $16,433 | $140,738 |
| 12 | 11 | $18,700 | $16,433 | $157,171 |

- **Year 1 operating profit: $158,371** on $181,900 of revenue.
- After the $1,200 startup spend: $157,171.
- Startup money earned back: month 2.
- Cash you need before it pays for itself: **$1,850**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 88% | 1 | $158,371 |
| Price -10% | 87% | 1 | $140,181 |
| Volume -20% | 87% | 1 | $125,137 |
| Unit costs +15% | 87% | 1 | $156,012 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
