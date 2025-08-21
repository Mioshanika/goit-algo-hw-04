from pprint import pprint

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid arguments. Expecting: add <name> <phone>"
    if name in contacts.keys():
        return "Contact already exists. Please use 'change' command instead."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid arguments. Expecting: change <name> <phone>"
    if name not in contacts.keys():
        return "There is no such contact. Please use an 'add' command instead."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    if not args:
        return "Invalid arguments. Expecting: phone <name>"
    name = args[0]
    if name not in contacts.keys():
        return f"Contact with name [{name}] was not found."
    return contacts[name]

def show_all(contacts):
    contacts_list = []
    for name, contact in contacts.items():
        contacts_list.append(f"{name} - {contact}")
    return contacts_list

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))     
        elif command == "all":
            pprint(show_all(contacts), width=40, compact=False)                   
        else:
            print("Invalid command. Available commands are: hello, add, change, phone, all, close, exit")

if __name__ == "__main__":
    main()
