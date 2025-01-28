import json
import pickle

class SerializationMixin:
    """
    Миксин для предоставления методов упаковки и распаковки данных
    с использованием json и pickle.
    
    Миксин (mixin) — это специальный класс в объектно-ориентированном программировании, 
    который служит для добавления функциональности другим классам через множественное наследование. 
    Сам по себе миксин обычно не используется для создания объектов. Его задача — предоставить 
    определённые методы или свойства для использования в классах, которые наследуют его.
    """
    def to_json(self, filepath = None, cls = None,data=None):
        """
        filepath, который по умолчанию равен None - можно вызвать метод без указания пути к файлу, 
        возвращая данные в виде JSON. 
        cls - параметр для Encoder класса.
        data - подготовленные данные Адаптера.
        Сохранить данные в файл, если указан путь filepath возвращая сам путь.
        data = self.__dict__ — содержит все атрибуты экземпляра класса в виде словаря.
        """
        # Если данные не переданы, используем атрибуты экземпляра
        if not data:
            data = self.__dict__
        # Сериализация в файл или строку
        if filepath:
            with open(filepath,'w',encoding='utf-8') as f:
                json.dump(data,f, cls=cls,ensure_ascii=False,indent=4)
            print(f"Данные сохранены в файл {filepath} в формате JSON.")
            return filepath
        return json.dumps(data,ensure_ascii=False,indent=4)
    
    @classmethod
    def from_json (cls, filepath=None, json_string=None):
        """ 
        filepath - Прочитать JSON из файла, если указан путь.
        json_string - Прочитать JSON из строки, если указана.
        Возвращаем новый объект класса, передавая его атрибуты через распаковку словаря (**data),
        data = {"brand": "Toyota", "model": "Camry", "year": 2020}
        Эквивалентно: Car(brand="Toyota", model="Camry", year=2020)
        """
        if filepath:
            with open(filepath,'r',encoding='utf-8') as f:
                data = json.load(f)
        elif json_string:
            data = json.loads(json_string)
        else:
            raise ValueError("Необходимо указать либо filepath, либо json_string.")
        return cls(**data)
    
    def to_pickle (self, filepath):
        """ 
        filepath - путь к сохранению бинарного файла в шифровке pickle
        """
        try:
            with open(filepath, 'wb') as f:
                pickle.dump(self, f)
            print(f"Данные сохранены в файл {filepath} в формате pickle.")
        except Exception as error:
            print(f"Ошибка при сохранении данных: {error}")
    
    @classmethod
    def from_pickle (cls, filepath):
        """ 
        filepath - путь к извлечению данных из бинарного файла в шифровке pickle
        """
        try:
            with open(filepath, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except FileNotFoundError:
            print(f"Файл {filepath} не найден.")
        except pickle.PickleError as e:
            print(f"Ошибка при загрузке данных: {e}")