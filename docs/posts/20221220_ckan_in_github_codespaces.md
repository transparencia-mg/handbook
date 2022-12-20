---
tags:
  - CKAN
  - GitHub
---

# Instalando instâncias CKAN no novo GitHub Codespaces

Resolvi testar o [GitHub Codespaces](https://github.com/features/codespaces) como uma das formas de criarmos uma instância do CKAN utilizando [docker](https://docs.ckan.org/en/2.9/maintaining/installing/install-from-docker-compose.html#installing-ckan-with-docker-compose).
Esta opção facilitará os testes do novo pacote [ckanext-datapackage-creator](https://github.com/transparencia-mg/ckanext-datapackage-creator) desenvolvido pela [empresa stefanini](https://transparencia-mg.github.io/work-stefanini/).
GitHub disponibiliza 15 horas/mês grátis para planos [free](https://github.com/settings/billing/plans#:~:text=GitHub%20Codespaces-,Spin,-up%20fully%20configured):

> A "core hour" is a measure used for included compute usage. On a 2-core machine, you would get 60 hours free. On a 4-core machine, you would get 30 hours free, etc...

Valores de Horas adicionais podem ser visualizadas na [documentação GitHub](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#:~:text=2%2Dcore%20machine.-,Component,-Machine%20type).

Testei a instalação para divsersas situações, explicadas abaixo:

## Instalação tag ckan-2.9.5

- Fork do repositório [ckan](https://github.com/ckan/ckan) na organização [gabrielbdornas](https://github.com/gabrielbdornas/ckan). **Não selecionar a opção de copiar apenas a branch master**.

- Dentro do fork do repositório selecionar a tag `ckan-2.9.5`:

![seleciona tag](https://imgur.com/g5KXuQx.png)

- Adiciona Codespaces com a opção `New with options...`:

![new codespaces](https://imgur.com/BJaHjtB.png)

- Muda apenas configuração `Machine type`, selecionando a opção `8-core`:

![codespace machine type](https://imgur.com/KLm3l0n.png)

- Vs-code dev será aberto (código e terminal).

- Navegar para pasta `contrib/docker/` com o comando `cd contrib/docker/`.

- Copiar arquivo `.env.template` para arquivo `.env` com o comando `cp .env.template .env`. **Descobri que via tags não é possível adicionar arquivo(s) na interface gráfica do GitHub**.

- Rodar o comando `docker-compose up` e aguardar o final da instalação.

- Instalação realizada com sucesso e disponível [em link próprio](https://gabrielbdornas-opulent-carnival-647jgw74g6639xv-5000.preview.app.github.dev/) quando máquina encontra-se com estado `Active`:

![codespaces active](https://imgur.com/6S4PHKC.png)

## Instalação versão dev 2.10

- Fork do repositório [ckan-docker](https://github.com/ckan/ckan-docker) na organização [gabrielbdornas](https://github.com/gabrielbdornas/ckan-docker).**Não selecionar a opção de copiar apenas a branch master**.

- Adiciona Codespaces com a opção `New with options...`:

![new codespaces](https://imgur.com/BJaHjtB.png)

- Muda apenas configuração `Machine type`, selecionando a opção `8-core`:

![codespace machine type](https://imgur.com/KLm3l0n.png)

- Vs-code dev será aberto (código e terminal).

- Rodar os comandos `docker-compose build` e `docker-compose up` e aguardar o final da instalação, conforme [documentação](https://github.com/ckan/ckan-docker#quick-start). **Não será necessário criar arquivo `.env` pois o mesmo já existia na raiz do repositório**.

- Instalação realizada com sucesso e disponível [em link próprio](https://gabrielbdornas-psychic-rotary-phone-rpvjgwvpg97hpx66-5000.preview.app.github.dev/) quando máquina encontra-se com estado `Active`:

![codespaces active](https://imgur.com/msZM5xj.png)
