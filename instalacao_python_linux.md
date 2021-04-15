# Instalação Python e pip3 - linux Ubuntu
- Faça backup do sistema utilizando Timeshift (garantir restaruação caso algo de errado)

- [Video YouTube de Referência para instalar Python3](https://www.youtube.com/watch?v=z3Hdewxuuoo)
```
$ cd             # HOME DIRECTORY
$ python3        # VISUALIZAR SE ESTÁ INSTALADO 
$ sudo apt install python3 # INSTALA python3
$ sudo apt install python3-pip # INSTALA pip
$ pip3                   #CHECA INSTALAÇÃO
$ pip3 install <nome_pacote>  # INSTALA PACOTE
```
- [Vídeo YouTube de Referência para gestão de ambientes (env) com Python](https://www.youtube.com/watch?v=Kg1Yvry_Ydk&t=5s)
    - Comandos pip3 e python3 para trabalhar com global e pip e python para trabalhar no local

```
# REQUISITOS: Python 3.3 ou maior

# LISTA DE TODOS OS PACOTES INSTALADOS GLOBALMENTE
$ pip3 list  

# CRIA O AMBIENTE (cria também uma pasta com o mome do projeto_versão)
# CRIA O AMBIENTE COM A MESMA VERSÃO DO python GLOBAL DO MOMENTO DA CRIAÇÃO
$ cd <diretorio_desejado> && python3 -m venv <nome_do_projeto_ou_versao>   
$ python3 -m venv venv --system-site-packages

# ATIVA A VERSÃO
$ source <nome_do_projeto_ou_versao>/bin/activate 

############## EXEMPLO DE VERSÃO ATIVADA######
➜ gabrielbdornas source project_env/bin/activate
(project_env) ➜  gabrielbdornas 
############## EXEMPLO DE VERSÃO ATIVADA######

# VERIFICA AONDE ESTÁ A VERSÃO ATIVADA
# python not found # APÓS VERSÃO DESATIVADA
$ which python   

############## EXEMPLO DE LOCAL VERSÃO ATIVADA######
(project_env) ➜  gabrielbdornas which python
/home/gabrielbdornas/code/gabrielbdornas/project_env/bin/python
(project_env) ➜  gabrielbdornas
############## EXEMPLO DE LOCAL VERSÃO ATIVADA######

# INSALAÇÃO DE PACOTES
# SE ALGUMA VERSÃO ESTIVER ATIVADA INSTALARÁ APENAS NELA E NÃO GLOBALMENTE
# pip install <nome_pacote>  

# SALVAR TODOS OS PACOTES INSTALADOS EM DETERMINADO AMBIENTE
$ pip freeze
# SALVAR TODOS OS PACOTES INSTALADOS EM DETERMINADO AMBIENTE E CRIAR UM ARQUIVO txt PARA ARMAZENAR
$ pip freeze > requerement.txt 
# INSTALA TODOS OS PACOTES PRESENTES NO ARQUIVO .TXT (IGUALAR AMBIENTES)
$ pip install -r requerements.txt


# DESATIVA A VERSÃO
$ deactivate

```
- Erro ao rodar "python3 -m venv <nome_do_projeto_ou_versao>":
    - Rodar "apt-get install python3-venv" como sugerido

```
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/gabrielbdornas/code/gabrielbdornas/project_env/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']
```

- Ideia para criação de versão descrita no vídeo
    - Criar/ativar a versão dentro da pasta do projeto

```
$ mkdir <nome_projeto>              # CRIA PASTA DO PROJETO (PODE SER CLONE GITHUB)
$ cd <nome_projeto>                 # ENTRA NA PASTA (CHANGE DIRECTORY)
$ python3 -m venv venv              # CRIA O AMBIENTE
$ source venv/bin/activate          # ATIVA O AMBIENTE
$ pip install -r requerements.txt   # CONFIGURA AMBIENTE COM MESMOS PACOTES EXPORTADOS DE OUTRO LOCAL
```

- Nunca colocar nenhum arquivo dentro da pasta venv criada
- Colocar pasta venv na raiz do projeto
- Não enviar a pasta venv para github ou commitar no local (gitgnore). Commitar e mandar para github apenas o arquivo requerements.txt, permitindo assim que as pessoas construam seus próprios ambientes
