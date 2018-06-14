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

### 4. Descrição dos métodos
- O Graph Cut, método mais complicado do trabalho, se baseia em utilizar o algoritmo de Max-flow de maneira modificada, de forma a ter dois vértices que são tanto fontes como terminais. A partir desses, inicia-se em ambos uma BFS, cujo destino inicial de um é o outro e vice e versa. No momento em que os caminhos percorridos se cruzam, o algoritmo termina esse processo de busca e passa ao estágio de expansão. Nessa parte do algoritimo, as arestas com o mesmo fluxo que o fluxo máximo são saturadas e seus vértices, agora não mais conectados as fontes orginais, tornam-se novas árvores, originando uma floresta, que dará continuidade à segmentação das diferentes regiões da imagem.
 
- O MST (minimal spanning tree) nada mais faz do que criar um vértice virtual fora da imagem e ligá-lo a vértices do grafo que são encontrados a partir de alguma seed, que em nosso caso, será um input do usuáŕio. As arestas recebem um peso baseado na distância de sua cor e da textura dos pixels ao redor em relação ao pixel da iteração atual. Depois disso, aplicamos o algoritmo de Prim de forma intercalada entre os dois vértices escolhidos, o que consolida uma competição entre as duas MSTs. Assim, ao final teremos duas regiões separadas no grafo, e mantemos a que o usuário escolheu de início.
 
- A equalizaçao de histograma acontece usando o histograma acumulado como função de transferência para equalizar a própria imagem.


