
from SQL_access_key import *
from login_page import *
from encryption_key import *
from PIL import Image
from io import BytesIO
from pathlib import Path #https://docs.python.org/3/library/pathlib.html


#used in upload_all_website_images() function
image_folder = Path("website_images") #it finds the folder where the image is storage. it is a python library 


def upload_all_website_images(): 
    conn = get_conn()
    curr = conn.cursor()

    curr.execute("""
        SELECT website_id, website_app
        FROM website""")

    websites = curr.fetchall()
    image_files = image_folder.glob("*.jpg")

    for image_path in image_files:
        #print(image_path.stem) #look up .stem  to explain it
        for website in websites:
            website_id = website[0]
            website_name = website[1]

            if website_name == image_path.stem:
                #print(website_id, website_name, image_path)
                upload_website_image(website_id, image_path)

    #print(websites)

    curr.close()
    conn.close()

def upload_website_image(website_id, image_path):
    conn = get_conn()
    curr = conn.cursor()
    curr.execute("""
        SELECT 1
        FROM website_images
        WHERE website_id = %s """, (website_id,))

    result = curr.fetchone()
    if result is None:

        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            curr.execute("""
            INSERT INTO website_images (website_id, image_data)
            VALUES (%s, %s)""", (website_id, image_data,))

    #else: 
        #print("ERROR: image exists")

    conn.commit()
    curr.close()
    conn.close()


    #print(len(image_data), "bytes loaded")

#testing
#upload_website_image(1, "google_image.jpg")

def get_website_image(website_id):
    conn = get_conn()
    curr = conn.cursor()

    curr.execute("""
        SELECT image_data
        FROM website_images
        WHERE website_id = %s
    """, (website_id,))

    result = curr.fetchone()

    if result is not None:
        image_data = result[0]
    else:
        image_data = None



    curr.close()
    conn.close()
    return image_data

def display_website_image(image_data):
    image = Image.open(BytesIO(image_data))
    image.show()

def show_websites():#working
    conn = get_conn()
    curr = conn.cursor()
    print("Available websites: \n")
   
    curr.execute("""SELECT website_id, website_app
    FROM website""") 

    result = curr.fetchall()

    #for row in result:
        #print(row)

    for row in result:
        website_id = row[0]
        website_name = row[1]

        print("Website ID:", website_id, "| Website:", website_name)
        image_data = get_website_image(website_id)

        if image_data is not None:
            display_website_image(image_data)
        else:
            print("No image available")

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
               pgp_sym_decrypt(encrypted_key, %s::text))
            FROM users
            WHERE website_id = %s""", (MASTER_KEY, website_id))
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






#upload_website_image(1, "meta_image.jpg")
