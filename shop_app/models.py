from project.db import DATABASE

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(100), nullable = False)
    description = DATABASE.Column(DATABASE.String)
    price = DATABASE.Column(DATABASE.Float, nullable=False)
    count = DATABASE.Column(DATABASE.Integer)
    discount = DATABASE.Column(DATABASE.Float)


