O exercício anterior implementou suporte ao `while` na sintaxe. Agora vamos 
implementar o suporte ao `while` no interpretador implementando o método
`While.eval`.

Lembre-se de alguns detalhes da semântica do Lox:

1. O `while` avalia a condição e somente executa o corpo se ela for verdadeira.
2. Somente `false` e `nil` são considerados falsos, portanto os laços abaixo
   não terminam: 
   -  `while (0) do_something()`
   -  `while ("") do_something()`
3. Lox não possui comandos como `break` e `continue`, o que facilita 
   consideravelmente a implementação dos laços.

Implemente o método `eval` na classe `While`. Depois, edite o arquivo
`maior.lox` e implemente um programa que imprime o maior número entre duas
opções. Importante: nossa linguagem não possui if, então temos que implementar o
programa usando whiles.