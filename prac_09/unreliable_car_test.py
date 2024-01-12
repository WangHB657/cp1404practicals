from unreliable_car import UnreliableCar


def main():
    my_unreliable_car = UnreliableCar("Old Clunker", 100, 50)

    for i in range(1, 6):
        distance_driven = my_unreliable_car.drive(30)
        print(f"Attempt {i}: Tried to drive 30km, drove {distance_driven}km")


if __name__ == '__main__':
    main()
