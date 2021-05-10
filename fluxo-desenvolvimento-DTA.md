## Fluxo para desenvolvimento DTA

### Premissas
- Todo código desenvolvido pela DTA ou em conjunto com outras unidades (DTI, por exemplo) deverá, preferencialmente, ser incluído em reposítório público em uma das seguintes organizações:
    - [Transparência MG](https://github.com/transparencia-mg/)
    - [Dados MG](https://github.com/dados-mg)
- Todo fluxo de desenvolvimento deverá ser documentado dentro do próprio repositório, utilizando-se para tanto ferramentas como issues e comentários ao longo dos scripts
- Os ciclos de desenvolvimento deverão ser documentados a partir da abertura de um issue. Neste deverão ser incluídos além das funcionalidades a serem desenvolvidas os motivos para a escolha dos mesmos e o histórico para tomada da decisão
    - Para facilitar este processo sugerimos a criação de [issues templates](https://github.com/transparencia-mg/handbook/blob/master/issue-template-desenvolvimento-dta-apps.md) quando da abertura do projeto
- Utilizar estrutura de nomenclatura de branch e commits segundo [repositório github](https://github.com/gabrielbdornas/issue-pull-requests)
    - Preceder todo desenvolvimento da criação de um issue
    - Nunca mergiar um código na branch principal (main ou master)
    - Desenvolver via criação de branchs, devendo sua nomenclatura seguir o formato: issue_numero/issue_descricao
        - Exemplo: 1/criacao-pasta-imagens
    - Incluir o maior número de Commits possíveis dentro da branch, quebrando o desenvolvimento em pedaços pequenos fáceis de se analisar, devendo as mensagens dos mesmos seguir o formato "[#issue_numero] - Mensagem do Commit"
        - [#issue_numbero] lincará o issue ou problema que está sendo resolvido com a sua resolução de fato

    - [Fazer constar na mensagem de fechamento do Pull Request](https://docs.github.com/pt/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue) deverá "close #issue_number". Desta forma issue será fechado automaticamente

