#!/usr/bin/env python3

# Created by: Angelo Garcia
# Created on: September 30th, 2025
# This program uses a try statement to catch input errors


def main():
    # This function uses a try statement to catch input errors

    # input
    integer_as_string = input("Enter the number of students: ")
    print("")

    # Process & output
    try:
        integer_as_number = int(integer_as_string)
        print("you entered an integer correctly!")
    except Exception:
        print("That was not an integer!")
    finally:
        print("Thank you for playing.")


if __name__ == "__main__":
    main()
