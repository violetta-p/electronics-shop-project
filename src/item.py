import csv
import os
from pathlib import Path

FILE_PATH = Path(__file__).parent.parent


class Item:
    """
    Класс для представления товара в магазине.
    """
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
        full_path_to_data = os.path.join(FILE_PATH, "items.csv")
        with open(full_path_to_data, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                name = item["name"]
                price = cls.string_to_number(item["price"])
                quantity = cls.string_to_number(item["quantity"])
                Item.all.append(cls(name, price, quantity))
