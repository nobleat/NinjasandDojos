from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"

class Ninjacls:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['age']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first)s, %(last)s, %(age)s %(dojo_id)s)"
        result = connectToMySQL(db).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s";
        result = connectToMySQL(db).query_db(query,{'id':id})
        # print(result)
        return cls(result[0])



    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM ninjas"
    #     results = connectToMySQL(db).query_db(query)
    #     # print(results)
    #     ninjalist = []
    #     for ninja in results:
    #         ninjalist.append(cls(ninja))
    #     return ninjalist