from psycopg2 import *
from SQL_access_key import *
from login_page import *
from website_manager import *
from account_manager import *

def main():
    while True:
        account_ans=input("Options\n" \
        "a Sign Up\n" \
        "b login and create accounts\n" \
        "c quit\n")
        
        if account_ans=="a":
            print("Create new user: ")
            signup()

        if account_ans=="b":
            if login(): #even with yellow line it still works
                print("Welcome to your password vault!")

                user_input = input("Options\n" \
                "1 create accounts and passwords for websites\n"
                "2 access accounts and passwords\n"
                "3 delete accounts and passwords\n") #does not exist (yet...)

                if user_input == "1":
                    create_account()

                if user_input == "2": 
                    select_websites()

        if account_ans=="c":
            break
  
if __name__ == "__main__":
    main()
