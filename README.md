# api_filmes
 Exercício Fazendo Requisições na Web

Com o exercício fui capaz de entender como funciona uma API e requisições web, como podemos usar o Try e Except para tratar possíveis erros e exercitar ainda mais as funções.

Inicialmente foram importadas duas bibliotecas, <b>requests:</b> biblioteca responsável por fazer as requisições web e <b>json:</b> para transformar o texto em dicionário python. (LINHAS 1 e 2)

Posteriormente foram criadas duas funções: requisicao e printar_detalhes.

<b>requisicao:</b> nessa função vamos fazer uma consulta pelo Título do filme direto na API pública www.omdbapi.com, mas antes mesmo vamos tratar possíveis erro como de conexão. Usamos o Try para fazer a requisição e logo depois transformamos o valor em dicionários para uma variável chamada <b>info</b> e retornamos ela mesmo; já o except vai apenas imprimir a string Erro na Conexão. (LINHAS 6 até 13)

<b>printar_detalhes:</b> já na próxima função vamos printar os detalhes do filme, pegando cada chave do dicionário que mais chamar a atenção como: Ano, Nome, Diretor...(LINHAS 17 até 25)

O programa feito com laço while inicia uma <b>variável</b> sair com o valor False. Enquanto sair não for True o programa vai ficar no laço, depois em uma variável <b>"op"</b>, solicita ao usuário o nome do filme ou a string SAIR. (LINHAS 29 até 31).
Se a variável "op" for igual a "SAIR" o programa vai imprimir a string "Saindo..." e a variável "op" recebe o valor True e o program encerra. (LINHAS 33 até 35). 
senão a variável <b>filme</b> vai receber a função requisicao com a variável "op" que o usuário alimentou. (LINHAS 36 e 37).
Temos mais uma tratativa onde se a resposta da API sobre o filme for igual a "False", printar que o filme não foi encontrado, senão printar a função printar_detalhes com a variável filme. (LINHAS 38 a 41).
