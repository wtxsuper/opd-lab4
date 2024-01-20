import os
import random
import string
import unittest

from login import check_credentials


class LoginTests(unittest.TestCase):

    def setUp(self):
        # Создание временного файла для хранения данных
        # Генерация случайного имени файла для хранения данных авторизации
        self.filename = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 10))) + '.txt'
        self.file = open(self.filename, 'w')
        self.file.writelines(["test_username\n", "test_password"])
        self.file.close()

    def tearDown(self):
        # Удаление файла после выполнения всех тестов
        os.remove(self.filename)

    def test_correct_credentials(self):
        # Тест при корректных данных
        result = check_credentials("test_username", "test_password", self.filename)
        self.assertTrue(result)

    def test_incorrect_username(self):
        # Тест при неправильном имени пользователя
        result = check_credentials("wrong_username", "test_password", self.filename)
        self.assertFalse(result)

    def test_incorrect_password(self):
        # Тест при неправильном пароле
        result = check_credentials("test_username", "wrong_password", self.filename)
        self.assertFalse(result)

    def test_file_not_found(self):
        # Тест при несуществующем файле
        result = check_credentials("test_username", "test_password", "non_existent_file.txt")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
