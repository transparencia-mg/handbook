---
comments: true
tags:
  - CKAN
  - regras de negócio
---

# Convenções sobre nomenclaturas: URLs dos conjuntos

## Background

No [issue #13](https://github.com/transparencia-mg/issues-dadosmg-legado/issues/13) tomamos uma decisão de reusar o mesmo nome do conjunto de dados em suas várias representações (eg. github, ckan, data package). 

No entanto, ainda não lidamos com o problema de que no CKAN não é permitido a reutilização do nome de conjuntos de dados entre organizações diferentes.

Isso é um problema porque faz sentido que a CGE, ou qualquer outro órgão, tenha que manter nomes únicos para seus conjuntos. Mas não faz sentido que a SEPLAG não possa ter um conjunto com o mesmo nome do que um da CGE.

Essa mudança [parece ser complexa](https://github.com/ckan/ckan/issues/1587), então vamos ter que utilizar alguma estratégia alternativa. 

Uma dessas alternativas é usar como nome do conjunto `{owner-org}-{dataset-name}`, mas fica a dúvida se isso deve estar registrado em todas as representações do conjunto ou somente no CKAN.

Particularmente me incomoda ficar com nomes de pastas e URLs no github muito grandes 

```
controladoria-geral-do-estado-cge-convenios-saida
```
## Benchmarking

No portal dados.gov.br, a nomenclatura de conjuntos com mesmo nome ficou ad-hoc (orcamento1, orcamento2) ou a sigla da organização está com o nome do conjunto na URL:
- [Planos de Dados Abertos](
https://dados.gov.br/dataset?q=plano+de+dados+abertos&sort=score+desc%2C+metadata_modified+desc)

- [Orçamento](https://dados.gov.br/dataset?q=orcamento&sort=score+desc%2C+metadata_modified+desc)

## Próximos passos

Para definir o que será feito com os conjuntos legados e novos, considerar:

- extensão exagerada dos nomes de pastas e URLs no github, p. ex.:
> controladoria-geral-do-estado-convenios-saida 

em vez disso, aplicar o padrão `siglaorg-nomeconjunto` como alternativa? p. ex.: 
> cge-convenios-saida;

- possibilidade de aplicar a regra de modificar o nome dos conjuntos somente nos casos de com mesmo nome em organizações diferentes, os quais deveriam sofrer a inclusão do nome/sigla do conjunto em seu nome;

Como melhoramento, uma pesquisa sobre uma extensão CKAN existente que configure na url o nome da organização antes do conjunto. Exemplo: `https://dados.mg.gov.br/cge/convenios-saida`.