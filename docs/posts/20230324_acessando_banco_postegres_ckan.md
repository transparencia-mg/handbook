---
comments: true
tags:
  - CKAN
  - SQL
  - Postgres
---

# Acessando banco de dados Postegres via terminal Linux

- Logar no banco Postgress utilizando o terminal:

```
# Abaixo algumas alternativas

sudo -u postgres psql
psql
```

- Logado, para listar todos os bancos de dados existentes basta utilizar `\l`:

```
postgres-# \l
```

- Selecionar um dos bancos:

```
postgres-# \c database_name
```

- Visualizar todas as tabelas do schema selecionado:

```
postgres-# \dt

# Alternativa
postgres-# SELECT * FROM pg_catalog.pg_tables;
```

- Durante a criação de consultas não esquecer de incluir o `;` no final da mesma.

- Para sair basta utilizar  `\q`.

## Referências

- [Resposta Stackoverflow](https://stackoverflow.com/a/769706/11755155)
- [Lista de comandos úteis](https://stackoverflow.com/a/47185648/11755155)