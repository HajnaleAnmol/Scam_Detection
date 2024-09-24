import streamlit as st
import pandas as pd

# Load user credentials from the CSV file
def load_users():
    return pd.read_csv("users.csv")

# Set the title of the app
st.title("Traud Detection Login")

# Load user data
users_df = load_users()

# Create a form for login
with st.form(key='login_form'):
    username = st.text_input("Username", max_chars=20)
    password = st.text_input("Password", type="password")

    # Create a submit button
    submit_button = st.form_submit_button(label='Login')

    if submit_button:
        # Check if the username exists in the DataFrame
        if username in users_df['username'].values:
            # Get the stored password for the given username
            stored_password = users_df.loc[users_df['username'] == username, 'password'].values[0]
            
            # Check if the entered password matches the stored password
            if stored_password == password:
                st.success("Login successful!")
                # You can redirect to another page or display a message here
            else:
                st.error("Invalid password.")
        else:
            st.error("Username not found.")
