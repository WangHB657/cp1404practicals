COLOR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}
print(COLOR_CODES)

color_name = input("Enter a color name: ").upper()

while color_name != "":
    if color_name in COLOR_CODES:
        print(f"The color code for {color_name} is {COLOR_CODES[color_name]}")
    else:
        print("Invalid color name")

    color_name = input("Enter a color name (blank to stop): ").upper()