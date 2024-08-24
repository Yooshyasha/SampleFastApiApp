from tortoise import Model, fields

class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField()