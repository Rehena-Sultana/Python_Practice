'''
Phone Book বানাও:
   - নাম দিয়ে number খোঁজো
   - নতুন contact add করো
   - Contact delete করো
   - সব contact alphabetically print করো
   (while loop দিয়ে menu driven program)
'''
phonebook = {
    "A": "01711-234567",
    "B": "01812-345678",
    "C": "01913-456789",
            }

def search_contact(name):
    if name in phonebook:
        print(f"  Found: {name} in the phonebook")
    else:
        print(f"  '{name}' not found.")

def add_contact(name, number):
    if name in phonebook:
        print(f"'{name}' already exists.")
    else:
        phonebook[name] = number
        print(f"'{name}' added successfully.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"'{name}' deleted.")
    else:
        print(f"'{name}' not found.")

def show_all():
    if not phonebook:
        print("Phonebook is empty.")
        return
    print(f"\n  {'Name':<10} {'Number'}")
    for name in sorted(phonebook):        # alphabetically
        print(f"  {name:<10} {phonebook[name]}")


# Main while loop — menu driven

while True:
    print("\nPhone Book ")
    print("  1. Search contact")
    print("  2. Add contact")
    print("  3. Delete contact")
    print("  4. Show all contacts")
    print("  5. Exit")

    choice = input("Choose (1-5): ").strip()

    if choice == "1":
        name = input("Enter name to search: ").strip()
        search_contact(name)

    elif choice == "2":
        name   = input("Enter name: ").strip()
        number = input("Enter number: ").strip()
        add_contact(name, number)

    elif choice == "3":
        name = input("Enter name to delete: ").strip()
        delete_contact(name)

    elif choice == "4":
        show_all()

    elif choice == "5":
        print("Goodbye!")
        break                             # while loop শেষ

    else:
        print("  Invalid choice. Enter 1-5.")