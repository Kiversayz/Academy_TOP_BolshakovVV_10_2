# Задание 1
""" 
Реализовать класс «Автомобиль» у которого будет
минимум 3 атрибута и 2 метода, добавьте
возможность упаковки и распаковки данных с
использованием json и pickle, для json метод упаковки
на ваш выбор.
"""

from SerializationMixin import SerializationMixin
import os

class Automobile(SerializationMixin):
    
    def __init__ (self, make='LADA', model='Sedan', year='2009'):
        self.make = make
        self.model = model
        self.year = year
    
    def get_data (self):
        return f'Информация об Автомобиле:\nМарка: {self.make}\nМодель: {self.model}\nГод выпуска: {self.year}'\
    
    def set_data (self, make, model, year):
        print(self.get_data())
        self.make = make
        self.model = model
        self.year = year
        print(f'Внесены изменения актуальная:\n{self.get_data()}')

if __name__ == "__main__":
    #Создаем объект класса
    auto = Automobile()
    
    #Выводим информацию
    print(auto.get_data())
    print()
    #Устанавливаем новое значение
    auto.set_data('Ogr','Drobitel','2099')
    print()
    #Устанавливаем путь
    folder = "data"
    filenameJSON = "example_HW_1.json"
    filepathJSON = os.path.join(folder, filenameJSON)
    filenamePickle = "example_HW_1.txt"
    filepathPickle = os.path.join(folder, filenamePickle)
    #Записываем на файл JSON
    auto.to_json(filepathJSON)
    #Роуспаковка файла JSON и сохранение в переменную
    auto2 = auto.from_json(filepathJSON)
    #Вывод информации из прочитанного файла JSON
    print(auto2.get_data())
    
    #Записываем на файл Pickle
    auto.to_pickle(filepathPickle)
    #Роуспаковка файла Pickle и сохранение в переменную
    auto2 = auto.from_pickle(filepathPickle)
    #Вывод информации из прочитанного файла Pickle
    print(auto2.get_data())