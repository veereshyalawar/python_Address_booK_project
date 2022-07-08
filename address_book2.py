class Contact:
    """
    In this class we are storing the details of a single contact

    """

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def display(self):
        return f"{self.first_name}\n" \
               f"{self.last_name}\n " \
               f"{self.phone_number}\n"

    def __repr__(self):
        return f"\n" \
               f" [FirstName = {self.first_name},  LastName = {self.last_name},  MobileNumber = {self.phone_number}]\n"


class AddressBook:
    def __init__(self, address_book_name):
        self.contact_dict = {}
        self.address_book_name = address_book_name

    def display(self):
        print(self.contact_dict)

    def add_contact(self, contact_obj):
        self.contact_dict.update({contact_obj.first_name: contact_obj})

    def get_contact(self, first_name):
        return self.contact_dict.get(first_name)

    def edit_contact(self, contact_obj, contact_data):
        contact_obj.first_name = contact_data.get("name")
        contact_obj.last_name = contact_data.get("last_name")
        contact_obj.phone_number = contact_data.get("number")

    def dlt_contact(self, first_name):
        del_contact = self.get_contact(first_name)
        if not del_contact:
            print(25 * "=")
            print("Name not Exist")
            print(25 * "=")
            return
        self.contact_dict.pop(first_name)
        print(25 * "=")
        print(f"'{first_name}'  contact deleted from AddressBook")
        print(25 * "=")


class AddressBookStore:
    def __init__(self):
        self.address_book_dict = {}

    def display_address_book_dict(self):
        print(self.address_book_dict)

    def add_address_book(self, address_book_obj):
        self.address_book_dict.update({address_book_obj.address_book_name: address_book_obj})

    def get_address_book(self, address_book_name):
        return self.address_book_dict.get(address_book_name)

    def dlt_addressbook(self, address_book_name):
        del_addressbook = self.get_address_book(address_book_name)
        if not del_addressbook:
            print(25 * "=")
            print("Address book name not exist")
            print(25 * "=")
            return
        self.address_book_dict.pop(del_addressbook.address_book_name)
        print(25 * "=")
        print(f"'{address_book_name}'  AddressBook deleted")
        print(25 * "=")


def exit():
    print(26 * "=")
    print("****Thank you****")
    print(26 * "=")


def create_addressbook():
    address_book_name = input("Enter address book name:->")
    add_address_book = address_book_store_obj.get_address_book(address_book_name)
    if add_address_book is not None:
        print(26 * "=")
        print("Address book already present")
        print(26 * "=")
    else:
        address_book_obj = AddressBook(address_book_name)
        address_book_store_obj.add_address_book(address_book_obj)


def display_address_book():
    address_book_store_obj.display_address_book_dict()


def add_new_contact():
    addressbook_name = input("Enter address book's name that you want to add a contact:-> ")
    address_book_obj = address_book_store_obj.get_address_book(addressbook_name)
    if address_book_obj is not None:
        contact_first_name = input("Enter first name:->")
        contact_las_name = input("Enter last name->")
        contact_phone_number = input("Enter phone num->")
        contact_obj = Contact(contact_first_name, contact_las_name, contact_phone_number)
        address_book_obj.add_contact(contact_obj)
    else:
        print("Address book not present")


def display_contact():
    addressbook_name = input("Enter address book name:-> ")
    address_book_obj = address_book_store_obj.get_address_book(addressbook_name)
    if address_book_obj is not None:
        address_book_obj.display()


def to_edit_contact():
    addressbook_name = input("Enter address book you want to edit:-> ")
    address_book_obj = address_book_store_obj.get_address_book(addressbook_name)
    if address_book_obj is not None:
        first_name = input("Enter first name of contact you want to edit->")
        contact_dict = address_book_obj.get_contact(first_name)
        if not contact_dict:
            print("Name not Exist")
        else:
            first_name = input("Enter new name->")
            last_name = input("Enter last name:->")
            phone_number = input("Enter new mobile number->")
            data_dict = {"name": first_name, "last_name": last_name, "number": phone_number}
            address_book_obj.edit_contact(contact_dict, data_dict)


def to_delete_contact():
    addressbook_name = input("Enter address book you want to edit:-> ")
    address_book_obj = address_book_store_obj.get_address_book(addressbook_name)
    if address_book_obj is not None:
        first_name = input("Enter first name of contact you want to delete->")
        address_book_obj.dlt_contact(first_name)
    else:
        print("contact not present")


def to_delete_Address_book():
    address_book_name = input("Enter address book you want to delete:-> ")
    address_book_store_obj.dlt_addressbook(address_book_name)


if __name__ == "__main__":

    print(26 * "=")
    print("**Welcome To AddressBook**")
    print(26 * "=")
    try:
        address_book_store_obj = AddressBookStore()
        while True:
            print("Enter your choice:-\n"
                  "1) To add Address book\n"
                  "2) To display AddressBook\n"
                  "3) To add new contact\n"
                  "4) To display contact\n"
                  "5) TO edit contact\n"
                  "6) To delete contact\n"
                  "7) To delete address book\n"
                  "0) To exit\n")

            choice_dict = {0: exit, 1: create_addressbook, 2: display_address_book, 3: add_new_contact,
                           4: display_contact, 5: to_edit_contact, 6: to_delete_contact, 7: to_delete_Address_book}
            choice = int(input("Enter a choice =>"))
            choice_dict.get(choice)()

    except Exception as e:
        print(e)
