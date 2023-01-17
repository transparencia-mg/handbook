---
comments: true
tags:
  - GitHub
  - Fluxo de Trabalho DCTA
---

# Adicionar Projeto a Issue via GitHub Actions

Como idéia para melhor organizar os issues criados dentro dos repositórios da organização [transparencia-mg](https://github.com/transparencia-mg) pensamos em sempre vincular issues criados ao projeto [@work-dta](https://github.com/orgs/transparencia-mg/projects/1).
Desta maneira periodicamente conseguiremos analisar o "estoque" de trabalho e realizar a priorização do mesmo.
Isso exigi um nível de organização muito grande, pois além de abrir o issue descrevendo a ação a ser feita deveremos lembrar de realizar a inclusão do projeto em questão.
A chance de erro material neste caso é grande.
Para automatizar este processo pesquisei [esta solução](https://github.com/orgs/community/discussions/9687#discussioncomment-4702790), para criar uma GitHub Actions a ser acionada toda vez que um issue for criado:

```
name: Add issues to project

on:
  issues:
    types: [opened]

jobs:
  add-to-project:
    name: Add issue to project
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v0.4.0
        with:
          project-url: https://github.com/users/<user id>/projects/<project id>
          github-token: ${{ secrets.ADD_TO_PROJECT_PAT }}
```

Caso o repositório que se deseja automatizar não tenha a pasta `.github/workflows`, a mesma deverá ser criada para incluir o arquivo `yml` conforme sugerido acima.
O repositório GitHub [add-to-project](https://github.com/actions/add-to-project) demonstra alguns outros [exemplos](https://github.com/actions/add-to-project#examples) de utilização, bem como explica os [inputs](https://github.com/actions/add-to-project#inputs) obrigatórios a serem fornecidos, como o `github-token`. 

Incluí como configuração na organização [transparencia-mg](https://github.com/transparencia-mg) `permitir acesso via access token pessoal (classic)` pois recebi o [erro](https://github.com/gabrielbdornas/notes/actions/runs/3939553780/jobs/6739545364) `Error: Personal access tokens with fine grained access do not support the GraphQL API` ao tentar utilizar a funcionalidade com o `fine-grained Personal Access Tokens`.
Ao que tudo indica, [não é possível este tipo de utilização](https://github.com/cli/cli/issues/6680).

![](https://imgur.com/rX68hvW.png)

Por fim, com intúito de padronizar, sugiro utilizarmos o nome `add_issues_to_projects.yml` para a actions que orquestratrá todo processo.

## Passos a serem seguidos

- Incluir `ADD_TO_PROJECT_PAT` no repositório que se deseja automatizar (settings/secrets/actions).
- Incluir arquivo `.github/workflows/add_issues_to_projects.yml` no repositório que se deseja automatizar com o seguinte conteúdo:

```
name: Add issues to project

on:
  issues:
    types: [opened]

jobs:
  add-to-project:
    name: Add issue to project
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v0.4.0
        with:
          project-url: https://github.com/orgs/transparencia-mg/projects/1
          github-token: ${{ secrets.ADD_TO_PROJECT_PAT }}
```
- Criar um issue para testar automatização.
- Deletar issue teste caso automatização funcione.
