# app.py - Simple Greeting Chatbot Backend
# Install: pip install flask

from flask import Flask, request, jsonify, send_file
from datetime import datetime
import random

app = Flask(__name__)

# Greeting responses
def get_greeting_response(message):
    msg = message.lower().strip()
    
    # Good morning
    if 'good morning' in msg or 'morning' in msg:
        responses = [
            "Good morning! ☀️ Have a wonderful day ahead!",
            "Morning! Hope you slept well! 😊",
            "Good morning! Ready to make today amazing?",
            "Rise and shine! 🌅 Morning!"
        ]
        return random.choice(responses)
    
    # Good afternoon
    elif 'good afternoon' in msg or 'afternoon' in msg:
        responses = [
            "Good afternoon! 🌤️ Hope you're having a great day!",
            "Afternoon! How's your day going?",
            "Good afternoon! Need an energy boost? ☕",
            "Hey there! Good afternoon! 😊"
        ]
        return random.choice(responses)
    
    # Good evening
    elif 'good evening' in msg or 'evening' in msg:
        responses = [
            "Good evening! 🌆 How was your day?",
            "Evening! Time to relax and unwind! 😌",
            "Good evening! Hope you had a productive day!",
            "Hey! Good evening to you too! 🌙"
        ]
        return random.choice(responses)
    
    # Good night
    elif 'good night' in msg or 'goodnight' in msg or 'night' in msg:
        responses = [
            "Good night! 🌙 Sleep well and sweet dreams!",
            "Night night! Don't let the bed bugs bite! 😴",
            "Good night! See you tomorrow! ⭐",
            "Sweet dreams! Rest well! 💤"
        ]
        return random.choice(responses)
    
    # Hello/Hi/Hey
    elif any(word in msg for word in ['hello', 'hi', 'hey', 'hii', 'hola']):
        responses = [
            "Hello! 👋 How are you doing today?",
            "Hi there! 😊 Great to see you!",
            "Hey! How can I brighten your day?",
            "Hello! Welcome! What's up?",
            "Hi! 🎉 How are you feeling today?"
        ]
        return random.choice(responses)
    
    # How are you
    elif 'how are you' in msg or 'how r u' in msg or "what's up" in msg or 'whats up' in msg:
        responses = [
            "I'm doing great! Thanks for asking! 😊 How about you?",
            "I'm wonderful! How are YOU doing?",
            "Feeling fantastic! 🎉 And you?",
            "I'm good! Hope you're having an amazing day!",
            "Doing well! Thanks! How's everything with you?"
        ]
        return random.choice(responses)
    
    # About bot / name
    elif any(phrase in msg for phrase in [
    'tell me about yourself',
    'who are you',
    'your name',
    'what is your name',
    'who r u'
    ]):
        return (
        "Hello! 🤖 I’m GreetBot, your friendly AI-powered chatbot."
        "✨ I love greeting people and spreading positivity."
        "🌱 I’m still learning, but I’ll always try my best to help you."
        "You can say hi, good morning, thank you, or just chat with me anytime! 😊"
        )

    # My name is
    elif 'my name is' in msg or 'i am' in msg or "i'm" in msg:
    # Extract name (full name)
        if 'is' in msg:
            name = msg.split('is', 1)[1].strip()
        else:
            name = msg.split('am', 1)[1].strip()
        if not name:
            name = 'friend'
    
        return f"Nice to meet you, {name}! 😊 How can I help you today?"
    
    # --- Day / Date / Year / Time queries ---
    elif any(phrase in msg for phrase in ["day", "what day", "tell me the day"]):
        now = datetime.now()
        current_day = now.strftime('%A')  # Monday, Tuesday...
        return f"Today is {current_day} 🗓️"

    elif any(phrase in msg for phrase in ["date", "what date", "tell me the date", "what date is today"]):
        now = datetime.now()
        current_date = now.strftime('%d-%m-%Y')  # 09-01-2026
        return f"Today's date is {current_date} 📅"

    elif any(phrase in msg for phrase in ["year", "what year", "tell me the year"]):
        now = datetime.now()
        current_year = now.strftime('%Y')  # 2026
        return f"The current year is {current_year} 📆"

    elif any(phrase in msg for phrase in ["time", "what time", "current time", "tell me the time", "what time is it now"]):
        now = datetime.now()
        current_time = now.strftime('%I:%M %p')  # 02:15 PM
        return f"The current time is {current_time} 🕒"

    # Thank you
    elif 'thank' in msg or 'thanks' in msg:
        responses = [
            "You're welcome! 😊 Happy to help!",
            "No problem at all! Anytime! 🎉",
            "My pleasure! Have a great day!",
            "You're most welcome! 💙"
        ]
        return random.choice(responses)
    
    # Bye
    elif 'bye' in msg or 'goodbye' in msg or 'see you' in msg:
        responses = [
            "Goodbye! 👋 Take care!",
            "See you later! Have a great day! 😊",
            "Bye bye! Come back soon! 🎉",
            "Take care! Until next time! 💙"
        ]
        return random.choice(responses)
    
    # Help
    elif 'help' in msg or 'what can you do' in msg:
        return "I'm a greeting bot! 🤖 I can:<br><br>" + \
           "• Say good morning ☀️<br>" + \
           "• Say good afternoon 🌤️<br>" + \
           "• Say good evening 🌆<br>" + \
           "• Say good night 🌙<br>" + \
           "• Chat and greet you 👋<br>" + \
           "• Respond to thank you 😊<br>" + \
           "• Say goodbye 👋<br><br>" + \
           "Just talk to me naturally!"

    # Default friendly response
    else:
        responses = [
            "That's interesting! Tell me more! 😊",
            "I hear you! How else can I help?",
            "Awesome! What else would you like to chat about?",
            "Cool! I'm here to chat anytime! 💙",
            "Nice! Anything else on your mind?"
        ]
        return random.choice(responses)

# Serve HTML page
@app.route('/')
def home():
    return send_file('index.html')

# Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_msg = data.get('message', '')
        
        if not user_msg:
            return jsonify({'error': 'Empty message'}), 400
        
        # Get response
        bot_reply = get_greeting_response(user_msg)
        
        return jsonify({
            'response': bot_reply,
            'time': datetime.now().strftime('%I:%M %p')
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🤖 GREETBOT STARTING...")
    print("="*50)
    print("📱 Open your browser and go to:")
    print("   👉 http://localhost:5000")
    print("\n⏹️  Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    app.run(debug=True, port=5000)