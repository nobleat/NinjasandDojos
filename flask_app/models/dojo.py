from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

db = "dojos_and_ninjas_schema"

class Dojocls:
    def __init__(self, data):
        self.id = data['id']
        self.location= data['location']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (location) VALUES (%(location)s)"
        result = connectToMySQL(db).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL(db).query_db(query,id)
        # print(result)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(db).query_db(query)
        # print(results)
        all_dojos = []
        for dojos in results:
            all_dojos.append(cls(dojos))
        return all_dojos

    @classmethod
    def joined(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id = dojo.id WHERE dojo.id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        dojo = cls(results[0])
        for ninja_row_db in results:
            ninja_data = {
                "id":ninja_row_db["ninja.id"],
                "first": ninja_row_db["first_name"],
                "last": ninja_row_db["last_name"],
                "age": ninja_row_db["age"],
            }
            dojo.ninjas.append(ninja.Ninjacls(ninja_data))
