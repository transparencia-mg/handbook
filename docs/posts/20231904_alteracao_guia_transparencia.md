---
comments: true
tags:
  - Alteração Guia de Transparência Ativa
---

# Instalação e configuração

### Ambiente virtual `venv`

1- Se as dependências python **não** estiverem instaladas em um ambiente virtual `venv`, siga os passos:

```bash
 python -m venv venv
```

2- Caso as dependências python estejam instaladas, lembre-se de ativar:

```bash
. venv/Scripts/activate # windows
. venv/bin/activate # linux
```
### Biblioteca do projeto

Verificar se a biblioteca que consta *`requirements.txt`* está instalada no ambiente:

```bash
pip list # verifica quais bibliotecas estão instaladas
```
```bash
pip install - r requirements.txt  # instala a biblioteca necessária
```
**Observação:**<br> Após instalação verificar se todas as bibliotecas foram instaladas

### MKdocs

Para verificar como documento está antes de realizar qual alteração.

```bash
mkdocks serve
```
**Observação:**<br> Caso o comando retorne erro referente a biblioteca '*babel*' ver [#66](https://github.com/transparencia-mg/handbook/issues/66)


# Alteração do Guia de Transparência

1- Verificar a versão do projeto através da *url*. Para isso é necessário usar o comando 'mkdocks serve' para gerar a URL.

COLOCAR IMAGEM

2- Crie uma *branch* para iniciar as alterações necessárias. A nova *branch* deverá ser criada a partir da *branch Review*.

  - Criar *branch* a partir da linha de comando:

```bash

```

# Publicar Guia de Transparência

Ver vídeo 

# Erro na publicação do documento

Ver vídeo 31:34
