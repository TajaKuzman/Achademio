import streamlit as st
from streamlit_chat import message
import openai

openai.api_key = open("API_key", "r").read()

# Now define the bot's knowledge:
#genre_survey = open("data/genre_survey.txt", "r").read()

#bot_knowledge = "You are especially knowledgeable on automatic genre identification. Here's what you know about it: {genre_survey[:1000]}"

#if 'context' not in st.session_state:
#    st.session_state.context = [ {'role':'system', 'content':"{}".format(bot_role)} ]

if 'button_option' not in st.session_state:
    st.session_state.button_option = ["rewrite"]


# In the on_click event of the button, transfer the query from text input into agent.run() function to start the chain execution. After the chain is finished, append the response and original prompt into two lists of st.session_state for display on the web by streamlit_chat component as chat history
def send_click():
    if st.session_state.user != '':
        prompt = st.session_state.user

        # Append the prompt to the context
        #curr_context.append({'role':'user', 'content':"Rewrite the following: {}".format(prompt)})

        # Define the bot role:
        bot_role = "You are AChatdemio, a bot that helps young researchers to write better research papers. You respond in a concise and academic style. Write short sentences, so that they are clear."

        # Define the ChatGPT model
        output = openai.ChatCompletion.create(
            # Define the model
            model="gpt-3.5-turbo",
            # Define the prompt - add the context
            messages = [
                {'role':'system', 'content':"{}".format(bot_role)},
                {'role':'user', 'content':"Rewrite the following: {}".format(prompt)}
            ],
            # Set the temperature to 0 to get the most stable results
            temperature = 0,
        )

        response = output['choices'][0].message.content

        st.write(response)

        # Add the response to the context
        #st.session_state.context.append({'role':'assistant', 'content': '{}'.format(response)})
        #return context

def academic():
    if st.session_state.user != '':
        prompt = st.session_state.user

        # Define the bot role:
        bot_role = "You are AChatdemio, a bot that helps young researchers to write better research papers. You respond in a clear, concise and academic style."

        # Define the ChatGPT model
        output = openai.ChatCompletion.create(
            # Define the model
            model="gpt-3.5-turbo",
            # Define the prompt - add the context
            messages = [
                {'role':'system', 'content':"{}".format(bot_role)},
                {'role':'user', 'content':"Rewrite the following text, delimited by triple backticks, in academic style: ```{}```".format(prompt)}
            ],
            # Set the temperature to 0 to get the most stable results
            temperature = 0,
        )

        response = output['choices'][0].message.content

        st.write(response)

def bullet():
    if st.session_state.user != '':
        prompt = st.session_state.user

        # Define the bot role:
        bot_role = "You are AChatdemio, a bot that helps young researchers to write better research papers. You respond in a clear, concise and academic style."

        # Define the ChatGPT model
        output = openai.ChatCompletion.create(
            # Define the model
            model="gpt-3.5-turbo",
            # Define the prompt - add the context
            messages = [
                {'role':'system', 'content':"{}".format(bot_role)},
                {'role':'user', 'content':"Provide one paragraph of text from the following bullet point list, delimited by triple backticks: ```{}```".format(prompt)}
            ],
            # Set the temperature to 0 to get the most stable results
            temperature = 0,
        )

        response = output['choices'][0].message.content

        st.write(response)

def proofreading():
    if st.session_state.user != '':
        prompt = st.session_state.user

        # Define the bot role:
        bot_role = "You are AChatdemio, a bot that helps young researchers to write better research papers. You respond in a clear, concise and academic style."

        # Define the ChatGPT model
        output = openai.ChatCompletion.create(
            # Define the model
            model="gpt-3.5-turbo",
            # Define the prompt - add the context
            messages = [
                {'role':'system', 'content':"{}".format(bot_role)},
                {'role':'user', 'content':"Find errors in the following text, delimited by triple backticks: ```{}```. Only ouput the errors and suggest how they should be corrected.".format(prompt)}
            ],
            # Set the temperature to 0 to get the most stable results
            temperature = 0,
        )

        response = output['choices'][0].message.content

        st.write(response)

st.title(":blue[Achademio] ☕")
st.write("# Improve the style of your research papers with AI")


# Create another two Streamlit widgets st.text_input() and st.button() to facilitate the query interface to users. 
st.text_area("Provide your text:", key="user")
option = st.selectbox("Select what would you like the Achademio bot to do:", ('Rewrite in academic style', 'Write a paragraph from my bullet point list', 'Proofread my text and output errors'))

if 'Rewrite in academic style' in option:
    academic()
elif 'Write a paragraph from my bullet point list' in option:
    bullet()
else:
    proofreading()


# Call message() function to display chat bubbles, if is_user=True, then the bubble will be on the right side, otherwise the left side. seed is used to show different styles of avatars.

# Print out all the context up so far:
#st.write(st.session_state.context)

#if st.session_state.prompts:
#        for i in range(len(st.session_state.responses)-1, -1, -1):
#            message(st.session_state.prompts[i], is_user=True, key=str(i) + '_user', seed=83)
#            message(st.session_state.responses[i], key=str(i), seed='Milo')
#            st.write(st.session_state.responses[i])