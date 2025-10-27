#!/usr/bin/env python3

# Created by: Angelo Garcia
# Created on: September 30th, 2025
# Program uses try/except/finally to check integer input


def main():
    # main function: run the input check

    # prompt user for number of students (stores text)
    integer_as_string = input("Enter the number of students: ")
    # print a blank line to separate input from output
    print("")

    try:
        # convert input text to an integer
        integer_as_number = int(integer_as_string)
        # notify user the input was a valid integer
        print("You entered an integer correctly!")
    except Exception:
        # notify user the input was not an integer
        print("That was not an integer!")
    finally:
        # always print a closing message
        print("Thank you for playing.")


if __name__ == "__main__":
    main()
