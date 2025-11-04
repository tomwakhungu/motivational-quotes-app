from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Extended collection of motivational quotes
QUOTES = [
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "category": "success"
    },
    {
        "text": "Believe you can and you're halfway there.",
        "author": "Theodore Roosevelt",
        "category": "belief"
    },
    {
        "text": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "author": "Winston Churchill",
        "category": "courage"
    },
    {
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "category": "dreams"
    },
    {
        "text": "It does not matter how slowly you go as long as you do not stop.",
        "author": "Confucius",
        "category": "persistence"
    },
    {
        "text": "Everything you've ever wanted is on the other side of fear.",
        "author": "George Addair",
        "category": "courage"
    },
    {
        "text": "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine.",
        "author": "Roy T. Bennett",
        "category": "belief"
    },
    {
        "text": "I learned that courage was not the absence of fear, but the triumph over it.",
        "author": "Nelson Mandela",
        "category": "courage"
    },
    {
        "text": "The only impossible journey is the one you never begin.",
        "author": "Tony Robbins",
        "category": "action"
    },
    {
        "text": "Your limitation—it's only your imagination.",
        "author": "Unknown",
        "category": "mindset"
    },
    {
        "text": "Great things never come from comfort zones.",
        "author": "Unknown",
        "category": "growth"
    },
    {
        "text": "Dream it. Wish it. Do it.",
        "author": "Unknown",
        "category": "action"
    },
    {
        "text": "Success doesn't just find you. You have to go out and get it.",
        "author": "Unknown",
        "category": "success"
    },
    {
        "text": "The harder you work for something, the greater you'll feel when you achieve it.",
        "author": "Unknown",
        "category": "work"
    },
    {
        "text": "Dream bigger. Do bigger.",
        "author": "Unknown",
        "category": "dreams"
    },
    {
        "text": "Don't stop when you're tired. Stop when you're done.",
        "author": "Unknown",
        "category": "persistence"
    },
    {
        "text": "Wake up with determination. Go to bed with satisfaction.",
        "author": "Unknown",
        "category": "discipline"
    },
    {
        "text": "Do something today that your future self will thank you for.",
        "author": "Sean Patrick Flanery",
        "category": "action"
    },
    {
        "text": "Little things make big days.",
        "author": "Unknown",
        "category": "gratitude"
    },
    {
        "text": "It's going to be hard, but hard does not mean impossible.",
        "author": "Unknown",
        "category": "persistence"
    },
    {
        "text": "Don't wait for opportunity. Create it.",
        "author": "Unknown",
        "category": "action"
    },
    {
        "text": "Sometimes we're tested not to show our weaknesses, but to discover our strengths.",
        "author": "Unknown",
        "category": "strength"
    },
    {
        "text": "The key to success is to focus on goals, not obstacles.",
        "author": "Unknown",
        "category": "focus"
    },
    {
        "text": "Dream it. Believe it. Build it.",
        "author": "Unknown",
        "category": "dreams"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quote')
def get_quote():
    """Return a random quote"""
    quote = random.choice(QUOTES)
    return jsonify(quote)

@app.route('/api/quote/category/<category>')
def get_quote_by_category(category):
    """Return a random quote from specific category"""
    filtered_quotes = [q for q in QUOTES if q['category'] == category]
    if filtered_quotes:
        quote = random.choice(filtered_quotes)
        return jsonify(quote)
    return jsonify({"error": "Category not found"}), 404

@app.route('/api/categories')
def get_categories():
    """Return all available categories"""
    categories = list(set(q['category'] for q in QUOTES))
    return jsonify({"categories": sorted(categories)})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'quotes_count': len(QUOTES)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
