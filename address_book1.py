class Contact:
    def __init__(self, contact):
        """
        :param contact: it is a dictionary created based on user input
        """
        self.first_name = contact.get("first_name")
        self.last_name = contact.get("last_name")
        self.address = contact.get("address")
        self.city = contact.get("city")
        self.state = contact.get("state")
        self.zip = contact.get("zip")
        self.phone_number = contact.get("number")
        self.email = contact.get("email")

    def __str__(self) -> str:
        return f"First Name = {self.first_name}, Last Name = {self.last_name}, Address = {self.address}, City = {self.city}," \
               f" State = {self.state}, Zip = {self.zip}, Phone Number = {self.phone_number}, Email = {self.email}"


class AddressBookConsoleService:
    address_books = {}

    def create_contact(self):

        """
        :return: return contact dict
        """
        contact_dict = {
            "first_name": "",
            "last_name": "",
            "address": "",
            "city": "",
            "state": "",
            "zip": "",
            "number": "",
            "email": ""
        }
        contact_obj = Contact(contact_dict)
        contact_obj = self.get_Details(contact_obj)
        return contact_obj

    def get_Details(self, contact):

        """
        :param contact: store all inforfamation related to a specific person
        :return:
        """
        contact.first_name = input("Enter first name \n")
        contact.last_name = input("Enter last name \n")
        contact.address = input("Enter address \n")
        contact.city = input("Enter city \n")
        contact.state = input("Enter state \n")
        contact.zip = input("Enter zip code \n")
        contact.phone_number = input("Enter phone number \n")
        contact.email = input("Enter email address \n")

        return contact

    def add_contact(self):

        """
        :return: add new contact details in the addressbook
        """
        new_contact = self.create_contact()
        print("contact created")
        address_book_name = input("Enter the address book name \n")
        address_book = self.address_books.get(address_book_name)
        # if book does no already exists then creating a new book
        if address_book is None:
            contact_list = [new_contact]
            self.address_books[address_book_name] = contact_list
            print("New address book created and contact added to it")
        # if book already exsists then adding contact to existing book
        else:
            contact = AddressBookConsoleService.search_by_first_name(address_book, new_contact.first_name)
            if len(contact) == 0:
                address_book.append(new_contact)
                print("Contact added successfully")
            else:
                print("Contact already exist")

    def display_contact(self):

        """
        :return: shows all contact details from addressbook dict
        """
        for address_book in self.address_books:
            contacts = "\n".join(str(contact) for contact in self.address_books.get(address_book))
            print(f"Contacts In {address_book} are \n{contacts}")

    def edit_contact(self):

        """
        :return: edited specified contact details
        """
        book_name = input("Enter the address book name ")
        address_book = self.address_books.get(book_name)
        if address_book is not None:
            first_name = input("Enter the person name \n")
            contact_to_edit = AddressBookConsoleService.search_by_first_name(address_book, first_name)
            if len(contact_to_edit) == 0:
                print("Contact not found")
            else:
                self.get_Details(contact_to_edit[0])
                print("Contact Edited Successfully")
        else:
            print("No such address book")

    def delete_contact(self):

        """
        :return: delete the specified person contact details
        """
        book_name = input("Enter the address book name ")
        address_book = self.address_books.get(book_name)
        if address_book is not None:
            first_name = input("Enter the person name \n")
            contact_to_delete = AddressBookConsoleService.search_by_first_name(address_book, first_name)
            if len(contact_to_delete) == 0:
                print("Contact not found")
            else:
                address_book.remove(contact_to_delete[0])
                print("Contact removed successfully")
        else:
            print("No such address book")

    @staticmethod
    def search_by_first_name(address_book, first_name):
        """
        :param address_book: book name in which we want to search
        :param first_name: first name of the person whom we want to search
        :return: the contact details of specified person
        """
        return [contact for contact in address_book if contact.first_name == first_name]

    def search_person_by_location(self):

        """
        :return: the person's detail based on location
        """
        contacts = self.contact_founder()
        if len(contacts) == 0:
            print("No such contact found")
        else:
            search_contacts = "\n".join(contact.first_name + " " + contact.last_name for contact in contacts)
            print(search_contacts)

    def view_person_by_location(self):
        """
        :return: person details by their location across the multiple address book
        """
        contacts = self.contact_founder()
        if len(contacts) == 0:
            print("No such contact found")
        else:
            view_contacts = "\n".join(str(contact) for contact in contacts)
            print(view_contacts)

    def contact_founder(self):

        """
        :return: the list of contact based on location
        """
        location = input("Enter the city or state of which contacts name you have to find \n")
        matched_contacts_with_location = []
        for address_book in self.address_books:
            matched_contacts_with_location.extend([contact for contact in self.address_books.get(address_book) if
                                                   contact.city == location or contact.state == location])
        return matched_contacts_with_location


if __name__ == "__main__":

    print("Welcome to Address Book Management System")
    console_service = AddressBookConsoleService()

    while True:
        print(" 1 Add Contact "
              "\n 2 Display Contact"
              "\n 3 Edit Contact"
              "\n 4 Delete Contact"
              "\n 5 Search by City or State"
              "\n 6 View Person by City or State"
              "\n 0 Exit")

        input_dict = {
            1: console_service.add_contact,
            2: console_service.display_contact,
            3: console_service.edit_contact,
            4: console_service.delete_contact,
            5: console_service.search_person_by_location,
            6: console_service.view_person_by_location,
            7: exit
        }
        user_choice = int(input())
        input_dict[user_choice]()