from peewee import *

db = PostgresqlDatabase('database2', host='localhost', port=5432, user='zlab', password='UMzLab!')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db
