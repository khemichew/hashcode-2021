from collections import deque
from dataclasses import dataclass


@dataclass
class Traffic:
    duration: int
    num_cities: int
    bonus_points: int
    streets: list
    cars: list
    name_to_streets: dict


@dataclass
class Street:
    name: str
    src: int
    dst: int
    length: int


@dataclass
class Car:
    paths: list[int]


class Input:
    @staticmethod
    def read(filename):
        with open(filename, "r") as file:
            lines = deque()
            for line in file:
                lines.append(line.rstrip())
            duration, num_cities, num_streets, num_cars, bonus_points = map(int, lines.popleft().split())

            streets = []
            for _ in range(num_streets):
                src, dst, name, length = lines.popleft().split()
                streets.append(Street(name, int(src), int(dst), int(length)))

            name_to_street = {street.name: street for street in streets}

            cars = []
            for _ in range(num_cars):
                paths = lines.popleft()[1:].split()
                cars.append(Car([name_to_street[pathname] for pathname in paths]))

            return Traffic(duration, num_cities, bonus_points, streets, cars, name_to_street)


class Algorithm:
    @staticmethod
    def process(traffic: Traffic):
        pass

class Output:
    @staticmethod
    def score():
        return


t = Input.read("input_data/a_an_example.in.txt")
print(t)
