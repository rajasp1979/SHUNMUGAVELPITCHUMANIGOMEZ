# Model.py
class Breed:
    def __init__(self, name, temperament, coat, id=None):
        self.id = id
        self.name = name
        self.temperament = temperament
        self.coat = coat

    def display(self):
        print(self.id)
        print(self.name)
        print(self.temperament)
        print(self.coat)


class Pupper:
    def __init__(self, name, sex, weight, height, color, date_of_birth, breed_id, ids=None):
        self.ids = ids
        self.name = name
        self.sex = sex
        self.weight = weight
        self.height = height
        self.color = color
        self.date_of_birth = date_of_birth
        self.breed_id = breed_id

    def display(self):
        print(self.ids)
        print(self.name)
        print(self.sex)
        print(self.weight)
        print(self.height)
        print(self.color)
        print(self.date_of_birth)
        print(self.breed_id)


