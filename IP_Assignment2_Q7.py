import json

def read_file(fname):
    try:
        with open(fname, 'r') as file:
            return json.load(file)
    except:
        return {}

def write_file(address_book, fname):
    with open(fname, 'w') as file:
        json.dump(address_book, file)

def insert_entry(address_book):
    name = input("Enter the name of the person: ")
    address = input("Enter the address of the person: ")
    phone = input("Enter the phone number of the person: ")
    email = input("Enter the email address of the person: ")
    if name in address_book:
        address_book[name].append({'address': address, 'phone': phone, 'email': email})
    else:
        address_book[name] = [{'address': address, 'phone': phone, 'email': email}]
    print(f'{name} has been added to the address book.')

def delete_entry(address_book):
    name = input("Enter the name of the person to delete: ")
    if name in address_book:
        del address_book[name]
        print(f'{name} has been deleted from the address book.')
    else:
        print(f'{name} not found in the address book.')

def find_entry(address_book):
    name = input("Enter the name or a part of the name to search: ")
    matching_entries = {}
    for key, value in address_book.items():
        if name.lower() in key.lower():
            matching_entries[key] = value
    return matching_entries

def find_by_phone_or_email(address_book):
    search_term = input("Enter the phone number or email address to search: ")
    matching_entries = {}
    for key, value in address_book.items():
        for item in value:
            if search_term in item.values():
                if key in matching_entries:
                    matching_entries[key].append(item)
                else:
                    matching_entries[key] = [item]
    return matching_entries

def merge_address_book(address_book, friend_address_book):
    address_book.update(friend_address_book)
    print("Address books merged successfully.")

address_book = read_file('addrbook.txt')
while True:
    choice = input("Enter your choice (i: insert, d: delete, f: find, p: find by phone/email, m: merge, e: exit): ")
    if choice == 'i':
        insert_entry(address_book)
    elif choice == 'd':
        delete_entry(address_book)
    elif choice == 'f':
        print(find_entry(address_book))
    elif choice == 'p':
        print(find_by_phone_or_email(address_book))
    elif choice == 'm':
        friend_address_book = read_file()
