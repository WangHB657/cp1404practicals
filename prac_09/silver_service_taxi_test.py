from silver_service_taxi import SilverServiceTaxi


def main():
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 4)
    luxury_taxi.drive(10)
    print(luxury_taxi)
    print(f"Total fare: ${luxury_taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
