# LP Turbo Partners — Vitrine Creators (Turbo Partners + Manual)

Landing page em HTML/CSS estático baseada no layout "Vitrine Creators"
(originalmente um export de website do Canva). O layout foi reconstruído a
partir dos dados de design do export: posições, tipografia, cores e o mockup
de iPhone em SVG.

## Estrutura

- `index.html` — página completa, auto-contida (um único arquivo).
- Fontes carregadas via Google Fonts: **Poppins** (nomes e labels), **Inter**
  ("top creators") e **Playfair Display** itálico ("Turbo Partners").
- Layout em canvas de 1366×768 por seção, escalado proporcionalmente ao
  viewport via `--u: calc(100vw / 1366)` — mesmo comportamento do site do Canva.

## Mídia (vídeos e posters)

Cada celular referencia um vídeo e um poster na pasta `videos/`, com nomes
previsíveis por creator (3 vídeos por seção):

```
videos/<slug>-1.mp4   videos/<slug>-1.jpg
videos/<slug>-2.mp4   videos/<slug>-2.jpg
videos/<slug>-3.mp4   videos/<slug>-3.jpg
```

Slugs: `alan-melo`, `luckyan-bessa`, `lucas-y-paz`, `diogo-brandao`,
`alexandre-soranz`, `gustavo-mazzei`, `stephan-orlandi`, `lucas-santos`,
`matheus-pessona`.

Sem os arquivos, a página degrada graciosamente: as telas dos celulares ficam
escuras e as marcas d'água são ocultadas. Os vídeos tocam em
autoplay/mudo/loop apenas quando visíveis.

## Seções

1. Hero — "top creators / Turbo Partners"
2. Alan Melo · 3. Luckyan Bessa · 4. Lucas Y Paz · 5. Diogo Brandão ·
6. Alexandre Soranz · 7. Gustavo Mazzei · 8. Stephan Orlandi ·
9. Lucas Santos · 10. Matheus Pessona

Cada seção tem 3 mockups de iPhone e o nome do creator, alternando lado
esquerdo/direito.
