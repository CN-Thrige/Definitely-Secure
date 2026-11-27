from psycopg2 import *
from SQL_access_key import *
#from login_page import *
from administrator_page import Administrator
from website_manager import *
from account_manager import *
from initialize_database import *

admin = Administrator() #creating the object from a class


def main(): 
    main_loop = 'c'

    while main_loop:
        menu_input=input("Password manger demo menu\n" \
        "1 Create a administrator acount\n" \
        "2 Add websites or app accounts\n" \
        "3 Access websites or app accounts\n" \
        "4 Delete websites or app account\n" \
        "5 Exit\n")
        
        if menu_input=="1": #create admin account
            print("Create administrator account: \n")
            admin.signup() #from login_page.py


        elif menu_input=="2": #add a website or app account to the password manager 
            if admin.login(): #open with admin account
                print("Add website or app account\n")
                create_account()
            else: 
                print("\nERROR\n"
                    "Login failed\n")
                main() #maybe...

        elif menu_input=="3": #access a website or app account
            if admin.login(): #open with admin account
                print("Access website or app account \n")
                select_websites() #website_manager.py 
            else: 
                print("\nERROR\n"
                    "Login failed\n")
                main()

        elif menu_input=="4": #delete a website or app account
            if admin.login(): #open with admin account
                print("Delete a website or app account \n")
                delete_account()
            else: 
                print("\nERROR\n"
                    "Login failed\n")
                main() 

        elif menu_input=="5":
            if admin.login():
                main_loop = input('> Would yould like to end the program? press c to continue or s to stop): ')

                if main_loop == "c":
                    continue

                elif main_loop == "s":
                    break #ends the program

                else:
                    print("\nERROR\n"
                    "Enter c to continue or s to stop the program\n")

            else: 
                print("\nERROR\n"
                        "Login failed\n")
                main()

        else:   
            print("\nERROR\n"
            "Enter a valid number from the menu\n")
            

  
if __name__ == "__main__":
    init_database() #This function intialize the database IF the 3 tables does not exist 
    upload_all_website_images() #Adds the functiality of adding pictures to each website (alpha - mainly for demoing) - remove afterwards
    main() #Intializes the entire program 
