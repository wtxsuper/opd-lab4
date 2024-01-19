def check_credentials(username: str, password: str) -> bool:
    try:
        with open("credentials.txt", "r") as F:
            cr_username = F.readline().strip()
            cr_password = F.readline().strip()
        if username == cr_username and password == cr_password:
            return True
        else:
            return False
    except Exception as error:
        print("Ошибка при проверке данных:", error)
        return False
