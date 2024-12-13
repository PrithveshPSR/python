def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True  # It is a leap year
            else:
                return False  # It is not a leap year
        else:
            return True  # It is a leap year
    else:
        return False  # It is not a leap year

def check_leap_year():
    while True:
        # Take input from the user
        year = int(input("Write and check a year if it is leap year or not: "))
        print(is_leap_year(year))

        # Ask if the user wants to check another year
        next_task = input("Do you want another calculation? (yes/no): ").lower()

        if next_task != 'yes':
            print("Thank you for using the leap year checker!")
            break  # Exit the loop if the user doesn't want another calculation

check_leap_year()
