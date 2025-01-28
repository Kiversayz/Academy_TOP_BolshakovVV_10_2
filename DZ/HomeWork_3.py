# Задание 3
""" 
Реализовать класс «Стадион» у которого будет минимум
3 атрибута и 2 метода добавьте
возможность упаковки и распаковки данных с
использованием json и pickle, для json метод упаковки
через Adapter.
"""

from SerializationMixin import SerializationMixin
import os

class Stadium(SerializationMixin):
    def __init__(self, name='StadiON', capacity = 666, location = 'Стадионопия'):
        self.name = name
        self.capacity = capacity
        self.location = location

    def show_info(self):
        print(f"Стадион {self.name} расположен в {self.location} и вмещает {self.capacity} зрителей.")
    
    def get_info(self):
        data = self.__dict__
        return data

class StadiumJsonAdapter:
    
    def prepare_data(self, stadium):
        """
        Подготавливает данные объекта Stadium для сериализации.
        Например, можно изменить структуру данных или добавить дополнительные поля.
        """
        stadium_dict = {
            'name': stadium.name,
            'capacity': stadium.capacity,
            'location': stadium.location
        }
        return stadium_dict
    


if __name__ == "__main__":
    #Создаем объект класса
    stad = Stadium()
    #Создаем объект класса Адаптера
    adapter = StadiumJsonAdapter()
    #Сохраняем данные подготовленные Адаптером
    data_stad_str = adapter.prepare_data(stad)
    
    #Выводим информацию
    print(stad.get_info())
    print()
    #Устанавливаем новое значение
    stad.show_info()
    print()
    #Устанавливаем путь
    folder = "data"
    filenameJSON = "example_HW_3.json"
    filepathJSON = os.path.join(folder, filenameJSON)
    filenamePickle = "example_HW_3.txt"
    filepathPickle = os.path.join(folder, filenamePickle)
    #Записываем на файл JSON
    stad.to_json(filepathJSON,data=data_stad_str)
    print()
    #Роуспаковка файла JSON и сохранение в переменную
    stad2 = stad.from_json(filepathJSON)
    print()
    #Вывод информации из прочитанного файла JSON
    print(stad2.get_info())
    print()
    stad2.show_info()
    print()
    
    #Записываем на файл Pickle
    stad.to_pickle(filepathPickle)
    print()
    #Роуспаковка файла Pickle и сохранение в переменную
    stad2 = stad.from_pickle(filepathPickle)
    print()
    #Вывод информации из прочитанного файла Pickle
    print(stad2.get_info())