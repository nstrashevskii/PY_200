from typing import Any, Sequence, Optional


class LinkedList:
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
            if not isinstance(next_, self.__class__) and next_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {next_.__class__.__name__}"
                raise TypeError(msg)
            self.__next = next_

        def __repr__(self):
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"Node({self.value}, {self.next})"

        def __str__(self):
            """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
            return f"{self.value}"

    def __init__(self, data: Sequence = None):
        """Конструктор связного списка"""
        self.__len = 0
        self.head = None
        self.tail = None

        if data:  # ToDo Проверить, что объект итерируемый. Метод self.is_iterable
            for value in data:
                self.append(value)

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f"{[value for value in self]}"

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"{type(self).__name__}({[value for value in self]})"

    def __len__(self):
        return self.__len

    def __step_by_step(self, index: int):
        """Встроенный метод, который возвращает узел по указанному индексу"""
        if not isinstance(index, int):
            raise TypeError('Введенное значение не int')

        if not 0 <= index < self.__len:
            raise IndexError('Индекс вышел за пределы списка')

        current_node = self.head

        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, item: int) -> Any:
        current_node = self.__step_by_step(item)
        return current_node.value

    def __setitem__(self, key: int, value: Any):
        current_node = self.__step_by_step(key)
        current_node.value = value

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.__linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.__len += 1

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def to_list(self) -> list:
        return [value for value in self]

    def insert(self, index: int, value: Any) -> None:
        if index == 0:
            insert_node = self.Node(value)
            self.__linked_nodes(insert_node, self.head)
            self.head = insert_node
            self.__len += 1

        elif 1 <= index <= self.__len:
            insert_node = self.Node(value)
            pref_node = self.__step_by_step(index - 1)
            current_node = pref_node.next

            self.__linked_nodes(insert_node, current_node)
            self.__linked_nodes(pref_node, insert_node)

            self.__len += 1

        elif index > self.__len:
            self.append(value)

    def clear(self) -> None:
        self.__len = 0
        self.head = None

    def index(self, value: Any) -> int:
        for i in enumerate(self):
            if value == i[1]:
                return i[0]

    def remove(self, value: Any) -> None:
        index = self.index(value)
        if index == 0:
            self.head = self.__step_by_step(1)
            self.__len -= 1

        elif 1 <= index < self.__len - 1:
            del_node = self.Node(value)
            pref_node = self.__step_by_step(index - 1)
            current_node = self.__step_by_step(index + 1)

            self.__linked_nodes(pref_node, current_node)

            self.__len -= 1
        elif index == self.__len - 1:
            del_node = self.Node(value)
            print(del_node)
            self.tail = self.__step_by_step(index - 1)
            self.__len -= 1

    def sort(self) -> None:
        ...

    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        ...


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4])
    print(LinkedList.__repr__(ll))
    ll.insert(3, 5)
    print(LinkedList.__repr__(ll))
    print(LinkedList.index(ll, 2))
    print(ll)
    ll.append(67)
    print(LinkedList.__repr__(ll))
