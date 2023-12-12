# Re-uploaded file, will re-attempt to process the Wimbledon data correctly
import csv
filename = "wimbledon.csv"


def read_wimbledon_data(filename):
    """
    Reads the Wimbledon data from the given file.
    Returns a list of lists containing the data.
    """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        data = [row for row in reader if row]  # Exclude empty rows
    return data[1:]  # Skip the header row


def process_champions(data):
    """
    Processes the Wimbledon data to find the number of wins per champion.
    Returns a dictionary with champion names as keys and win counts as values.
    """
    champion_wins = {}
    for row in data:
        # Assuming the champion's name is in the second column (index 1)
        champion = row[2]
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
    return champion_wins


def process_countries(data):
    """
    Processes the Wimbledon data to find the countries of the champions.
    Returns a set containing the countries.
    """
    countries = set()
    for row in data:
        # Assuming the country is in the third column (index 2)
        country = row[1]
        countries.add(country)
    return countries


def main(filename):
    """
    Main function to process Wimbledon data and display processed information.
    """
    # Read data from file
    wimbledon_data = read_wimbledon_data(filename)

    # Process champions and count their wins
    champions = process_champions(wimbledon_data)

    # Process countries
    countries = process_countries(wimbledon_data)

    # Display champions and their win counts
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items(), key=lambda item: item[1], reverse=True):
        print(f"{champion} {wins}")

    # Display countries in alphabetical order
    print("\nThese countries have won Wimbledon:")
    print(', '.join(sorted(countries)))


# Run the main function
main(filename)