# AI Email Bot

## Introduction
Welcome to the Creator Manager Chatbot! This Python script utilizes the power of OpenAI's GPT-3.5 model to act as a personalized response system for collaboration request emails on behalf of content creators. The chatbot analyzes the content of inbound messages and generates replies tailored to a specified content creator's preferences.

## Features
- **Personalized Responses**: The chatbot crafts responses based on the provided creator's information.
- **Role Simulation**: Simulates the role of the content creator, ensuring responses are accurate and aligned with their preferences.
- **Email Analysis**: Analyzes incoming emails, considering factors such as collaboration offers, rates, sender information, and typos.
- **Dynamic Response Generation**: Tailors each response to the specific content of the email, accepting or declining offers accordingly.

## Usage
1. **Set Up OpenAI Client**: Obtain an API key from OpenAI and set it up as an environment variable named `OPENAI_API_KEY`.
2. **Run the Script**: Execute the Python script, which prompts for an email to respond to and generates a response based on the provided creator's information.
3. **Provide Creator Information**: Ensure the `initial_message.txt` file contains accurate information about the content creator's preferences, rates, and typical responses.
4. **Respond to Emails**: Follow the prompts to simulate how the content creator would respond to the given email.

## Configuration
- **System Role**: Define the chatbot's role and instructions for responding to emails.
- **Creator Information**: Store details about the content creator in the `initial_message.txt` file and replace the filepath with your filepath in the code.
- **Email Prompt**: Input the email content that the chatbot will respond to.

## Dependencies
- `openai` library: Install via `pip install openai`.

