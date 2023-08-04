---
comments: true
tags:
  - Minas de Dados
---

# Preparação apresentação Minas de Dados e a importância que deve ser dada ao processo de documentação de uma base de dados.

No [issue 75 do repositório handbook](https://github.com/transparencia-mg/handbook/issues/75) começamos a discutir o conteúdo da apresentação que a DCTA realizará para o grupo Minas de Dados dia 17/08/2023.
Na [apresentação](https://transparencia-mg.github.io/reveal.js/presentations/20230328_gerenciar_dados_abertos_com_dpckan/index.html) que realizamos para OKBR sobre as ferramentas que estamos desenvolvendo para gerenciar abertura de dados encontrei o link para [esta apresentação relâmpago](https://www.youtube.com/watch?v=JUW60w1jDdM&t=1346s) realizada por Francisco no CodaBr21.
Por acreditar que a mesma pode servir de fonte de inspiração para nosso encontro dia 17/08/2023 incluo aqui a transcrição revisada[^1] desta fala[^2].

### Fala Francisco CodaBr21 - Apresentações Relâmpago

A Diretoria Central de Transparência Ativa - DCTA/CGE é responsável por gerenciar o [Portal de Dados Abertos do Estado de Minas Gerais](https://dados.mg.gov.br/), buscando, principalmente, aprimorar a qualidade das informações ali divulgadas.
Para alcançar esse objetivo, nossa principal estratégia é o estímulo à produção de documentação padronizada das bases de dados publicadas.
Esta medida tenta alcançar tanto nosso público interno, aqui representado por nossos colegas servidores públicos, quanto o externo, ou a população de um modo geral.
Uma brincadeira para ilustrar a importância da documentação no processo de publicação de uma base de dados é a pergunta **se uma informação só existe com a pessoa que a gerou, e essa pessoa não está disponível, essa informação realmente existe?**[^3].

Mas antes de falar mais sobre este processo é necessário contextualizar as ferramentas do ecossistema em que ele se encaixa.

A primeira delas é a [Frictionless](https://frictionlessdata.io/), uma iniciativa da [Open Knowledge](https://okfn.org/) que visa resolver a fricção no trabalho de dados.
**Essa fricção acontece quando recebemos planilhas sem explicações claras sobre o significado de cada coluna, ou quando os caracteres estão desconfigurados, ou ainda quando a leitura de um arquivo `.csv` é prejudicada por delimitadores incorretos.**
Todo esse tempo gasto antes do trabalho real é o que chamamos de fricção, e as ferramentas [Frictionless](https://github.com/frictionlessdata) buscam acabar com essa fricção para favorecer o trabalho de fato[^4].
Neste sentido, Frictionless oferece um padrão de metadados ou vocabulário padronizado para descrever um conjunto de dados que chamamos de pacote de dados ou datapackage[^5].
**Essas especificações podem ser utilizadas em diversos softwares para a engenharia de dados, facilitando o fluxo de informações**.

Uma outra seria a aplicação da filosofia [Docs Like Code](https://www.docslikecode.com/) em todas as fases[^6] que compõem o processo de publicação de dados.
Essa abordagem é baseada na ideia de tratar a documentação como tratamos o código-fonte de um projeto. Assim como o código é versionado, revisado e mantido em repositórios, a documentação também é tratada da mesma forma.

Além de gerenciar o [Portal de Dados Abertos do Estado de Minas Gerais](https://dados.mg.gov.br/), a DCTA/CGE também cuida do [Portal da Transparência](https://www.transparencia.mg.gov.br/), divulgando informações sobre arrecadação e execução de despesas do estado.
Como forma de promover a abertura de bases de maneira perene e testar o modelo de documentação que nós mesmo estamos propondo publicamos todas as bases do [Portal da Transparência](https://www.transparencia.mg.gov.br/) em formato aberto, com documentação em texto simples e utilizando sistemas de controle de versão para garantir a rastreabilidade das alterações ao longo do tempo.
Os benefícios percebidos são economia de tempo em equipes cada vez mais sobrecarregadas, colaboração facilitada, permitir que as mudanças sejam compreendidas em contexto, evitar a obsolescência da documentação e garantir o foco no trabalho de análise dos dados[^4].
Toda esta abordagem permitiu construir todos artefatos de documentação automaticamente para publicação no [Portal de Dados Abertos do Estado de Minas Gerais](https://dados.mg.gov.br/)[^7].

Seguindo então para a abordagem em Minas Gerais, adotamos estes padrões de metadados propostos pela Frictionless em um processo sucinto, quase como um código-fonte, o que nos ajuda a armazenar e revisar as informações adequadamente.

Isso economiza tempo e evita sobrecarregar, ainda mais as equipes.


A documentação precisa melhorar constantemente para evitar que ela fique obsoleta e para preservar o contexto das informações. Assim, garantimos que os dados estejam corretamente interpretados e validados, tornando-se legíveis tanto para humanos quanto para máquinas.

Por fim, após essa etapa de documentação, é o momento de fazer a publicação para o consumo das pessoas no catálogo do estado de Minas. Usamos o modelo de convite para um repositório específico, gerando um processo de implantação dessa documentação.

Espero que agora o texto esteja mais claro e bem estruturado. Se tiver mais alguma dúvida, é só me perguntar!







[^1]: Revisão realizada com auxílio do [ChatGPT](https://chat.openai.com/).
[^2]: Transcrição autogerada do vídeo do YouTube.
[^3]: Podemos complementar esta brincadeira parafraseando [@mtholder](https://twitter.com/kcranstn/status/370914072511791104?s=20), para dizer que você, de 6 meses atrás, não está mais disponível.
[^4]: Trabalho de fato aqui compreendido como o estudo e entendimento dos dados (problemas, contexto, limitações) não possuindo para este atalhos.
[^5]: [O que é um datapackage](https://specs.frictionlessdata.io/#overview).
[^6]: Escrita, revisão, construção e publicação.
[^7]: https://github.com/transparencia-mg/age7
