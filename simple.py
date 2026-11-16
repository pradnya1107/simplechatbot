print("🤖 Welcome to My Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: I am Python Chatbot.")

    elif user == "what is python":
        print("Bot: Python is a programming language.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
