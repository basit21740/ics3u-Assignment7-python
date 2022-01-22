#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program reverses a list


def reverse_list(not_reversed_list):
    # this function reverses a list
    reversed_list = []
    counter = len(not_reversed_list) - 1

    while counter >= 0:
        temp = not_reversed_list[counter]
        reversed_list.append(temp)
        counter = counter - 1

    return reversed_list


def main():
    # This function is the main function
    not_reversed_list = []
    reversed_list = []
    user_input = ""

    print("Keep entering anything and when you are done enter 'DONE' .")

    print()

    while user_input != "DONE":
        user_input = input("Insert:")
        if user_input != "DONE":
            not_reversed_list.append(user_input)

    reversed_list = reverse_list(not_reversed_list)

    print("\nReversed:")

    for counter in range(len(reversed_list)):
        print("{}".format(reversed_list[counter]))

    print("\nDone.")


if __name__ == "__main__":
    main()
