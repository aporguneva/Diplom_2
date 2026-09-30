class Url:
    BASE_URL = "https://stellarburgers.education-services.ru"

    #Создание пользователя
    CREATE_USER = "/api/auth/register"  #POST

    #Логин пользователя
    LOGIN_USER = "/api/auth/login" #POST

    #Создание заказа
    CREATE_ORDER = "/api/orders" #POST

    #Удаление пользователя
    DELETE_USER = "/api/auth/user" #DELETE
