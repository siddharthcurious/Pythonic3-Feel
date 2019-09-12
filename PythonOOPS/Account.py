class Account:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Person(Account):
    def __init__(self, name, address, data):
        super().__init__(name, address)
        self.data = data


if __name__ == "__main__":

    obj = Person("a","b","c")
    print(obj.name, obj.address, obj.data)