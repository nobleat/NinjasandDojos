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
        return connectToMySQL(db).query_db(query,data)


    # @classmethod
    # def get_one(cls,id):
    #     query = "SELECT * FROM dojos WHERE id = %(id)s";
    #     result = connectToMySQL(db).query_db(query,id)
    #     # print(result)
    #     return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(db).query_db(query)
        all_dojos = []
        for dojos in results:
            all_dojos.append(cls(dojos))
        return all_dojos

    @classmethod
    def ninjas_with_dojos(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for ninja_row_db in results:
            ninja_data = {
                "id":ninja_row_db["ninjas.id"],
                "first_name": ninja_row_db["first_name"],
                "last_name": ninja_row_db["last_name"],
                "age": ninja_row_db["age"],
                "created_at": ninja_row_db["ninjas.created_at"],
                "updated_at": ninja_row_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninjacls(ninja_data))
        return dojo
