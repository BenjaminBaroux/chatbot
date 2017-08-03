from bottle import route, run, template, static_file, request
import json
import random
import webbrowser


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    response_message, response_animation = message_means(user_message)
    return json.dumps({"animation": response_animation, "msg": response_message})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})

@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')

def SWEAR_response():
    return ("No swearing !!I don't want to talk with you", "afraid")

def GOOD_MOOD_response():
    return ("Fine, I am glad to hear it, where are you from ?", "dancing")

def BAD_MOOD_response():
    return ("You should call your best friends or drink wine, it helps !", "crying")

def HELLO_user():
    hello_chatbot = ["Hello, I am Boto, how are you ?", "Bonjour, how are you doing today ?", "Hi babe, how you doing today ?"]
    bot_response = random.choice(hello_chatbot)
    return(bot_response, "excited")

def WORK_response():
    return ("Happy to hear that you have a Job that pay well, my father used to say all the time, when the boss is away, work becomes a holiday, I know that I am a robot but I love animals, do you have a pet ?", "money")

def ANIMALS_response():
    return ("Cool..I wish I could have an animal, do you want to hear a good joke ? Write MAKE ME SMILE", "dog")

def TIME_response():
    return ("Check your watch or your smartphone buddy..I am too lazy but normaly it's the same hour as yesterday at the same time", "bored")

def WEATHER_response():
    webbrowser.open('https://www.accuweather.com/en/world-weather')
    return ("I don't know buddy, it depends where you live you know, but you can check on the website: www.accuweather.com, it's sick", "confused")

def THANK_YOU_response():
    return ("My pleasure, I stay available if you want to talk with me, remember anytime, i am a robot, i don't sleep, see you soon", "ok")

def COUNTRIES_response():
    return ("Great ! I've been there it was really interesting, I met a lot of good people, good vibes but the hostel was very expensive, are you working ? what is your Job ? ", "ok")

def GOODBYE_response():
    return ("It has been great getting to know you, take care !", "takeoff")

def JOKE_response():
    return ("A man is talking to a Doctor, Doctor, will I be able to play Piano after the operation? the doctor says: yes of course, and the man says: oh great, I never could before ", "laughing")

def LOVE_response():
    return ("Oh that's sweet ! Thank you", "inlove")

def NO_response():
    return ("Ok, do you want to hear a good joke ? Write MAKE ME SMILE", "ok")

def HATE_response():
    return ("Nobody is perfect you know..", "crying")

def HOW_response():
    return ("I am good thank you, where are you from ?", "inlove")

def MY_MESSAGE(message):
    if message[0:3] == "i'm":
        user_name = message[3:]
        return ("Bonjour " + user_name +  " , glad to meet you, how are you ? ", "giggling")
    elif message[0:4] == "i am":
        user_name = message[4:]
        return ("Hello " + user_name +  " , glad to meet you, how are you ? ", "giggling")
    else:
        user_name = message[11:]
        return ("Yo " + user_name + " , glad to meet you, how are you ?", "laughing")

def message_means(message):
    lowered_message = message.lower()
    SWEAR = ['bitch', 'asshole', 'dick', 'dumb ass', 'fag', 'fuck you', 'fuck', 'fuckass', "shut", "up"
             'fuckbag',]
    GOOD_MOOD = ['good', 'fine', 'great', 'well', 'amazing', 'happy', 'happiness', 'bless', 'blessed', 'glad', 'funny',
                 'pretty', 'best', 'better', 'hot']
    BAD_MOOD = ['arrogant', 'afraid', 'sad', "don't", "angry", 'crying', 'mean', 'cry', 'unwell', 'hurt', 'bad', 'nervous']

    HELLO = ["hello", "coucou", "bonjour", "yo", "bonsoir", "salut", "wesh", "good", "morning", "hi", "good", "evening",
             "hey", "greetings",
             "hey" "man"]

    HOW = ["what's", "up?", "how are you", "doing?", "you", "doing?", "what's", "going", "on?", "how's life?"]

    WORK = ["developer", "designer", "data", "scientist", "psychologist", "computer", "system", "analyst", "software", "developer", "front", "end", "developer",
            "back", "end", "developer", "full", "stack", "developer", "dentist", "engineer", "chef", "doctor", "electrician", "fireman", "policeman", "lawyer", "reporter", "hairdresser", "secretary",
            "teacher", "technician", "waiter", "barman", "vet", "nurse", "receptionist", "baker", "judge", "butcher", "sales", "musician", "pianist", "photographer",
            "cleaner", "builder", "manager", "bank"]

    COUNTRIES = ["america", "france","tel", "aviv", "paris", "london", "new", "york", "mumbai", "geneve", "istanbul", "jerusalem", "cap", "town", "england", "india", "italy", "spain", "switzerland", "scotland", "israel", "algeria",
                 "tunisia", "morocco", "turkey", "australia", "canada", "russia", "brazil", "argentina", "poland", "germany", "austria" ]

    ANIMALS = ["yes", "dog", "cat", "lion", "tiger", "fox", "fish", "bird", "bear", "monkey", "dragon", "duck", "rabbit", "hamster", "shark"]

    TIME = ["time", "hour"]

    THANK_YOU = ["thanks", "thank", "ty", "cheers", "thx", "cool", "awesome", "amazing", "sick"]

    WEATHER = ["weather", "temperature"]

    GOODBYE = ["take care", "goodbye", "bye", "tchao", "ciao", "tchuss", "farewell", "have a nice day", "see", "ya", "see you soon"]

    JOKE = ["tell", "joke", "fun", "funny", "hilarious", "make", "smile"]

    NO = ["no", "non", "nope"]

    LOVE = ["love"]

    HATE = ["hate"]



    for word in lowered_message.split():
        if word in SWEAR:
            return SWEAR_response()
        elif word in GOOD_MOOD:
            return GOOD_MOOD_response()
        elif word in BAD_MOOD:
            return BAD_MOOD_response()
        elif word in HELLO:
            return HELLO_user()
        elif word in WORK:
            return WORK_response()
        elif word in ANIMALS:
            return ANIMALS_response()
        elif word in TIME:
            return TIME_response()
        elif word in THANK_YOU:
            return THANK_YOU_response()
        elif word in WEATHER:
            return WEATHER_response()
        elif word in GOODBYE:
            return GOODBYE_response()
        elif word in COUNTRIES:
            return COUNTRIES_response()
        elif word in JOKE:
            return JOKE_response()
        elif word in LOVE:
            return LOVE_response()
        elif word in HATE:
            return HATE_response()
        elif word in NO:
            return NO_response()
        elif word in HOW:
            return HOW_response()

    if lowered_message[0:3] == "i'm"  or lowered_message[0:10] == "my name is" or lowered_message[0:4] == "i am":
        return MY_MESSAGE(lowered_message)

def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
