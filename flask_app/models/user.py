from flask_app.config.mysqlconnection import connectToMySQL

class User:

    db_name='users'
    def __init__(self,data):
        self.id=data['id'],
        self.name=data['name'],
        self.lastName=data['lastName'],
        self.email=data['email'],
        self.created_at=data['created_at'],
        self.update_at=data['update_at']

    @classmethod
    def getAllUsers(cls):
        query ='SELECT * FROM users;'
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append(row)
        return users

    @classmethod
    def create_user(cls,data):
        query="INSERT INTO users (name, lastName, email) VALUES (%(name)s,%(lastName)s,%(email)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def delete_user(cls,data):
        query="DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL(cls.db_name).query_db(query,data)

    

    @classmethod
    def get_user_by_id(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results[0]
    
    @classmethod
    def update_user(cls,data):
        query="UPDATE users SET name=%(name)s, lastName=%(lastName)s, email=%(email)s WHERE id=%(id)s"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results

        