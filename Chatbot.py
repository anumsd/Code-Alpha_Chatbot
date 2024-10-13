import spacy
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

# Expanded corpus with different functionalities
corpus = """
Hello! How can I help you today?
I am a basic chatbot.
How are you doing today?
I am here to provide valuable information and help you with your tasks.
What are you doing?
I am doing well, thank you for asking.
I was built using Python and NLTK.
I am here to chat with you and assist you.
I can assist with general questions and basic responses.
Sure, I can suggest a few popular fast food places nearby.
Do you want recommendations for fast food?
Can you help me find some fast food places?
You can try McDonald's, KFC, or a local favorite!
I was built by a programmer interested in Python and AI!
I can't dance, but I can make you imagine a great dance in your mind!
Do you want to know the weather today?
I can provide a mock weather report if you're interested.
Would you like to hear some recent news headlines?
I can share a motivational quote with you if you're feeling down.
"""
tokenizesent = [sent.text for sent in nlp(corpus).sents]

inputgreeting = ["sup", "hey", "hello", "what's up", "hi", "what is up", "what's up?", "greetings"]
replygreeting = ["Hi", "Hello", "Greetings", "Hey", "Heyyyyy", "*nods*"]

response_null = [
    "I'm sorry, I don't have enough information on that.",
    "Sorry I don't have any answer to that.",
    "It would be better if you could clarify your question.",
    "Please make me understand what you want."
]

response_fixed = {
    "how are you?": "I am fine, thank you for asking!",
    "how are you": "I am fine, thank you for asking!",
    "what are you doing": "Just trying to assist you!",
    "what do you do": "I assist users with general queries, provide information, and chat with you!",
    "what is your purpose?": "I assist users with general queries, provide information, and chat with you!",
    "what are you doing?": "Just trying to assist you!",
    "what is your purpose": "I assist users with general queries, provide information, and chat with you!",
    "can you paint?": "I would love to, but for now I can only assist you.",
    "suggest me some fast food places": "You should try KFC, McDonald's, or Optp",
    "who created you": "I was built by a programmer who loves Python and AI.",
    "who is your owner?": "I was built by a programmer who loves Python and AI.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "weather": "The weather today is sunny with a high of 25°C. Perfect day for a walk!",
    "news": "Here are today's top headlines: \n1. Global markets show mixed results. \n2. Scientists discover a new species of deep-sea fish. \n3. Local community organizes a tree-planting drive.",
    "motivate me": "Keep pushing forward! Remember, success is the result of hard work and determination.",
    "suggest me some places to visit": "You could visit the local park, explore the city's museums, or go to a nearby beach for some relaxation.",
    "suggest entertainment": "Why not catch a movie? Or if you're staying in, try binge-watching a new TV series!"
}

def greeting(sentences):
    for singleword in sentences.split():
        if singleword.lower() in inputgreeting:
            return random.choice(replygreeting)

def customresponse(user_response):
    user_response = user_response.lower()
    for key, value in response_fixed.items():
        if key in user_response:
            return value
    return None

def functionresponse(user_response):
    user_response = user_response.lower()
    tokenizesent.append(user_response)
    TfidfVec = TfidfVectorizer(stop_words='english')
    tfidf = TfidfVec.fit_transform(tokenizesent)
    vals = cosine_similarity(tfidf[-1], tfidf[:-1])
    idx = vals.argsort()[0][-1]
    flat = vals.flatten()
    flat.sort()
    reqtfidf = flat[-1]

    if reqtfidf < 0.5: 
        chatbotresponse = random.choice(response_null)
    else:
        chatbotresponse = tokenizesent[idx]
    tokenizesent.pop()  
    return chatbotresponse

def chatbot():
    print("Bot: Hey! I am your chatbot assistant. To exit, type 'Bye' or 'bye'.")
    while True:
        response_by_user = input("You: ").lower()
        if response_by_user == 'bye':
            print("Bot: Bye! Nice to meet you!")
            break
        else:
            if greeting(response_by_user) is not None:
                print("Bot:", greeting(response_by_user))
            else:
                customreply = customresponse(response_by_user)
                if customreply is not None:
                    print("Bot:", customreply)
                else:
                    print("Bot:", functionresponse(response_by_user))

# Start the chatbot
chatbot()
