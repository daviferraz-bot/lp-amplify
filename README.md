# LP Amplify — Vitrine Creators (Amplify + Manual)

Réplica em HTML/CSS estático da landing page "20260128 Vitrine Creators | Manual"
(originalmente um export de website do Canva). Todo o layout foi reconstruído a
partir dos dados de design do export: posições, tipografia, cores e o mockup de
iPhone em SVG.

## Estrutura

- `index.html` — página completa, auto-contida (um único arquivo).
- Fontes carregadas via Google Fonts: **Poppins** (nomes e labels), **Inter**
  ("top creators") e **Playfair Display** itálico ("Amplify").
- Layout em canvas de 1366×768 por seção, escalado proporcionalmente ao
  viewport via `--u: calc(100vw / 1366)` — mesmo comportamento do site do Canva.

## Mídia (vídeos e imagens)

Os vídeos dos creators e as imagens de marca d'água referenciam os caminhos
originais do export do Canva (`_assets/video/*.mp4`, `_assets/media/*.png`).
Para os vídeos tocarem, copie a pasta `_assets/` do export original para a
raiz deste projeto. Sem os assets, a página degrada graciosamente: as telas
dos celulares ficam escuras e as marcas d'água/posters são ocultados.

## Seções

1. Hero — "top creators / Amplify"
2. Jota Matiotti · 3. Joab Andrade · 4. Állan Braga · 5. Arthur Nunes ·
6. Eduardo Antenum · 7. Luiz Danyel · 8. Tiago Rocha · 9. Lucas Maroquides ·
10. Cleon Rodrigues

Cada seção tem 3 mockups de iPhone (com vídeo em autoplay/mudo/loop quando
visível) e o nome do creator, alternando lado esquerdo/direito.
