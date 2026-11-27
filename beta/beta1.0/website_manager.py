
from SQL_access_key import *
from login_page import *
from encryption_key import *



def show_websites():#working
    conn = get_conn()
    curr = conn.cursor()
    print("Available websites: \n")
   
    curr.execute("""SELECT website_id, website_app
    FROM website""") 

    result = curr.fetchall()

    for row in result:
        print(row)

    curr.close()
    conn.close()

#show_websites()

def select_websites():
    conn = get_conn()
    curr = conn.cursor()
    show_websites()

    print("log in to access passwords \n")

    if login():
        select_id_input = input("Enter a websites ID: ")

        #sql 
        curr.execute("""SELECT website_id, website_app
        FROM website
        WHERE website_id = %s""", (select_id_input,)) 

        result = curr.fetchone()

        if result is not None:
            website_id=result[0]
            print("Website selected:", result[1], "\n") #result[1] is the website_app.
            
            curr.execute("""
    SELECT username,
           pgp_sym_decrypt(
               password,
               pgp_sym_decrypt(encrypted_key, %s::text)
           )
    FROM users
    WHERE website_id = %s
""", (MASTER_KEY, website_id))
            credentials = curr.fetchall() 

            #print(len(credentials)) #for debugning 

           
            for number, row in enumerate(credentials, start=1):      
                #number is the account number (1, 2, etc)
                #row contains the username and password.

                print(number, "Account name:", row[0])
                print("Password: *****\n")


            account_choice = int(input("Enter a number to select a account: ")) #convert string to interger
            selected_account= credentials[account_choice - 1]

            print("Confirm your identity by login in with your username and password\n")

            if login():
                print(number, "Account name:", selected_account[0])
                print("Password:", selected_account[1], "\n")
            

        else:
            print("Website not found")

    else: 
        print("Login failed")


  

    curr.close()
    conn.close()






