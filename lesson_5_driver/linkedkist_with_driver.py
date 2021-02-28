"""
Реализовать класс LinkedListWithDriver от класса LinkedList.
Дочерний класс должен уметь работать с реализованными ранее драйверами.
    1. Реализовать свойство driver, которое будет возвращать используемый драйвер и проверять, что устанавливаемый
        драйвер является экземпляром класса IStructureDriver.
    2. Реализовать метод read, который с помощью встроенного драйвера будет получать последовательность элементов и
        помещать их в самого себя. При вызове метода связанный список должен полностью перезаписываться новыми элементами.
    3. Реализовать метод write, который передавать последовательность элементов для записи драйвером.
    4. Протестировать паттерн "Стратегия" в ключе независимости работы экземляров LinkedListWithDriver от драйверов
        IStructureDriver. LinkedListWithDriver должен уметь работать со всеми экземплярами дочерних классов класс IStructureDriver.
    5. LinkedListWithDriver должен поддерживать "горячую замену" драйвера, то есть без удаления и создания нового
        экземпляра LinkedListWithDriver, а замена драйвера существующего экземпляра.
"""

from py_class.LinketList import LinkedList
from lesson_5_driver.driver import IStructureDriver, JsonFileDriver, SimpleFileDriver


class LinkedListWithDriver(LinkedList):
    def __init__(self, data, driver_: IStructureDriver = None):
        super().__init__(data)
        self.__driver = driver_

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver_: IStructureDriver):
        if not isinstance(driver_, IStructureDriver) and driver_ is not None:
            msg = f"Драйвер должен быть экземпляром класса {IStructureDriver}"
            raise TypeError(msg)
        self.__driver = driver_

    def read(self):
        """Взять драйвер и считать из него информацию в LinkedList"""
        data_from_driver = self.__driver.read(self)
        self.clear()
        for value in data_from_driver:
            self.append(value)

    def write(self):
        """Взять драйвер и записать в него информацию из LinkedList"""
        self.__driver.write(self)


if __name__ == '__main__':
    # driver = JsonFileDriver('tmp.json')
    ll = LinkedListWithDriver([1, 2, 3, 4, 57])
    ll.driver = SimpleFileDriver('tmp.txt')

    ll.write()