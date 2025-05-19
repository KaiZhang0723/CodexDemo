#!/usr/bin/env python3

def main():
    try:
        first = int(input("Enter first integer: "))
        second = int(input("Enter second integer: "))
    except EOFError:
        print("Input ended unexpectedly. Please provide two integers.")
        return
    except ValueError:
        print("Please enter valid integers.")
        return
    total = first + second
    print(f"The sum is {total}")

if __name__ == "__main__":
    main()
