import json
import logging
import random
import hotel_data

# Hotel concierge responses database
WELCOME_RESPONSES = [
    "Welcome to Luxury Grand Hotel! How can I assist you today?",
    "Hello! I'm your virtual concierge at Luxury Grand Hotel. What can I help you with?",
    "Thank you for contacting the Luxury Grand Hotel concierge. How may I assist you?"
]

ROOM_SERVICE_RESPONSES = [
    "I'd be happy to help with your room service order. Could you please provide your room number and what you would like to order?",
    "Certainly! Our room service is available from 6:00 AM to 11:00 PM. What would you like to order?",
    "I'll assist you with your room service request. May I know your room number and your order details?"
]

RECOMMENDATION_RESPONSES = [
    "I'd be delighted to recommend some local attractions. Are you interested in restaurants, shopping, or sightseeing?",
    "There are many wonderful places to visit nearby. What kind of activities or cuisine are you interested in?",
    "I can suggest some excellent local spots. Are you looking for dining, entertainment, or cultural experiences?"
]

HOTEL_INFO_RESPONSES = [
    "I'm happy to provide information about our hotel. Is there something specific you'd like to know about our facilities or services?",
    "Our hotel offers a variety of amenities. What information are you looking for specifically?",
    "I can tell you about our hotel services. Would you like to know about our spa, dining options, or something else?"
]

GENERAL_RESPONSES = [
    "I'm here to make your stay comfortable. How else can I assist you?",
    "Is there anything else you'd like to know about our hotel or the surrounding area?",
    "How can I further enhance your stay at Luxury Grand Hotel?"
]

FAREWELL_RESPONSES = [
    "Thank you for chatting with me. If you need anything else, don't hesitate to ask!",
    "I'm here 24/7 to assist you. Enjoy your stay at Luxury Grand Hotel!",
    "Please let me know if you need any further assistance. Have a wonderful day!"
]

# Important hotel information for quick responses
HOTEL_QUICK_INFO = {
    "checkin": "Check-in time is 3:00 PM. Early check-in may be available based on room availability.",
    "checkout": "Check-out time is 11:00 AM. Late check-out can be arranged for an additional fee.",
    "wifi": "Complimentary high-speed WiFi is available throughout the hotel. Network name: LuxuryGrand_Guest",
    "pool": "Our pool is open from 7:00 AM to 9:00 PM daily.",
    "gym": "The fitness center is available 24 hours with your room key card.",
    "breakfast": "Breakfast is served at The Grand Dining Room from 6:30 AM to 10:30 AM.",
    "parking": "Valet parking is available for $45 per night.",
    "spa": "The spa is open from 9:00 AM to 8:00 PM. Would you like to book a treatment?",
    "room service": "Room service is available from 6:00 AM to 11:00 PM with a limited menu overnight."
}

