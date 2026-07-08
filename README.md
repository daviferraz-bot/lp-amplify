# LP Turbo Partners — Vitrine Creators (Turbo Partners + Manual)

Landing page em HTML/CSS estático baseada no layout "Vitrine Creators"
(originalmente um export de website do Canva). O layout foi reconstruído a
partir dos dados de design do export: posições, tipografia, cores e o mockup
de iPhone em SVG.

## Estrutura

- `index.html` — página completa, auto-contida (um único arquivo).
- Logo da Turbo (PNG branco no CDN) centralizada no topo do hero, acima do
  título — em destaque e próxima do texto.
- Tipografia da marca: **Neue Kaine** (variável, local em `fonts/`) para
  títulos e nomes dos creators, e **Plus Jakarta Sans** (Google Fonts) para
  labels e textos — como no logo "Turbo partners".
- Paleta da marca: Dark `#0B0726` (fundo da página), Ice `#F7F9F9` (texto),
  Green `#37D3A4` (acentos), Blu `#415FF2` (acento de marca),
  Black `#03020A` (telas dos celulares) e
  Black `#03020A`/Gray 500 `#9398A1` (rodapé).
- Layout em canvas de 1366×768 por seção, escalado proporcionalmente ao
  viewport via `--u: calc(100vw / 1366)` — mesmo comportamento do site do Canva.

## Mídia (vídeos e posters)

Os creators com vídeo já enviado referenciam URLs remotas (CDN da Shopify)
direto na tag `<video>` — nada de vídeo é versionado no repositório. Já têm
vídeo (3 cada, na ordem esquerda → centro → direita): **Alan Melo**,
**Luckyan Bessa**, **Arthur Zon**, **Lucas Y Paz**, **Diogo Brandão**,
**Alexandre Soranz**, **Gustavo Mazzei**, **Stephan Orlandi** e **Lucas Santos**
— todos os creators da página.

Para adicionar/trocar vídeos, edite o dicionário `VIDEO_URLS` no gerador
(scratchpad `gen.py`) ou diretamente os `src` das tags `<video>` no
`index.html`. Vídeos remotos usam `#t=0.1` no `src` para o navegador exibir o
primeiro frame como poster. Todos tocam em autoplay/mudo/loop quando visíveis.

### Mini-player em cada mockup

Cada iPhone tem controles próprios, que aparecem ao passar o mouse (desktop)
ou tocar na tela (mobile):

- **Play/pause** e barra de progresso arrastável (seek) com tempo em `mm:ss`.
- **Voltar 10s** e **avançar 10s**.
- **Som on/off** — ativar o som de um vídeo silencia automaticamente os demais
  (áudio exclusivo).

Pausar manualmente um vídeo impede que ele volte a tocar sozinho ao rolar a
página (respeita a intenção do usuário).


## Seções

1. Hero — "top creators / Turbo Partners"
2. Alan Melo · 3. Luckyan Bessa · 4. Arthur Zon · 5. Lucas Y Paz ·
6. Diogo Brandão · 7. Alexandre Soranz · 8. Gustavo Mazzei ·
9. Stephan Orlandi · 10. Lucas Santos

O lado (esquerda/direita) de cada nome é calculado por índice, alternando
automaticamente — inserir/remover creators mantém o zigue-zague.

Cada seção tem 3 mockups de iPhone e o nome do creator, alternando lado
esquerdo/direito.
