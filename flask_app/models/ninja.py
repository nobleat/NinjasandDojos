from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"

class ninjacls:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['age']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL(db).query_db(query,id)
        return cls(result[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age) VALUES (%(first)s, %(last)s, %(age)s)"
        result = connectToMySQL(db).query_db(query,data)
        return result
