"""
Expressões regulares simples
============================

Complete o atributo regex = r"..." no retorno de cada função com
a expressão regular correta que aceita todos os exemplos da seção "aceita" e
recusa todos os exemplos da seção "recusa".

Se a expressão contiver size caracteres ou menos, a questão será considerada
100% correta. Se a questão contiver entre size e max_size, será considerada 70%
correta. Se for maior que isso, será considerada incorreta, idependente de acertar
ou não os exemplos.

Você pode testar essa questão usando o pytest ou executando este arquivo
diretamente.
"""

from lox.ax import check_re

# Classe de exemplo já respondida. Observe que existe uma lista de exemplos
# que a regex deve aceitar, seguida por uma lista em branco e uma lista de
# exemplos que a regex deve recusar
@check_re(size=4, max_size=6, skip=True)
def exemplos_de_números():
    """
    aceita:
        1
        42
        10
        20
        007

    recusa:
        1.2
        .1
    """
    return r"\d+"

#
# A partir daqui é com você!
#

@check_re(size=17, max_size=32)
def nome_minúsculo_com_a_notação_de_ponto_pt0_75():
    """
    aceita:
        foo
        foo.bar
        foo.bar.baz
        x.y.z
        verylongname

    recusa:
        .foo
        foo..bar
        foo.
        foo.bar.
        foo$foo
        ...
    """
    return r"[a-z]+(\.[a-z]+)*"

@check_re(size=13, max_size=20)
def nome_de_variável_simples_começando_com_letra_minúscula_pt0_75():
    """
    aceita:
        foo
        bar
        foo_bar
        fooBar
        x1
        _Foo
        a
        b
        _

    recusa:
        Foo
        FooBar
        FOO
        2foo
    """
    return r"[_a-z]\w*"

@check_re(size=11, max_size=16)
def número_hexadecimal_positivo_com_letras_maiúsculas_pt0_75():
    """
    aceita:
        0x0
        0x01
        0xFF
        0x1F
        0xFA32A3

    recusa:
        0xf
        FF
        0x
        0x1G
        -0xAF
    """
    return r"0x[0-9A-F]+"

@check_re(size=23, max_size=45)
def número_inteiro_com_underscores_obrigatórios_separando_milhares_pt1_00():
    """
    aceita:
        0
        1
        42
        123
        1_000
        12_345
        20_240_519
        123_456_789

    recusa:
        01
        10_00
        3000
        1_0000
        1__000_000
    """
    return r"0|[1-9]\d{0,2}(_\d{3})*"
@check_re(size=33, max_size=60)
def número_com_parte_decimal_opcional_e_notação_científica_pt1_00():
    """
    aceita:
        42
        1.000
        13.24
        1.2e-10
        3.13e+3
        -1.2345
        1000.4e-1000
        1e+10
        2e-5
        -1

    recusa:
        01
        1e10
        1E+10
        +1
        1.
        .1415
        1$0
        -1 1234 12_34
    """
    return r"-?([1-9]\d*|0)(\.\d+)?(e[+-]\d+)?"
