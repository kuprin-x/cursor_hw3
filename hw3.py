from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def person_info(self):
        raise NotImplementedError

    @abstractmethod
    def mk_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, house, realtor):
        pass


class Person(Human):
    def __init__(self, name, age, money, homes: list):
        self.name = name
        self.age = age
        self.money = money
        self.homes = homes

    def person_info(self):
        print(f"My name is {self.name}. I'm {self.age} years old.\nI have ${self.money} at my credit card.")
        if len(self.homes) >= 1:
            print(f"{self.name} - I have - {self.homes}.")
        else:
            print(f"{self.name} - I have no realty.")

    def mk_money(self):
        print(f"I earned money. \nNow I have ${self.money} at my credit card.")
        self.money += random.randrange(100, 500, 244)

    def buy_house(self, house, realtor):
        if realtor.steal_money is True:
            self.money = 0
            print("Realtor stole money.")
            return
        if house in realtor.houses:
            if self.money >= house.cost:
                print(f"{self.name}  - buy the house {house.address} with area {house.area} m2 which costs"
                      f" ${house.cost}.")
                self.money -= house.cost
                print(f"I have ${self.money}.")
                self.homes.append(house.address)
                realtor.sold_house(house)
            else:
                while self.money < house.cost:
                    print(f"Can't buy this house {house.address}. Need money.")
                    print("What should we do?\n")
                    mk_moneys = input("how to make money? Enter one of the ways: 1, 2, 3, 4 => ")
                    if mk_moneys == "1":
                        self.mk_money()
                    elif mk_moneys == "2":
                        return
                    elif mk_moneys == "3":
                        self.mk_money()
                    elif mk_moneys == "4":
                        self.mk_money()
                    else:
                        print("Incorrect! Try again!")
        else:
            return "No houses available"


class Home(ABC):
    @abstractmethod
    def apply_a_purchase_discount(self, discount):
        raise NotImplementedError


class House(Home):
    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def apply_a_purchase_discount(self, discount):
        if discount > 0:
            print(f"Discount for house {self.address} is {discount}!\nNew costs {self.cost - round(self.cost * discount)}")
            self.cost -= round(self.cost * discount)
        else:
            print(f"No discount for house - {self.address}.")


class SmallTypicalHouse(House):
    def __init__(self, address, cost, area=40):
        super().__init__(address, area, cost)


class RealtorMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):

    def __init__(self, name, houses: list, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def info_about_houses(self):
        if self.houses is not []:
            print(f"Realtor - {self.name}.\nThere are such houses:")
            for house in self.houses:
                print(f"! - {house.address} - {house.area} m2 which costs ${house.cost}")

        else:
            print("No houses on sale!")

    def discounted(self, house):
        house.apply_a_purchase_discount(self.discount)

    def steal_money(self):
        steal = random.randrange(1, 10)
        if steal == 1:
            print(f"The realtor {self.name} steal your money!")
            return 1

    def sold_house(self, house):
        self.houses.remove(house)


hous1 = House("Kharkiv 1", 120, 23000)
hous2 = House("Kharkiv 2", 150, 26210)
hous3 = House("Kharkiv 3", 100, 20800)
vadym = Person("Vadym", 26, 76000, [])
vadym.person_info()
realt = Realtor("Mark", houses=[hous1, hous2, hous3], discount=round(random.uniform(0.05, 0.25), 2))
realt.steal_money()
realt.info_about_houses()
realt.discounted(hous1)
vadym.buy_house(hous1, realt)
vadym.person_info()
print('|-----|-----|-----|-----|-----|-----|')
Leo = Person("Leo", 23, 29000, ["Kharkiv 10"])
Leo.person_info()
realt.info_about_houses()
realt.steal_money()
realt.discounted(hous3)
Leo.buy_house(hous3, realt)
Leo.person_info()
print('|-----|-----|-----|-----|-----|-----|')
Olga = Person("Olga", 28, 10000, [])
Olga.buy_house(hous2, realt)
Olga.person_info()
