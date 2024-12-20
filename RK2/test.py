from main import *
import pytest

class TestFunctions:

    def test_func_1(self):
        mass = [("ИУ5", 125, "Мы"), ("ФН12", 60, "Слишком умные"), ("ИБМ3", 46, "Слишком богатые"),
                ("РК1", 74, "Слишком умные")]
        assert task_1(mass) == [("ИУ5", "Мы"), ("ИБМ3", "Слишком богатые")]

    def test_func_2(self):
        mass = [("ИУ5", 125, "Системы обработки информации и управления"), ("ФН4", 60, "Техническая физика"),
                ("ИУ6", 46, "Компьютерные системы и сети")]
        print("2: ", task_2(mass))
        assert task_2(mass) == ['Компьютерные системы и сети: 46', 'Техническая физика: 60', 'Системы обработки информации и управления: 125']

    def test_func_3(self):
        mass = [("ИУ5", 125, "Мы"), ("ФН12", 60, "Слишком умные"), ("ИБМ3", 46, "Слишком богатые"),
                ("РК1", 74, "Слишком умные")]
        print("3: ", task_3(mass))
        assert task_3(mass) == ['ИБМ3: Слишком богатые', 'ИУ5: Мы', 'РК1: Слишком умные', 'ФН12: Слишком умные']

