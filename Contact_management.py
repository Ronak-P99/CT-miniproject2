
import re
import os



def add_number(contacts):
    name = input("What is the contact name you would like to add? ")
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
    while True:
        number = input("Now provide the number associated with the name ")
        email = input("Lastly, provide a valid email address ")
        if len(number) == 10 and re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email) :
            contacts[name] = {'Number': re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', number), 'Email': email}
            return contacts
        else:
            print("\nNot a valid number or email. Please make sure the number length is 10 and we will format the rest! Also make sure to format your email correctly!\n")



def edit_contact(contacts):
    user_input = input("\nWhat would you like to edit?\n1. Phone number\n2. Email?\n")
    
    while True:
        if user_input == '1':
            name_number = input("What is the name asscoiated with the number? ")
            new_number = input("Now provide the new number you would like ")
        
            if(name_number in contacts):
                contacts[name_number]["Number"] = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', new_number)
                break
            else:
                print(f"No name {name_number} found in contacts.")
        
        if user_input == '2':
            name_email = input("What is the name asscoiated with the email? ")
            new_email = input("Now provide the new email you would like ")

            if(name_email in contacts):
                if re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", new_email):
                    contacts[name_email]["Email"] = new_email
                    break
                else:
                    print("Invalid email format!")
            else:
                print(f"No name {name_email} found in contacts.")



def delete_contact(contacts):
    print("\n!!!Keep in mind once a contact information is deleted, you will need to enter ALL the information again to bring it back!!!")
    user_input = input("What is the name of the contact you would like to delete? ")

    if user_input in contacts:
        del contacts[user_input]
        print("\nContact has been safely deleted!")
    else:
        print("Name not found in contact. Try again")



def search_contact(contacts):
    while True:
        user_input = input("\nPlease provide the name of the contact you would like to search for ")

        if user_input in contacts:
            print(f"\n{user_input}'s contact information:")

            for number, email in contacts[user_input].items():
                print(f"{number} - {email}")
                break
        else:
            print("\nThe contact name you have chosen is not in your contact!")




def export_contacts(contacts):
    try:
        with open('contacts.txt', 'w') as file_object:
                for name in contacts:
                    file_object.write(f"{name}:\n")
                    for number, email in contacts[name].items():
                        file_object.write(f"{number} - {email}\n")

    except FileNotFoundError:
        print("No available file!")



#I am confident with all my other functions but struggled with this one. If any tips, I will redo it! Thanks and hope everything else works smoothly!
def import_contacts(filename):
    try:
        with open(filename, 'r') as file:
            file_dict = {}
            lines = file.readlines() 

            for line in lines:
                key = line.split(':')
                file_dict[key[0]] = {'Number' + ':' + key[2] + ':' + key[3]}
                print(file_dict) 
    
    except FileNotFoundError:
        {}



def main():
    contacts = {'Ronak': {'Number': '(215) 313-3219', 'Email': 'rocky101299@gmail.com'}, 'Ricky': {'Number': '(630) 923-0126', 'Email': 'rickypatel00@gmail.com'}}
    print("\nWelcome!")
    
    while True:
        print("\n1. Add a new Contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Export contacts to a text file\n6. Import contacts from a text file\n7. Quit\n")
        user_input = input("Which number would you like to select? ")

        if user_input == '1':
            add_number(contacts)
        if user_input == '2':
            edit_contact(contacts)
        if user_input == '3':
            delete_contact(contacts)
        if user_input == '4':
            search_contact(contacts)
        if user_input == '5':
            export_contacts(contacts)
        if user_input == '6':
            import_contacts('import_contacts.txt')
        if user_input == '7':
            break
           
if __name__ == "__main__":
    main()
  
