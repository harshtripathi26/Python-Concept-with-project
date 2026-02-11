class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def fullname(self):
        return f"{self.__brand}  {self.model}"
    


    def get_brand(self):
        return self.__brand + "!"
    

    def fuel(self):
        return "petrol or disel"



class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery  = battery


    def fuel(self):
        return "Electric charge"
    


Ecar = ElectricCar("Tesla","Model S" , "48kwh")
# print(Ecar.fullname())

print(Ecar.fuel())
print(Ecar.get_brand())

safari = Car("tata","safari")

print(safari.fuel())


# my_car = Car("toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())

# my_new_car = Car("Tata", "Safari")

# print(my_new_car.brand)