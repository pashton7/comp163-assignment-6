# GITHUB LINK: 
user_input = ""

while user_input.upper() != "DONE":
    # Get user input and set up variables
    user_input = input("Enter contact information (format: name|phone|email|address): ")
    string_list = user_input.split("|")
    name = string_list[0]
    phone = string_list[1]
    email = string_list[2]
    address = string_list[3]
