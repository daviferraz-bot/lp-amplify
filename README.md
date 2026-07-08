# LP Turbo Partners — Vitrine Creators (Turbo Partners + Manual)

Landing page em HTML/CSS estático baseada no layout "Vitrine Creators"
(originalmente um export de website do Canva). O layout foi reconstruído a
partir dos dados de design do export: posições, tipografia, cores e o mockup
de iPhone em SVG.

## Estrutura

- `index.html` — página completa, auto-contida (um único arquivo).
- Tipografia da marca: **Neue Kaine** (variável, local em `fonts/`) para
  títulos e nomes dos creators, e **Plus Jakarta Sans** (Google Fonts) para
  labels e textos — como no logo "Turbo partners".
- Paleta da marca: Blu `#415FF2` (fundo), Ice `#F7F9F9` (texto),
  Green `#37D3A4` (acentos), Dark `#0B0726` (telas dos celulares) e
  Black `#03020A`/Gray 500 `#9398A1` (rodapé).
- Layout em canvas de 1366×768 por seção, escalado proporcionalmente ao
  viewport via `--u: calc(100vw / 1366)` — mesmo comportamento do site do Canva.

## Mídia (vídeos e posters)

Os creators com vídeo já enviado referenciam URLs remotas (CDN da Shopify)
direto na tag `<video>` — nada de vídeo é versionado no repositório. Já têm
vídeo: **Alan Melo**, **Luckyan Bessa**, **Diogo Brandão** e **Gustavo Mazzei**
(3 vídeos cada, na ordem esquerda → centro → direita).

Os demais creators (Lucas Y Paz, Alexandre Soranz, Stephan Orlandi, Lucas
Santos, Matheus Pessona) ficam com a tela no placeholder escuro até os vídeos
serem enviados; nesse caso o padrão é `videos/<slug>-N.mp4`.

Para adicionar/trocar vídeos, edite o dicionário `VIDEO_URLS` no gerador
(scratchpad `gen.py`) ou diretamente os `src` das tags `<video>` no
`index.html`. Vídeos remotos usam `#t=0.1` no `src` para o navegador exibir o
primeiro frame como poster. Todos tocam em autoplay/mudo/loop quando visíveis.


## Seções

1. Hero — "top creators / Turbo Partners"
2. Alan Melo · 3. Luckyan Bessa · 4. Lucas Y Paz · 5. Diogo Brandão ·
6. Alexandre Soranz · 7. Gustavo Mazzei · 8. Stephan Orlandi ·
9. Lucas Santos · 10. Matheus Pessona

Cada seção tem 3 mockups de iPhone e o nome do creator, alternando lado
esquerdo/direito.
