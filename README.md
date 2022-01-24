projeto api rest ordenacaoAPICross

libs requests e Flask
# ordenaçãoapicross
>receber dados de uma api REST ordenar os dados e retornar atraves de uma API REST



um projeto simples em Python que recebe dados de uma api, le todas as paginas disponiveis, ordena os dados através do Quick Sort e os retorna.


## Instalação

projeto utilizando a biblioteca Flask
no terminal execute:
python main.py
no navegador acesse:
http://127.0.0.1:5000/

no terminal ele informará as paginas que estão sendo consultadas e quando começãr a ordenação

## Exemplo de uso

apenas rode o projeto e acesse a pagina no localhost, ele informara no terminal os passos que estão sendo dados, apos ler todas as paginas disponibilizadas ele ordenara os dados e retornará um JSON com todos os dados ordenados.
Caso aja falha na requisição ele esperará 3 segundos e tentará novamente, executara este passo por 3 vezes, o programa irá parar de tentar buscar novas páginas quando receber um conjunto de dados vazios.

