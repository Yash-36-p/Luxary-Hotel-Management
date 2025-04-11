"""
In-memory data storage for hotel information, room service menu, and local recommendations.
"""

# Room service menu items
ROOM_SERVICE_MENU = {
    "breakfast": [
        {"id": "b1", "name": "Continental Breakfast", "description": "Fresh pastries, fruit, yogurt, and coffee", "price": 18.00},
        {"id": "b2", "name": "American Breakfast", "description": "Eggs, bacon, toast, and potatoes", "price": 22.00},
        {"id": "b3", "name": "Healthy Start", "description": "Egg white omelet with vegetables and whole grain toast", "price": 24.00},
        {"id": "b4", "name": "Belgian Waffles", "description": "With maple syrup and fresh berries", "price": 19.00}
    ],
    "lunch": [
        {"id": "l1", "name": "Club Sandwich", "description": "Triple-decker with turkey, bacon, lettuce, and tomato", "price": 24.00},
        {"id": "l2", "name": "Caesar Salad", "description": "Romaine lettuce, croutons, parmesan, and Caesar dressing", "price": 18.00},
        {"id": "l3", "name": "Burger", "description": "Half-pound Angus beef with fries", "price": 26.00},
        {"id": "l4", "name": "Vegetable Wrap", "description": "Grilled vegetables, hummus, and mixed greens", "price": 19.00}
    ],
    "dinner": [
        {"id": "d1", "name": "Filet Mignon", "description": "8oz with roasted vegetables and mashed potatoes", "price": 48.00},
        {"id": "d2", "name": "Grilled Salmon", "description": "With lemon butter sauce and quinoa pilaf", "price": 36.00},
        {"id": "d3", "name": "Pasta Primavera", "description": "Seasonal vegetables in a light cream sauce", "price": 28.00},
        {"id": "d4", "name": "Roasted Chicken", "description": "Half chicken with herb jus and wild rice", "price": 32.00}
    ],
    "desserts": [
        {"id": "ds1", "name": "Chocolate Cake", "description": "With vanilla ice cream", "price": 14.00},
        {"id": "ds2", "name": "Cheesecake", "description": "New York style with berry compote", "price": 12.00},
        {"id": "ds3", "name": "Fruit Plate", "description": "Seasonal fresh fruit", "price": 10.00}
    ],
    "beverages": [
        {"id": "bv1", "name": "Coffee", "description": "Regular or decaf", "price": 6.00},
        {"id": "bv2", "name": "Tea", "description": "Selection of premium teas", "price": 6.00},
        {"id": "bv3", "name": "Soft Drinks", "description": "Coke, Diet Coke, Sprite, etc.", "price": 5.00},
        {"id": "bv4", "name": "Bottled Water", "description": "Still or sparkling", "price": 5.00},
        {"id": "bv5", "name": "Wine", "description": "By the glass, see wine list", "price": 14.00}
    ]
}

# Local recommendations
LOCAL_RECOMMENDATIONS = {
    "attractions": [
        {"name": "City Museum", "description": "Historical exhibits and art galleries", "distance": "0.5 miles", "category": "museum"},
        {"name": "Central Park", "description": "Large urban park with walking trails", "distance": "0.3 miles", "category": "outdoors"},
        {"name": "Opera House", "description": "Historic venue with regular performances", "distance": "0.8 miles", "category": "entertainment"},
        {"name": "Harbor Cruise", "description": "Scenic boat tour of the city skyline", "distance": "1.2 miles", "category": "activity"},
        {"name": "Observation Deck", "description": "Panoramic city views from the 70th floor", "distance": "0.7 miles", "category": "sightseeing"}
    ],
    "restaurants": [
        {"name": "Luigi's", "description": "Authentic Italian cuisine", "distance": "0.4 miles", "category": "italian", "price_range": "$$$"},
        {"name": "Blue Ginger", "description": "Modern Asian fusion", "distance": "0.6 miles", "category": "asian", "price_range": "$$$"},
        {"name": "Steakhouse 45", "description": "Prime cuts and fine wines", "distance": "0.5 miles", "category": "steakhouse", "price_range": "$$$$"},
        {"name": "Green Leaf", "description": "Vegetarian and vegan options", "distance": "0.8 miles", "category": "vegetarian", "price_range": "$$"},
        {"name": "Seaside", "description": "Fresh seafood with harbor views", "distance": "1.0 miles", "category": "seafood", "price_range": "$$$"}
    ],
    "shopping": [
        {"name": "City Center Mall", "description": "Large shopping center with designer brands", "distance": "0.5 miles", "category": "mall"},
        {"name": "Artisan Market", "description": "Local crafts and unique gifts", "distance": "0.9 miles", "category": "market"},
        {"name": "Fashion District", "description": "Upscale boutiques and flagship stores", "distance": "1.1 miles", "category": "clothing"},
        {"name": "Electronics Emporium", "description": "Latest gadgets and tech accessories", "distance": "0.7 miles", "category": "electronics"}
    ]
}

