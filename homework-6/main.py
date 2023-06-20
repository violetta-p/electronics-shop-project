from src.item import Item

if __name__ == '__main__':
    NORMAL_FILE = "items.csv"
    NON_EXISTENT_FILE = "item1.csv"
    KEY_ERROR_FILE = "item(key_er).csv"
    VALUE_ERROR_FILE = "item(val_er).csv"
    MISSING_DATA_FILE = "item(missing).csv"
    Item.csv_file_name = MISSING_DATA_FILE
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv
    # В файле items.csv удалена последняя колонка.
    Item.csv_file_name = NORMAL_FILE
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
