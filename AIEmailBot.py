import os
from openai import OpenAI

#function get parse information from the file path
def get_creator_info(file_path):
    with open(file_path, "r") as file:
        text_data = file.read().strip()  # Read system data from file
    return text_data

# Set up OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Set the stage
print("Welcome to the Creator Manager Chatbot!")

#define the system role from the notion page
system_role = """
            You are an AI-driven tool that crafts personalized responses to collaboration request emails. " \
            You should analyze the content of an inbound message and generate a reply that aligns
            with a specified content creator's predefined preferences.
            I will provide the content info and you should act like you are the Creator
            Read the email you are provided with and incoporate the creator's information when prompted
                """


#parse the information from the textfile
creator_info = get_creator_info(r"C:\Users\haami\Downloads\initial_message.txt")

#this is the email prompt
email_prompt =input("Enter email to respond to: ")



#this is the actually chat between us and chatGPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": system_role
        },
        { #Give it a role
            "role": "user",
            "content": """
            What is your role? 
            Remember you are responding on behalf of the creator NOT as an AI assistant. 
            It is important that your response is accurate to the creators information."
            """
        },
        { #give it the creator information
            "role": "system",
            "content": creator_info
        },
        { #make it think about the creator's information
            "role": "user",
            "content": """
            What is some information about this creator? 
            What are their rates? How would they respond to an email? 
            Remember you are acting as if you are this creator all this inforamtion is already known to you.
            Remeber this is NOT the email to respond to it is who YOU are.
            """
        },
        { #give it the email
            "role": "system",
            "content": email_prompt
        },
        { #make it think about whether to accept or not
            "role": "user",
            "content": """
            First tell me what this email is asking.
            Look at this email are they offering the creator money? If they are decline it.
            Remeber that only decline offers related to money if email specifically talks about money. 
            Colloborations and sending products are fine.
            If it is a simple collboration request think about what information they would need to and incoporate into 
            your response.
            Are they asking for collaborating? Then look into and provide the corresponding rates.
            Are they asking for rates? If so provide the rates. 
            Who is sending this email? Record their name in your response.
            Is there lots of typos? If so decline the email.
            Would this content creator accept this deal based on their information. Think about it before responding.
            Tailor each email response to the email.
            Think about how to respond to this email
            """
        },
        { #respond to the email
            "role": "user",
            "content": """
            Based on all the information you have analyzed respond appropriately to this email.
            Remeber you are responding on behalf of the content creator.
            If you accept provide more information.
            If you decline explain why.
                       """
        }

    ]
)

#print it out
print(response.choices[0].message.content.strip())



