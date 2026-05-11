from faker import Faker


fake = Faker()

def generate_user_data():
    return {
        "email": f"{fake.user_name()}{fake.random_int()}@test.com",
        "password": fake.password(length=10),
        "name": fake.name()
    }

def get_access_token(response):
    return response.json().get("accessToken")