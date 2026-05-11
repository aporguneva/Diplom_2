class ResponseMessagesUser:

    #Создание пользователя
    NOT_ENOUGH_DATA_ERROR = "Email, password and name are required fields" 
    USER_EXISTS_ERROR = "User already exists"
 
    #Логин курьера
    LOGIN_ERROR = "email or password are incorrect" #неверный логин или пароль, или нет одного из полей 


class ResponseMessagesOrder:
    EMPTY_CART_ERROR = "Ingredient ids must be provided"



