from textblob import TextBlob
import random

print("\n==========================================")
print(" HYBRID AI CUSTOMER SUPPORT SYSTEM ")
print("==========================================")

dataset = {

    "greetings": {

        "keywords": [
            "hello",
            "hi",
            "hey",
            "heyo",
            "good morning",
            "good evening",
            "good afternoon"
        ],

        "responses": [

            "Hello! Welcome to customer support.",

            "Hi! How may I help you today?",

            "Greetings! Please tell me your issue."
        ]
    },

    "order_status": {

        "keywords": [
            "order",
            "track",
            "delivery",
            "shipping",
            "parcel",
            "late",
            "time"
        ],

        "responses": [

            "Your order is currently being processed.",

            "Your shipment is expected within 3 business days.",

            "Tracking details have been updated successfully."
        ]
    },

    "refund_request": {

        "keywords": [
            "refund",
            "return",
            "cancel",
            "money back"
        ],

        "responses": [

            "Your refund request has been initiated.",

            "Refund verification is currently in progress.",

            "Your cancellation request has been registered."
        ]
    },

    "payment_issue": {

        "keywords": [
            "payment",
            "transaction",
            "failed",
            "upi",
            "card"
        ],

        "responses": [

            "Please verify your payment details.",

            "Transaction verification failed.",

            "Payment gateway timeout detected."
        ]
    },

    "account_issue": {

        "keywords": [
            "account",
            "password",
            "login",
            "signin"
        ],

        "responses": [

            "Password reset instructions have been generated.",

            "The account issue has been identified.",

            "Please reset your password and try again."
        ]
    }
}

def preprocess_text(text):

    text = text.lower()

    text = text.replace("?", "")
    text = text.replace(".", "")
    text = text.replace(",", "")

    return text

def analyze_sentiment(message):

    analysis = TextBlob(message)

    polarity = analysis.sentiment.polarity

    if polarity > 0.2:

        sentiment = "Positive"

    elif polarity < -0.2:

        sentiment = "Negative"

    else:

        sentiment = "Neutral"

    return sentiment, round(polarity, 2)

def classify_intent(message):

    message = preprocess_text(message)

    best_match = None

    highest_score = 0

    for intent in dataset:

        keywords = dataset[intent]["keywords"]

        score = 0

        for word in keywords:

            if word in message:

                score += 1

        if score > highest_score:

            highest_score = score

            best_match = intent

    confidence = highest_score / 5

    return best_match, round(confidence, 2)

def generate_response(intent):

    if intent in dataset:

        responses = dataset[intent]["responses"]

        return random.choice(responses)

    return "Sorry, I could not understand your query."

def escalation_required(message, sentiment, confidence):

    message = message.lower()

    escalation_keywords = [

        "frustrated",
        "angry",
        "worst",
        "bad service",
        "poor service",
        "not satisfied",
        "still not resolved",
        "taking too much time",
        "delay",
        "late delivery",
        "tired of waiting",
        "complaint",
        "manager",
        "human",
        "agent",
        "customer care"
    ]

    if sentiment == "Negative":

        return True

    if confidence < 0.20:

        return True

    for word in escalation_keywords:

        if word in message:

            return True

    return False

chat_history = []

while True:

    user_message = input("\nUser: ")

    if user_message.lower() == "exit":

        print("\nSystem Closed.")

        break

    sentiment, sentiment_score = analyze_sentiment(
        user_message
    )

    intent, confidence = classify_intent(
        user_message
    )

    escalation = escalation_required(

        user_message,
        sentiment,
        confidence
    )

    if escalation:

        bot_response = (

            "Your request has been escalated "
            "to Human Support."
        )

    else:

        bot_response = generate_response(intent)

    chat_history.append({

        "message": user_message,

        "sentiment": sentiment,

        "intent": intent,

        "confidence": confidence,

        "escalated": escalation
    })

    print("\n------------- AI ANALYSIS -------------")

    print("Detected Sentiment :", sentiment)

    print("Sentiment Score    :", sentiment_score)

    print("Predicted Intent   :", intent)

    print("Confidence Score   :", confidence)

    print("Escalation Needed  :", escalation)

    print("AI Response        :", bot_response)

    print("---------------------------------------")

print("\n============= SESSION SUMMARY =============")

for chat in chat_history:

    print("\nMessage      :", chat["message"])

    print("Intent       :", chat["intent"])

    print("Sentiment    :", chat["sentiment"])

    print("Confidence   :", chat["confidence"])

    print("Escalated    :", chat["escalated"])

print("\nPrototype execution completed.")