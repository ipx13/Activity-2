def menu():
    print("\n----- Menu -----\n"
          "1 -> Add an element\n"
          "2 -> Insert an element\n"
          "3 -> Modify an element\n"
          "4 -> Delete an element\n"
          "5 -> Arrange in ascending order\n"
          "6 -> Arrange in descending order\n"
          "7 -> Exit the program")

arr0 = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]

print("\nWelcome to my program! You can do stuff to the given array using the functions I've implemented. Feel free to test each of it!")
print("\nGiven Array: {}".format(arr0))

while True:
    menu()
    choice = input("\nWhat do you want to do? (1-7): ")
    if choice in ("1", "2", "3", "4", "5", "6", "7"):
        if choice == "1":
            print("\n----- Adding an element -----\n"
                  "What element would you like to add to the array?\n"
                  "NOTE: Please provide an integer for the number.\n")
            print("Current Array:", arr0,"\n")
            while True:
                try:
                    addch1 = int(input("Number: "))
                    break
                except:
                    print("Please enter an integer.\n")
                    continue
            arr0.append(addch1)
            print("\nSuccessfully Implemented!\n"
                  "Added element:", addch1)
            print("New Array:", arr0)
            continue

        elif choice == "2":
            print("\n----- Inserting an element -----\n"
                  "What element would you like to insert in the array?\n"
                  "NOTE: Please enter integers ONLY.\n")
            print("Current Array:", arr0, "\n")
            while True:
                try:
                    print("Enter the number to be inserted")
                    insch2 = int(input("Number: "))
                    break
                except:
                    print("Please enter an integer.\n")
                    continue
            while True:
                try:
                    print("At which index?")
                    indch2 = int(input("Index: "))
                    break
                except:
                    print("Please enter an integer.\n")
                    continue
            arr0.insert(indch2, insch2)
            print("\nSuccessfully Implemented!\n"
                  "Inserted", insch2, "at index", indch2)
            print("New Array:", arr0)
            continue

        elif choice == "3":
            print("\n----- Modifying an element -----\n"
                  "Which element would you like to modify in the array?\n"
                  "NOTE: Please provide integers.\n")
            print("Current Array:", arr0, "\n")
            while True:
                try:
                    print("Which number should be modified? Please enter its index.")
                    indch3 = int(input("Index: "))
                    break
                except:
                    print("Please enter an integer.\n")
                    continue
            while True:
                try:
                    print("What number are you going to replace it with?")
                    modch3 = int(input("Number: "))
                    break
                except:
                    print("Please enter an integer.\n")

            moddch3 = arr0.pop(indch3)
            arr0.insert(indch3, modch3)
            print("\nSuccessfully Implemented!\n"
                  "Previous number:", moddch3, "\n"
                  "Modified number:", modch3, "\n")
            print("New Array:", arr0)
            continue

        elif choice == "4":
            print("\n----- Deleting an element -----\n"
                  "Which element would you like to delete in the array?\n"
                  "NOTE: Please provide an integer for the index.\n")
            print("Current Array:", arr0, "\n")
            while True:
                try:
                    print("Which number should be deleted? Please enter its index.")
                    indch4 = int(input("Index: "))
                    break
                except:
                    print("Please enter an integer.\n")
                    continue

            delch4 = arr0.pop(indch4)
            print("\nSuccessfully Implemented!\n"
                  "Deleted number:", delch4, "\n")
            print("New Array:", arr0)
            continue

        elif choice == "5":
            print("\n----- Sorting in Ascending Order -----\n")
            arr0.sort()
            print("\nSuccessfully Implemented!\n")
            print("New Array:", arr0)
            continue

        elif choice == "6":
            print("\n----- Sorting in Descending Order -----\n")
            arr0.sort(reverse=True)
            print("Successfully Implemented!\n")
            print("New Array:", arr0)
            continue


        elif choice == "7":
            print("\nThank you for using this program! :D")
            break
        break
    else:
        print("Please enter either of the integers from 1-7.")
        continue