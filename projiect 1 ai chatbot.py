print("Chatbot: Hello! I am your AI Chatbot.")
print("Chatbot: Welcome!")

inputs = ["hello", "your name", "how are you", "what can you do", "thank you", "bye"]

for user_input in inputs:
    print("You:", user_input)

    if user_input in ["hello", "hi", "hey"]:
        print("Chatbot: Hello! How can I help you?")

    elif "your name" in user_input or "who are you" in user_input:
        print("Chatbot: I am an AI Chatbot.")

    elif "how are you" in user_input:
        print("Chatbot: I am fine! Thank you for asking.")

    elif "what can you do" in user_input:
        print("Chatbot: I can answer simple questions and have a basic conversation.")

    elif "thank you" in user_input or "thanks" in user_input:
        print("Chatbot: You're welcome!")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a great day!")

    else:
        print("Chatbot: Sorry, I don't understand that.")