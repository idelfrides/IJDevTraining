#!usr/bin/env python3
# -*- coding: utf-8 -*-


'''
---------------------------------------------------------------------------------------
                            CLASSES ABSTRATAS EM PYTHON
---------------------------------------------------------------------------------------

Trata-se de classes que definem (criam) atributos e métodos, porém não os
implementa.

As classes abstratas são usadas para definir atributos (características) e ações (métodos) 
que são implementados/utilizados em outras classes que são chamadas classes filhas.

São usadas em projetos de grande porte onde vários componentes implementam a mesma ação, 
ou seja, possuem a mesma interface.

Python não possui/define classes abstratas de maneira nativa, e sim possui um módulo
base de classes abstratas chamado 'abc', no qual é criado uma class base abstrata que é ABC.

Em Python uma classe é abstrata se ela tiver pelo menos 1 método abstrato.
Ex. Classe Animal é abstrata

Um método é abstrato quando é decorado com uma função chamada
@abstractmethod ( com '@' colado a ele para representar um decorator (decorador) )

OBS.: para funcionar na prática as classes derivadas têm q obrigatoriamente implementar
todos os métodos abstratos definidos na classe mãe (a class q herda da class ABC e define métodos abstratos)

'''

# --------------------------------------------------------------------------


from abc import ABC, abstractmethod
from utilLibs.lib_manager import (
    print_log
)


class Animal(ABC):
    """
    # Abstract class Animal
    ### Is a super class unhiered by other classes called subclass

    """

    def __init__(self) -> None:
        self.name_type = "Abstract class, Animal(ABC)"

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def talk(self):
        print_log(f'I AM A ABSTRACT METHOD - TALK')
        print_log(f'\n\n--------------------------------')

    @abstractmethod
    def eat(self):
        pass


class Person(Animal):
    """# class Person(Animal) """

    def move(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM PERSON AND I CAN MOVE')

    def eat(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A PERSON AND I EAT PIZZA')
        return

    def talk(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A PERSON AND I can TALK with other person or by myself')
        return


class Dog(Animal):
    """# class Dog(Animal) """

    def move(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A DOG AND I CAN LATIR')

    def talk(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A DOG AND I CAN NOT TALK')
        return

    def eat(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A DOG AND I CAN EAT FOOD')
        return


class DogClass():

    def walk(self):
        print_log('*walking*')
        return

    def speak(self):
        print_log('Speak DogClass | Woof! wwwwwwwwwwwwwwwwwww')
        return


class JackRussellTerrier(DogClass):
    def speak(self):
        print_log('Speak JackRussellTerrier | Arff! Aaaaaaaaaaaaaaaaaaaaaaaaaa')


class Cat(Animal):
    """# class Cat(Animal) """

    def move(self):
        print_log(
            f'MY NAMA IS [ {self.name_type} ]. I AM A CAT E EU POSSO MIAR')

    def eat(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A DOG AND I CAN NOT TALK')
        return

    def talk(self):
        return super().talk()


class Lion(Animal):
    """# class Lion(Animal) """

    def move(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. EU SOU UM LEÃO E POSSO RUGIR')

    def eat(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A LION AND I CAN EAT FOOD')
        return

    def talk(self):
        return super().talk()


class Eagle(Animal):
    """# class Eagle(Animal) """

    def move(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A EAGLE AND I CAN MAKE A SOUND')

    def eat(self):
        print_log(
            f'MY NAME IS [ {self.name_type} ]. I AM A DOG AND I CAN EAT FOOD')
        return

    def talk(self):
        return super().talk()
