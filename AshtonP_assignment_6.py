# GITHUB LINK: 
user_input = ""
contacts_dictionary = {}
count = 1
print("Enter contact information (format: name|phone|email|address):")
while user_input.upper() != "DONE": # Run loop until DONE has been entered
    # Get user input and set up variables
    user_input = input()

    if user_input.upper() != "DONE": # If string is not equal to DONE then format the split value and enter it into the table
        string_list = user_input.split("|")
        unformated_name = string_list[0]
        unformated_phone = string_list[1]
        unformated_email = string_list[2]
        unformated_address = string_list[3]

        # Clean up name and address 
        name = unformated_name.strip().title()
        address = unformated_address.strip().title()

        # Standardize the Phone Number and format email
        email = unformated_email.strip().lower()
        digitsOnly = ""
        for char in unformated_phone:
            if char.isdigit():
                digitsOnly += char
        area_code = "(" + digitsOnly[:3] + ") "
        number = digitsOnly[3:6] + "-" + digitsOnly[6:]
        phone = area_code + number

        # Smart state detection 
        address_split = address.split(" ")
        address = ""
        for index, word in enumerate(address_split): # Run through the split list and when it finds a two letter word convert it to all uppercase
            if word.isalpha() and len(word) == 2:
                address_split[index] = word.upper()
        address = " ".join(address_split) # Join the address together with the updated state identifier 

        contacts_dictionary[count] = {"name":name, "address":address, "phone":phone, "email":email} # Save our new formatted contact into a dictionary to pull from later
        count += 1 # increase our incriment

# Print all the contacts that were added to the table
print("\n=== CONTACT DIRECTORY ===\n")
for contact in contacts_dictionary: # Go through each contact in the dictionary
    print(f"CONTACT {contact}:")
    print(f"Name:     {contacts_dictionary[contact]['name']}") # Pulls name from the table
    print(f"Phone:    {contacts_dictionary[contact]['phone']}") # Pulls phone number from the table
    print(f"Email:    {contacts_dictionary[contact]['email']}") # Pulls email from the table
    print(f"Address:  {contacts_dictionary[contact]['address']}") # Pulls address from the table
    print()
# Display how many contacts were added to the table in total
print("=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {len(contacts_dictionary)}\n")

# Display a quick overview of the contacts that were added
print("=== FORMATTED FOR PRINTING ===")
for contact in contacts_dictionary:
    name_split = contacts_dictionary[contact]['name'].split(" ")
    last_first = name_split[-1] + ", "
    name_split.pop(-1)
    last_first += " ".join(name_split)
    print(f"{last_first:<30}{contacts_dictionary[contact]['phone']:<20}{contacts_dictionary[contact]['email']}")