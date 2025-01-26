def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide both a name and a phone number."
    name, phone = args
    if name in contacts:
        return f"Error: Contact {name} already exists. Use 'change' to update the phone number."
    contacts[name] = phone
    return f"Contact {name} has been added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide both a name and a phone number."
    name, phone = args
    if name not in contacts:
        return f"Error: Contact {name} does not exist. Use 'add' to create a new contact."
    contacts[name] = phone
    return f"Contact {name} has been updated."


def get_phone(args, contacts):
    if len(args) != 1:
        return "Error: Please provide a name to look up."
    name = args[0]
    if name not in contacts:
        return f"Error: Contact {name} does not exist."
    return f"{name}: {contacts[name]}"


def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
