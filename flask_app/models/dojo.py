from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"

class dojocls:
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
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(db).query_db(query)
        # print(results)
        userlist = []
        for user in results:
            userlist.append(cls(user))
        return userlist