def get_ai_response(user_message, chat_history):
    """
    Get a rule-based response based on the user's message and chat history
    """
    try:
        # Process the message to see what category it falls into
        message_type = categorize_message(user_message)
        user_message_lower = user_message.lower()
        
        # Check for specific information requests first
        for keyword, info in HOTEL_QUICK_INFO.items():
            if keyword in user_message_lower:
                return info + " " + random.choice(GENERAL_RESPONSES)
        
        # Handle different types of requests
        if message_type == "room_service":
            # Provide menu information
            menu_items = hotel_data.get_room_service_menu('all')
            
            # Check for specific category mentions
            for category in menu_items.keys():
                if category in user_message_lower:
                    items_text = "\n\nHere are our " + category + " options:\n"
                    for item in menu_items[category]:
                        if not isinstance(item, dict):
                            continue
                        name = item.get("name") if "name" in item else ""
                        price = item.get("price") if "price" in item else 0
                        description = item.get("description") if "description" in item else ""
                        items_text += f"• {name} (${price:.2f}) - {description}\n"
                    return items_text + "\n" + random.choice(ROOM_SERVICE_RESPONSES)
            
            # General room service response
            return random.choice(ROOM_SERVICE_RESPONSES) + " Our menu includes breakfast, lunch, dinner, desserts, and beverages."
        
        elif message_type == "recommendations":
            # Provide recommendations
            recommendations = hotel_data.get_local_recommendations('all', 'all')
            
            # Check for specific category mentions
            for category in recommendations.keys():
                if category in user_message_lower or is_category_match(category, user_message_lower):
                    items_text = f"\n\nHere are some {category} recommendations nearby:\n"
                    # Limit to 3 recommendations
                    for i, item in enumerate(recommendations[category]):
                        if i >= 3:
                            break
                        if not isinstance(item, dict):
                            continue
                        name = item.get("name") if "name" in item else ""
                        distance = item.get("distance") if "distance" in item else ""
                        description = item.get("description") if "description" in item else ""
                        items_text += f"• {name} ({distance}) - {description}\n"
                    return items_text + "\n" + "Would you like more information about any of these places?"
            
            # General recommendation response
            return random.choice(RECOMMENDATION_RESPONSES)
        
        elif message_type == "hotel_info":
            # Provide hotel information
            hotel_info = hotel_data.get_hotel_info('all')
            
            # Check for specific information types
            for info_type in hotel_info.keys():
                if info_type in user_message_lower:
                    info_data = hotel_info[info_type]
                    if isinstance(info_data, dict):
                        info_text = f"\n\nHere's information about our {info_type}:\n"
                        for key, value in info_data.items():
                            if isinstance(value, dict):
                                name = value.get('name') if 'name' in value else ''
                                hours = value.get('hours') if 'hours' in value else ''
                                info_text += f"• {key.replace('_', ' ').title()}: {name} - {hours}\n"
                            else:
                                info_text += f"• {key.replace('_', ' ').title()}: {value}\n"
                        return info_text + "\n" + random.choice(GENERAL_RESPONSES)
            
            # General hotel info response
            return random.choice(HOTEL_INFO_RESPONSES)
        
        # Handle farewell messages
        if any(word in user_message_lower for word in ["bye", "goodbye", "thank you", "thanks"]):
            return random.choice(FAREWELL_RESPONSES)
        
        # Handle greetings
        if any(word in user_message_lower for word in ["hello", "hi", "hey", "greetings"]):
            return random.choice(WELCOME_RESPONSES)
        
        # Default response for anything else
        return "I'm here to assist with room service, local recommendations, and information about our hotel. " + random.choice(GENERAL_RESPONSES)
        
    except Exception as e:
        logging.error(f"Error getting response: {str(e)}")
        return "I'm sorry, I'm having trouble processing your request. Please contact the front desk for assistance."

def categorize_message(message):
    """
    Categorize the message to determine what kind of response is needed
    """
    message_lower = message.lower()
    
    # Check for room service related keywords
    if any(keyword in message_lower for keyword in ["room service", "food", "breakfast", "lunch", "dinner", 
                                                   "order", "meal", "hungry", "drink", "beverage", "menu"]):
        return "room_service"
    
    # Check for recommendation related keywords
    if any(keyword in message_lower for keyword in ["recommend", "suggestion", "visit", "attraction", 
                                                   "restaurant", "activity", "things to do", "nearby", 
                                                   "what's good", "where to", "places", "shopping"]):
        return "recommendations"
    
    # Check for hotel info related keywords
    if any(keyword in message_lower for keyword in ["checkin", "checkout", "wifi", "pool", "gym", 
                                                   "breakfast", "parking", "hours", "amenity", 
                                                   "service", "hotel info", "spa"]):
        return "hotel_info"
    
    # Default category
    return "general"

def is_category_match(category, message):
    """
    Check if the user's message is asking about a specific category
    """
    category_mapping = {
        "attractions": ["sightseeing", "tourist", "visit", "see"],
        "restaurants": ["eat", "food", "dining", "cuisine"],
        "shopping": ["buy", "shop", "mall", "store"]
    }
    
    if category in category_mapping:
        return any(keyword in message for keyword in category_mapping[category])
    
    return False
