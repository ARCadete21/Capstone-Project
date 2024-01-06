import streamlit as st
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('your_database_name.db')
c = conn.cursor()

# Functions
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT, title TEXT, question TEXT, qdate DATE)')

def add_data(author, title, question, qdate):
    c.execute('INSERT INTO blogtable(author, title, question, qdate) VALUES (?,?,?,?)', (author, title, question, qdate))
    conn.commit()

def view_all_questions():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

# Streamlit UI
create_table()

st.subheader("Do you have any questions? Feel free to ask us!")
st.markdown("")
st.markdown("Fill in the form below!")
st.markdown("")

# Asking the user to insert his name
name = st.text_input("Name:", max_chars=40)
# Title of the request
question_title = st.text_input("State your question briefly (Title of your Request)", max_chars=100)
# Corpus of the question
question = st.text_area("Insert your question explained here")
# Entering date
qdate = st.date_input("Enter the current date:")

if st.button("Add"):
    with conn:
        add_data(name, question_title, question, qdate)
        st.write(f"Question: {question_title} saved")

# Close the connection when done
conn.close()
