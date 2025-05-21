#​ ​Edite​ as classes​ ​nesse​ ​arquivo. Boa ​prova!
from abc import ABC
from dataclasses import dataclass
from typing import Callable, List as ListType

from . import runtime
from .ctx import Ctx
from .runtime import truthy

# Declaramos nossa classe base num módulo separado para esconder um pouco de
# Python relativamente avançado de quem não se interessar pelo assunto.
#
# A classe Node implementa um método `pretty` que imprime as árvores de forma
# legível. Também possui funcionalidades para navegar na árvore usando cursores
# e métodos de visitação.
from .node import Node

#
# TIPOS BÁSICOS
#

# Tipos de valores que podem aparecer durante a execução do programa
Value = bool | str | float | None


class Expr(Node, ABC):
    """
    Classe base para expressões.

    Expressões são nós que podem ser avaliados para produzir um valor.
    Também podem ser atribuídos a variáveis, passados como argumentos para
    funções, etc.
    """


class Stmt(Node, ABC):
    """
    Classe base para comandos.

    Comandos são associdos a construtos sintáticos que alteram o fluxo de
    execução do código ou declaram elementos como classes, funções, etc.
    """


@dataclass
class Program(Node):
    """
    Representa um programa.

    Um programa é uma lista de comandos.
    """

    stmts: list[Stmt]

    def eval(self, ctx: Ctx):
        for stmt in self.stmts:
            stmt.eval(ctx)


#
# EXPRESSÕES
#

@dataclass
class BinOp(Expr):
    """
    Uma operação infixa com dois operandos.

    Ex.: x + y, 2 * x, 3.14 > 3 and 3.14 < 4
    """

    left: Expr
    right: Expr
    op: Callable[[Value, Value], Value]

    def eval(self, ctx: Ctx):
        left_value = self.left.eval(ctx)
        right_value = self.right.eval(ctx)
        return self.op(left_value, right_value)


@dataclass
class Var(Expr):
    """
    Uma variável no código

    Ex.: x, y, z
    """

    name: str

    def eval(self, ctx: Ctx):
        try:
            return ctx[self.name]
        except KeyError:
            raise NameError(f"variável {self.name} não existe!")


@dataclass
class Literal(Expr):
    """
    Representa valores literais no código, ex.: strings, booleanos,
    números, etc.

    Ex.: "Hello, world!", 42, 3.14, true, nil
    """

    value: Value

    def eval(self, ctx: Ctx):
        return self.value


@dataclass
class UnaryOp(Expr):
    """
    Uma operação prefixa com um operando.

    Ex.: -x, !x
    """

    op: Callable[[Value], Value]
    expr: Expr

    def eval(self, ctx: Ctx):
        value = self.expr.eval(ctx)
        return self.op(value)


@dataclass
class Call(Expr):
    """
    Uma chamada de função.

    Ex.: fat(42)
    """

    name: str
    params: list[Expr]

    def eval(self, ctx: Ctx):
        func = ctx[self.name]
        params = []
        for param in self.params:
            params.append(param.eval(ctx))

        if callable(func):
            return func(*params)
        raise TypeError(f"{self.name} não é uma função!")


@dataclass
class Assign(Expr):
    """
    Atribuição de variável.

    Ex.: x = 42
    """

    name: str
    value: Expr

    def eval(self, ctx: Ctx):
        value = self.value.eval(ctx)
        ctx[self.name] = value
        return value


@dataclass
class List(Expr):
    """
    Representa uma lista de expressões.

    Ex.: [1, 2, "a"]
    """

    elems: ListType[Expr]

    def eval(self, ctx: 'Ctx'):
        value = []
        for elem in self.elems:
            value.append(elem.eval(ctx))
        return value


#
# COMANDOS E DECLARAÇÕES
#

@dataclass
class Print(Stmt):
    """
    Representa uma instrução de impressão.

    Ex.: print "Hello, world!";
    """

    expr: Expr

    def eval(self, ctx: Ctx):
        value = self.expr.eval(ctx)
        runtime.print(value, end="\n")


@dataclass
class VarDef(Stmt):
    """
    Representa uma declaração de variável.

    Ex.: var x = 42;
    """

    name: str
    value: Expr | None

    def eval(self, ctx: Ctx):
        value = None if self.value is None else self.value.eval(ctx)
        ctx[self.name] = value


@dataclass
class Block(Node):
    """
    Representa bloco de comandos.

    Ex.: { var x = 42; print x;  }
    """

    stmts: list[Stmt]

    def eval(self, ctx: Ctx):
        for stmt in self.stmts:
            stmt.eval(ctx)


@dataclass
class While(Stmt):
    """
    Representa um laço de repetição.

    Ex.: while (cond) { ... }
    """

    condition: Expr
    body: Stmt

    def eval(self, ctx: 'Ctx'):
        while truthy(self.condition.eval(ctx)):
            self.body.eval(ctx)
