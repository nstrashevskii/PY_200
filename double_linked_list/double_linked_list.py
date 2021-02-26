"""
Двусвязный список на основе односвязного списка.
    Самостоятельное задание. В двусвязном списке должны быть следующие методы:
    - **`__str__`**
    - **`__repr__`**
    - **`__getitem__`**
    - **`__setitem__`**
    - **`__len__`**
    - **`insert`**
    - **`index`**
    - **`remove`**
    - **`append`**
    - **`__iter__`**
    Необязательно все эти методы должны быть переопределены в явном виде. По максимуму используйте
    наследование, если поведение списков в контексте реализации указанных метод схоже.
    С точки зрения наследования по минимуму перегружайте методы. При необходимости рефакторите базовый класс,
    чтобы локализовать части кода во вспомогательные функции, которые имеют различное поведение
    в связном и двусвязном списках.
    Стремитесь к минимизации кода в дочернем классе.
    Есть какой-то метод класса DoubleLinkedList хотите отработать в явном виде ещё раз, не возбраняется.
"""

from typing import Any, Sequence, Optional, Iterator
from collections.abc import Iterable
from py_class.LinketList import LinkedList


class DoubleLinkedList(LinkedList):
    class DoubleLinkedNode(LinkedList.Node):
        def __init__(self, value: Any,
                     next_: Optional['Node'] = None,
                     prev_: Optional['Node'] = None):
            super().__init__(value, next_)
            self.prev = prev_

        @property
        def prev(self):
            return self.__prev

        @prev.setter
        def prev(self, prev_):
            self._check_node(prev_)
            self.__prev = prev_

        def __repr__(self) -> str:
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"Node({self.value}, {self.prev}, {self.next})"

    def __init__(self, data: Sequence = None):
        super().__init__(data)

    @staticmethod
    def __linked_nodes(left, right) -> None:
        left.next = right
        right = left.prev


if __name__ == '__main__':
    ll = DoubleLinkedList([1, 2, 3, 4])
    print(DoubleLinkedList.__repr__(ll))
    ll.insert(3, 5)
    print(DoubleLinkedList.__repr__(ll))
    print(DoubleLinkedList.index(ll, 2))
    print(ll)
    ll.append(67)
    print(DoubleLinkedList.__repr__(ll))
    ll.remove(3)
    print(ll)