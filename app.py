import os
import json
import requests
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from mock_flight_data import get_mock_flight_data
from airport_codes import get_all_locations, get_airport_code
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configure the Gemini API


API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# Set up the model
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/locations', methods=['GET'])
def get_locations():
    """API endpoint to get all available locations for autocomplete"""
    locations = get_all_locations()
    return jsonify(locations)

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for chatbot functionality"""
    data = request.json
    user_message = data.get('message', '')

    # Get context if available
    context = data.get('context', {})

    try:
        # Check if this is a location-specific query
        location_keywords = ["in", "at", "for", "about", "near", "around"]
        cities = ["paris", "london", "new york", "tokyo", "rome", "barcelona", "amsterdam", "berlin",
                 "sydney", "bangkok", "dubai", "singapore", "hong kong", "istanbul", "venice", "prague",
                 "vienna", "madrid", "lisbon", "athens", "cairo", "marrakech", "rio", "mexico city"]

        # Extract location if present
        location = None
        lower_message = user_message.lower()

        for city in cities:
            if city in lower_message:
                location = city.title()
                break

        # Create a prompt for the chatbot
        if "hotel" in lower_message or "stay" in lower_message or "accommodation" in lower_message or "place to sleep" in lower_message:
            if location:
                prompt = f"""
                You are a helpful travel assistant chatbot. The user is asking about hotel recommendations in {location}.

                User message: {user_message}

                Provide a specific, helpful response with 3-5 actual hotel recommendations in {location}.
                For each hotel, include:
                1. The hotel name
                2. A brief description (1 sentence)
                3. A general price range (budget, mid-range, luxury)

                Format as a numbered list. Be concise but specific.
                """
            else:
                prompt = f"""
                You are a helpful travel assistant chatbot. The user is asking about hotel recommendations.

                User message: {user_message}

                Ask which city they're interested in, and provide general tips for finding good accommodations.
                Be concise but helpful.
                """
        elif "restaurant" in lower_message or "food" in lower_message or "eat" in lower_message or "dining" in lower_message or "cuisine" in lower_message:
            if location:
                prompt = f"""
                You are a helpful travel assistant chatbot. The user is asking about food or restaurant recommendations in {location}.

                User message: {user_message}

                Provide a specific, helpful response with 3-5 actual restaurant recommendations in {location}.
                For each restaurant, include:
                1. The restaurant name
                2. The type of cuisine
                3. A signature dish or specialty

                Format as a numbered list. Be concise but specific.
                """
            else:
                prompt = f"""
                You are a helpful travel assistant chatbot. The user is asking about food or restaurant recommendations.

                User message: {user_message}

                Ask which city they're interested in, and provide general tips about local cuisine.
                Be concise but helpful.
                """
        elif "attraction" in lower_message or "see" in lower_message or "visit" in lower_message or "sight" in lower_message or "tour" in lower_message:
            if location:
                prompt = f"""
                You are a helpful travel assistant chatbot. The user is asking about attractions or sightseeing in {location}.

                User message: {user_message}

                Provide a specific, helpful response with 3-5 must-see attractions in {location}.
                For each attraction, include:
                1. The attraction name
                2. A brief description (1 sentence)
                3. A practical tip for visiting

                Format as a numbered list. Be concise but specific.
                """
            else:
                prompt = f"""
                You are a helpful travel assistant chatbot. The user is asking about attractions or sightseeing.

                User message: {user_message}

                Ask which city they're interested in, and provide general tips for sightseeing.
                Be concise but helpful.
                """
        else:
            prompt = f"""
            You are a helpful travel assistant chatbot. The user is asking about travel planning.

            User message: {user_message}

            Provide a helpful, friendly response about travel planning. If the query mentions a specific location, include specific information about that place.
            Keep your response concise (2-4 sentences).
            Focus on being practical and informative with specific recommendations when possible.
            """

        # Generate response from Gemini
        response = model.generate_content(prompt)

        return jsonify({
            'success': True,
            'response': response.text
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

def get_real_flight_data(source, destination, date):
    """
    Fetch real flight data from SERP API

    Args:
        source (str): Source location (city, state, or country)
        destination (str): Destination location (city, state, or country)
        date (str): Travel date in YYYY-MM-DD format

    Returns:
        dict: Flight data from SERP API or error message
    """
    # Convert source and destination to airport codes
    source_airport = get_airport_code(source)
    destination_airport = get_airport_code(destination)

    # Check if both source and destination are valid
    if not source_airport:
        return {
            "error": f"Could not find airport code for '{source}'. Please enter a valid city, state, or country."
        }

    if not destination_airport:
        return {
            "error": f"Could not find airport code for '{destination}'. Please enter a valid city, state, or country."
        }

    # Extract airport codes
    source_code = source_airport['code']
    destination_code = destination_airport['code']

    # Construct the SERP API URL with the actual API key
    
    SERP_API_KEY = os.getenv("SERP_API_KEY")
    serp_api_url = f"https://serpapi.com/search.json?engine=google_flights&type=2&departure_id={source_code}&arrival_id={destination_code}&outbound_date={date}&currency=USD&hl=en&api_key={SERP_API_KEY}"

    try:
        # Make the API request
        response = requests.get(serp_api_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            flight_data = response.json()

            # Add the original user-provided locations and API URL
            flight_data["user_source"] = source
            flight_data["user_destination"] = destination
            flight_data["serp_api_url"] = serp_api_url

            return flight_data
        else:
            # Return an error message if the request failed
            return {
                "error": f"Failed to fetch flight data. Status code: {response.status_code}",
                "user_source": source,
                "user_destination": destination,
                "serp_api_url": serp_api_url
            }
    except Exception as e:
        # Return an error message if an exception occurred
        return {
            "error": f"An error occurred while fetching flight data: {str(e)}",
            "user_source": source,
            "user_destination": destination,
            "serp_api_url": serp_api_url
        }

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    # Get user inputs
    data = request.json
    source = data.get('source')
    destination = data.get('destination')
    dates = data.get('dates')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    budget = data.get('budget')
    travelers = data.get('travelers')
    interests = data.get('interests')
    include_flights = data.get('include_flights', False)
    
    # Create prompt for Gemini
    prompt = f"""
    Create a detailed travel plan with the following information:
    - Source: {source}
    - Destination: {destination}
    - Travel Dates: {dates} (From {start_date} to {end_date})
    - Budget: {budget}
    - Number of Travelers: {travelers}
    - Interests: {interests}
    
    Please include:
    1. A day-by-day itinerary
    2. Recommended accommodations within budget
    3. Transportation options
    4. Must-visit attractions based on interests
    5. Estimated costs for each component
    6. Local food recommendations
    7. Travel tips specific to the destination
    8. Weather considerations for the travel dates
    
    Format the response in a structured way that's easy to read.
    """
    
    # Get flight information if requested
    flight_data = None
    if include_flights:
        # Use real flight data from SERP API
        try:
            flight_data = get_real_flight_data(source, destination, start_date)
            print(f"Successfully fetched flight data for {source} to {destination}")
        except Exception as e:
            print(f"Error fetching real flight data: {str(e)}")
            # Fall back to mock data if real API fails
            flight_data = get_mock_flight_data(source, destination, start_date)

    try:
        # Generate response from Gemini
        response = model.generate_content(prompt)

        # Prepare response data
        response_data = {
            'success': True,
            'plan': response.text
        }

        # Add flight data if available
        if flight_data:
            response_data['flight_data'] = flight_data

        # Return the generated travel plan
        return jsonify(response_data)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    # Ensure templates are not cached
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True, use_reloader=True)