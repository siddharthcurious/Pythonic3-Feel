import sys

cities = []
vehicles = {}

class Vehicle:
    def __init__(self, license_number):
        self.license_number = license_number

class City:
    def __init__(self, name):
        self.name = name

class CarService:
    def __init__(self):
        pass
    def add_city(self, city, cars):
        cities.append(city)
        for car in cars:
            vehicles.update({car: {"city": city, "status": "IDLE"}})
        return "OK"

    def add_vehicle(self, city, cars):
        for car in cars:
            vehicles.update({car: { "city": city, "status": "IDLE"}})
        return "OK"

class Trip:
    def __init__(self):
        pass
    def rent_vehicle(self, from_city, to_city):
        if from_city not in cities:
            return None
        elif to_city not in cities:
            return None
        else:
            for car, vals in vehicles.items():
                if vals.get("status") == "IDLE":
                    return "OK {}".format(car)

    def start_trip(self):
        pass
    def end_trip(self):
        pass

class Status:
    def __init__(self):
        pass

if __name__ == "__main__":

    args = sys.argv
    if args[1] == "add_city":
        city = args[2]
        nums = int(args[3])
        cars = args[4:]
        c = CarService()
        r = c.add_city(city, cars)
        print(r)

    elif args[1] == "add_vehicle":
        city = args[2]
        nums = int(args[3])
        vs = args[4:]
        c = CarService()
        r = c.add_vehicle(city, vs)
        print(r)

    elif args[1] == "rent_vehicle":
        from_city = args[2]
        to_city = args[3]
        t = Trip()
        r=t.rent_vehicle(from_city, to_city)
        print(r)

    elif args[1] == "end_trip":
        pass

    elif args[1] == "print_status" and args[2] == "city":
        pass
    elif args[1] == "print_status" and args[2] == "world":
        pass