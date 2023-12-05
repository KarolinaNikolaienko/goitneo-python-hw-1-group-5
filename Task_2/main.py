
def parse_input(user_input):
    """Parses entered by user command.
    The command splits on 'cmd' - action that user wants the program to do,
    and 'args' - data on which the action is performed.
    """
    if user_input:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    else:
        return [""]

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid data was given. Cannot add contact"
    name, phone = args
    name = name.title()
    if contacts and contacts.get(name, False): # if contacts are not empty and the contact being added already exists
        print(f"Contact {name} already exists. Do you want to rewrite it?")
        command = input("Yes / No:  ").strip().lower()
        while command not in ["yes", "no"]:
            command = input("Invalid command\nYes / No:  ").strip().lower()
        if command == "no":
            return "Contact remained unchanged"
        elif command == "yes":
            contacts[name] = phone
            return "Contact was rewritten"
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid data was given. Cannot change contact"
    name, phone = args
    name = name.title()
    if contacts and contacts.get(name, False): 
        contacts[name] = phone
        return "Contact updated"
    else:
        print(f"Contact {name} does not exist. Do you want to add it?")
        command = input("Yes / No:  ").strip().lower()
        while command not in ["yes", "no"]:
            command = input("Invalid command\nYes / No:  ").strip().lower()
        if command == "no":
            return "Contact was not added"
        elif command == "yes":
            contacts[name] = phone
            return "Contact added"

def show_phone(name, contacts):
    name = name.title()
    contact_number = contacts.get(name, False)
    if contact_number:
        return f"{contact_number}"
    else:
        return f"Contact {name} does not exist"

def all_contacts(contacts):
    if not contacts:
        return "Contact list is empty"
    str = ""
    for name, number in contacts.items():
        str += f"{name} {number}\n"
    return str.strip()
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        command = parse_input(input("Enter a command: ").strip().lower())

        if command[0] in ["close", "exit"]:
            print("Good bye!")
            break

        elif command[0] == "hello":
            print("How can I help you?")
        
        elif command[0] == "add":
            print(add_contact(command[1:], contacts))
        elif command[0] == "change":
            print(change_contact(command[1:], contacts))
        elif command[0] == "phone":
            print(show_phone(command[1], contacts))
        elif command[0] == "all":
            print(all_contacts(contacts))
        
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()