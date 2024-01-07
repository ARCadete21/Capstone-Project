import streamlit as st
from streamlit_option_menu import option_menu 
import json


######## Setting a new style for the page ########
st.set_page_config(
    layout='wide',
    page_title='AiTHLETES F1 Hub | Homepage',
    page_icon="🏎️",
    initial_sidebar_state='collapsed',
    #menu_items = {'item': 'link'} could be interesting to explore (top right corner)
)



# Load users if file exists, else create an empty dictionary
try:
    with open('users.json', 'r') as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

def authenticate(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

def register(username, password):
    if username in users:
        return False
    else:
        users[username] = password
        with open('users.json', 'w') as f:
            json.dump(users, f)
        return True

def display_home_page():
       
    # Add your news content here
    st.title("Latest News!")
    st.subheader("Verstappen's winning streak keeps on going as he wins in Spa!")
    st.image("https://www.autoracing1.com/wp-content/uploads/2023/f1/spa/podium2.jpg", width=1150)
    
    st.subheader("It's a disappointing drive from Daniel Ricciardo as he finishes below his teammate for the first time of the year!")
    st.image("https://i.guim.co.uk/img/media/d7be378ebe1048d91fee6e3dc2b53432a1c6acd2/0_0_5413_3248/master/5413.jpg?width=465&dpr=1&s=none", width=1150)

def display_registration_page():

    menu = ["Login", "SignUp"]
    choice = st.radio("", menu)

    if choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            if authenticate(username, password):
                st.success("Logged In as {}".format(username))
            else:
                st.warning("Incorrect Username/Password")
    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Enter username")
        new_password = st.text_input("Enter a password", type='password')

        if st.button("SignUp"):
            if register(new_user, new_password):
                st.success("You have successfully created an account")
                st.info("Go to Login Menu to login")
            else:
                st.warning("Username already exists")



import json
import hashlib

def hash_password(password):
    # Use a secure hashing algorithm like SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def authenticate(username, password):
    if username in users and users[username]["password"] == hash_password(password):
        return True
    else:
        return False

def register(username, password):
    if username in users:
        return False
    else:
        users[username] = {"password": hash_password(password)}
        with open('users.json', 'w') as f:
            json.dump(users, f)
        return True




def display_profile_settings(username):
    st.title(f"{username}'s Profile")
    st.subheader("Profile Settings for {}".format(username))

    current_password = st.text_input("Current Password", type='password')
    new_password = st.text_input("New Password", type='password')
    confirm_new_password = st.text_input("Confirm New Password", type='password')

    if st.button("Update Password"):
        if authenticate(username, current_password):
            if new_password == confirm_new_password:
                # Update the hashed password in your user data
                users[username]["password"] = hash_password(new_password)
                with open('users.json', 'w') as f:
                    json.dump(users, f)
                st.success("Password updated successfully!")
            else:
                st.warning("New Passwords do not match.")
        else:
            st.warning("Incorrect Current Password")

    # You can add more profile settings here based on your requirements


def main():
    menu_options = ["Home", "Registration", 'Profile']
    selected_option = option_menu("Select Menu", menu_options, orientation="horizontal")

  

    if selected_option == "Home":
            display_home_page()
    elif selected_option == 'Settings':
            display_profile_settings()
    elif selected_option == "Registration":
            display_registration_page()



                
                
                


if __name__ == "__main__":
    main()






























####To Finish Off the Sidebar with Trademark
st.sidebar.markdown('''
---
Website developed for the \n Capstone Project Course
                    
                    © AiTHLETES  
''')


st.sidebar.markdown("Social Media Links")
# st.sidebar.markdown('<a href="https://twitter.com/AiTHLETS" target="_blank"><img src="https://img.freepik.com/vetores-gratis/novo-design-de-icone-x-do-logotipo-do-twitter-em-2023_1017-45418.jpg?size=338&ext=jpg&ga=GA1.1.1412446893.1704585600&semt=ais" height="30" width="30" style="border-radius: 50%;"></a>', unsafe_allow_html=True)   
# st.sidebar.markdown('<a href="https://www.instagram.com/f1_aithletes/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/2048px-Instagram_logo_2016.svg.png" height="30" width="30"></a>', unsafe_allow_html=True)


st.sidebar.markdown('<a href="https://twitter.com/AiTHLETS" target="_blank"><img src="https://img.freepik.com/vetores-gratis/novo-design-de-icone-x-do-logotipo-do-twitter-em-2023_1017-45418.jpg?size=338&ext=jpg&ga=GA1.1.1412446893.1704585600&semt=ais" height="30" width="30" style="border-radius: 50%;"></a >'
                    '&nbsp;&nbsp;&nbsp;'
                        '<a href="https://www.instagram.com/f1_aithletes/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/2048px-Instagram_logo_2016.svg.png" height="30" width="30" style="border-radius: 50%;"></a>', unsafe_allow_html=True)
