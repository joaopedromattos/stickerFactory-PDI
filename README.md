# stickerFactory-PDI
### Integrantes do grupo 
- João Pedro Rodrigues Mattos - 10295732 
- Gustavo Sasaki Roncaglia - 10295652

### 1. Contextualização
Fazer "adesivos virtuais" (stickers) a partir de fotografias para o aplicativo móvel de mensagens Telegram é uma tarefa complicada e demorada, nosso projeto para a disciplina de Processamento de Imagens visa a facilitar este processo. Para tal, serão utilizadas imagens coloridas ou não, cujo formato pode ou não ser o PNG.

### 2. Objetivo 
Utilizar das técnicas de compressão, ajuste de imagens coloridas com equalização de histograma e segmentação de imagens para automatizar e facilitar o processo de criação de stickers no Telegram em conjunto com a API oficial do aplicativo, de forma que, ao fim da execução do programa, obtenha-se um sticker pronto para uso na rede social. 

### 3. Etapas
- Selecao do método (Semi-automático/graph-cut ou Automático/MST Image Segmentation);
- Indicação do objeto principal da cena utilizando uma interface gráfica
- Pré-segmentação das imagens usando a técnica "Graph cuts";
- Ajuste de partes da imagem a serem removidas pelo usuário a partir de uma interface gráfica; 
- No caso de ter sido escolhida a opcao automática, a segmentação será dada pelo algoritmo de MST utilizando seeds do usuário; 
- Compressão da imagem já segmentada;
- Equalização de histogramas + ajuste de gamma;
- Correção do formato atual para o formato PNG; 
- Upload da imagem para o bot de stickers do Telegram.
