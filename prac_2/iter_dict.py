"""
    Сделать свою реализацию словаря, в котором будет переопределен метод __iter__,
    чтобы он возвращал итератор не по ключам, а сразу по паре ключ, значение.
    Используйте наследование от встроеного типа dict, и полиморфизм для метода __iter__.
    Конструктор базового класса переопределять не нужно.
    Чтобы получить пары ключ-значение используйте либо метод базового self.items() либо
    функцию zip() для self.keys() и self.values()
"""

from typing import Iterator, Tuple, Hashable, Any


class MyDict(dict):  # ToDo Наследование от класса dict
    def __iter__(self) -> Iterator[Tuple[Hashable, Any]]:
        for i, k in self.items():
            yield i, k


if __name__ == '__main__':
    ll = {1: 'c', 2: '2'}
    print(next(MyDict.__iter__(ll)))