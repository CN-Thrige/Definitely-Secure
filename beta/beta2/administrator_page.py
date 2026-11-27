from SQL_access_key import * 


class Administrator:

    def __init__(self):
        self.authenticated = False #authentication status:
        
    def signup(self):
        conn = get_conn()
        curr = conn.cursor()

        username_input = input("Enter a username for the administrator account: ")
        password_input= input("Enter a password: ")
        print("\n") #fluff

        curr.execute("""
        INSERT INTO finger_print_pseudo (username, password)
        VALUES (%s, crypt(%s, gen_salt('bf')))""",(username_input, password_input)) #%s is a placeholder to storage data
        #values are now being hashed to encrypt them. read up on this...


        conn.commit() #commits the value to database
        curr.close() #closes to the cursor 
        conn.close() #closes the connection

    def login(self):
        self.authenticated = False #Checks if the user is suppose to have access or not 


        conn = get_conn()
        curr = conn.cursor()

        print("Finger print scanner demo: \n")
        check_username=input("Enter the administrator username: ")
        print("\n") 
        check_password=input("Enter the password: ")
        print("\n") 

        curr.execute("""SELECT username
        FROM finger_print_pseudo
        WHERE username = %s""", (check_username,)) #this only checks where or not a username exits

        result = curr.fetchone() #this retrives the username from the sql database 

        if result is not None: 
            """
            None in the if-statement means that. 
            IF something is true, then log in. 
            but if it is false, then don't log in the user. This is critical,
            as this structure is used through out the project
            """

            curr.execute("""
            SELECT username
            FROM finger_print_pseudo
            WHERE username = %s
            AND password = crypt(%s, password)""", (check_username, check_password))

            result = curr.fetchone()

            if result is not None:
                print("Login successful")
                #continue to the rest of the program from here...
                login_success = True 
                self.authenticated = True #this is double layer of security to check if the user is authoritized to log in 

            
            else:
                print("Incorrect password")
                #login()
        
        else:
            print("Username does not exist")
            #register()

        curr.close()
        conn.close()
        return self.authenticated



admin = Administrator()

admin.login()
#print(admin.authenticated)

