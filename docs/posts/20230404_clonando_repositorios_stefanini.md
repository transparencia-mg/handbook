---
comments: true
tags:
  - Fluxo de Trabalho DCTA
---

# Clonando Repositórios Stefanini

- Repositórios para clonar:
  - [work-stefanini](https://github.com/transparencia-mg/work-stefanini)
  - [ckanext-datapackage-creator](https://github.com/transparencia-mg/ckanext-datapackage-creator)

- Clonar os dois repositórios localmente (em uma pasta diferente dos repositórios da organização `transparencia-mg`). Não queremos utilizar a opção de `fork` para deixar os repositórios "copiadas" totalmente separados dos originais.

```
git clone https://github.com/transparencia-mg/ckanext-datapackage-creator.git

git clone https://github.com/transparencia-mg/work-stefanini.git
```

0bs.: Nos comandos acima pode ser necessário utilizar `ssh` no lugar de `https` dependendo das configuração da sua máquina. 

- Na interface gráfica do GitHub crie dois novos repositórios em sua organização pessoal: `work-stefanini` e `ckanext-datapackage-creator`.

```
git remote rm origin
git remote add origin https://github.com/<sua-organizacao>/ckanext-datapackage-creator.git
git remote -v
```

- No repositório original da transparência:

```
gh issue list -s all -L 2500 --json title --json body --json comments > <caminho-relativo-novo-repo>/issues.json
```

Obs.: Necessário [gh CLI](https://cli.github.com/) estar instalado na máquina.

```
# Adiciona novo issues.json
git add .

# Commita novo arquivo
git commit -m "Add issues.json"

# Push para novo repositório
git push origin main
```

