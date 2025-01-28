# Задание 2
""" 
Реализовать класс «Книга» у которого будет минимум 3
атрибута и 2 метода добавьте возможность упаковки и
распаковки данных с использованием json и pickle, для
json метод упаковки через Encoder.
"""

from SerializationMixin import SerializationMixin
import os
import json

class Book(SerializationMixin):
    def __init__(self, title='Война и мир', author='Лев Толстой', publication_year='1863'):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def display_info(self):
        print(f"Информация о книге:\nЗаголовок: {self.title}\nАвтор: {self.author}\nГод публикации: {self.publication_year}")
    
    def get_info(self):
        data = self.__dict__
        return data

class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                'title': obj.title,
                'author': obj.author,
                'publication_year': obj.publication_year
            }
        return super().default(obj)

if __name__ == "__main__":
    #Создаем объект класса
    bok = Book('Война и мир','Лев Толстой',18999)
    
    #Получаем информацию
    print(bok.get_info())
    print()
    #Выводим информацию
    bok.display_info()
    print()
    #Устанавливаем путь
    folder = "data"
    filenameJSON = "example_HW_2.json"
    filepathJSON = os.path.join(folder, filenameJSON)
    filenamePickle = "example_HW_2.txt"
    filepathPickle = os.path.join(folder, filenamePickle)
    #Записываем на файл JSON
    bok.to_json(filepathJSON,cls=BookEncoder)
    print()
    #Роуспаковка файла JSON и сохранение в переменную
    bok2 = bok.from_json(filepathJSON)
    print()
    #Вывод информации из прочитанного файла JSON
    print(bok2.get_info())
    print()
    bok2.display_info()
    print()
    
    #Записываем на файл Pickle
    bok.to_pickle(filepathPickle)
    print()
    #Роуспаковка файла Pickle и сохранение в переменную
    bok2 = bok.from_pickle(filepathPickle)
    print()
    #Вывод информации из прочитанного файла Pickle
    print(bok2.get_info())