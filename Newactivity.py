# greet the user
print("Hello! I am AI Bot. What's your name? : ")

#get user input
name = input()

#respond to the user's name
print (f"Nice to meet you, {name}!")

#Ask a question
print("How are you feeling today? : ")
mood = input().lower()

#Use conditional statement to respond based on input
if mood == "good":
    print("I'm glat to hear that")
elif mood == "bad":
    print("I'm sorry to hear that.")
else:
    print("I see. Sometimes it's har to put feelings into words")

    #End the conversation
    print(f"It was nice chatting with you {name}. Goodbye")
