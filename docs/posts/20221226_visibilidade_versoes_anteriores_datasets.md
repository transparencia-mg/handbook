---
comments: true
tags:
  - CKAN
---

# Visibilidade de versões anteriores de conjuntos de dados

## Contexto

Em reunião de [02/12/2022](https://github.com/transparencia-mg/work-stefanini/blob/main/docs/atas_de_reuniao/20221201_estoria_usuario_melhoria_paginas_html.md#issues-para-investiga%C3%A7%C3%A3o-em-paralelo), estranhamos o fato das versões anteriores dos conjuntos publicados (tanto em produção quanto em homologação) não estarem visíveis para usuários deslogados, mas apenas para logados.

Esta funcionalidade tem importância pelo dispositivo legal de 'manutenção do histórico' dos dados abertos, vide [art 29 da Lei 14.129](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm#art29), inciso VI:

> Art. 29.  Os dados disponibilizados pelos prestadores de serviços públicos, bem como qualquer informação de transparência ativa, são de livre utilização pela sociedade, observados os princípios dispostos no [art. 6º da Lei nº 13.709, de 14 de agosto de 2018](https://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2018/Lei/L13709.htm#art6) (Lei Geral de Proteção de Dados Pessoais).
> § 1º  Na promoção da transparência ativa de dados, o poder público deverá observar os seguintes requisitos:
> I - observância da publicidade das bases de dados não pessoais como preceito geral e do sigilo como exceção;
> II - garantia de acesso irrestrito aos dados, os quais devem ser legíveis por máquina e estar disponíveis em formato aberto, respeitadas as [Leis nºs 12.527, de 18 de novembro de 2011](https://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12527.htm) (Lei de Acesso à Informação), e [13.709, de 14 de agosto de 2018](https://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2018/Lei/L13709.htm) (Lei Geral de Proteção de Dados Pessoais);
> III - descrição das bases de dados com informação suficiente sobre estrutura e semântica dos dados, inclusive quanto à sua qualidade e à sua integridade;
> IV - permissão irrestrita de uso de bases de dados publicadas em formato aberto;
> V - completude de bases de dados, as quais devem ser disponibilizadas em sua forma primária, com o maior grau de granularidade possível, ou referenciar bases primárias, quando disponibilizadas de forma agregada;

> **VI - atualização periódica, mantido o histórico, de forma a garantir a perenidade de dados, a padronização de estruturas de informação e o valor dos dados à sociedade e a atender às necessidades de seus usuários;**

## Documentação 

Na documentação do CKAN, a configuração _default_ desde o [upgrade v.2.9.0](https://docs.ckan.org/en/2.9/changelog.html#v-2-9-0-2020-08-05) é:

> A full history of dataset changes is now displayed in the Activity Stream to admins, and optionally to the public. By default this is enabled for new installs, but disabled for sites which upgrade (just in case the history is sensitive). When upgrading, open data CKANs are encouraged to make this history open to the public, by setting this in production.ini: ckan.auth.public_activity_stream_detail = true ([#3972](https://github.com/ckan/ckan/pull/3972))

> When upgrading from previous CKAN versions, the Activity Stream needs a migrate_package_activity.py running for displaying the history of dataset changes

Entretanto, a despeito do trecho citado acima, a funcionalidade de visualização das versões anteriores parece ser restrita a usuários logados pelo menos como editores, segundo [esse outro trecho da documentação do CKAN](https://docs.ckan.org/en/2.9/maintaining/authorization.html?highlight=ckan.auth.public_activity_stream_detail#ckan-auth-public-activity-stream-detail):

> `ckan.auth.public_activity_stream_detail = True`
> Default value: False (however the default config file template sets it to True)

> Restricts access to ‘view this version’ and ‘changes’ in the Activity Stream pages. These links provide **users with the full edit history of datasets** etc - what they showed in the past and the diffs between versions. If this option is set to False then only admins (e.g. whoever can edit the dataset) can see this detail. If set to True, anyone can see this detail (assuming they have permission to view the dataset etc).

## Benchmarking

De fato, esse parece ser o comportamento esperado do CKAN, conforme exemplos de outros estados:

- [Alagoas](https://dados.al.gov.br/catalogo/dataset/activity/unidades-de-conservacao-no-estado-de-alagoas)
- [Belo Horizonte](https://dados.pbh.gov.br/dataset/activity/estacionamento-publico-destinacao-especifica)
- [Espírito Santo](https://dados.es.gov.br/dataset/activity/estoque-de-sangue-hemoes)
- [Rio Grande do Sul](https://dados.rs.gov.br/dataset/activity/dados-abertos)
- [Santa Catarina](https://dados.sc.gov.br/dataset/activity/arrecadacao-municipios)