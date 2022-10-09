# Building Fast Queries on a CSV

## Sobre o projeto:
  O projeto é baseado no [Guided Project: Building Fast Queries on a CSV](https://app.dataquest.io/c/86/m/481/guided-project%3A-building-fast-queries-on-a-csv) da plataforma [dataquest](https://app.dataquest.io/). O projeto tem o objetivo de mostrar e comparar a eficiência de algoritmos de diferentes complexidades para realizar buscas em arquivos CSV, evidenciando qual é a melhor implementação para se ter uma busca rápida, ou seja, qual algoritmo possui complexidade ótima.
  
## Descrição do projeto:
  ### Esse projeto possui três funcionalidades principais:
   - **Dado um id de uma mensagem no Reddit, retornar todas as informações sobre a mensagem:** Para essa funcionalidade foram implementadas duas funções, ``` get_message_for_id(self, id)``` e ```get_message_for_id_fast(self, id)```. Para primeira função é realizado uma busca percorrendo todo o dataset e comparando o id passado como argumento com o id da variável de iteração a cada iteração, esse algoritmo apresenta complexidade linear. Para segunda função é utlizado um dicionário, ```key: id``` e ```value: mensagem```, para executar a busca utiliza-se o operador ```in```  para verificar se o id passado como argumento está contido no dicionário, esse algoritmo possui complexidade constante.
   - **Dado um limite inferior e superior da coluna "sentiment", retornar todas as mensagens com valores de sentimento entre os limites inferior e superior:** 
   
          
   

  
  
  
  
  Esse projeto utiliza o dataset [The Reddit Climate Change Dataset](https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset)
