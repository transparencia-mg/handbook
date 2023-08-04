---
comments: true
tags:
  - Alteração Guia de Transparência Ativa
---

# Alteração dados do Guia de Transparência

### 1- Clonar repositório

- Clonar repositório localmente através do comando:

```bash
git clone https://github.com/transparencia-mg/guia-transparencia-ativa.git
```


### 2 - Instalação e configuração

### Ambiente virtual `venv`

* Se as dependências python **não** estiverem instaladas em um ambiente virtual `venv`, siga os passos:<br>
Nota: Para identificar se as dependências estão instaladas deve existir uma pasta chama *venv* junto as demais pastas do repositório.

```bash
 python -m venv venv
```

* Caso as dependências python estejam instaladas, lembre-se de ativar:

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
pip install -r requirements.txt  # instala a biblioteca necessária
```
**Observação:**<br>
- Após instalação verificar se todas as bibliotecas foram instaladas


### 2 - Criar nova branch

* Criar uma *branch* para fazer as alterações necessárias. **A nova *branch* deve ser criada a partir da *branch Review*.**

  - Criar *branch* a partir da linha de comando:

Acessar a *branch Review* : 
```bash
git checkout review
```
![image](https://user-images.githubusercontent.com/53793354/233437565-78cc3625-47cd-4af3-9d29-7ce427d4f2a2.png)

Em seguida crie a nova branch:

```bash
git checkout - b <nome da branch>
```

![image](https://user-images.githubusercontent.com/53793354/233439007-bb3b909c-6321-4afe-bbe6-529fbe9aed84.png)

- Criar *branch* a partir da web no github:

Entre na *branch Review* e em seguida digite o nome da nova branch na caixa de pesquisa.

![branch](https://user-images.githubusercontent.com/53793354/233434091-cffb7c56-5a1c-43f1-8537-82dc28c326e5.gif)

### Verificar documento - MKdocs

Para verificar qual a situação do documento é necessário usar o comando: 

```bash
mkdocs serve
```
**Observação:**<br> Caso o comando retorne erro referente a biblioteca '*babel*' ver [#66](https://github.com/transparencia-mg/handbook/issues/66)

Copie e cole no navegador a url apresentada:

![image](https://user-images.githubusercontent.com/53793354/233441870-0fcffa44-e22d-40f1-8336-77dcf7b6ce31.png)

Para retornar o uso da linha de comando digite: *ctrl +c*

### Alterações

* Todas as alterações devem ser realizadas na pasta *docs*. 
* Antes de realizar o commit é importante verificar se todas as alterações estão conforme o desejado, isso evita um retrabalho desnecessário caso tenha esquecido de algo. Utilize o comando:

```bash
mkdocs serve
```

* Após todas as alterações e *commits* serem realizados será necessário a abertura do *Pull request*.

**Importante:** <br>O *Pull request* deve fazer referência a *branch Review* e não a *branch main*

![image](https://user-images.githubusercontent.com/53793354/233443519-ae6c9717-7fbc-4e41-89f9-9dd6b7ffbf7b.png)

* O responsável pela revisão irá realizar o merge do *pull request*. Após o merge todas as alterações propostas serão migradas para a *branch Review*.

### Publicar Guia de Transparência


O passo a passo de todas as informações acima podem ser assistidas nos vídeos disponíveis em:

https://youtu.be/p3IncxI16s0

https://youtu.be/vRK_Pu8Txxc
