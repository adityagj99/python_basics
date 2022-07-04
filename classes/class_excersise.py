# class excersise

import csv
from re import I


# Parrent class
class Items:


    # class level attrubute - available for entire class
    pay_rate = 0.7     # payable ammount after 30% disscount
    all_items = []

    # __init__() intiate by default (constructor)
    def __init__(self, name: str, price: float, quantity=0) -> None:

        # validation check for assign arguments
        assert price >= 0,f"Price {price} should be greater than zero."
        assert quantity >= 0,  f"Quantity {quantity} is less than or equal to zero."

        # assign self to object
        self.name = name
        self.price = price
        self.quantity = quantity

        Items.all_items.append(self)    # appends all attribute in list default as created inside __init__


    # method(function) to calculate total price
    def total_price(self):
        return self.price * self.quantity
    
    # methode to calculate discount
    def disscount(self):
        self.price =  self.price * self.pay_rate

    # magic method represent all objects in string
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity}"

    # Class methode
    @classmethod    # class decorator "@ "
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            #print(items)
        
        # Creating automatic instances based on csv file
        for i in items:
            Items(
                name = i.get('name'),
                price = float(i.get('price')),
                quantity = int(i.get('quantity'))
            )

# Child class for inheritance
class Phones(Items):
    all_items = []

    def __init__(self, name: str, price: float, quantity=0, broken_phone=0) -> None:
        
        # super function inherits all parrent attribuits to add new one for child
        super().__init__(name, price, quantity)

        # new attribute broken_phones
        self.broken_phone = broken_phone

        Phones.all_items.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity, self.broken_phone}"

# creating instances
item1 = Items("item_1", 100, 1)   # instance_1
item2 = Items("item_2", 1000, 3) # instance_2
Items.instantiate_from_csv()        # from CSV

# Creating instances for child class
phone_1 = Phones("LG", 34.34, 10, 76)
phone_2 = Phones("Moto", 12, 2, 65)

def understanding_class_attributes():

    print("understanding_class_attributes")

    # used default assign class level attribute
    print(Items.pay_rate)
    print(item1.pay_rate)
    item1.disscount()
    print(item1.price)

    # change default class attribute to instance level attribute
    item2.pay_rate = 0.5
    print(item2.pay_rate)
    item2.disscount()
    print(item2.price)


def looping_through_all_instances():

    print(Items.all_items, "\n")  # print all instances in obj format

    for instances in Items.all_items:   # looping through indivisual attributes of instances
        print(instances.name, instances.price, instances.quantity)

    print(item1.__dict__)   # magic method to print key-calue pair of created objects


def class_method():
    # print(Items.all_items)
    for i in Items.all_items:
        print(i)

def child_class():
    print(Phones.all_items)

    print(Items.all_items)

child_class()
