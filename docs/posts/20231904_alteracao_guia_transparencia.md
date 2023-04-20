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

1- Clonar repositório localmente

```bash
git clone https://github.com/transparencia-mg/guia-transparencia-ativa.git
```
2- Criar uma *branch* para iniciar as alterações necessárias. **A nova *branch* deve ser criada a partir da *branch Review*.**

  - Criar *branch* a partir da linha de comando:

```bash
git checkout - b <nome da branch>
```
- Criar *branch* a partir da web no github:

Entre na *branch Review* e em seguida digite o nome da nova branch na caixa de pesquisa.

COLOCAR IMAGEM
--
3- Verificar qual a versão do projeto através da *url*. Para isso é necessário usar o comando 'mkdocks serve' para gerar a URL.

COLOCAR IMAGEM

4- Após todas as alterações e *commits* serem realizados será necessário a abertura do *Pull request*.

**Importante:** <br>O *Pull request* deve fazer deve fazer referência a *branch Review* e não a *branch main*

COLOCAR IMAGEM
--

5- O responsável pela revisão irá realizar o merge do *pull request*. Após todas as alterações propostas serão migradas para a *branch Review*.

# Publicar Guia de Transparência



# Erro na publicação do documento

Ver vídeo 31:34
