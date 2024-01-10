# Atualização e validação no GitHub

## Premissas

Sempre que os dados forem alterados as novas informações devem ser atualizadas no repositório do GitHub.

1) O nome da planilha não deve ser alterado;
2) A ordem das colunas não podem ser alteradas;
3) O arquivo deve ser salvo no formato .xlxs.

## 1. Atualização

- Clicar na pasta "dataset" para alterar os aquivos: README, CHANGELOG, CONTRIBUTING, DATAPACKEGE.yaml
    
  **NÃO ALTERAR/EDITAR DATAPACKEGE.json, apenas mexer no DATAPACKEGE.yaml.**

- Clicar na pasta "upload" para os arquivos em excel (XLSX)

![image](https://github.com/transparencia-mg/handbook/assets/53793354/4a172a62-1d24-4192-9305-e8cfbe956984)

As modificações automáticas só serão publicadas no CKAN se as alterações forem realizadas nestas pastas.

### 1.1 Upload

Após a atualização dos dados, acesse a sua conta do [Github](https://github.com/login) e em seguida acesse o repositório do conjunto de dados a ser alterado.

- Na pasta **/upload/** clique em *Add file* (Adicionar arquivo) e em seguida clique em *upload files* (upload de arquivos*);

![image](https://github.com/transparencia-mg/handbook/assets/53793354/59024edd-60e0-4857-9783-dae6eb93d2b0)

- Arraste o arquivo ou clique em *choose your files* para selecionar o arquivo no computador local.

![image](https://github.com/transparencia-mg/handbook/assets/53793354/0da232cc-69c1-4636-bf72-dcb0a868853f)

- Após o arquivo ser carregado digite na área *Commit changes* uma mensagem curta e significativa que descreva a alteração feita no arquivo e clique no botão verde *Commit changes*                    
 ***Exemplo***: *Atualiza arquivo conforme a Deliberação XX.*

![image](https://github.com/transparencia-mg/handbook/assets/53793354/0d2068c9-3c59-4306-bebf-49accf8ab0e9)


### 1.2 Alterações nos demais arquivos: README, CHANGELOG, CONTRIBUTING, DATAPACKEGE.yaml

Usaremos como exemplo o arquivo "Changelog".

* Acesse o arquivo [CHANGELOG.md]() dentro da pasta dataset;
* Clique em *Edit this file*;
  
![image](https://github.com/transparencia-mg/handbook/assets/53793354/a48d687a-87c5-4e31-ab19-2f1b090b7bbf)

* Após as informações serem inseridas digite na área *Commit changes* uma mensagem curta e significativa que descreva a alteração feita no arquivo e clique no botão verde *Commit changes*.

***Nota***: Para acrescentar um link em algum texto coloque entre colchetes o  [TEXTO] e o link entre parênteses(LINK).
  * **Exemplo**: '[texto] (link)', não deve haver espaço entre o último colchete eo primeiro parêntese.


## 2. Validação

Após realizar o *commit* do arquivo é necessário verificar se o mesmo foi validado, ou seja, se o arquivo está de acordo com as regras de validação estabelecidas.

Caso **não seja realizado nenhuma alteração** do arquivo carregado o fluxo de validação não será iniciado, pois o sistema irá considerar a mesma *hash*.

- Na página do Repositório clique em *Actions*. 

![image](https://github.com/transparencia-mg/handbook/assets/53793354/08db381f-5954-40ef-b526-ba87f21fc14d)

- Se o processo for exibido como concluído em todas as etapas, apenas verifique no Portal de Dados Abertos se os dados alterados realmente foram carregados.

- Se aparecer algum problema durante a validação, siga os passos abaixo:

  - Clique em *validate* e no link que apresenta o erro de validação;
  - Em seguida verifique qual o erro apresentado e faça as correções necessárias.

![image](https://github.com/transparencia-mg/handbook/assets/53793354/78fe8ce3-0ce1-41c6-8603-09c7c776fb61)

* Faça novamente o *upload* do arquivo corrigido e repita os passos executados anteriormente.

