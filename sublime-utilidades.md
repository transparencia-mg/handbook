# Sublime utilidades

##  corretor ortográfico em português - instalar e ativar 

1. na tela de edição, digitar 'Ctrl + Shift + P'

2. quando abrir a caixa de seleção, marcar 'Package Control: Install Packages'

3. digitar 'Portuguese', vai aparecer uma opção de dicionário em português para baixar (Cucumber)

4. na opção 'view' da barra de ferramentas - marcar 'spell check'

5. ainda na opção 'view' - acessar 'dictionary' ao final da lista e trocar para 'português'


## preview - instalar e configurar atalho

1. na tela de edição, digitar 'Ctrl + Shift + 'P'

2. quando abrir a caixa de seleção, digitar 'Package Control: Install Packages'

3. digitar 'Markdown preview', baixar o pacote

4. na opção 'preferences' da barra de ferramentas, acessar 'key bindings'

5. para criar o atalho como no ATOM, inserir o comando abaixo entre os colchetes da parte direita da janela de 'key bindings':

````
{
        "keys": ["ctrl+shift+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"pandoc"} 
    }
````
