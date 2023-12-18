from guitar import Guitar


def main():
    guitars = []

    with open('guitars.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name, year, cost = parts
                guitars.append(Guitar(name, int(year), float(cost)))

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()

    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
