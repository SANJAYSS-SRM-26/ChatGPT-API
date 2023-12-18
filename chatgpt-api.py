import openai
import gradio

openai.api_key = "YOUR_API_KEY_HERE"

# Initializing the conversation with a system message
messages = [{"role": "system", "content": "You are a financial expert specializing in real estate investment and negotiation."}]

def CustomChatGPT(user_input):
    # Appending user input to the conversation history
    messages.append({"role": "user", "content": user_input})

    # Requesting a response from the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150  # Adjust token limit as needed
    )

    # Retrieving the model's response and appending it to the conversation history
    model_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": model_reply})
    return model_reply

# Creating a Gradio interface for the chatbot
iface = gradio.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="Real Estate Pro",
    placeholder="Start chatting..."
)

iface.launch(share=True)
