# Building Fast Queries on a CSV

## Sobre o projeto:
  O projeto é baseado no [Guided Project: Building Fast Queries on a CSV](https://app.dataquest.io/c/86/m/481/guided-project%3A-building-fast-queries-on-a-csv) da plataforma [dataquest](https://app.dataquest.io/). O projeto tem o objetivo de mostrar e comparar a eficiência de algoritmos de diferentes complexidades para realizar buscas em arquivos CSV, evidenciando qual é a melhor implementação para se ter uma busca rápida, ou seja, qual algoritmo possui complexidade ótima. Esse projeto utiliza o dataset [The Reddit Climate Change Dataset](https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset)
  
## Descrição do projeto:
  ### A classe Clima possui três funcionalidades principais:
   - **Dado um id de uma mensagem no Reddit, retornar todas as informações sobre a mensagem:** Para essa funcionalidade foram implementadas duas funções, ``` get_message_from_id(self, id)``` e ```get_message_from_id_fast(self, id)```. Para primeira função é realizado uma busca percorrendo todo o dataset e comparando o id passado como argumento com o id da variável de iteração a cada iteração, esse algoritmo apresenta complexidade linear. Para segunda função é utlizado um dicionário, ```key: id``` e ```value: mensagem```, para executar a busca utiliza-se o operador ```in```  para verificar se o id passado como argumento está contido no dicionário, esse algoritmo possui complexidade constante.
   - **Dado um limite inferior e superior da coluna "sentiment", retornar todas as mensagens com valores de sentimento entre os limites inferior e superior:** Para essa funcionalidade foi implementada uma função ```get_by_sentiment(self, sentiment_inf, sentiment_sup)```. Para determinar se a mensagem está dentro dos limites passados como argumento, a função percorre o dataset e verifica se a variável de iteração está dentro do intervalo. Esse algoritmo apresenta complexidade linear.
   - **Dado um valor de parâmetro, retornar duas mensagens cuja soma do valor da coluna "score" é igual ao parâmetro. Retornar -1 se não existir:** Para essa funcionalidade foram implementadas duas funções, ```TwoScoreSum(self, target)``` e ```TwoScoreSum_fast(self, target)```. Para primeira função foram utilizados dois laços de repitação para percorrer o dataset ao mesmo tempo e obter-se os valores a serem comparados. Esse algoritmo apresenta complexidade quadrática. Para segunda função temos uma implentação utilizando dicionários, implementação semelhante ao problema do TwoNumberSum, dado um alvo e o resultado da subtração entre o alvo e o atual valor da variável de iteração estiver contido no dicionário, o valor da subtração e o valor atual da variável de iteração, são os números que resultam na soma do alvo. Esse algoritmo possui complexidade linear.   
   

 ## Como executar:
  Com o arquivo ```Clima.py``` na pasta do projeto execute:
  ```python
  from Clima import Clima
  ```
  Exemplo de utilização dos métodos da classe Clima: [Project](https://github.com/ClaudianoLeonardo/Building_Fast_Queries_on_a_CSV/blob/main/Project.ipynb)
## Discentes participantes do projeto:
  
  [Claudiano Leonardo da Silva](https://github.com/ClaudianoLeonardo)
  
  [David Willian Pereira Jatobá](https://github.com/DavidWillian7)

## Referências:
  
  [datastructure](https://github.com/ivanovitchm/datastructure)
  
  [dataquest](https://app.dataquest.io/)
  
  [Kaggle](https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset)
  
