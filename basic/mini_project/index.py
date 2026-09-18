import requests
import pandas as pd
import mysql.connector

##Parent Class
class ApiService:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            return response.json()

        return []


# child Class

class UserApi(ApiService):
    def get_data(self):
        # parent Class ka get Data function
        user_data = super().get_data()

        response_data = []

        for user in user_data:
            response_data.append({
                "id": user["id"],
                "name": user["name"],
                "username": user["username"],
                "email": user["email"],
                "city": user["address"]["city"],
            })
        return response_data


# =============
# Another Child Class
# Polymorphism
# ====

class PostApi(ApiService):
    def get_data(self):
        # parent class ka function
        post_data = super().get_data()

        response_post_data = []

        for post in post_data:
            response_post_data.append({
                "id": post["id"],
                "user_id": post["userId"],
                "title": post["title"]
            })

        return response_post_data


# ===========
# database
# ===========

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_db"
        )

        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS `users`
                            (
                                id       INT PRIMARY KEY AUTO_INCREMENT,
                                name     VARCHAR(255),
                                username VARCHAR(255),
                                email    VARCHAR(255),
                                city     VARCHAR(255)
                            )
                            """)
        self.conn.commit()

    def insert_user(self, user):
        sql = """
              INSERT INTO users
                  (id, name, username, email, city)
              VALUES (%s, %s, %s, %s, %s)
              ON DUPLICATE KEY UPDATE name     = VALUES(name),
                                      username = VALUES(username),
                                      email    = VALUES(email),
                                      city     = VALUES(city) \
              """
        values = (
            user["id"],
            user["name"],
            user["username"],
            user["email"],
            user["city"]
        )

        self.cursor.execute(sql, values)

        self.conn.commit()

    def get_users(self):
        sql = "SELECT * FROM users"
        return pd.read_sql(sql, self.conn)

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


user = UserApi("https://jsonplaceholder.typicode.com/users")
post = PostApi("https://jsonplaceholder.typicode.com/posts")

users = user.get_data()
posts = post.get_data()

# df = pd.DataFrame(users)
# print("\nPandas online Api Data:")
# print(df.to_string(index=False))


# database

database = Database()

database.create_table()

# obj Creation

for data in users:
    database.insert_user(data)

# PRINT database data using database Api
mysql_data = database.get_users()

print("\n Mysql Data:")
print(mysql_data.to_string(index=False))
