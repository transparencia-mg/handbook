---
comments: true
tags:
  - CKAN
  - Erros
---

# Erro durante comando `docker exec -it ckan bash`

Post Relacionados:

- [Instalando instâncias CKAN local utilizando Docker](../20221220_Instancia_local_ckan_docker/#erro-instalacao-extencoes-versao-dev-210)
- [Instalando instâncias CKAN no novo GitHub Codespaces](../20221220_ckan_in_github_codespaces/#erro-instalacao-extencoes-versao-dev-210)

Como dito nos dois posts citados acima, durante a tentativa de instalação de extensões `docker exec -it ckan bash` recebi o seguinte erro `OCI runtime exec failed: exec failed: unable to start container process: exec: "bash": executable file not found in $PATH: unknown`.
[Esta resposta stackoverflow](https://stackoverflow.com/a/62434418/11755155) orientou utilizar `sh` via `docker exec -it <containerId> sh`, foi o que fiz e funcionou:

```
# Codespace
@gabrielbdornas ➜ /workspaces/ckan-docker (master) $ docker exec -it ckan sh
/srv/app #
```

```
# Local
ckan-docker git:(master) docker exec -it ckan sh
/srv/app #
```
> I was also getting this kind of error on alpine base image, because I was executing command using bash not from shell. For alpine base image use shell
