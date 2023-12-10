# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Lamp:
    def __init__(self, voltage: float, power: float):
        """
        Создание и подготовка к работе объекта "Лампочка"

        :param voltage: напряжение лампочки
        :param power: мощность лампочки

        Примеры:
        >>> lamp = Lamp(220.0, 25.0)  # инициализация экземпляра класса
        """
        if not isinstance(voltage, float):
            raise TypeError("Напряжение лампочки должно быть типа float")
        if voltage < 0:
            raise ValueError("Напряжение лампочки должно быть неотрицательным числом")
        self.voltage = voltage
        if not isinstance(power, float):
            raise TypeError("Мощность лампочки должна быть типа float")
        if power < 0:
            raise ValueError("Мощность лампочки должна быть неотрицательным числом")
        self.power = power

    def amperage(self) -> float:
        """
        Функция которая определяет силу тока в лампочке

        :return: сила тока -> float

        Примеры:
        >>> lamp = Lamp(220.0, 25.0)
        >>> lamp.amperage()
        """
        ...

    def temperature(self) -> float:
        """
        Функция которая определяет температуру лампочки
        :return: температура -> float

        Примеры:
        >>> lamp = Lamp(220.0, 25.0)
        >>> lamp.temperature()
        """
        ...


class Window:
    def __init__(self, is_open: bool, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Окно"

        :param is_open: открыто ли окно?
        :param width: ширина окна
        :param height: высота окна

        Примеры:
        >>> window = Window(False, 40.5, 155.5)  # инициализация экземпляра класса
        """

        if not isinstance(is_open, bool):
            raise TypeError("Открыто ли окно должно быть типа bool")
        self.is_open = is_open
        if not isinstance(width, float):
            raise TypeError("Ширина окна должна быть типа float")
        if width <= 0:
            raise ValueError("Ширина окна должна быть положительным числом")
        self.width = width
        if not isinstance(height, float):
            raise TypeError("Высота окна должна быть типа float")
        if height <= 0:
            raise ValueError("Высота окна должна быть положительным числом")
        self.height = height

    def area(self) -> float:
        """
        Функция которая определяет площадь окна

        :return: значение площади

        Примеры:
        >>> window = Window(False, 22.5, 205.0)
        >>> window.area()
        """
        ...

    def close(self) -> None:
        """
        Функция которая закрывает окно
        :return: окно закрыто

        Примеры:
        >>> window = Window(False, 22.5, 205.0)
        >>> window.close()
        """
        ...

    def open(self) -> None:
        """
        Функция которая открывает окно
        :return: окно открыто

        Примеры:
        >>> window = Window(False, 22.5, 205.0)
        >>> window.open()
        """
        ...


class Account:
    def __init__(self, name: str, stocks: int):
        """
        Создание и подготовка к работе объекта "Аккаунт"

        :param name: имя пользователя
        :param stocks: количество акций

        Примеры:
        >>> account = Account("Tasas", 15)  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not name.isalpha():
            raise ValueError("В имени должны быть только буквы")
        self.name = name
        if not isinstance(stocks, int):
            raise TypeError("Количество акций должно быть типа int")
        if stocks < 0:
            raise ValueError("Количество акций быть неотрицательным числом")
        self.stocks = stocks

    def rename(self, new_name) -> None:
        """
        Переименование пользователя.
        return: имя пользоваиеля

        :param new_name: Новое имя пользователя.

        :raise ValueError: Если имя состоит не из букв

        Примеры:
        >>> account = Account("Tasas", 15)
        >>> account.rename("Thomas")
        """
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть типа str")
        if not new_name.isalpha():
            raise ValueError("В имени должны быть только буквы")
        ...

    def sell_stocks(self, count: int) -> None:
        """
        Функция для продажи акции.

        return: количество акций уменьшилось

        :param count: Количество продаваемых акций.

        :raise ValueError: Если количество акций меньше нуля или если продается больше акций чем есть на аккаунте

        Примеры:
        >>> account = Account("Tasas", 15)
        >>> account.sell_stocks(2)
        """
        if not isinstance(count, int):
            raise TypeError("Количество акций должно быть типа int")
        if count < 0 and self.stocks - count >= 0:
            raise ValueError("Количество акций должно быть неотрицательным числом и не превышать"
                             "количества имеющихся акций")
        ...

    def buy_stocks(self, count: int) -> None:
        """
        Функция для покупки акции.

        return: количество акций увеличилось

        :param count: Количество покупаемых акций.

        :raise ValueError: Если количество акций меньше нуля

        Примеры:
        >>> account = Account("Tasas", 15)
        >>> account.buy_stocks(13)
        """
        if not isinstance(count, int):
            raise TypeError("Количество акций должно быть типа int")
        if count < 0:
            raise ValueError("Количество акций должно быть неотрицательным числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
