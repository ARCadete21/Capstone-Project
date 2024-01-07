import streamlit as st
import openai

######## Setting the overall page configuration ########
st.set_page_config(
    layout='wide',
    page_title='AiTHLETES F1 Hub | F1 Pilot',
    page_icon="🏎️",
    initial_sidebar_state='collapsed'
)


# st.text("Insert Bot :)")

user_message = st.text_input("You:", "")

# Output area for chat history
# st.text_area("Chat History:", value="", height=200, max_chars=None)


if user_message:
    # Append user's message to the chat history
    st.text_area("Chat History:", value=user_message, height=200, max_chars=None)

    # Generate a response from GPT-3.5
    response = openai.Completion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )

    # Extract and display the bot's response
    bot_response = response['choices'][0]['message']['content']
    st.text_area("Chat History:", value=f"{user_message}\nBot: {bot_response}", height=200, max_chars=None)

















####To Finish Off the Sidebar with Trademark
st.sidebar.markdown('''
---
Website developed for the \n Capstone Project Course
                    
                    © AiTHLETES  
''') 