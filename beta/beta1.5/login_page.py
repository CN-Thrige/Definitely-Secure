from SQL_access_key import * 




def signup():
    conn = get_conn()
    curr = conn.cursor()

    username_input = input("choose your username: ")
    password_input= input("choose your password: ")

    curr.execute("""
    INSERT INTO finger_print_pseudo (username, password)
    VALUES (%s, crypt(%s, gen_salt('bf')))""",(username_input, password_input)) #%s is a placeholder to storage data
    #values are now being hashed to encrypt them. read up on this...


    conn.commit() #commits the value to database
    curr.close() #closes to the cursor 
    conn.close() #closes the connection

def login():
    #Boolean variable
    login_success = False

    conn = get_conn()
    curr = conn.cursor()
    
    check_username=input("Enter your username: ")
    check_password=input("Enter your password: ")

    curr.execute("""SELECT username
FROM finger_print_pseudo
WHERE username = %s""", (check_username,)) #this only checks where or not a username exits

    result = curr.fetchone() #this retrives the username from the sql database 

    if result is not None:

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
        
        else:
            print("Incorrect password")
            #login()
    
    else:
        print("Username does not exist")
        #register()

    curr.close()
    conn.close()
    return login_success


