# Atualização e validação no GitHub

#### 2.1 Premissas

Sempre que os dados forem alterados as novas informações devem ser atualizadas no repositório do GitHub.

1) O nome da planilha não deve ser alterado;
2) A ordem das colunas não podem ser alteradas;
3) O arquivo deve ser salvo no formato .xlxs.

#### 2.2 Atualização

- Clicar na pasta "dataset" para alterar os aquivos: README, CHANGELOG, CONTRIBUTING, DATAPACKEGE.yaml
    
  **NÃO ALTERAR/EDITAR DATAPACKEGE.json, apenas mexer no DATAPACKEGE.yaml.**

- Clicar na pasta "upload" para os arquivos em excel (XLSX)



 As modificações automáticas só serão publicadas no CKAN se as alterações forem realizadas nestas pastas.



Após a atualização dos dados, acesse a sua conta do [Github](https://github.com/login) e em seguida acesse o repositório do conjunto de dados a ser alterado.

- Na pasta **/upload/** clique em *Add file* (Adicionar arquivo) e em seguida clique em *upload files* (upload de arquivos*);

![](static/upload.png)

- Arraste o arquivo ou clique em *choose your files* para selecionar o arquivo no computador local.

![](static/arrastar.png)

- Após o arquivo ser carregado digite na área *Commit changes* uma mensagem curta e significativa que descreva a alteração feita no arquivo e clique no botão verde *Commit changes*                    
 ***Exemplo***: *Atualiza arquivo conforme a Deliberação XX.*

![](static/commit.png)

## 3. Validação

Após realizar o *commit* do arquivo é necessário verificar se o mesmo foi validado, ou seja, se o arquivo está de acordo com as regras de validação estabelecidas.

Caso **não seja realizado nenhuma alteração** do arquivo carregado o fluxo de validação não será iniciado, pois o sistema irá considerar a mesma *hash*.

- Na página do [Repositório](https://github.com/transparencia-mg/acordo-judicial-reparacao-vale) clique em *Actions*. O campo *All workflows* irá apresentar todos os *commits* realizados no repositório.
- Clique no *commit* desejado e verifique o fluxo de validação.

![](static/actions.png)

- Se o processo for exibido como concluído em todas as etapas, apenas verifique no Portal de Dados Abertos se os dados alterados realmente foram carregados.

![](static/fluxo-validacao.png)

- Se aparecer algum problema durante a validação, siga os passos abaixo:

  - Clique em *validate* e no link que apresenta o erro de validação;
  - Em seguida verifique qual o erro apresentado e faça as correções necessárias.

![](static/erro.png)

---

![](static/erro-link.png)

-------

![](static/erro-frictionless.png)


* Faça novamente o *upload* do arquivo corrigido e repita os passos executados anteriormente.

## 4. Controle de Alterações (Changelog)

Um changelog é um arquivo que contém uma lista selecionada, ordenada cronologicamente, de mudanças significativas para cada versão de um projeto.

Para facilitar que usuários e contribuidores vejam precisamente quais mudanças significativas foram realizadas entre cada versão publicada de um projeto é necessário que todas as alterações relevenantes sejam documentadas.

* Acesse o arquivo [CHANGELOG.md](https://github.com/transparencia-mg/acordo-judicial-reparacao-vale-projetos/blob/main/CHANGELOG.md);
* Clique em *Edit this file*;
* Indique o número correspondente e a data em que o arquivo .xlsx foi atualizado;
  - [x.x.x] - AAAA-MM-DD e
  - Descrição da alteração.


* Após as informações serem inseridas digite na área *Commit changes* uma mensagem curta e significativa que descreva a alteração feita no arquivo e clique no botão verde *Commit changes*.

***Nota***: Para acrescentar um link em algum texto coloque entre colchetes o  [TEXTO] e o link entre parênteses(LINK).
  * **Exemplo**: '[texto] (link)', não deve haver espaço entre o último colchete eo primeiro parêntese.

![](static/controle-alteracoes.gif)


## 5. Acrescentar novos projetos

Caso alguma deliberação crie ou altere o código ou descrição de algum projeto é necessário que essa alteração seja refletida no *enum* da tabela correspondente dentro do arquivo *Schema*. Os valores dentro do *enum*  devem corresponder exatamente a um valor na tabela matriz.

**Exemplo**:
O *enum* da tabela codigo_projeto é representado pelos códigos dos projetos. Caso o arquivo .xlsx contenha algum código de projeto não listado no *enum* da tabela ocorrerá erro no momento da validação.

* Clique em *Schema >> [schema_v1.yaml](https://github.com/transparencia-mg/acordo-judicial-reparacao-vale-projetos/blob/main/schemas/schema_v1.yaml)*;
* Para editar os dados clique em *Edit this file* e localize a tabela que deseja alterar;
* Insira a alteração obedecendo a mesma formatação utilizada;
* Após as informações serem inseridas digite na área *Commit changes* uma mensagem curta e significativa que descreva a alteração feita no arquivo e clique no botão verde *Commit changes*.


![](static/altera-schema.gif)
