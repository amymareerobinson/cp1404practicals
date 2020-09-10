"""
CP1404 2020 - Practical 6
Student Name: Amy Robinson
Program - Used Cars
"""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # 7. Now add names (literals) to the constructors where you create Car objects in the used_cars.py program.
    my_car = Car("Car", 180)
    my_car.drive(30)

    # print("fuel =", my_car.fuel)
    # print("odo =", my_car.odometer)

    # print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # 1. Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("Limo", 100)

    # 2. Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)

    # 3. Print the amount of fuel in the car.
    print(f"fuel = {limo.fuel}")

    # 4. Attempt to drive the car 115km using the drive method.
    limo.drive(115)

    # 5. Print the car's odometer reading.
    print(f"odometer = {limo.odometer}")

    # 8. In your used_cars.py program,
    # just print your car object/s to make sure that the __str__ method is working as expected.
    print(my_car)
    print(limo)


main()
