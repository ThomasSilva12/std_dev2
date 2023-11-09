### Thomas Silva
### Nov 6, 2023
### ENGR 103 Project 6 c.


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

def std_dev(persons):
    total_age = sum([person.get_age() for person in persons])
    mean_age = total_age / len(persons)

    sum_squared_diff = sum([(person.get_age() - mean_age) ** 2 for person in persons])

    population_std_dev = (sum_squared_diff / len(persons)) ** 0.5

    return population_std_dev

persons = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 35)]
std_deviation = std_dev(persons)
print("Population Standard Deviation:", std_deviation)

