---
comments: true
---

# Treinamento Dados Abertos - Novo Dataset Template

**Data:** 18/07/2023

## Participantes:

- Gabriel Dornas
- Antonio Marcel

## Gravação do encontro

[![Watch the video](https://img.youtube.com/vi/Y1ZKHX0sAfg/maxresdefault.jpg)](https://youtu.be/VbsRpYB1G-U)

## Links relacionados

- [Ata da primeira reunião mostrando setup de um projeto de abertura de dados](../20230710_publicacao_dados_comissao_etica).
- [Repositório GitHub](https://github.com/transparencia-mg/new-dataset-template).
- [Repositório criado no treinamento](https://github.com/conset-cge-mg/lista-comissoes-treinadas-spci).
- [Conjunto publicado em ambiente homologação](https://homologa.cge.mg.gov.br/dataset/lista-comissoes-treinadas-spci).

## Assuntos tratados
O new dataset template é um conjunto de automatizações desenvolvidas pela Diretoria Central de Transparência Ativa - DCTA/CGE para criação, documentação, validação e publicação (criação e atualização em instâncias do CKAN) de conjunto de dados ou datasets.

### Fluxo de execução

```mermaid
graph TD;
    1(Início)-->2;
    2[Forcar dataset template]-->3;
    3[Cadastrar secrets]-->4;
    4[Configurar github pages]-->5;
    5[Incluir arquivo .xls na pasta upload]-->6;
    6[Script publica novo conjunto no CKAN]-->7;
    7(Fim)
```

### Setup do projeto
- Realize o fork do projeto (utilizaremos um fork para conseguir atualizar as automatizações com maior facilidade no futuro):

![Fork-do-Projeto](https://camo.githubusercontent.com/bcfa46bd43ef1711eaf0a4556fd63a1427e0cab05ac7e7df5f6e6f72ed803ea0/68747470733a2f2f696d6775722e636f6d2f754f5a6c6838612e706e67
)

- Selecione a organização a qual o novo conjunto de dados será criado e preencha o nome do novo repositório (o nome deverá ser o mesmo do conjunto que será criado na instância do CKAN).

![Organização](https://camo.githubusercontent.com/721c75279b5e41b149f86718da4329234dade6aa6a7c612f578002859082bb59/68747470733a2f2f696d6775722e636f6d2f6271536a7379512e706e67)

- Cadastre Secrets para publicação em instância CKAN:

![Settings](https://camo.githubusercontent.com/9eaad8cc30f8a8c48d341d16e70c8a23a30177b33b7daeb6309ab815f7768ad4/68747470733a2f2f696d6775722e636f6d2f49334f465177752e706e67)
![Secrets](https://camo.githubusercontent.com/753262b182e18ce29efeaabc6ba284ef8c5bee754f77575e22123097095b7856/68747470733a2f2f696d6775722e636f6d2f61616e30484e642e706e67)
![New repository secret](https://camo.githubusercontent.com/e0e329e4ce1c5f80217bf9de4cdbed9387591dfc10f61fd806077ea9f61de87c/68747470733a2f2f696d6775722e636f6d2f586732544c43642e706e67)

- Deverão ser criadas três secrets:

    - OWNER_ORG: Organização dentro da instância do CKAN desejada a qual o conjunto de dados será vinculado (nome disponível na url CKAN após https://ckan-instance/organization/)

    - CKAN_HOST: Instância CKAN desejada, exemplo: https://homologa.cge.mg.gov.br

    - CKAN_KEY_USUARIOGITHUB: se meu usuário GitHub é gabrielbdornas este secret será CKAN_KEY_GABRIELBDORNAS. Para o andrelamor, o secret CKAN_KEY_ANDRELAMOR

        - Necessário criar um novo API Token na instância CKAN desejada (copiar e colar o valor API TOKEN created da 4ª tela printada a seguir):
        
![API Token 1](https://camo.githubusercontent.com/a96e640138cbea88e09971eb3d61328002fc6d972351fe8cd1b7d4b46f790d15/68747470733a2f2f696d6775722e636f6d2f447231567847382e706e67)

![API Token 2](https://camo.githubusercontent.com/9a90d54821274b4353838472bb29a2966ae8f09aa8da7af76368e636d39e0f7d/68747470733a2f2f696d6775722e636f6d2f547055516f4c4d2e706e67)

![API Token 3](https://camo.githubusercontent.com/0b27ba4afc4d3f0e0c73c648d345d4ebae7f3f44e290f69e5dff93897c51572a/68747470733a2f2f696d6775722e636f6d2f417744386867632e706e67)

![API Token 4](https://camo.githubusercontent.com/d85d76be449c06c3eb75f35fbc9532c4ac1bfb97bed262ed2385fd8c3f9ecb2a/68747470733a2f2f696d6775722e636f6d2f347167443748532e706e67)

- Configurar permissão para Actions ler e escrever no repositório:

OBS.: Caso a permissão para Actions ler e escrever no repositório não esteja habilitada, esta configuração deverá ser feita também no nível da organização.

![Actions-Settings-1](https://camo.githubusercontent.com/9eaad8cc30f8a8c48d341d16e70c8a23a30177b33b7daeb6309ab815f7768ad4/68747470733a2f2f696d6775722e636f6d2f49334f465177752e706e67)

![Actions-Settings-2](https://user-images.githubusercontent.com/49699290/254383904-7e5f739a-1b15-4bd1-a225-1cd75655d80b.png)