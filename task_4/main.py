from typing import Callable, Dict, List, Tuple


# Decorator to handle input errors
def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format or missing arguments."

    return inner


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 1:
        raise ValueError
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts: Dict[str, str]) -> str:
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."


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
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
