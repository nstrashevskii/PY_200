"""
Сделать DoubleLinkedNode наследуясь от класса Node
    1. В конструкторе DoubleLinkedNode обязательно вызвать конструктор базоваго класса и определить дополнительный
        атрибут self.prev, хранящий в себе ссылку на предыдущий узел. Тем сымым дополняя функциональность базового класса,
        сохраняя его логику.
    2. Атрибут экземпляра prev сделать свойством prev. Определить для него getter и setter c проверками аналогичными
        свойству next в класса Node.
    3. В классе Node вынести проверку присваемого узла в setter свойства next во внутренний метод.
        Данный метод должен быть внутренним и не доступным пользователю.
    4. В классе DoubleLinkedNode воспользоваться методом из прошлого шага, чтобы проверить setter свойства prev.
        Каким должен быть этот метод?
            - protected
            - private
    5. Для DoubleLinkedNode перегрузить метод __repr__, метод __str__ оставить без изменений.
"""
from typing import Any, Optional


class Node:
    """
    Внутренний класс, класса LinkedList.
    Пользователь напрямую не работает с узлами списка, узлами оперирует список.
    """

    def __init__(self, value: Any, next_: Optional['Node'] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # Вызывается сеттер

    @property
    def next(self):
        """Getter возвращает следующий узел связного списка"""
        return self.__next

    @next.setter
    def next(self, next_: Optional['Node']):
        """Setter проверяет и устанавливает следующий узел связного списка"""
        self._check_node(next_)
        self.__next = next_

    def _check_node(self, node: 'Node'):
        if not isinstance(node, self.__class__) and node is not None:
            msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                  f"или None, не {node.__class__.__name__}"
            raise TypeError(msg)

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"Node({self.value}, next_={None})"

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f"{self.value}"


class DoubleLinkedNode(Node):
    def __init__(self, value: Any,
                 next_: Optional['Node'] = None,
                 prev: Optional['Node'] = None, prev_=None):
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
