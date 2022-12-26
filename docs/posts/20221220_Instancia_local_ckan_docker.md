---
comments: true
tags:
  - CKAN
---

# Instalando instâncias CKAN local utilizando Docker

- Realizada a partir do post [Instalação Augusto Herrmann](https://herrmann.tech/en/blog/2020/09/30/how-to-install-and-configure-ckan-2-9-0-using-docker.html). - Post instala [versão 2.9.0](https://herrmann.tech/en/blog/2020/09/30/how-to-install-and-configure-ckan-2-9-0-using-docker.html#:~:text=out%20its%20corresponding-,tag,-%3A) eu instalei versão [2.10-dev](https://github.com/ckan/ckan-docker/tree/7e244290a5d436ecf1ac00a51051825d550f1608).
- Não precisei `cd contrib/docker` pois o repositório que utilizei já tinha na raiz os arquivos necessários.
- Seguindo orientação do [README.md](https://github.com/ckan/ckan-docker/tree/7e244290a5d436ecf1ac00a51051825d550f1608#:~:text=public%20CKAN%20instance.-,To%20build%20the%20images,-%3A) do repositório utilizado rodei `docker-compose build` e `docker-compose up`.
- Checar docker volumes: `docker volume ls` (armazenados em `/var/lib/docker`).
- Checar containers: `docker ps`

## Erro instalação extenções versão dev 2.10

Durante a tentativa de instalação de extensões `docker exec -it ckan bash` recebi o seguinte erro `OCI runtime exec failed: exec failed: unable to start container process: exec: "bash": executable file not found in $PATH: unknown` que deverá ser investigado. Solução encontrada e relatada no post [Erro durante comando `docker exec -it ckan bash`](../20221222_erro_apos_docker_exec_instancia_ckan)

## Referências

- [ckan-demo-data](https://github.com/ckan/ckan-demo-data)

- [ckan-docker](https://github.com/ckan/ckan-docker)

- [Instalação Augusto Herrmann](https://herrmann.tech/en/blog/2020/09/30/how-to-install-and-configure-ckan-2-9-0-using-docker.html)