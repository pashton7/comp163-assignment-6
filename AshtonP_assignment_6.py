# GITHUB LINK: 
user_input = ""
contacts_dictionary = {}
count = 1
while user_input.upper() != "DONE":
    # Get user input and set up variables
    user_input = input("Enter contact information (format: name|phone|email|address): ")
    if user_input.upper() != "DONE":
        string_list = user_input.split("|")
        name = string_list[0]
        phone = string_list[1]
        email = string_list[2]
        address = string_list[3]

        # Clean up name and address 
        name = name.strip().title()
        address = address.strip().title()

        contacts_dictionary[count] = {"name":name, "address":address} # Save our new formatted contact into a dictionary to pull from later
        count += 1 # increase our incriment
        
print("=== CONTACT DIRECTORY ===")
for contact in contacts_dictionary: # Go through each contact in the dictionary
    print(f"CONTACT {contact}")
    print(f"Name: {contacts_dictionary[contact]['name']}")
    print(f"Address: {contacts_dictionary[contact]['address']}")