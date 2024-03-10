"""
Mock database of airport codes for the Travel Planner AI application.
This simulates a database of airport codes for common cities, states, and countries.
"""

# Dictionary mapping locations (cities, states, countries) to airport codes
# Format: 'location_name_lowercase': {'code': 'XXX', 'name': 'Full Airport Name'}
AIRPORT_CODES = {
    # Major international cities
    'delhi': {'code': 'DEL', 'name': 'Indira Gandhi International Airport'},
    'new delhi': {'code': 'DEL', 'name': 'Indira Gandhi International Airport'},
    'mumbai': {'code': 'BOM', 'name': 'Chhatrapati Shivaji Maharaj International Airport'},
    'bangalore': {'code': 'BLR', 'name': 'Kempegowda International Airport'},
    'bengaluru': {'code': 'BLR', 'name': 'Kempegowda International Airport'},
    'chennai': {'code': 'MAA', 'name': 'Chennai International Airport'},
    'kolkata': {'code': 'CCU', 'name': 'Netaji Subhas Chandra Bose International Airport'},
    'hyderabad': {'code': 'HYD', 'name': 'Rajiv Gandhi International Airport'},
    'ahmedabad': {'code': 'AMD', 'name': 'Sardar Vallabhbhai Patel International Airport'},
    'goa': {'code': 'GOI', 'name': 'Goa International Airport'},
    'lucknow': {'code': 'LKO', 'name': 'Chaudhary Charan Singh International Airport'},
    'jaipur': {'code': 'JAI', 'name': 'Jaipur International Airport'},
    'pune': {'code': 'PNQ', 'name': 'Pune Airport'},
    'kochi': {'code': 'COK', 'name': 'Cochin International Airport'},
    'cochin': {'code': 'COK', 'name': 'Cochin International Airport'},
    'kozhikode': {'code': 'CCJ', 'name': 'Calicut International Airport'},
    'calicut': {'code': 'CCJ', 'name': 'Calicut International Airport'},
    'thiruvananthapuram': {'code': 'TRV', 'name': 'Trivandrum International Airport'},
    'trivandrum': {'code': 'TRV', 'name': 'Trivandrum International Airport'},
    'coimbatore': {'code': 'CJB', 'name': 'Coimbatore International Airport'},
    'nagpur': {'code': 'NAG', 'name': 'Dr. Babasaheb Ambedkar International Airport'},
    'patna': {'code': 'PAT', 'name': 'Jay Prakash Narayan International Airport'},
    'bhubaneswar': {'code': 'BBI', 'name': 'Biju Patnaik International Airport'},
    'indore': {'code': 'IDR', 'name': 'Devi Ahilyabai Holkar Airport'},
    'varanasi': {'code': 'VNS', 'name': 'Lal Bahadur Shastri International Airport'},
    'srinagar': {'code': 'SXR', 'name': 'Sheikh ul-Alam International Airport'},
    'chandigarh': {'code': 'IXC', 'name': 'Chandigarh International Airport'},
    'amritsar': {'code': 'ATQ', 'name': 'Sri Guru Ram Dass Jee International Airport'},
    'visakhapatnam': {'code': 'VTZ', 'name': 'Visakhapatnam Airport'},
    'vizag': {'code': 'VTZ', 'name': 'Visakhapatnam Airport'},
    'raipur': {'code': 'RPR', 'name': 'Swami Vivekananda Airport'},
    'agartala': {'code': 'IXA', 'name': 'Maharaja Bir Bikram Airport'},
    'dehradun': {'code': 'DED', 'name': 'Dehradun Airport'},
    'ranchi': {'code': 'IXR', 'name': 'Birsa Munda Airport'},
    'udaipur': {'code': 'UDR', 'name': 'Maharana Pratap Airport'},
    'vadodara': {'code': 'BDQ', 'name': 'Vadodara Airport'},
    'bhopal': {'code': 'BHO', 'name': 'Raja Bhoj Airport'},
    'mangalore': {'code': 'IXE', 'name': 'Mangalore International Airport'},
    'mangaluru': {'code': 'IXE', 'name': 'Mangalore International Airport'},
    'tirupati': {'code': 'TIR', 'name': 'Tirupati Airport'},
    'jammu': {'code': 'IXJ', 'name': 'Jammu Airport'},
    'leh': {'code': 'IXL', 'name': 'Kushok Bakula Rimpochee Airport'},
    'dibrugarh': {'code': 'DIB', 'name': 'Dibrugarh Airport'},
    'imphal': {'code': 'IMF', 'name': 'Imphal International Airport'},
    'guwahati': {'code': 'GAU', 'name': 'Lokpriya Gopinath Bordoloi International Airport'},
    
    # US cities
    'new york': {'code': 'JFK', 'name': 'John F. Kennedy International Airport'},
    'los angeles': {'code': 'LAX', 'name': 'Los Angeles International Airport'},
    'chicago': {'code': 'ORD', 'name': 'O\'Hare International Airport'},
    'houston': {'code': 'IAH', 'name': 'George Bush Intercontinental Airport'},
    'phoenix': {'code': 'PHX', 'name': 'Phoenix Sky Harbor International Airport'},
    'philadelphia': {'code': 'PHL', 'name': 'Philadelphia International Airport'},
    'san antonio': {'code': 'SAT', 'name': 'San Antonio International Airport'},
    'san diego': {'code': 'SAN', 'name': 'San Diego International Airport'},
    'dallas': {'code': 'DFW', 'name': 'Dallas/Fort Worth International Airport'},
    'san jose': {'code': 'SJC', 'name': 'Norman Y. Mineta San Jose International Airport'},
    'austin': {'code': 'AUS', 'name': 'Austin-Bergstrom International Airport'},
    'seattle': {'code': 'SEA', 'name': 'Seattle-Tacoma International Airport'},
    'boston': {'code': 'BOS', 'name': 'Boston Logan International Airport'},
    'las vegas': {'code': 'LAS', 'name': 'Harry Reid International Airport'},
    'washington': {'code': 'IAD', 'name': 'Washington Dulles International Airport'},
    'washington dc': {'code': 'DCA', 'name': 'Ronald Reagan Washington National Airport'},
    'atlanta': {'code': 'ATL', 'name': 'Hartsfield-Jackson Atlanta International Airport'},
    'miami': {'code': 'MIA', 'name': 'Miami International Airport'},
    'denver': {'code': 'DEN', 'name': 'Denver International Airport'},
    'san francisco': {'code': 'SFO', 'name': 'San Francisco International Airport'},
    
    # European cities
    'london': {'code': 'LHR', 'name': 'London Heathrow Airport'},
    'paris': {'code': 'CDG', 'name': 'Charles de Gaulle Airport'},
    'rome': {'code': 'FCO', 'name': 'Leonardo da Vinci International Airport'},
    'amsterdam': {'code': 'AMS', 'name': 'Amsterdam Airport Schiphol'},
    'madrid': {'code': 'MAD', 'name': 'Adolfo Suárez Madrid–Barajas Airport'},
    'barcelona': {'code': 'BCN', 'name': 'Josep Tarradellas Barcelona–El Prat Airport'},
    'berlin': {'code': 'BER', 'name': 'Berlin Brandenburg Airport'},
    'frankfurt': {'code': 'FRA', 'name': 'Frankfurt Airport'},
    'munich': {'code': 'MUC', 'name': 'Munich Airport'},
    'zurich': {'code': 'ZRH', 'name': 'Zurich Airport'},
    
    # Asian cities
    'tokyo': {'code': 'HND', 'name': 'Tokyo Haneda Airport'},
    'beijing': {'code': 'PEK', 'name': 'Beijing Capital International Airport'},
    'shanghai': {'code': 'PVG', 'name': 'Shanghai Pudong International Airport'},
    'hong kong': {'code': 'HKG', 'name': 'Hong Kong International Airport'},
    'bangkok': {'code': 'BKK', 'name': 'Suvarnabhumi Airport'},
    'bankok': {'code': 'BKK', 'name': 'Suvarnabhumi Airport'},  # Common misspelling
    'bankkong': {'code': 'BKK', 'name': 'Suvarnabhumi Airport'},  # Common misspelling
    'bangkock': {'code': 'BKK', 'name': 'Suvarnabhumi Airport'},  # Common misspelling
    'singapore': {'code': 'SIN', 'name': 'Singapore Changi Airport'},
    'seoul': {'code': 'ICN', 'name': 'Incheon International Airport'},
    'kuala lumpur': {'code': 'KUL', 'name': 'Kuala Lumpur International Airport'},
    'dubai': {'code': 'DXB', 'name': 'Dubai International Airport'},
    'abu dhabi': {'code': 'AUH', 'name': 'Abu Dhabi International Airport'},
    
    # Australian/Oceania cities
    'sydney': {'code': 'SYD', 'name': 'Sydney Airport'},
    'melbourne': {'code': 'MEL', 'name': 'Melbourne Airport'},
    'brisbane': {'code': 'BNE', 'name': 'Brisbane Airport'},
    'perth': {'code': 'PER', 'name': 'Perth Airport'},
    'auckland': {'code': 'AKL', 'name': 'Auckland Airport'},
    'wellington': {'code': 'WLG', 'name': 'Wellington International Airport'},
    
    # African cities
    'cairo': {'code': 'CAI', 'name': 'Cairo International Airport'},
    'johannesburg': {'code': 'JNB', 'name': 'O.R. Tambo International Airport'},
    'cape town': {'code': 'CPT', 'name': 'Cape Town International Airport'},
    'nairobi': {'code': 'NBO', 'name': 'Jomo Kenyatta International Airport'},
    'lagos': {'code': 'LOS', 'name': 'Murtala Muhammed International Airport'},
    
    # South American cities
    'sao paulo': {'code': 'GRU', 'name': 'São Paulo/Guarulhos International Airport'},
    'rio de janeiro': {'code': 'GIG', 'name': 'Rio de Janeiro/Galeão International Airport'},
    'buenos aires': {'code': 'EZE', 'name': 'Ministro Pistarini International Airport'},
    'lima': {'code': 'LIM', 'name': 'Jorge Chávez International Airport'},
    'bogota': {'code': 'BOG', 'name': 'El Dorado International Airport'},
    'santiago': {'code': 'SCL', 'name': 'Santiago International Airport'},
    
    # Countries (using main airport)
    'india': {'code': 'DEL', 'name': 'Indira Gandhi International Airport'},
    'usa': {'code': 'JFK', 'name': 'John F. Kennedy International Airport'},
    'united states': {'code': 'JFK', 'name': 'John F. Kennedy International Airport'},
    'uk': {'code': 'LHR', 'name': 'London Heathrow Airport'},
    'united kingdom': {'code': 'LHR', 'name': 'London Heathrow Airport'},
    'france': {'code': 'CDG', 'name': 'Charles de Gaulle Airport'},
    'germany': {'code': 'FRA', 'name': 'Frankfurt Airport'},
    'italy': {'code': 'FCO', 'name': 'Leonardo da Vinci International Airport'},
    'spain': {'code': 'MAD', 'name': 'Adolfo Suárez Madrid–Barajas Airport'},
    'china': {'code': 'PEK', 'name': 'Beijing Capital International Airport'},
    'japan': {'code': 'HND', 'name': 'Tokyo Haneda Airport'},
    'australia': {'code': 'SYD', 'name': 'Sydney Airport'},
    'brazil': {'code': 'GRU', 'name': 'São Paulo/Guarulhos International Airport'},
    'canada': {'code': 'YYZ', 'name': 'Toronto Pearson International Airport'},
    'mexico': {'code': 'MEX', 'name': 'Mexico City International Airport'},
    
    # US states (using main airport)
    'california': {'code': 'LAX', 'name': 'Los Angeles International Airport'},
    'new york state': {'code': 'JFK', 'name': 'John F. Kennedy International Airport'},
    'texas': {'code': 'DFW', 'name': 'Dallas/Fort Worth International Airport'},
    'florida': {'code': 'MIA', 'name': 'Miami International Airport'},
    'illinois': {'code': 'ORD', 'name': 'O\'Hare International Airport'},
    'pennsylvania': {'code': 'PHL', 'name': 'Philadelphia International Airport'},
    'ohio': {'code': 'CLE', 'name': 'Cleveland Hopkins International Airport'},
    'georgia': {'code': 'ATL', 'name': 'Hartsfield-Jackson Atlanta International Airport'},
    'michigan': {'code': 'DTW', 'name': 'Detroit Metropolitan Wayne County Airport'},
    'north carolina': {'code': 'CLT', 'name': 'Charlotte Douglas International Airport'},
}

