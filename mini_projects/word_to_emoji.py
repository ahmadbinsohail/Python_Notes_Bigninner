message = input("Type 'exit' to exit or enter your message > ")
while message.lower() != "exit" :
    emoji = {
        "sad" : "😔",
        "happy" : "😊",
        "funny" : "😂",
        "smile" : "😊",
        "love" : "😘",
        "angry" : "😡",
        "rude" : "😒"
    }
    words = message.split()
    output_emoji = " "
    for word in words:
        #print(emoji.get(word,word))
        output_emoji += emoji.get(word,word) + " "
    print(output_emoji)
    message = input("Type 'exit' to exit or enter your message > ")
if message.lower() == 'exit':
    print("Exit successfully")
    
