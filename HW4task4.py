def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name,phone = args
    if name not in contacts:
        return "Name Not Found"
    else:
        contacts[name] = phone
        return "Contact updated"
    
def phone_username(args, contacts):
    try:
        phone = contacts[args[0]]
        return phone
    except Exception:
        return "Contacts not found"

def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "all":
            print(contacts)
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(phone_username(args,contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()