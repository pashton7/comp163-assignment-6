# GITHUB LINK: 
user_input = ""
contacts_dictionary = {}
count = 1
while user_input.upper() != "DONE":
    # Get user input and set up variables
    user_input = input("Enter contact information (format: name|phone|email|address): ")
    if user_input.upper() != "DONE":
        string_list = user_input.split("|")
        unformated_name = string_list[0]
        unformated_phone = string_list[1]
        unformated_email = string_list[2]
        unformated_address = string_list[3]

        # Clean up name and address 
        name = unformated_name.strip().title()
        address = unformated_address.strip().title()

        # Standardize the Phone Number and format email
        email = unformated_email.lower()
        digitsOnly = ""
        for char in unformated_phone:
            if char.isdigit():
                digitsOnly += char
        area_code = "(" + digitsOnly[:3] + ") "
        number = digitsOnly[3:6] + "-" + digitsOnly[6:]
        phone = area_code + number

        contacts_dictionary[count] = {"name":name, "address":address, "phone":phone, "email":email} # Save our new formatted contact into a dictionary to pull from later
        count += 1 # increase our incriment
        
print("=== CONTACT DIRECTORY ===")
for contact in contacts_dictionary: # Go through each contact in the dictionary
    print(f"CONTACT {contact}")
    print(f"Name: {contacts_dictionary[contact]['name']}")
    print(f"Phone: {contacts_dictionary[contact]['phone']}")
    print(f"Email: {contacts_dictionary[contact]['email']}")
    print(f"Address: {contacts_dictionary[contact]['address']}")
    