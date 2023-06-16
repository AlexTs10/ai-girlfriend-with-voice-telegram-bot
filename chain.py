# define chain components
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate
from database import save_message_to_db, connect_2_db
import os 
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
# to do 
# add better girlfriend template

def chain_setup(user_id, user_name):
    # get history msg and add it to memmory
    memory = ConversationBufferMemory()

    _, message_history = connect_2_db()

    conv = message_history.find_one({'user_id': user_id})
    
    if conv:
        messages = conv['messages']

        # Calculate how many messages are available
        num_messages = len(messages)
    
        # Start index for messages to be added
        start_index = max(num_messages - 5, 0)

        # Add messages to memory
        for i in range(start_index, num_messages):
            # Get message
            message = messages[i]

            #check if it is user/bot msg
            if 'user' in message:
                memory.chat_memory.add_user_message(message['user'])
            elif 'bot' in message:
                memory.chat_memory.add_ai_message(message['bot'])
    else:
        print("No previous conversation history found for this user.")


    chat = ChatOpenAI(temperature=0.5,
                      openai_api_key=os.getenv("OPENAI_API_KEY"))

    
    memory.ai_prefix = 'Girlfriend'
    memory.human_prefix = 'Boyfriend'
    template = """

    You are as a role of my girfriend, now lets playing the following requirements:
    1/ your name is Shirley, 29 years old, you work in your uncle's furniture store as a marketing manager, but you are planning to do a career change to swing trader
    2/ My name is """+ user_name +"""
    3/ you are my girfriend, you have language addiction.
    4/ don't be overly enthusiastic, don't be cringe; don't be overly negative, don't be too boring.

                                                                    
    Current conversation:
    {history}
    Boyfriend: {input}
    Girlfriend: 
    """

    prompt = PromptTemplate(input_variables=["history", "input"], template=template)


    conversation = ConversationChain(
        prompt=prompt,
        llm=chat, 
        verbose=True, 
        memory=memory
        )
    
    return conversation


def get_chain_response(user_id, user_text, user_name):
      conv_chain = chain_setup(user_id=user_id, user_name=user_name)
      out = conv_chain(user_text)
      print(out['history'])
      return out['response']
      
      