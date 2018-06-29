# stickerFactory

## Dupla:
João Pedro Rodrigues Mattos - 10295732
Gustavo Sasaki Roncaglia - 10295652

## Tema do projeto: Segmentação de imagens
### Descrição:
Nosso trabalho consiste na implementação de dois métodos diferentes de segmentação de imagens (GrabCut e MST segmentation) para comparação da sua eficácia na tarefa de auxílio de criação de stickers para Telegram. 

### Como usar
Ao executar o script "main.py", o usuário deverá fornecer o diretório da imagem como *input* e escolher o método de segmentação desejado entre as opções "Automatic Segmentation" (MST Segmentation) e "Semi-automatic Segmentation" (Grab Cut).

#### Automatic Segmentation
O usuario deve escolher as duas seeds a partir dos pixels da imagem selecionada. Um deles (Foreground) será mantido em cena, enquanto o outro (Background), será segmentado. Depois de selecionados os pontos de partida, o algoritmo MST Segmentation se iniciará e o resultado será uma imagem segmentada. 

#### Semi-automatic Segmentation
O usuário deve, inicialmente, utilizar a ferramenta "Rectangle" para selecinonar toda a região da imagem em que o objeto desejado se encontra. Depois de clicar em "Save", o resultado da segmentação da primeira iteração do algoritmo Grab Cut será exibido.


### Implementação

A implementação do trabalho se apoiou no uso de bibliotecas e de código open source, tanto para a interface homem-computador, quanto na realização dos métodos de processamento de imagens propriamente ditos. Para a interface gráfica, utilizamos Tkinter e, nas conversões e implementação do algoritmo Grab Cut, foi utilizada a biblioteca Open CV.

### Metodos

#### Grab Cut 
Depois de clicar em "Save", é executado o método de segmentação *Grab Cut*, que consiste em várias iterações de um algoritmo de *Max Flow* junto a um Modelo de Mistura Gaussiano para escolher a *sink* e a *source* da imagem, agora modelada como um grafo. As arestas da representação em questão possuem um peso equivalente ao de uma função de similaridade, que leva em consideração a distância entre pixels em relação às suas respectivas cores, posições e vizinhos. Posteriormente a este procedimento, um *Min Cut* é realizado na representação de grafo da imagem e a *source*, junto a todos os pixels aos quais se encontra ligada, será o *foreground* (parte da imagem a ser conservada) e a *sink* junto a seus pixels, será o *background*.

#### MST Segmentation
Depois de clicar em "Save", a imagem é modelada como um grafo conexo e, numa matriz, processamos previmente os pesos das arestas, que correspondem às diferenças acumuladas entre os três canais do espaço de cor HSV. Dessa forma, mesmo que pixels adjacentes possuam cores muito diferentes, eles ainda receberão uma aresta de peso menor, devido ao fato de estarem mais próximos uns dos outros, conservando assim, as propriedades espaciais da imagem. Por fim,a MST terá dois galhos e será considerado *foreground* aquele que for oriundo da seed selecionada como tal pelo usuário.

### Resultados e discussão
Apesar do longo tempo de execução necessário para apresentar resultados, ambos os métodos são funcionais e apresentam resultados satisfatórios, haja vista a complexidade de se segmentar uma imagem de forma semi-automática partindo de informações básicas inseridas pelo usuário. De qualquer forma, em nossos testes a segmentação se mostrou, muitas vezes, pouco utilizável sem o auxílio do usuário e de métodos mais complexos de detecção de objeto e bordas. 


### Imagens resultados
- [Imagem teste](https://imgur.com/a/zt1bC0N)
- [Resultado do Grab Cut](https://imgur.com/a/PVQngos)
- [Resultado do MST Segmentation](https://imgur.com/a/EWAr3PL) 

### Observações
Tivemos problemas com a implementação do MST. Apesar de seu conceito ter ficado claro, devido ao prazo de entrega, não conseguimos deixar o método tão funcional quanto o proposto inicialmente.


