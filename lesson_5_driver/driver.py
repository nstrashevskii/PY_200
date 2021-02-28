"""
    1. Реализовать класс JsonFileDriver, который будет описывать логику считывания (записи) элементов из (в) json файл.
    2. Реализовать класс SimpleFileDriver, который будет описывать логику считывания (записи) элементов из (в) файл.
    3. В блоке __main__ протестировать работу драйверов
"""

from typing import Sequence
from abc import ABC, abstractmethod
import json


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер
        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер
        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, json_filename):
        self.json_filename = json_filename

    def read(self) -> Sequence:
        with open(self.json_filename) as f:
            input_ = json.load(f)
        if not isinstance(input_, list):
            raise TypeError(f'Неверный формат')
        return input_

    def write(self, data: Sequence) -> None:
        output_ = [value for value in data]
        with open(self.json_filename, 'w') as f:
            json.dump(output_, f, indent=4)


class SimpleFileDriver(IStructureDriver):
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self) -> Sequence:
        with open(self.file_name, 'w') as f:
            return [int(line) for line in f]

    def write(self, data: Sequence) -> None:
        with open(self.file_name, 'w') as f:
            for value in data:
                f.write(repr(value))
                f.write('\n')


if __name__ == '__main__':
    driver = JsonFileDriver('tmp.json')
    driver.write([1, 2, 3])
    data = driver.read()
    print(data)