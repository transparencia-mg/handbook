---
comments: true
---

# Treinamento Dados Aberto Antônio Marcel

**Data:** 10/07/2023

## Participantes:

- Gabriel Dornas
- Antônio Marcel

## Assuntos tratados

- Gabriel solicitou Antônio a criação de uma organização da Comissão de Ética no GitHub.
- Organização [consed-cge-mg](https://github.com/conset-cge-mg) criada.
- Criação do primeiro conjunto de dados na organização [consed-cge-mg](https://github.com/conset-cge-mg/treinamento-dados-abertos).
- Verificamos que a versão do Python instalada na máquina do Antônio via `python --version` é 3.9.7.
- Comandos utilizados para setup inicial do projeto:

```python
# Criação estrutura inicial da pasta
mkdir treinamento-dados-abertos # Criar pasta
cd treinamento-dados-abertos # Entrar na pasta criada
New-Item README.md # Criar arquivo README.md
New-Item .gitignore # Criar arquivo .gitignore
New-Item .env # Criar arquivo .env
# Incluir venv no arquivo .gitignore
# Incluir .env no arquivo .gitignore

# Iniciando controle de versão com git
git init
git add .
git commit -m "Commit Inicial"

# Criando ambiente virtual python
conda deactivate
python -m venv venv
. venv/Scripts/activate
New-Item requirements.txt
# inclui dpckan==0.1.21 no requirements.txt
pip install -r requirements.txt # Instala pacotes

# Cria repositório online github, com mesmo nome do projeto local
git push origin main # Sincronza repo local com github
```

- Criar o dataset conforme especificação [Frictionless](https://specs.frictionlessdata.io/#overview):
    - [Package](https://specs.frictionlessdata.io/tabular-data-package/).
    - [Resource](https://specs.frictionlessdata.io/data-resource/#language).
    - [Table Schema](https://specs.frictionlessdata.io/table-schema/).

- Criação de usuário no [homologa](https://homologa.cge.mg.gov.br/)

```python
New-Item data.csv
# inclusão das colunas e dados no arquivo data.csv
frictionless describe data.csv --type package > datapackage.yaml
frictionless validate datapackage.yaml
frictionless describe datapackage.yaml --type package --json > datapackage.json
frictionless validate datapackage.json

# dpckan
dpckan dataset create
```

- Documentação [dpckan](https://github.com/transparencia-mg/dpckan).

- Durante comando `dpckan dataset create` recebemos o erro:

```python
Creating resource: data
Error during https://dados.mg.gov.br//dataset/treinamento-dados-abertos creation
```

- Para corrigir o erro acima listado incluimos a propriedade `title` no resource.
- [Conjunto criado em homologação](https://homologa.cge.mg.gov.br/dataset/treinamento-dados-abertos).
- Instalação e utilização pacote [taskipy](https://github.com/taskipy/taskipy).
    - `New-Item pyproject.toml`.

    ```python
    [tool.taskipy.tasks]
    datapackage-json = { cmd = "frictionless describe datapackage.yaml --type package --json > datapackage.json", help = "Converte datapackage.yaml em datapackage.json." }
    dataset-update= { cmd = "dpckan --datastore dataset update", help = "Atualiza CKAN." }
    ```

    - Ver tasks com `task --list`.

## Decisões

- Criação de [Issues](https://github.com/conset-cge-mg/treinamento-dados-abertos/issues) para gestão de melhorias do repositório criado.

## Pendências

- Incluir logo nova organização [consed-cge-mg](https://github.com/conset-cge-mg) criada.
- Abrir um issue no repositório dpckan para relatar o erro de falta de propriedade `title`.

## Referências

- [Apresentação OKBR](https://transparencia-mg.github.io/reveal.js/presentations/20230328_gerenciar_dados_abertos_com_dpckan/index.html)
