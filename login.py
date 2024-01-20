def check_credentials(username: str, password: str, filepath: str) -> bool:
    try:
        # Открываем файл для чтения и считываем имя пользователя и пароль
        with open(filepath, "r") as F:
            cr_username = F.readline().strip()
            cr_password = F.readline().strip()
        # Если полученные данные и данные из файла совпадают, возвращаем истину
        if username == cr_username and password == cr_password:
            return True
        else:
            return False
    except Exception as error:
        print("Ошибка при проверке данных:", error)
        return False