# Hotel information
HOTEL_INFO = {
    "general": {
        "name": "Luxury Grand Hotel",
        "address": "123 Elegant Avenue, Cityville",
        "phone": "+1 (555) 123-4567",
        "email": "concierge@luxurygrandhotel.com",
        "website": "www.luxurygrandhotel.com"
    },
    "amenities": {
        "wifi": "Complimentary high-speed WiFi throughout the property",
        "pool": "Heated indoor pool and hot tub (7:00 AM - 9:00 PM)",
        "spa": "Full-service spa offering massages and treatments (9:00 AM - 8:00 PM)",
        "gym": "24-hour fitness center with cardio and weight equipment",
        "business_center": "Business center with computers and printing services (24 hours)",
        "concierge": "Concierge desk (7:00 AM - 10:00 PM)"
    },
    "policies": {
        "check_in": "3:00 PM",
        "check_out": "11:00 AM",
        "late_checkout": "Available upon request (fee may apply)",
        "pets": "Pet-friendly rooms available (fee applies)",
        "smoking": "Non-smoking property",
        "parking": "Valet parking available ($45 per night)"
    },
    "dining": {
        "main_restaurant": {
            "name": "The Grand Dining Room",
            "hours": "Breakfast: 6:30 AM - 10:30 AM, Lunch: 11:30 AM - 2:00 PM, Dinner: 5:30 PM - 10:00 PM",
            "dress_code": "Smart casual"
        },
        "lounge": {
            "name": "Skyline Lounge",
            "hours": "12:00 PM - 12:00 AM",
            "description": "Cocktails and light fare with city views"
        },
        "room_service": {
            "hours": "6:00 AM - 11:00 PM",
            "late_night": "Limited menu available 11:00 PM - 6:00 AM"
        }
    },
    "transportation": {
        "airport_shuttle": "Available with 24-hour advance reservation ($30 one-way)",
        "taxi": "Available at the front entrance",
        "public_transport": "Metro station 2 blocks away"
    }
}

def get_room_service_menu(category='all'):
    """
    Get room service menu items by category
    """
    if category == 'all':
        return ROOM_SERVICE_MENU
    elif category in ROOM_SERVICE_MENU:
        return {category: ROOM_SERVICE_MENU[category]}
    else:
        return {"error": "Category not found"}

def get_local_recommendations(category='all', distance='all'):
    """
    Get local recommendations filtered by category and/or distance
    """
    if category == 'all' and distance == 'all':
        return LOCAL_RECOMMENDATIONS
    
    filtered_results = {}
    
    for key, items in LOCAL_RECOMMENDATIONS.items():
        if category != 'all' and key != category:
            continue
            
        filtered_items = []
        for item in items:
            if distance != 'all':
                # Parse the distance (remove "miles" and convert to float)
                item_distance = float(item['distance'].split()[0])
                max_distance = float(distance)
                
                if item_distance <= max_distance:
                    filtered_items.append(item)
            else:
                filtered_items.append(item)
                
        if filtered_items:
            filtered_results[key] = filtered_items
    
    return filtered_results

def get_hotel_info(info_type='all'):
    """
    Get hotel information by type
    """
    if info_type == 'all':
        return HOTEL_INFO
    elif info_type in HOTEL_INFO:
        return {info_type: HOTEL_INFO[info_type]}
    else:
        return {"error": "Information type not found"}
