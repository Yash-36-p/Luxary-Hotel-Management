import os
import logging
from flask import Flask, render_template, request, jsonify, session
import ai_service
import hotel_data

# Set up logging for easier debugging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Initialize session data
@app.before_request
def before_request():
    if 'chat_history' not in session:
        session['chat_history'] = []

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Process chat messages from the user"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Please enter a message'}), 400
        
        # Add user message to history
        if 'chat_history' not in session:
            session['chat_history'] = []
        
        session['chat_history'].append({'role': 'user', 'content': user_message})
        
        # Get AI response based on the message context
        ai_response = ai_service.get_ai_response(user_message, session['chat_history'])
        
        # Add AI response to history
        session['chat_history'].append({'role': 'assistant', 'content': ai_response})
        session.modified = True
        
        return jsonify({
            'response': ai_response,
        })
    
    except Exception as e:
        logging.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': 'An error occurred processing your request'}), 500

@app.route('/api/room-service-menu', methods=['GET'])
def room_service_menu():
    """Get the room service menu items"""
    try:
        category = request.args.get('category', 'all')
        menu_items = hotel_data.get_room_service_menu(category)
        return jsonify(menu_items)
    except Exception as e:
        logging.error(f"Error fetching room service menu: {str(e)}")
        return jsonify({'error': 'Could not retrieve menu items'}), 500

@app.route('/api/local-recommendations', methods=['GET'])
def local_recommendations():
    """Get local attraction recommendations"""
    try:
        category = request.args.get('category', 'all')
        distance = request.args.get('distance', 'all')
        recommendations = hotel_data.get_local_recommendations(category, distance)
        return jsonify(recommendations)
    except Exception as e:
        logging.error(f"Error fetching recommendations: {str(e)}")
        return jsonify({'error': 'Could not retrieve recommendations'}), 500

@app.route('/api/hotel-info', methods=['GET'])
def hotel_info():
    """Get general hotel information"""
    try:
        info_type = request.args.get('type', 'all')
        info = hotel_data.get_hotel_info(info_type)
        return jsonify(info)
    except Exception as e:
        logging.error(f"Error fetching hotel info: {str(e)}")
        return jsonify({'error': 'Could not retrieve hotel information'}), 500

@app.route('/api/reset-chat', methods=['POST'])
def reset_chat():
    """Reset the chat history"""
    try:
        session['chat_history'] = []
        session.modified = True
        return jsonify({'status': 'success'})
    except Exception as e:
        logging.error(f"Error resetting chat: {str(e)}")
        return jsonify({'error': 'Could not reset chat'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
