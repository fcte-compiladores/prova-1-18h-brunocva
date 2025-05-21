[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rvOmLE7f)
# Compiladores / Prova 1


## Instruções 

Salve seu nome e matrícula e horário da turma na qual você está matriculado(a)
no arquivo provas.py. Depois execute esse script usando `python3 prova.py` (ou
`python prova.py`, vai depender da sua configuração)` Ele selecionará uma das
versões de prova, irá salvá-la na pasta atual e apagará as outras. **PREENCHA A
MATRÍCULA CORRETAMENTE** para não resolver a prova errada.

## Sobre a prova

Você deve selecionar 5 das 6 questões disponíveis. Edite o arquivo prova.py de 
acordo com as questões que você quer que sejam corrigidas.


## Regras

Você pode fazer a prova no computador do laboratório ou no computador pessoal e
durante a prova pode acessar alguns sites:

* O livro https://craftinginterpreters.com/contents.html
* O Github classroom da disciplina.
* O repositório do Github da turma.
* Seu repositório da prova.
* https://docs.astral.sh/uv/ para baixar o UV, se necessário

A utilização de qualquer outro site é proibida. Em particular a utilização de
modelos de linguagem como ChatGPT, DeepSeek, Gemini, Grok, etc está
EXPRESSAMENTE PROIBIDA! A utilização de qualquer um desses modelos durante a
prova implica na anulação da mesma.

Além disso, a utilização de qualquer sistema de mensageria (WhatsApp, Telegram,
Gmail, Instagram, TikTok etc) tanto no celular quanto no computador também
implica na anulação da prova. Desligue as notificações do celular durante a
prova e se precisar atender o celular em alguma emergência, fale antes com o
professor.


## Rodando os exemplos e testes

A prova usa o `uv` para gerenciar sua versão do Python. Você pode usar outras
ferramentas se quiser, mas já está tudo configurado para funcionar com o `uv`.
Os comandos abaixo podem ser úteis:

    # Roda os testes
    uv run pytest 
    uv run pytest --maxfail=1       # para no 1o erro
    uv run pytest tests/test_q1.py  # seleciona uma questão
    uv run pytest -l                # mostra variáveis locais no traceback
    uv run pytest --tb=no           # relatório curto, também aceita short, line

    # Executa o lox
    uv run lox --help
    uv run lox some_file.lox

    # Executa a questão 1
    uv run q1-regex.py


## Entrega

A prova será entregue subindo um commit para a branch master. Você pode usar
comandos do git, mas já sabendo que a rede da UnB bloqueia mais acessos que o
ideal, se planeje para ter que subir os arquivos importantes manualmente.

Somente os seguintes arquivos serão considerados na correção:

* lox/ast.py
* lox/grammar.lark
* lox/transformer.py
* q1-regex.py
* q6-arquitetura.md
* fib.lox ou maior.lox, dependendo da prova.

Se precisar subir os arquivos manualmente, confira se todos dessa lista estão
no repositório.