Nesse exercício, vamos extender a gramática de Lox para suportar listas. Para
manter a simplicidade, vamos assumir que uma lista é delimitada por colchetes e
cada elemento é separado por vírgulas, como abaixo:

```lox
[1, x, 40 + 2, "string"]
```

Lembre-se de suportar listas vazias

```lox
[]
```

e listas dentro de listas

```lox
[[1, 2, [3, [4]]]]
```

Também queremos aceitar a última vírgula opcional:

```lox
[   
    "primeiro", 
    "segundo",
]
```

Mas cuidado para não aceitar uma vírgula perdida `[,]`.

Você deve implementar suporte a listas na gramática e implementar o método eval
mais ou menos da seguinte forma:

```python
@dataclass
class List(Expr):
    elems: list[Expr]

    def eval(self, ctx: Ctx):
        value = []
        for elem in self.elems: # ou outro meio de produzir os elementos da lista
            value.append(elem.eval(ctx))
        return value
```