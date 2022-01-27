## Fluxo de trabalho em repositórios no Github

- Todo conteúdo elaborado pela DTA deverá, preferencialmente, ser incluído em repositório público em uma das seguintes organizações:
    - [Transparência MG](https://github.com/transparencia-mg/); e
    - [Dados MG](https://github.com/dados-mg).

- O fluxo de trabalho deve ser documentado nos repositórios utilizando-se de issues, commits, pull requests e conexões entre eles.

- O fluxo de trabalho inicia-se com a abertura de um issue. Neste deverão ser incluídos, além do escopo do trabalho a ser desenvolvido, as principais decisões e material de referência para definição/concepção do trabalho a ser realizado.

- O nome da branch deverá conter o número do issue e uma descrição mais resumida possível do trabalho que será elaborado. Exemplo:
    - 42/fix-bug

- A mensagem de cada commit deverá, sempre que possível, referenciar o issue correspondente. Exemplo: 
    - See #101

- Essa mensagem padrão (See #issue) faz a conexão entre os commits, que implementam o trabalho, e os issues, que inicializam a demanda.

- O pull request, por sua vez, representa o agrupamento de commits relacionados que serão avaliados durante o processo de revisão por pares.

- Os issues, commits e pull requests devem agrupar um conjunto de alterações logicamente relacionadas como forma de facilitar o processo de revisão.

- Na [mensagem de fechamento do pull pequest](https://docs.github.com/pt/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue) inserir o comentário "close #numero" quando o pull request tiver implementado a demanda presente no issue. Essa mensagem fecha automaticamente o issue mencionado.
