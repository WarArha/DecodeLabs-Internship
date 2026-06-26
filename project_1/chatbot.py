def intro():
    print("--------------------- WECLOME TO DECODE BOT ----------------------")
    print("                     RULE BASED AI CHAT BOT")
    print("          type 'help' to see the domains of questions")
    print("          type 'exit','bye', or 'quit' to end the chat ")

def give_res(user_inp):
    predefined_res={
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! Nice to meet you.",
        "hey": "Hey! What would you like to ask?",
        "how are you": "I am doing great. Thanks for asking!",
        "what is your name": "My name is DecodeBot, your rule-based AI assistant.",
        "who created you": "I was created as part of an Artificial Intelligence Project 1.",
        "what is ai": "AI means Artificial Intelligence. It allows machines to perform tasks that usually need human intelligence.",
        "what is chatbot": "A chatbot is a program that can respond to user messages automatically.",
        "what is rule based chatbot": "A rule-based chatbot gives replies using fixed rules, conditions, and predefined responses.",
        "what is python": "Python is a popular programming language used in AI, web development, automation, and data analysis.",
        "help": "You can ask me about AI, chatbot, Python, my name, or say hello.",
        "thanks": "You're welcome!",
        "thank you": "You're welcome!",
    }

    return predefined_res.get(user_inp,"you can press 'help' to see what questions can be asked")


def main():
    intro()
    while (True):
        user_input=input("\nyou:")
        cleaned_input=user_input.lower().strip()
        if cleaned_input in ["exit","bye","quit"]:
            break
        if cleaned_input=="":
            print("plz enter something")
            continue
        else :
            print("bot:",give_res(cleaned_input))


main()