def get_airport_code(location):
    """
    Get the airport code for a given location.

    Args:
        location (str): The name of the city, state, or country

    Returns:
        dict: A dictionary containing the airport code and name, or None if not found
    """
    if not location:
        return None

    # Normalize the location name (lowercase and remove extra spaces)
    location_key = location.lower().strip()

    # Check if the location is too short after stripping
    if len(location_key) < 2:
        return None

    # Check if the input contains an airport code in parentheses (e.g., "New York (JFK)")
    if '(' in location_key and ')' in location_key:
        # Extract the code from the parentheses
        code_start = location_key.find('(') + 1
        code_end = location_key.find(')')
        if code_end > code_start:
            code = location_key[code_start:code_end].strip().upper()
            # Find the airport by code
            for airport in AIRPORT_CODES.values():
                if airport['code'] == code:
                    return airport

    # Direct lookup
    if location_key in AIRPORT_CODES:
        return AIRPORT_CODES[location_key]

    # Partial match (for cases where user enters partial name or with extra words)
    for key, value in AIRPORT_CODES.items():
        if key in location_key or location_key in key:
            return value

    # Fuzzy matching for typos and misspellings
    # Calculate similarity scores based on character overlap
    best_match = None
    best_score = 0

    for key, value in AIRPORT_CODES.items():
        # Skip very short keys to avoid false matches
        if len(key) < 3:
            continue

        # Simple character-based similarity score
        # Count matching characters in sequence
        score = 0
        loc_chars = set(location_key)
        key_chars = set(key)
        common_chars = loc_chars.intersection(key_chars)

        # Calculate similarity as percentage of matching characters
        similarity = len(common_chars) / max(len(loc_chars), len(key_chars))

        # Check for common prefixes (first 3 letters matching is a strong signal)
        prefix_bonus = 0
        min_len = min(len(location_key), len(key))
        for i in range(min(3, min_len)):
            if location_key[i] == key[i]:
                prefix_bonus += 0.1

        total_score = similarity + prefix_bonus

        # If this is a better match than what we've seen so far
        if total_score > best_score and total_score > 0.5:  # Threshold of 50% similarity
            best_score = total_score
            best_match = value

    # Return the best fuzzy match if found
    if best_match:
        return best_match

    # If no match found
    return None

def get_all_locations():
    """
    Get a list of all available locations for auto-suggest.

    Returns:
        list: A list of dictionaries with location names and their airport codes
    """
    locations = []

    for location, airport in AIRPORT_CODES.items():
        # Skip very short location names and duplicates
        if len(location) < 3:
            continue

        # Format the location name for display (capitalize words)
        display_name = ' '.join(word.capitalize() for word in location.split())

        locations.append({
            'value': location,
            'label': f"{display_name} ({airport['code']})",
            'code': airport['code'],
            'airport': airport['name']
        })

    # Sort by location name
    return sorted(locations, key=lambda x: x['label'])