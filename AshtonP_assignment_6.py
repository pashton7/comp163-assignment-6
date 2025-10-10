# AshtonP_assignment_6.py 
# Student: Ashton Partridge
# Assignment 6: Contact Information Formatter 
# Demonstrates mastery of string methods for data cleaning and formatting

# GITHUB LINK: https://github.com/pashton7/comp163-assignment-6

# Initial setup
user_input = "" # Variable to hold new user inputs that will be checked by the WHILE loop
contacts_dictionary = {} # Dictionary to hold our contact values
print("Enter contact information (format: name|phone|email|address):") # Initial prompt
count = 0 # Creates an int value that iterates through every successful iteration of the While loop and is used to set the key value of each contact

# While loop function that continually gets user input and formats the contacts they enter
while user_input.upper() != "DONE": # Run loop until DONE has been entered
    # Get user input and set up variables
    user_input = input() # Ask user for input

    if user_input.upper() != "DONE": # If string is not equal to DONE then format the split value and enter it into the table
        string_list = user_input.split("|") # split our string

        if len(string_list) < 4: # If the required fields are not inputed then print User Error and skip this iteration
            print("ERROR! All fields must be entered!")
            continue
        # Set unformatted variables to list elements
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
        for char in unformated_phone: # Iterate through every character in the string and set only those that are digits to digitsOnly string
            if char.isdigit():
                digitsOnly += char
        area_code = "(" + digitsOnly[:3] + ") " # Get the first 3 digits and set it as area code containted in "()"
        full_number = digitsOnly[3:6] + "-" + digitsOnly[6:] # Connect the next 3 numbers and the remaining numbers together putting "-" between them
        phone = area_code + full_number # Combine the area code and full_number to get the formatte phone number

        # Smart state detection
        address_split = address.split(" ") #split the address for iteration
        address = ""
        for index, word in enumerate(address_split): # Run through the split list and when it finds a two letter word convert it to all uppercase
            if word.isalpha() and len(word) == 2:
                address_split[index] = word.upper()
        address = " ".join(address_split) # Join the address together with the updated state identifier 

        contacts_dictionary[count] = {"name":name, "address":address, "phone":phone, "email":email} # Save our new formatted contact into a dictionary to pull from later
        count += 1 # Iterate count
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
for contact in contacts_dictionary: # Loops through all contacts in the dictionary
    name_split = contacts_dictionary[contact]['name'].split(" ") # Splits the first and last names
    last_first = name_split[-1] + ", " # Setup string to have last name appear first
    name_split.pop(-1) # Remove last name from the name_split list
    last_first += " ".join(name_split) # Add the remaining list elements to the last_first string
    print(f"{last_first:<30}{contacts_dictionary[contact]['phone']:<20}{contacts_dictionary[contact]['email']}") # Print the contact variables in correct format