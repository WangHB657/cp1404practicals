from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0
    running = True

    while running:
        print("Let's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()

        if user_choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for taxi in taxis:
                print(f"{taxi}")
            running = False
        elif user_choice == 'c':
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")
            try:
                current_taxi = taxis[int(taxi_choice)]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif user_choice == 'd':
            if current_taxi:
                drive_taxi(current_taxi)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
                print(f"Bill to date: ${total_bill:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxi):
    distance = input("Drive how far? ")
    try:
        distance = float(distance)
        taxi.start_fare()
        taxi.drive(distance)
    except ValueError:
        print("Invalid distance. Please enter a number.")


main()
