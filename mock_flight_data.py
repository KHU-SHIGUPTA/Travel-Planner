"""
Mock flight data for the Travel Planner AI application.
This simulates responses from the SERP API for flights.
"""
from airport_codes import get_airport_code
from datetime import datetime, timedelta

def get_mock_flight_data(source, destination, date):
    """
    Return mock flight data for the given parameters.
    
    Args:
        source (str): Source location (city, state, or country)
        destination (str): Destination location (city, state, or country)
        date (str): Travel date
        
    Returns:
        dict: Mock flight data or error message
    """
    # Print debug information
    print(f"Searching for airport code for source: '{source}'")
    print(f"Searching for airport code for destination: '{destination}'")
    
    # Convert source and destination to airport codes
    source_airport = get_airport_code(source)
    destination_airport = get_airport_code(destination)
    
    # Print results of the lookup
    print(f"Source airport lookup result: {source_airport}")
    print(f"Destination airport lookup result: {destination_airport}")
    
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

    # Store the original user-provided locations
    user_source = source
    user_destination = destination
    
    # Format the date for the API URL
    try:
        departure_date = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = departure_date.strftime("%Y-%m-%d")
    except:
        # If date parsing fails, use a default
        formatted_date = "2025-03-17"
    
    # Construct the SERP API URL with the actual API key
    SERP_API_KEY = os.getenv("SERP_API_KEY")
    serp_api_url = f"https://serpapi.com/search.json?engine=google_flights&type=2&departure_id={source_code}&arrival_id={destination_code}&outbound_date={formatted_date}&currency=USD&hl=en&api_key={SERP_API_KEY }"

    print(f"Using SERP API URL: {serp_api_url}")
    
    # Return mock flight data that matches the SERP API response format
    return {
        "serp_api_url": serp_api_url,
        "user_source": user_source,
        "user_destination": user_destination,
        "best_flights": [
            {
                "flights": [
                    {
                        "departure_airport": {
                            "name": "Beijing Capital International Airport",
                            "id": "PEK",
                            "time": "2025-03-17 19:20"
                        },
                        "arrival_airport": {
                            "name": "San Francisco International Airport",
                            "id": "SFO",
                            "time": "2025-03-17 15:50"
                        },
                        "duration": 690,
                        "airplane": "Boeing 777",
                        "airline": "United",
                        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/UA.png",
                        "travel_class": "Economy",
                        "flight_number": "UA 889",
                        "legroom": "31 in",
                        "extensions": [
                            "Average legroom (31 in)",
                            "Wi-Fi for a fee",
                            "In-seat power & USB outlets",
                            "On-demand video",
                            "Carbon emissions estimate: 698 kg"
                        ],
                        "overnight": True
                    },
                    {
                        "departure_airport": {
                            "name": "San Francisco International Airport",
                            "id": "SFO",
                            "time": "2025-03-17 18:30"
                        },
                        "arrival_airport": {
                            "name": "Austin-Bergstrom International Airport",
                            "id": "AUS",
                            "time": "2025-03-17 23:59"
                        },
                        "duration": 209,
                        "airplane": "Airbus A319",
                        "airline": "United",
                        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/UA.png",
                        "travel_class": "Economy",
                        "flight_number": "UA 2077",
                        "legroom": "30 in",
                        "extensions": [
                            "Average legroom (30 in)",
                            "Wi-Fi for a fee",
                            "In-seat power & USB outlets",
                            "Stream media to your device",
                            "Carbon emissions estimate: 246 kg"
                        ]
                    }
                ],
                "layovers": [
                    {
                        "duration": 160,
                        "name": "San Francisco International Airport",
                        "id": "SFO"
                    }
                ],
                "total_duration": 1059,
                "carbon_emissions": {
                    "this_flight": 945000,
                    "typical_for_this_route": 851000,
                    "difference_percent": 11
                },
                "price": 997,
                "type": "One way",
                "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/UA.png",
                "booking_token": "WyJDalJJVTB0VFlYVlFXamxxY1VsQlJuZGpWbmRDUnkwdExTMHRMUzB0TFhaMGNtZ3hOa0ZCUVVGQlIyWlhZMVpOUVU5ZlMzVkJFZ3hWUVRnNE9YeFZRVEl3TnpjYUN3akppZ1lRQWhvRFZWTkVPQnh3eVlvRyIsW1siUEVLIiwiMjAyNS0wMy0xNyIsIlNGTyIsbnVsbCwiVUEiLCI4ODkiXSxbIlNGTyIsIjIwMjUtMDMtMTciLCJBVVMiLG51bGwsIlVBIiwiMjA3NyJdXV0="
            },
            {
                "flights": [
                    {
                        "departure_airport": {
                            "name": "Beijing Capital International Airport",
                            "id": "PEK",
                            "time": "2025-03-17 15:35"
                        },
                        "arrival_airport": {
                            "name": "Incheon International Airport",
                            "id": "ICN",
                            "time": "2025-03-17 18:30"
                        },
                        "duration": 115,
                        "airplane": "Boeing 777",
                        "airline": "Asiana Airlines",
                        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/OZ.png",
                        "travel_class": "Economy",
                        "flight_number": "OZ 334",
                        "legroom": "33 in",
                        "extensions": [
                            "Above average legroom (33 in)",
                            "In-seat power & USB outlets",
                            "On-demand video",
                            "Carbon emissions estimate: 101 kg"
                        ]
                    },
                    {
                        "departure_airport": {
                            "name": "Incheon International Airport",
                            "id": "ICN",
                            "time": "2025-03-17 20:50"
                        },
                        "arrival_airport": {
                            "name": "San Francisco International Airport",
                            "id": "SFO",
                            "time": "2025-03-17 15:00"
                        },
                        "duration": 610,
                        "airplane": "Airbus A350",
                        "airline": "Asiana Airlines",
                        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/OZ.png",
                        "travel_class": "Economy",
                        "flight_number": "OZ 212",
                        "legroom": "32 in",
                        "extensions": [
                            "Above average legroom (32 in)",
                            "Wi-Fi for a fee",
                            "In-seat power & USB outlets",
                            "On-demand video",
                            "Carbon emissions estimate: 696 kg"
                        ],
                        "overnight": True,
                        "often_delayed_by_over_30_min": True
                    },
                    {
                        "departure_airport": {
                            "name": "San Francisco International Airport",
                            "id": "SFO",
                            "time": "2025-03-17 18:04"
                        },
                        "arrival_airport": {
                            "name": "Austin-Bergstrom International Airport",
                            "id": "AUS",
                            "time": "2025-03-17 23:33"
                        },
                        "duration": 209,
                        "airplane": "Boeing 737MAX 9 Passenger",
                        "airline": "Alaska",
                        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AS.png",
                        "travel_class": "Economy",
                        "flight_number": "AS 534",
                        "ticket_also_sold_by": [
                            "Hawaiian"
                        ],
                        "legroom": "31 in",
                        "extensions": [
                            "Average legroom (31 in)",
                            "Wi-Fi for a fee",
                            "In-seat power & USB outlets",
                            "Stream media to your device",
                            "Carbon emissions estimate: 219 kg"
                        ]
                    }
                ],
                "layovers": [
                    {
                        "duration": 140,
                        "name": "Incheon International Airport",
                        "id": "ICN"
                    },
                    {
                        "duration": 184,
                        "name": "San Francisco International Airport",
                        "id": "SFO"
                    }
                ],
                "total_duration": 1258,
                "carbon_emissions": {
                    "this_flight": 1018000,
                    "typical_for_this_route": 851000,
                    "difference_percent": 20
                },
                "price": 1023,
                "type": "One way",
                "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/multi.png",
                "booking_token": "WyJDalJJVTB0VFlYVlFXamxxY1VsQlJuZGpWbmRDUnkwdExTMHRMUzB0TFhaMGNtZ3hOa0ZCUVVGQlIyWlhZMVpOUVU5ZlMzVkJFaEZQV2pNek5IeFBXakl4TW54QlV6VXpOQm9MQ1B5ZUJoQUNHZ05WVTBRNEhIRDhuZ1k9IixbWyJQRUsiLCIyMDI1LTAzLTE3IiwiSUNOIixudWxsLCJPWiIsIjMzNCJdLFsiSUNOIiwiMjAyNS0wMy0xNyIsIlNGTyIsbnVsbCwiT1oiLCIyMTIiXSxbIlNGTyIsIjIwMjUtMDMtMTciLCJBVVMiLG51bGwsIkFTIiwiNTM0Il1dXQ=="
            },
            {
                "flights": [
                    {
                        "departure_airport": {
                            "name": "Beijing Capital International Airport",
                            "id": "PEK",
                            "time": "2025-03-17 10:50"
                        },
                        "arrival_airport": {
                            "name": "Incheon International Airport",
                            "id": "ICN",
                            "time": "2025-03-17 13:45"
                        },
                        "duration": 115,
                        "airplane": "Boeing 777",
                        "airline": "Asiana Airlines",
                        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/OZ.png",
                        "travel_class": "Economy",
                        "flight_number": "OZ 332",
                        "legroom": "33 in",
                        "extensions": [
                            "Above average legroom (33 in)",
                            "In-seat power & USB outlets",
                            "On-demand video",
                            "Carbon emissions estimate: 99 kg"
                        ]
                    },
                    {
                        "departure_airport": {
                            "name": "Incheon International Airport",
                            "id": "ICN",
                            "time": "2025-03-17 17:50"
                        },
                        "arrival_airport": {
                            "name": "Dallas Fort Worth International Airport",
                            "id": "DFW",
                            "time": "2025-03-17 16:45"
                        },
                        "duration": 775,
                        "airplane": "Boeing 777",
                        "airline": "American",
                        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
                        "travel_class": "Economy",
                        "flight_number": "AA 280",
                        "legroom": "31 in",
                        "extensions": [
                            "Average legroom (31 in)",
                            "Wi-Fi for a fee",
                            "In-seat power & USB outlets",
                            "On-demand video",
                            "Carbon emissions estimate: 691 kg"
                        ],
                        "overnight": True,
                        "often_delayed_by_over_30_min": True
                    },
                    {
                        "departure_airport": {
                            "name": "Dallas Fort Worth International Airport",
                            "id": "DFW",
                            "time": "2025-03-17 19:00"
                        },
                        "arrival_airport": {
                            "name": "Austin-Bergstrom International Airport",
                            "id": "AUS",
                            "time": "2025-03-17 20:06"
                        },
                        "duration": 66,
                        "airplane": "Embraer 175",
                        "airline": "American",
                        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
                        "travel_class": "Economy",
                        "flight_number": "AA 3748",
                        "legroom": "30 in",
                        "extensions": [
                            "Average legroom (30 in)",
                            "Wi-Fi for a fee",
                            "In-seat power & USB outlets",
                            "Stream media to your device",
                            "Carbon emissions estimate: 70 kg"
                        ]
                    }
                ],
                "layovers": [
                    {
                        "duration": 245,
                        "name": "Incheon International Airport",
                        "id": "ICN"
                    },
                    {
                        "duration": 135,
                        "name": "Dallas Fort Worth International Airport",
                        "id": "DFW"
                    }
                ],
                "total_duration": 1336,
                "carbon_emissions": {
                    "this_flight": 860000,
                    "typical_for_this_route": 851000,
                    "difference_percent": 1
                },
                "price": 1145,
                "type": "One way",
                "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/multi.png",
                "booking_token": "WyJDalJJVTB0VFlYVlFXamxxY1VsQlJuZGpWbmRDUnkwdExTMHRMUzB0TFhaMGNtZ3hOa0ZCUVVGQlIyWlhZMVpOUVU5ZlMzVkJFaEZQV2pNek1ueFFXakl4TW54QlFUTTNORGdLQ3dqcnJnWVFBaG9EVlZORU9CeHc2NjRHIixbWyJQRUsiLCIyMDI1LTAzLTE3IiwiSUNOIixudWxsLCJPWiIsIjMzMiJdLFsiSUNOIiwiMjAyNS0wMy0xNyIsIkRGVyIsbnVsbCwiQUEiLCIyODAiXSxbIkRGVyIsIjIwMjUtMDMtMTciLCJBVVMiLG51bGwsIkFBIiwiMzc0OCJdXV0="
            }
        ]
    }