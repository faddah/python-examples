"""Distance conversion utility for converting between kilometers and miles."""


def distconv(dist, km, miles, choice):
    """Convert and display a distance between kilometers and miles.

    Args:
        dist: The original distance value entered by the user.
        km: The distance converted to kilometers.
        miles: The distance converted to miles.
        choice: 1 to convert km to miles, 2 to convert miles to km.
    """
    if choice == 1:
        print(f"{dist:.2f} km = {miles:.2f} miles.")
    elif choice == 2:
        print(f"{dist:.2f} miles = {km:.2f} km.")
    else:
        print("Invalid choice.")
def main():
    """Prompt the user for a conversion type and distance, then display the result."""
    choice = int(input("1: km -> miles, 2: miles -> km: "))
    dist = float(input("Enter distance: "))
    miles = dist / 1.60934
    km = dist * 1.60934
    print(distconv(dist, km, miles, choice))

if __name__ == "__main__":
    main()
