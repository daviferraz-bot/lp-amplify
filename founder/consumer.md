# Painel de consumidores: LP Amplify

Dois painéis rápidos com os **mesmos 20 donos de negócio simulados** (seed 7). Só muda o preço da mensagem: R$ 997 em `panel/` e R$ 397 em `panel-397/`. O perfil do cliente (`customer.json`) é uma estimativa a partir do briefing e das reclamações em `competitors.md`, sem dados reais. A mensagem testada está em `pitch-997.md` e `pitch-397.md`.

## Resultado

| Preço na mensagem | Compram | Não compram |
| --- | ---: | ---: |
| R$ 997 | 0 | 20 |
| R$ 397 | 0 | 20 |

**Baixar o preço não mudou nada.** Nos dois painéis, ninguém recusou principalmente pelo preço (só 1 dos 20 no painel de R$ 997). Os motivos foram outros:

| Motivo | R$ 997 | R$ 397 |
| --- | ---: | ---: |
| Confiança (número desconhecido, parece golpe, já se queimou) | 11 | 11 |
| Necessidade (Instagram, Google e indicação já resolvem) | 8 | 9 |
| Preço | 1 | 0 |

## Por que recusam, nas palavras deles (simuladas)

- **Confiança:** "Número que eu não conheço, dizendo que já fez um site pra mim sem eu pedir e querendo reunião? Isso tem cara de golpe, apago igual apago as outras." (P004, R$ 997)
- **Necessidade:** "Meu Instagram já faz o papel de site e os clientes novos chegam por indicação e pelo Google Maps." (P001, R$ 997)
- **O que vem depois:** quase todos perguntaram quem paga domínio e hospedagem e quem faz alterações. Para eles, o silêncio da mensagem sobre isso soa como mensalidade escondida.
- **Reunião:** vários não querem parar o trabalho para uma reunião de 15 minutos com um desconhecido.

## O que viraria um "não" (repetido em quase todas as respostas)

1. **Prova local:** alguém do mesmo ramo e da mesma região que ganhou clientes com a página, de preferência alguém que eles conheçam.
2. **Ver a página pronta direto no WhatsApp, sem reunião.**
3. **Tudo por escrito:** domínio e hospedagem do primeiro ano e algumas alterações incluídos, sem mensalidade surpresa.
4. **Pagar só depois:** depois de publicada, ou metade depois, ou depois de ver resultado.
5. **Saber quem é o vendedor:** CNPJ, Instagram com clientes reais.

## Respostas de preço

| Pergunta | Mediana (viu R$ 997) | Mediana (viu R$ 397) |
| --- | ---: | ---: |
| Barato demais para ser bom | R$ 100 | R$ 80 |
| Uma pechincha | R$ 250 | R$ 150 |
| Começa a ficar caro | R$ 500 | R$ 325 |
| Caro demais, não compra | R$ 800 | R$ 550 |

As respostas caíram quando o preço mostrado caiu. É efeito de âncora: o preço que aparece na mensagem puxa o que o comprador acha justo, e modelos de linguagem exageram esse efeito. Leia esses números como uma faixa aproximada (algo entre R$ 300 e R$ 800 para uma página avulsa), não como um preço exato. O `/founder-pricing` faz a conta completa.

## Limites

São compradores simulados, não clientes. Servem para achar objeções e frases que você não tinha pensado, e erram ao prever a taxa real de conversão: tendem a concordar demais, então leia a taxa de compra como um teto. Aqui o teto foi 0%, o que é um sinal forte contra a mensagem atual. 20 compradores por painel é pouco, e por isso todos os segmentos aparecem como "thin". Nada disso substitui mandar a mensagem para donos de verdade, e as falas acima não podem ser usadas como depoimento.

## O que mudar antes de gastar tempo

O problema não é o preço, é a abordagem. Antes de mandar uma mensagem de verdade, refaça a oferta para responder às objeções de confiança e de "o que vem depois": link da página pronta sem reunião, tudo incluso por escrito, pagar só se aprovar e um primeiro caso real no nicho. Isso é trabalho do `/founder-offer`, que reescreve a oferta e testa de novo num painel rápido.
