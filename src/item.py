import csv
import os
from pathlib import Path

FILE_PATH = Path(__file__).parent
# FILE_PATH = ".."+os.sep+"src"


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'csv-файл поврежден'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    csv_file_name = 'items.csv'
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Недопустимое значение")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    @staticmethod
    def string_to_number(number):
        num = 0
        if "." in number:
            num = float(number)
        elif "." not in number:
            num = int(number)
        return num

    @classmethod
    def instantiate_from_csv(cls):
        full_path_to_data = os.path.join(FILE_PATH, cls.csv_file_name)
        try:
            with open(full_path_to_data, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for item in reader:
                    try:
                        name = item["name"]
                        price = cls.string_to_number(item["price"])
                        quantity = cls.string_to_number(item["quantity"])
                        Item.all.append(cls(name, price, quantity))
                    except KeyError:
                        raise InstantiateCSVError()
                    except ValueError:
                        raise InstantiateCSVError()
                    else:
                        if not (item["name"] and item["price"] and item["quantity"]):
                            raise InstantiateCSVError('В файле пропущены данные')
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует csv-файл")
