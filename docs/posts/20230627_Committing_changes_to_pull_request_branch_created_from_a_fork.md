---
comments: true
tags:
  - Fluxo de Trabalho DCTA
---

# Como conferir PR criados em repositórios forkados

- Dúvida surgiu durante avaliação [deste PR](https://github.com/transparencia-mg/violencia-contra-mulher/pull/1).
- [Este post](https://my-base-knowledge.braico.me/1.0.0/texts/20230627_como_fazer_checkout_em_um_branch_fork_pr) também explica como realizar o procedimento.
- Caso a avaliação não demande nenhuma mudança adicional (novos commits) a solução proposta [neste post](https://stackoverflow.com/a/65172690/11755155) atende bem a demanda com `gh pr checkout <PR-NUMERO>` (necessário instalar a CLI do github para ter acesso ao comandos `gh`).
    - Mudanças adicionais também podem ser sugeridas na revisão do PR e não realizadas diretamente via novo commit.
- Para mudanças adicionais via novos commits, a sugestão que mais atendeu foi clonar o repositório fork, conforme sugerido no post [Committing changes to a pull request branch created from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/committing-changes-to-a-pull-request-branch-created-from-a-fork).

```python
# Acesse o repo forkado para ter acesso ao remote
git clone <REMOTE>
cd <NOME-REPO-CLONADO> # Cuidado para não clonar com o nome de algum repo já existente
git checkout <BRANCH-DESEJADO>

# Faça seus testes
# Caso necessite realizar algum commit basta
git push origin <BRANCH-DESEJADO> # Your new commits will be reflected on the original pull request on GitHub.com.
```
