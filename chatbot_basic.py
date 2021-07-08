from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I am here to help ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is Bot Bahadur. ",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm feeling well", "gr8 !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["One fine morning sushant got bored and wrote stuff on google collab",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Football. My favourite club is Barcelona",]
    ],
    [
        r"what (.*) (film|movie)?",
        ["Avatar"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

#default message at the start of chat
print("Hi, I'm bot bahadur, a chat bot.\nPlease type lowercase English language to start a conversation. Type quit to leave ")

chat = Chat(pairs, reflections)
chat.converse()

