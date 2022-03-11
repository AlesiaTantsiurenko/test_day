import unittest
from day import days
"""
Тестируем нашу функцию
"""


class TestDays(unittest.TestCase):

    def test_day_title(self):
        """ Проверям правильность вычесления нашей функции """
        self.assertEqual(days("Понедельник"), "Вторник")

    def test_day_not_title(self):
        """ Проверям работу метода title() """
        self.assertEqual(days("понедельник"), "Вторник")

    def test_day_upper_lower(self):
        self.assertEqual(days("ПОНЕДЕЛЬНИК"), "Вторник")
        self.assertEqual(days("ПОНЕДельник"), "Вторник")

    def test_values(self):
        """ Проверяем, было ли поднято исключение """
        with self.assertRaises(ValueError):
            days("поо")
            days(7)
            days(True)
            days(["Понедельник", "вторник"])

    #Запускаем проверку с помощью строки: python -m unittest -v test_day