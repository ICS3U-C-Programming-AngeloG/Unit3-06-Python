# ...existing code...
#!/usr/bin/env python3

# Created by: Angelo Garcia
# Created on: September 30th, 2025
# This program uses a try statement to catch input errors


def main():
    # This function demonstrates validating user input with try/except/finally

    # input - prompt the user for the number of students (input returns a string)
    integer_as_string = input("Enter the number of students: ")
    print("")

    # Process & output
    try:
        # Try to convert the input string to an integer
        integer_as_number = int(integer_as_string)
        print("You entered an integer correctly!")
    except Exception:
        # If conversion fails, inform the user the input was not an integer
        print("That was not an integer!")
    finally:
        # This always runs whether conversion succeeded or failed
        print("Thank you for playing.")


if __name__ == "__main__":
    main()
