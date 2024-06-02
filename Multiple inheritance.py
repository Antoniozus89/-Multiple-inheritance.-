class Vehicle:
    def __init__(self):
        self.vehicle_type = None
        return self.vehicle_type

class Car:
    PRICE = 1000000

    def __init__(self, model):
        self.model = model

    def horse_powers(self):
        self.horse_powers = 400
        return self.horse_powers

    def __str__(self):
        return '{} цена: {}, мощность двигателя: {}, транспортное средство: {}'.format(self.model, self.PRICE,
                                                                                      self.horse_powers,
                                                                                      self.vehicle_type)


class Nissan(Vehicle, Car):
    def __init__(self, model):
        self.model = model
        self.vehicle_type = True

    PRICE = 1500000

    def horse_powers(self):
        self.horse_powers = 450

kashkai = Nissan(model = 'Кашкай')
kashkai.horse_powers()
print(kashkai)