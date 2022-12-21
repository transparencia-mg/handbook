---
tags:
  - CKAN
---

# Licenças em dados abertos: background e representação

## Background

O campo de licenças é um metadado obrigatório:

- para o Portal Federal de Dados Abertos, regulamentado no [Decreto Federal 8777](https://www.planalto.gov.br/CCIVIL_03/_Ato2015-2018/2016/Decreto/D8777.htm#art2) e na [resolução CGINDA 2 de 2017](https://wiki-dados.cgu.gov.br/GetFile.aspx?File=%2fComiteGestor%2fResolu%c3%a7%c3%b5es%2fresolucao-cginda-2-24-3-2017%2cpdf.pdf):


- para o [datapackage creator da Frictionless](https://create.frictionlessdata.io/), que contém uma lista predefinidas de possíveis licenças:

![](static/licences-datapackage-creator.png)

- está sendo incluído como item nas especificações das nossas necessidades com a Stefanini: [issue descritivo](https://github.com/transparencia-mg/work-stefanini/issues/69)

- e será incluído como metadado obrigatório no [Manual de Dados Abertos de MG](https://transparencia-mg.github.io/manual-abertura/pages/002_metadados.html#metadados-obrigat%C3%B3rios-e-facultativos-no-portal-de-dados-abertos-de-minas-gerais)

A discussão interna que fundamenta a escolha do tipo de licença está [neste card](https://trello.com/c/OQVjhGeM/877-escolher-licen%C3%A7a-aberta-para-dados-de-interesse-coletivo-e-geral), que foi originado da demanda registrada [nesse outro card](https://trello.com/c/auyl56pH/91-licenciamento-de-uso-de-dados-3-artefatos).

## Representação

Como utilizamos as especificações da Frictionless para documentar nossos conjuntos, os valores e hiperlinks da licença que [convencionamos utilizar no ano passado](https://trello.com/c/OQVjhGeM/877-escolher-licen%C3%A7a-aberta-para-dados-de-interesse-coletivo-e-geral#comment-610ab3589a7b7e1ec9a1c564) são representados pelos valores da lista de dicionários conforme abaixo:

````
  "licenses": [
    {
      "name": "CC-BY-SA-4.0",
      "title": "Creative Commons Attribution Share-Alike 4.0",
      "path": "https://creativecommons.org/licenses/by-sa/4.0/"
    }
  ]
````
Entretanto, o `datapackage.json` é lido como um recurso qualquer no CKAN, como se fosse um arquivo de dados, e nem todas os valores das propriedades nele descritas encontram correspondência (vide questões de trasnposição 'de-para' nos issues sobre extensão ckanext-scheming)[^1] 

Assim, o hiperlink da versão 4.0 da licença CC-BY não está aparecendo na GUI (interface gráfica do usuário) do CKAN:

![](static/licença-sem-hiperlink.png)

Uma maneira transitória é fazer a atribuição da licença via GUI, para fazer demonstrar o hiperlink de forma correta e possibilitar ao usuário acessar a página que descreve as prerrogativas da licença:

![](static/atrib-licenca-GUI.png)

![](static/licenca-com-hiperlink.png)

Entretanto, qualquer atualização via CLI (linha de comando) ou dataset-template do conjunto de dados no github vai sobrescrever a atribuição do hiperlink da licença via GUI e retornar somente o texto sem hiperlink, contendo o nome da licença atribuída para aquele conjunto.

A solução definitiva para esse caso, dentre outros de falta de correspondência entre os metadados padrão Fricionless e padrão CKAN, é a adoção de extensões que fazem esse trabalho, como estamos estudando em:

1. [Frictionless CKAN Mapper](https://github.com/frictionlessdata/frictionless-ckan-mapper)

1.

1.

[^1]: Nota