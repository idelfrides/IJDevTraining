"""Decoratos in python
-------
[ 1 ]

# @property  

---

1) Vantagens das propriedades em Python

Vamos começar contextualizando um pouco. Para que usaríamos propriedades em Python?

As propriedades podem ser consideradas a maneira em Python de se trabalhar com atributos, pois:

    A sintaxe usada para definir as propriedades é muito concisa e legível.
    Você pode acessar atributos de instância exatamente como se fossem atributos públicos e, 
    ao mesmo tempo, usar a "magia" dos intermediadores (getters e setters) para validar
    novos valores e evitar o acesso ou a modificação dos dados diretamente.
    Ao usar @property, você pode "reutilizar" o nome de uma propriedade para evitar criar
    nomes novos para os getters, setters e deleters.

2) Introdução aos decorators ( CONCEITO )

Uma função decorator é, basicamente, uma função que adiciona uma nova funcionalidade 
a uma função que é passada como argumento. 
Usar uma função decorator é como adicionar granulado de chocolate a um sorvete. 
Ela dá  uma nova funcionalidade a uma função existente sem modificá-la.


O que aconteceu de fato, foi, a function
'funcao_inicial' foi passada como argumento para o decorator 'test_decorator'

e perceba que quem é chamada é a  funcao_inicial ( a function decorada )

A @property é um decorator integrado à função property() em Python
(texto em inglês). Ela é usada para dar uma funcionalidade "especial" a 
certos métodos para fazer com que ajam como getters, setters ou deleters 
quando definimos as propriedades em uma classe.

Atributos de instancia --> aqueles definidos no def __init__(self): da classe.

Especificamente, você pode definir três métodos para uma propriedade:

    Um getter - para acessar o valor do atributo.
    Um setter - para definir/modificar o valor do atributo.
    Um deleter - para excluir o atributo de instância.

---

[ 2 ]  Método de classe 

# @classmethod

---

O risco em se utilizar métodos de classe erroneamente

Uma característica bastante importante dos métodos de classe em Python é
que um método de classe só pode invocar outros métodos de classe. 
Esse comportamento se dá em virtude das passagens de argumentos implícitas
de Python nas chamadas de métodos. Quando invocamos os métodos de classe o Python 
passa implicitamente a própria classe como primeiro argumento do método. 
Quando invocamos métodos da instância Python passa implicitamente a própria 
instância como primeiro argumento. Logo, vamos considerar o seguinte código:

OBS: métodos de classes podem invocar somente outros métodos de classes, 
e nunca métodos de instancia.

---

[ 3 ] Dataclass

# @dataclass

"""

# exemplo de decorator inicial/conceitual

# def test_decorator(f):
#     def nova_funcao():
#         f()
#         print("I am a DECORATOR over [ funcao_inicial ] function ")
#     return nova_funcao

# @test_decorator
# def funcao_inicial():
#     print("Funcionalidade inicial")

# funcao_inicial()


# Rogéria Nantes Nunes Braga

class House():

    def __init__(self, price) -> None:
        self._price = price   # atributo de instancia

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print(
                f"\nINVALID NEW PRICE [{new_price}]. PLEASE ENTER A VALID VALUE")

    @price.deleter
    def price(self):
        del self._price


class MyClass:

    def __init__(self, some_parameter) -> None:
        self.attr_value = some_parameter

    @classmethod
    def some_class_method(cls):
        return cls.some_instance_method()

    def some_instance_method(self):
        print(f"some_instance_method -->  {self.attr_value}...")
        return 1


class Livro:
    def __init__(self, titulo, paginas=None):
        self.titulo = titulo
        self.paginas = [] if not paginas else paginas

    @classmethod
    def cria_a_partir_de_paginas(cls, paginas):
        return cls(titulo="", paginas=paginas)
