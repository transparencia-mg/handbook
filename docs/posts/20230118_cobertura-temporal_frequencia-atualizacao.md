---
comments: true
tags:
  - CKAN
  - metadados
  - temporal
  - atualização
  - regras de negócio
---

# Cobertura temporal e periodicidade de atualização

É muito importante comunicar aos usuários dos conjuntos de dados publicados a qual período se referem os dados e a qual frequência temporal eles estão sendo atualizados. Dados de séries histórica podem gerar confusão no seu uso, se o recorte do período específico da publicação não estiver claro. Por outro lado, a frequência de tempo usada para sua atualização é importante mecanismo de verificação da regularidade de sua alimentação pelos custodiantes responsáveis (autor, publicador). Além disso, para usuários costumeiros, saber exatamente quando o dado será atualizado é útil para consulta.


## Background

As informações sobre cobertura temporal e periodicidade de atualização são metadados mencionados:

- no [Portal Federal de Dados Abertos](https://dados.gov.br/pagina/manuais-e-orientacoes);

- no [Modelo de Referência de Abertura de Dados](https://www.gov.br/cgu/pt-br/governo-aberto/a-ogp/planos-de-acao/4o-plano-de-acao-brasileiro/compromisso-2-docs/modelo-de-referencia-de-abertura-de-dados_versao-final-2.pdf)(vide página 31/99)

- estão sendo incluídas como item nas especificações das nossas necessidades com a Stefanini: [ver critério 007](https://transparencia-mg.github.io/work-stefanini/0.6/estorias_de_usuarios/sprint_04/06_edicao_do_conjunto_de_dados/):

> RN008 - A combobox Frequência de Atualização deverá conter as seguintes informações: diário, semanal, quinzenal, mensal, bimestral, trimestral, anual, sob demanda e como padrão a opção selecione**

- e será incluído como metadado obrigatório no [Manual de Dados Abertos de MG](https://transparencia-mg.github.io/manual-abertura/pages/002_metadados.html#metadados-obrigat%C3%B3rios-e-facultativos-no-portal-de-dados-abertos-de-minas-gerais).

A discussão interna que motiva a adoção desses metadados, e também discute um pouco da dificuldade de se fazê-los representar, encontra-se [neste issue](https://github.com/transparencia-mg/issues-dadosmg-legado/issues/69).


## Representação

Há algumas dificuldades consideráveis de se fazer representar essas duas informações no dicionário de dados e no CKAN. 

#### Sobre o `temporal`

A Frictionless Standard tem um forma de representação das informações de início e fim da série temporal através da propriedade [`temporal`](https://specs.frictionlessdata.io/data-package/#:~:text=Adherence%20to%20the%20specification%20does%20not%20imply%20that%20additional).

O `datapackage.json` é lido como um recurso qualquer no CKAN, como se fosse um arquivo de dados, e nem todas os valores das propriedades nele descritas encontram correspondência (vide questões de trasnposição 'de-para' nos [issues sobre a extensão ckanext-scheming](https://github.com/ckan/ckanext-scheming/issues) . 

Assim, uma notação legível por máquina:

![](assets/images/temporal_JSON.png)

Não é adequadamente interpretada para ser legível por pessoas na interface gráfica do CKAN como 'fonte', autor', 'mantenedor' 

![](assets/images/temporal_CKAN.png)


#### Sobre a frequência de atualização ou `accrualPeriodicity`

Os nomes das propriedades do JSON e YAML [podem conter espaço e acentos](https://github.com/transparencia-mg/crimes-violentos/blob/7db841f373444afe52925d690f483e47801f9988/datapackage.yaml#L19), mas essa flexibilidade pode provocar incompatibilidade com ferramentas diversas:

````
licenses:
  - name: CC-BY-4.0
    title: Creative Commons Attribution 4.0
    path: https://creativecommons.org/licenses/by/4.0/
**frequência de atualização: mensal**
temporal:
  - start: '2012-01-31'
    end: '2022-09-30'
````

Além disso, o nome da propriedade em outro idioma que não seja o inglês faz perder a consistência com os demais metadados aderentes À especificação Frictionless.

A Dublin Core, um padrão de metadados bem difundido e que é basilar para outros, tem o [accrualPeriodicity](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/accrualPeriodicity/) como propriedade para fazer representar a frequência de atualização.

O fato de ser algo padronizado pela Dublin Core e [utilizada no DCAT](https://www.w3.org/TR/vocab-dcat-2/#Property:dataset_frequency) pesa em seu favor, mas `accrualPeriodicity` não comunica seu significado com suficiência e os valores em inglês vão gerar dificuldades:

````
Semiannual [freq:semiannual]
> Three times a year [freq:threeTimesAYear]
> Quarterly [freq:quarterly]
> Bimonthly [freq:bimonthly]
> Monthly [freq:monthly]
> Semimonthly [freq:semimonthly]
> Biweekly [freq:biweekly]
````

O ckanext-scheming parece ter um [padrão para frequência de atualização](https://github.com/ckan/ckanext-scheming/blob/7d5d6cb91c3d82bd14982dd355c53206c839bbc6/ckanext/scheming/subfields.yaml#L96-L113
): 

````
field_name: frequency
    label: Frequency
    preset: select
    choices:
    - label: Daily
      value: 1d
    - label: Weekly
      value: 7d
    - label: Monthly
      value: 1m
    - label: Quarterly
      value: 3m
    - label: Semiannual
      value: 6m
    - label: Annual
      value: 1y
    - label: Decennial
      value: 10y
````

A princípio, um universo de valores possíveis mais restrito que o Dublin Core, mas parecendo abarcar quase todas as possibilidades de frequência de atualização dos atuais conjuntos publicados no PdA.

## Metadados fora de padrões das especificações

Como fazer representar chaves e valores dessas propriedades, ou metadados, extremamente úteis aos usuários, mas com tais dificuldades de transposição leitura humana a leitura por máquina (e vice-versa)?

Alternativas de outros padrões ou em outros softwares difundidos podem sempre aparecer, mas é necessário estabelecer uma fórmula geral mais ou menos bem aceita, que acomode a compreensibilidade a "olho nu", por usuários mais leigos em ferramentas de dados, bem como o interesse dos usuários mais experimentados em dados na consistência e compatibilidade com ferramentas.

A possibildiade de inclusão de qualquer campo de metadado com chave e valor na interface gráfica (extensão em desenvolvimento pela empresa contratada) já é um passo para mitigar essa dificuldade, mas está longe de ser suficiente, na medida em que abre a brecha para inclusão de metadados fora de padrões das especificações.

A propriedade "frequência de atualização", quando registrada em português, é um exemplo. Utilizar ao máximo as especificações e incluir um dicionário de dados legível por pessoas, em pdf, por exemplo, é uma forma de tentar fazer equilibrar as duas necessidades. Afinal, atualmente possuímos um `datapackage.json` cuja interpretabilidade pode ser bastante reduzida pela maiori a dos usuários do Portal de Dados Abertos.