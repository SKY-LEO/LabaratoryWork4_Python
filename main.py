import time


main_menu = ("1. Создать класс Список\n ",
             "2. Создать класс Светофор\n ",
             "3. Реализовать класс канцелярская принадлежность\n ",
             "4. Собственный класс\n ",
             "0. Выход")


class List:
    def __init__(self):
        self.my_list = []

    def list_add(self, info):
        self.my_list.append(info)

    def list_extend(self, info):
        self.my_list.extend(info)

    def list_pop(self):
        return self.my_list.pop()

    def list_view(self):
        for val in self.my_list:
            print(val, "", end="")
        print()

    def list_delete(self, index):
        try:
            self.my_list.remove(index)
        except ValueError:
            print("Данный элемент отсутствует в списке!")

    def list_reverse(self):
        return self.my_list.reverse()


def task1():
    # Создать класс List (список), в котором реализовать методы для работы со
    # списком (не менее 5).
    my_list = [43, 'hi', 67.9, 'qwertyuiop']
    example = List()
    print("Добавим в список:", my_list)
    example.list_extend(my_list)
    print("Получилось:")
    example.list_view()
    print("Удалим hi")
    example.list_delete('hi')
    print("Результат:", example.my_list)
    print("Удалим последний элемент списка:", example.list_pop())
    example.list_reverse()
    print("Развернем список:", example.my_list)


class TrafficLight:
    __color = {"Красный": 7, "Желтый": 2, "Зеленый": 3}
    __color_reference = ("Красный", "Желтый", "Зеленый")

    def running(self):
        i = 0
        for col, sec in self.__color.items():
            if col == self.__color_reference[i]:
                print(col, "!", sep="")
                time.sleep(sec)
                i += 1
            else:
                print("Неправильный порядок цветов!")
                break


def task2():
    # Создать класс TrafficLight (светофор).
    # 1. Определить у него один атрибут color (цвет) и метод running (запуск);
    # 2. Атрибут реализовать как приватный;
    # 3. В рамках метода реализовать переключение светофора в режимы: красный,
    # жёлтый, зелёный;
    # 4. Продолжительность первого состояния (красный) составляет 7 секунд,
    # второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
    # 5. Переключение между режимами должно осуществляться только в
    # указанном порядке (красный, жёлтый, зелёный);
    # 6. Проверить работу примера, создав экземпляр и вызвав описанный метод.
    # Задачу можно усложнить, реализовав проверку порядка режимов. При его
    # нарушении выводить соответствующее сообщение и завершать скрипт.
    light = TrafficLight()
    light.running()
    light._TrafficLight__color["Оранжевый"] = light._TrafficLight__color.pop("Красный")
    light.running()


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки:", self.title)


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки:", self.title)


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки:", self.title)


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки:", self.title)


def task3():
    # Реализовать класс Stationery (канцелярская принадлежность),
    # определить в нём атрибут title (название) и метод draw (отрисовка). Метод
    # выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen
    # (ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать
    # переопределение метода draw. Для каждого класса метод должен выводить
    # уникальное сообщение; создать экземпляры классов и проверить, что
    # выведет описанный метод для каждого экземпляра.
    pen = Pen("Ручка")
    pencil = Pencil("Карандаш")
    handle = Handle("Маркер")
    pen.draw()
    pencil.draw()
    handle.draw()


class MyClass:

    def __init__(self, name, state=None):
        if state is not None:
            self.is_turned_on = state
            self.name = name
        else:
            self.is_turned_on = False
            self.name = name

    def turn_on_device(self):
        self.is_turned_on = True

    def print_info(self):
        print("Устройство", self.name, self.is_turned_on)

    @classmethod
    def turn_off_all_devices(cls):
        cls.is_turned_on = False

    @staticmethod
    def stat():
        print("hello")


def task4():
    # Придумать класс самостоятельно, реализовать в нем методы экземпляра
    # класса, статические, методы, методы класса.
    lamp = MyClass("lampa", True)
    phone = MyClass("phone")
    MyClass.turn_off_all_devices()
    lamp.print_info()
    phone.print_info()


def menu():
    while True:
        print("Список заданий:\n", "".join(main_menu))
        variant = input("Выберите задание: ")
        try:
            variant = int(variant)
        except ValueError:
            print("Введите целочисленное число!")
            continue
        if variant > len(main_menu) - 1 or variant < 0:
            print("Ошибка, введите число в заданном интервале!")
        else:
            match variant:
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 0:
                    break
                case _:
                    print("Ошибка!")
                    return -1
    return 0


if __name__ == '__main__':
    menu()
