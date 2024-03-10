document.addEventListener('DOMContentLoaded', function() {
    const travelForm = document.getElementById('travel-form');
    const resultContainer = document.getElementById('result');
    const loadingIndicator = document.getElementById('loading');
    const sourceInput = document.getElementById('source');
    const destinationInput = document.getElementById('destination');
    const backToTopButton = document.getElementById('backToTop');
    const travelPlanSection = document.getElementById('travel-plan-section');

    // Initialize autocomplete for source and destination
    initializeAutocomplete();

    // Back to top button functionality
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('visible');
        } else {
            backToTopButton.classList.remove('visible');
        }
    });

    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Chat Bot Functionality
    const chatBotButton = document.getElementById('chatBotButton');
    const chatContainer = document.getElementById('chatContainer');
    const chatCloseBtn = document.getElementById('chatCloseBtn');
    const chatInput = document.getElementById('chatInput');
    const chatSendBtn = document.getElementById('chatSendBtn');
    const chatMessages = document.getElementById('chatMessages');

    // Toggle chat container visibility
    chatBotButton.addEventListener('click', function() {
        chatContainer.classList.add('active');
        chatInput.focus();
    });

    chatCloseBtn.addEventListener('click', function() {
        chatContainer.classList.remove('active');
    });

    // Send message when clicking the send button
    chatSendBtn.addEventListener('click', sendMessage);

    // Send message when pressing Enter in the input field
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Function to send a message
    async function sendMessage() {
        const message = chatInput.value.trim();

        if (message === '') return;

        // Add user message to chat
        addMessage(message, 'user');

        // Clear input
        chatInput.value = '';

        // Show typing indicator
        showTypingIndicator();

        try {
            // Get bot response (with a minimum delay for natural feeling)
            const minTypingTime = 1000 + Math.random() * 1000; // Random delay between 1-2 seconds
            const responsePromise = getBotResponse(message);

            // Wait for both the minimum typing time and the response
            const [response] = await Promise.all([
                responsePromise,
                new Promise(resolve => setTimeout(resolve, minTypingTime))
            ]);

            // Remove typing indicator
            removeTypingIndicator();

            // Add bot response to chat
            addMessage(response, 'bot');
        } catch (error) {
            console.error('Error in sendMessage:', error);

            // Remove typing indicator
            removeTypingIndicator();

            // Add error message
            addMessage("I'm having trouble connecting right now. Please try again later.", 'bot');
        }

        // Scroll to the bottom
        scrollToBottom();
    }

    // Function to add a message to the chat
    function addMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);

        // Format the message - replace newlines with <br> tags
        const formattedMessage = message.replace(/\n/g, '<br>');

        messageElement.innerHTML = `
            <div class="message-content">
                <p>${formattedMessage}</p>
            </div>
        `;

        chatMessages.appendChild(messageElement);
    }

    // Function to show typing indicator
    function showTypingIndicator() {
        const typingElement = document.createElement('div');
        typingElement.classList.add('message', 'bot-message', 'typing-indicator');

        typingElement.innerHTML = `
            <div class="message-content">
                <div class="chat-typing">
                    <span>Travel Assistant is typing</span>
                    <div class="typing-dots">
                        <div class="typing-dot"></div>
                        <div class="typing-dot"></div>
                        <div class="typing-dot"></div>
                    </div>
                </div>
            </div>
        `;

        chatMessages.appendChild(typingElement);
        scrollToBottom();
    }

    // Function to remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = document.querySelector('.typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    // Function to scroll to the bottom of the chat
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Function to get a response from the bot
    async function getBotResponse(message) {
        try {
            // First try to get a response from the server
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    context: window.chatContext || {}
                })
            });

            const data = await response.json();

            if (data.success) {
                return data.response;
            }

            // If server fails, fall back to client-side responses
            return getFallbackResponse(message);
        } catch (error) {
            console.error('Error getting bot response:', error);
            return getFallbackResponse(message);
        }
    }

    // Fallback responses if the server is unavailable
    function getFallbackResponse(message) {
        // Convert message to lowercase for easier matching
        const lowerMessage = message.toLowerCase();

        // Check for location-specific queries
        const cities = {
            'paris': {
                hotels: [
                    "1. Hotel Fabric - A stylish boutique hotel in a former textile factory (mid-range).",
                    "2. CitizenM Paris Gare de Lyon - Modern, tech-forward hotel with affordable luxury rooms.",
                    "3. Le Bristol Paris - Iconic luxury hotel with exceptional service and an indoor rooftop pool.",
                    "4. Generator Paris - Trendy, design-focused hostel with private rooms and great social spaces (budget).",
                    "5. Hotel des Grands Boulevards - Charming hotel with beautiful decor in a central location (mid-range)."
                ],
                restaurants: [
                    "1. Le Comptoir du Relais - Classic French bistro with seasonal menu by chef Yves Camdeborde.",
                    "2. Chez L'Ami Jean - Rustic Basque restaurant known for its rice pudding dessert.",
                    "3. Breizh Café - Best crepes and galettes in Paris with quality ingredients.",
                    "4. Bouillon Chartier - Historic budget-friendly restaurant serving traditional French cuisine since 1896.",
                    "5. L'As du Fallafel - Famous street food spot in Le Marais for the best falafel in Paris."
                ],
                attractions: [
                    "1. Eiffel Tower - Iconic symbol of Paris; visit at night to see it sparkle on the hour.",
                    "2. Louvre Museum - World's largest art museum housing the Mona Lisa; enter through the less crowded Porte des Lions entrance.",
                    "3. Montmartre - Bohemian hilltop neighborhood with stunning city views from Sacré-Cœur Basilica.",
                    "4. Seine River Cruise - Relaxing way to see many landmarks from the water; sunset cruises are particularly beautiful.",
                    "5. Luxembourg Gardens - Beautiful park perfect for a picnic or people-watching on a sunny day."
                ]
            },
            'london': {
                hotels: [
                    "1. The Hoxton, Shoreditch - Trendy hotel with stylish rooms in East London (mid-range).",
                    "2. CitizenM Tower of London - Modern hotel with amazing views of the Tower of London (mid-range).",
                    "3. The Goring - Classic luxury hotel near Buckingham Palace with royal connections.",
                    "4. Premier Inn London County Hall - Reliable budget chain with excellent location near London Eye.",
                    "5. The Zetter Townhouse - Quirky boutique hotel with unique decor and excellent cocktail bar (mid-range)."
                ],
                restaurants: [
                    "1. Dishoom - Popular Indian restaurant serving Bombay-inspired cuisine; famous for their bacon naan roll breakfast.",
                    "2. Borough Market - Food market with numerous stalls; don't miss the grilled cheese from Kappacasein.",
                    "3. Padella - Small pasta restaurant with handmade pasta at reasonable prices; expect a queue.",
                    "4. Bao - Taiwanese restaurant known for their fluffy bao buns with various fillings.",
                    "5. The Wolseley - Grand European café-restaurant perfect for a special breakfast or afternoon tea."
                ],
                attractions: [
                    "1. British Museum - World-class museum with free entry; houses the Rosetta Stone and Egyptian mummies.",
                    "2. Tower of London - Historic castle housing the Crown Jewels; join a Yeoman Warder tour for fascinating stories.",
                    "3. Tate Modern - Contemporary art museum in a former power station; head to the viewing platform for panoramic views.",
                    "4. Buckingham Palace - Royal residence with the famous Changing of the Guard ceremony (check schedule before visiting).",
                    "5. Hyde Park - Expansive park perfect for a stroll; rent a rowboat on the Serpentine lake in summer."
                ]
            }
        };

        // Check if the message mentions a specific city
        let cityInfo = null;
        for (const city in cities) {
            if (lowerMessage.includes(city)) {
                cityInfo = {
                    name: city.charAt(0).toUpperCase() + city.slice(1),
                    data: cities[city]
                };
                break;
            }
        }

        // If we have city-specific information
        if (cityInfo) {
            // Hotel recommendations
            if (lowerMessage.includes('hotel') || lowerMessage.includes('stay') || lowerMessage.includes('accommodation') || lowerMessage.includes('place to sleep')) {
                return `Here are some recommended hotels in ${cityInfo.name}:\n\n${cityInfo.data.hotels.join('\n\n')}`;
            }

            // Restaurant recommendations
            if (lowerMessage.includes('restaurant') || lowerMessage.includes('food') || lowerMessage.includes('eat') || lowerMessage.includes('dining') || lowerMessage.includes('cuisine')) {
                return `Here are some recommended restaurants in ${cityInfo.name}:\n\n${cityInfo.data.restaurants.join('\n\n')}`;
            }

            // Attraction recommendations
            if (lowerMessage.includes('attraction') || lowerMessage.includes('see') || lowerMessage.includes('visit') || lowerMessage.includes('sight') || lowerMessage.includes('tour')) {
                return `Here are the top attractions to visit in ${cityInfo.name}:\n\n${cityInfo.data.attractions.join('\n\n')}`;
            }
        }

        // General travel questions
        if (lowerMessage.includes('flight') || lowerMessage.includes('fly') || lowerMessage.includes('plane')) {
            return "For flight information, make sure to check the 'Include flight information' box when generating your travel plan. This will show you available flights, prices, and booking options.";
        }

        if (lowerMessage.includes('hotel') || lowerMessage.includes('stay') || lowerMessage.includes('accommodation')) {
            return "Which city are you planning to visit? I can provide specific hotel recommendations for many popular destinations. Just ask something like 'recommend hotels in Paris' or 'where to stay in London'.";
        }

        if (lowerMessage.includes('budget') || lowerMessage.includes('cost') || lowerMessage.includes('money') || lowerMessage.includes('expensive')) {
            return "You can specify your budget in the form, and we'll tailor recommendations to fit within that range. This includes accommodations, activities, and dining options. For specific budget advice about a destination, just mention the city name.";
        }

        if (lowerMessage.includes('weather') || lowerMessage.includes('temperature') || lowerMessage.includes('climate')) {
            return "Your travel plan includes weather information for your destination during your travel dates. This helps you pack appropriately and plan outdoor activities. Which destination are you interested in learning about?";
        }

        if (lowerMessage.includes('food') || lowerMessage.includes('restaurant') || lowerMessage.includes('eat') || lowerMessage.includes('cuisine')) {
            return "I can recommend restaurants and local cuisine for many popular destinations. Just mention which city you're interested in, like 'restaurants in Paris' or 'where to eat in London'.";
        }

        if (lowerMessage.includes('activity') || lowerMessage.includes('attraction') || lowerMessage.includes('see') || lowerMessage.includes('visit') || lowerMessage.includes('do')) {
            return "I can suggest attractions and activities for many popular destinations. Just mention which city you're interested in, like 'attractions in Paris' or 'things to do in London'.";
        }

        if (lowerMessage.includes('transport') || lowerMessage.includes('get around') || lowerMessage.includes('travel') || lowerMessage.includes('commute')) {
            return "Your travel plan includes information on local transportation options at your destination. For specific advice about getting around a particular city, just mention the city name.";
        }

        if (lowerMessage.includes('thank')) {
            return "You're welcome! If you have any other questions about your travel plan or specific destinations, feel free to ask.";
        }

        if (lowerMessage.includes('hello') || lowerMessage.includes('hi') || lowerMessage.includes('hey')) {
            return "Hello! How can I help with your travel plans today? You can ask me about specific destinations, hotels, restaurants, attractions, or general travel advice.";
        }

        // Default response
        return "I'm here to help with your travel planning. For the most specific recommendations, please mention which city you're interested in. You can ask about hotels, restaurants, attractions, or any other aspect of your trip.";
    }

    travelForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Show travel plan section
        travelPlanSection.classList.remove('d-none');

        // Hide result container and show loading indicator
        resultContainer.classList.add('d-none');
        loadingIndicator.classList.remove('d-none');
        resultContainer.innerHTML = '';

        // Scroll to the travel plan section
        travelPlanSection.scrollIntoView({ behavior: 'smooth' });
        
        // Get form values
        const startDate = document.getElementById('start_date').value;
        const endDate = document.getElementById('end_date').value;

        // Format dates for display
        const formattedDates = formatDateRange(startDate, endDate);

        const formData = {
            source: document.getElementById('source').value,
            destination: document.getElementById('destination').value,
            dates: formattedDates,
            start_date: startDate,
            end_date: endDate,
            budget: document.getElementById('budget').value,
            travelers: document.getElementById('travelers').value,
            interests: document.getElementById('interests').value,
            include_flights: document.getElementById('include_flights').checked
        };
        
        // Send request to backend
        fetch('/generate_plan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading indicator
            loadingIndicator.classList.add('d-none');

            // Show result container
            resultContainer.classList.remove('d-none');

            if (data.success) {
                // Format and display the travel plan
                let formattedPlan = formatTravelPlan(data.plan);
                
                // Add flight information if available
                if (data.flight_data) {
                    // Store flight data in a global variable for the details modal
                    window.currentFlightData = data.flight_data;
                    
                    const flightInfo = formatFlightInfo(data.flight_data);
                    formattedPlan = `
                        <div class="flight-info-section mb-4">
                            ${flightInfo}
                        </div>
                        <div class="travel-plan-section">
                            <h2>Travel Plan</h2>
                            ${formattedPlan}
                        </div>
                    `;
                }
                
                // Show the result and hide the loading indicator
                loadingIndicator.classList.add('d-none');
                resultContainer.classList.remove('d-none');
                resultContainer.innerHTML = formattedPlan;
            } else {
                // Show error message
                loadingIndicator.classList.add('d-none');
                resultContainer.classList.remove('d-none');
                resultContainer.innerHTML = `
                    <div class="alert alert-danger">
                        <h4><i class="bi bi-exclamation-triangle-fill me-2"></i>Error</h4>
                        <p>${data.error}</p>
                        <p class="mt-3 mb-0">Please try again with different inputs.</p>
                    </div>
                `;
            }
        })
        .catch(error => {
            // Hide loading indicator and show result container with error
            loadingIndicator.classList.add('d-none');
            resultContainer.classList.remove('d-none');
            resultContainer.innerHTML = `
                <div class="alert alert-danger">
                    <h4><i class="bi bi-exclamation-triangle-fill me-2"></i>Network Error</h4>
                    <p>Failed to generate travel plan. Please check your internet connection and try again.</p>
                    <p class="mt-2"><strong>Technical details:</strong> ${error.message}</p>
                </div>
            `;
        });
    });
    
    // Function to format flight information
    function formatFlightInfo(flightData) {
        // Check for API errors
        if (flightData.error) {
            return `<div class="alert alert-warning">
                <p><strong>Flight Information Notice:</strong> ${flightData.error}</p>
                <p>Try checking the spelling or using a major city name instead.</p>
                <p>Examples: "New York", "London", "Tokyo", "Bangkok", "Sydney"</p>
            </div>`;
        }

        if (!flightData || !flightData.best_flights || flightData.best_flights.length === 0) {
            return '<p>No flight information available.</p>';
        }

        // Get the top 3 flights or fewer if less are available
        const topFlights = flightData.best_flights.slice(0, 3);
        
        // Create a booking URL using the booking token
        const createBookingUrl = (flight) => {
            // In a real implementation, this would use the booking_token to create a direct booking link
            // For demonstration purposes, we'll create a Google Flights URL
            const sourceId = flight.flights[0].departure_airport.id;
            const destId = flight.flights[flight.flights.length - 1].arrival_airport.id;
            const date = flight.flights[0].departure_airport.time.split(' ')[0];
            return `https://www.google.com/travel/flights?q=Flights%20to%20${destId}%20from%20${sourceId}%20on%20${date}`;
        };

        // Start with a header section
        let flightHtml = `
            <div class="flight-options mb-2">
                <h3>Flight Options</h3>
                <p class="text-muted">One-way flights from ${flightData.user_source} to ${flightData.user_destination}</p>
                
                <div class="table-responsive">
                    <table class="table table-bordered table-hover flight-table">
                        <thead class="table-primary">
                            <tr>
                                <th>Airline</th>
                                <th>Departure</th>
                                <th>Arrival</th>
                                <th>Duration</th>
                                <th>Stops</th>
                                <th>Price</th>
                                <th>Actions</th>
                                <th>Book Now</th>
                            </tr>
                        </thead>
                        <tbody>
        `;

        // Add each flight as a row in the table
        topFlights.forEach((flight, index) => {
            const firstFlight = flight.flights[0];
            const lastFlight = flight.flights[flight.flights.length - 1];
            const numStops = flight.flights.length - 1;
            const bookingUrl = createBookingUrl(flight);
            
            // Format departure time
            const depTime = firstFlight.departure_airport.time.split(' ')[1];
            const depDate = new Date(firstFlight.departure_airport.time);
            const depDateStr = depDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
            
            // Format arrival time
            const arrTime = lastFlight.arrival_airport.time.split(' ')[1];
            const arrDate = new Date(lastFlight.arrival_airport.time);
            const arrDateStr = arrDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
            
            // Create airline display with logo
            const airlineDisplay = flight.flights.length > 1 
                ? `<div><img src="${flight.airline_logo}" alt="${flight.flights[0].airline}" width="20" height="20"> Multiple Airlines</div>`
                : `<div><img src="${flight.airline_logo}" alt="${flight.flights[0].airline}" width="20" height="20"> ${flight.flights[0].airline}</div>`;
            
            // Create stops display
            let stopsDisplay = numStops === 0 
                ? '<span class="badge bg-success">Nonstop</span>' 
                : `<span class="badge bg-warning text-dark">${numStops} stop${numStops > 1 ? 's' : ''}</span>`;
                
            // Add layover information if available
            if (flight.layovers && flight.layovers.length > 0) {
                stopsDisplay += '<div class="small text-muted mt-1">';
                flight.layovers.forEach(layover => {
                    stopsDisplay += `${layover.id} (${formatDuration(layover.duration)})<br>`;
                });
                stopsDisplay += '</div>';
            }
            
            flightHtml += `
                <tr>
                    <td class="align-middle">
                        <div class="d-flex align-items-center">
                            <img src="${flight.airline_logo}" alt="${flight.flights[0].airline}" width="24" height="24" class="me-2">
                            <div>
                                <div class="fw-bold">${flight.flights.length > 1 ? 'Multiple' : flight.flights[0].airline}</div>
                                <div class="small text-muted">${flight.flights[0].flight_number}${flight.flights.length > 1 ? ' +' : ''}</div>
                            </div>
                        </div>
                    </td>
                    <td class="align-middle">
                        <div class="fw-bold">${depTime}</div>
                        <div class="small text-muted">${depDateStr}</div>
                        <div class="small text-muted">${firstFlight.departure_airport.id}</div>
                    </td>
                    <td class="align-middle">
                        <div class="fw-bold">${arrTime}</div>
                        <div class="small text-muted">${arrDateStr}</div>
                        <div class="small text-muted">${lastFlight.arrival_airport.id}</div>
                    </td>
                    <td class="align-middle">
                        <div class="fw-bold">${formatDuration(flight.total_duration)}</div>
                        ${flight.overnight ? '<div class="small text-danger"><i class="bi bi-moon-fill"></i> Overnight</div>' : ''}
                    </td>
                    <td class="align-middle">
                        ${stopsDisplay}
                    </td>
                    <td class="align-middle">
                        <div class="fw-bold text-primary">$${flight.price}</div>
                        <div class="small text-muted">per person</div>
                    </td>
                    <td class="align-middle">
                        <button class="btn btn-sm btn-outline-primary d-block mb-1" onclick="showFlightDetails(${index})">
                            <i class="bi bi-info-circle"></i> Details
                        </button>
                    </td>
                    <td class="align-middle">
                        <a href="https://www.google.com/travel/flights?q=Flights%20to%20${lastFlight.arrival_airport.id}%20from%20${firstFlight.departure_airport.id}%20on%20${firstFlight.departure_airport.time.split(' ')[0]}"
                           target="_blank" class="btn btn-sm btn-success d-block">
                            <i class="bi bi-airplane"></i> Google Flights
                        </a>
                    </td>
                </tr>
            `;
        });

        // Close the table and add a note about the SERP API
        flightHtml += `
                        </tbody>
                    </table>
                </div>
            </div>
        `;

        return flightHtml;
    }

    // Function to format duration from minutes to hours and minutes
    function formatDuration(minutes) {
        const hours = Math.floor(minutes / 60);
        const mins = minutes % 60;
        return `${hours}h ${mins}m`;
    }
    
    // Function to initialize autocomplete for location inputs
    function initializeAutocomplete() {
        // Fetch all available locations from the server
        fetch('/api/locations')
            .then(response => response.json())
            .then(locations => {
                // Initialize jQuery UI Autocomplete for source input
                $(sourceInput).autocomplete({
                    source: locations,
                    minLength: 2,
                    select: function(event, ui) {
                        // Set the input value to the selected location
                        $(this).val(ui.item.label.split(' (')[0]);
                        return false;
                    }
                }).autocomplete("instance")._renderItem = function(ul, item) {
                    // Custom rendering of autocomplete items
                    return $("<li>")
                        .append(`<div class="location-item">
                                    <span class="location-name">${item.label}</span>
                                    <span class="location-airport">${item.airport}</span>
                                </div>`)
                        .appendTo(ul);
                };
                
                // Initialize jQuery UI Autocomplete for destination input
                $(destinationInput).autocomplete({
                    source: locations,
                    minLength: 2,
                    select: function(event, ui) {
                        // Set the input value to the selected location
                        $(this).val(ui.item.label.split(' (')[0]);
                        return false;
                    }
                }).autocomplete("instance")._renderItem = function(ul, item) {
                    // Custom rendering of autocomplete items
                    return $("<li>")
                        .append(`<div class="location-item">
                                    <span class="location-name">${item.label}</span>
                                    <span class="location-airport">${item.airport}</span>
                                </div>`)
                        .appendTo(ul);
                };
            })
            .catch(error => {
                console.error('Error fetching locations:', error);
            });
    }

    // Function to show detailed flight information
    window.showFlightDetails = function(flightIndex) {
        // Get the flight data from the global variable
        if (!window.currentFlightData || !window.currentFlightData.best_flights || !window.currentFlightData.best_flights[flightIndex]) {
            alert('Flight details not available');
            return;
        }
        
        const flight = window.currentFlightData.best_flights[flightIndex];
        
        // Create a modal with flight details
        let modalHtml = `
            <div class="modal fade" id="flightDetailsModal" tabindex="-1" aria-labelledby="flightDetailsModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <div class="modal-header bg-primary text-white">
                            <h5 class="modal-title" id="flightDetailsModalLabel">
                                <i class="bi bi-airplane"></i> Flight Details
                            </h5>
                            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="card mb-3">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col-md-8">
                                            <h5 class="card-title">
                                                ${flight.flights[0].departure_airport.name} (${flight.flights[0].departure_airport.id}) 
                                                <i class="bi bi-arrow-right"></i> 
                                                ${flight.flights[flight.flights.length-1].arrival_airport.name} (${flight.flights[flight.flights.length-1].arrival_airport.id})
                                            </h5>
                                            <p class="text-muted mb-0">
                                                ${flight.flights.length > 1 ? 
                                                    `${flight.flights.length - 1} stop${flight.flights.length > 2 ? 's' : ''} · ` : 
                                                    'Nonstop · '}
                                                ${formatDuration(flight.total_duration)} total
                                                ${flight.overnight ? ' · <i class="bi bi-moon-fill"></i> Overnight flight' : ''}
                                            </p>
                                        </div>
                                        <div class="col-md-4 text-md-end">
                                            <h4 class="text-primary mb-0">$${flight.price}</h4>
                                            <p class="text-muted small">per person</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <h6 class="mb-3"><i class="bi bi-calendar-event"></i> Flight Itinerary</h6>

                            <div class="flight-segments">
        `;
        
        // Add each flight segment
        flight.flights.forEach((segment, idx) => {
            modalHtml += `
                <div class="card mb-3 border-primary">
                    <div class="card-header bg-light">
                        <div class="d-flex align-items-center">
                            <img src="${segment.airline_logo}" alt="${segment.airline}" width="30" height="30" class="me-2">
                            <div>
                                <span class="fw-bold">${segment.airline} ${segment.flight_number}</span>
                                <span class="badge bg-info ms-2">${segment.travel_class}</span>
                            </div>
                            <span class="ms-auto text-muted">${segment.airplane}</span>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="row align-items-center">
                            <div class="col-md-5">
                                <div class="d-flex align-items-center">
                                    <div class="flight-icon bg-primary text-white me-3">
                                        <i class="bi bi-airplane-fill"></i>
                                    </div>
                                    <div>
                                        <div class="fw-bold fs-5">${segment.departure_airport.time.split(' ')[1]}</div>
                                        <div>${segment.departure_airport.name}</div>
                                        <div class="text-primary">${segment.departure_airport.id}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-2 text-center">
                                <div class="flight-duration">
                                    <div class="fw-bold">${formatDuration(segment.duration)}</div>
                                    <div class="flight-line">
                                        <i class="bi bi-airplane flight-icon-line"></i>
                                    </div>
                                    ${segment.overnight ? '<div class="text-danger small"><i class="bi bi-moon-fill"></i> Overnight</div>' : ''}
                                </div>
                            </div>
                            <div class="col-md-5">
                                <div class="d-flex align-items-center">
                                    <div class="flight-icon bg-success text-white me-3">
                                        <i class="bi bi-geo-alt-fill"></i>
                                    </div>
                                    <div>
                                        <div class="fw-bold fs-5">${segment.arrival_airport.time.split(' ')[1]}</div>
                                        <div>${segment.arrival_airport.name}</div>
                                        <div class="text-primary">${segment.arrival_airport.id}</div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="mt-4 pt-3 border-top">
                            <h6 class="mb-3"><i class="bi bi-info-circle"></i> Flight Information</h6>
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="mb-3">
                                        <div class="text-muted small">Aircraft</div>
                                        <div>${segment.airplane}</div>
                                    </div>
                                    <div class="mb-3">
                                        <div class="text-muted small">Seat</div>
                                        <div>${segment.travel_class} (${segment.legroom})</div>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="mb-3">
                                        <div class="text-muted small">Flight Duration</div>
                                        <div>${formatDuration(segment.duration)}</div>
                                    </div>
                                    <div class="mb-3">
                                        <div class="text-muted small">Flight Number</div>
                                        <div>${segment.flight_number}</div>
                                    </div>
                                </div>
                            </div>
                            
                            <h6 class="mb-2"><i class="bi bi-stars"></i> Amenities</h6>
                            <div class="row">
            `;
            
            // Add amenities
            segment.extensions.forEach(ext => {
                modalHtml += `
                    <div class="col-md-6 mb-2">
                        <div class="d-flex align-items-center">
                            <i class="bi bi-check-circle-fill text-success me-2"></i>
                            <span class="small">${ext}</span>
                        </div>
                    </div>`;
            });
            
            modalHtml += `
                            </div>
                        </div>
                    </div>
                </div>
            `;
            
            // Add layover information if this is not the last segment
            if (idx < flight.flights.length - 1 && flight.layovers && flight.layovers[idx]) {
                const layover = flight.layovers[idx];
                modalHtml += `
                    <div class="layover-info text-center mb-4">
                        <div class="layover-line"></div>
                        <div class="layover-badge">
                            <i class="bi bi-clock-history text-warning me-1"></i>
                            <span class="fw-bold">${formatDuration(layover.duration)}</span> layover in 
                            <span class="fw-bold">${layover.name}</span> (${layover.id})
                        </div>
                        <div class="small text-muted mt-1">Time to change planes and stretch your legs</div>
                    </div>
                `;
            }
        });
        
        // Add carbon emissions information
        if (flight.carbon_emissions) {
            const emissionClass = flight.carbon_emissions.difference_percent < 0 ? 'text-success' : 
                                 flight.carbon_emissions.difference_percent > 10 ? 'text-danger' : 'text-warning';
            const emissionIcon = flight.carbon_emissions.difference_percent < 0 ? 'bi-leaf-fill' : 
                               flight.carbon_emissions.difference_percent > 10 ? 'bi-exclamation-triangle-fill' : 'bi-info-circle-fill';
            
            modalHtml += `
                <div class="card mt-4 border-${emissionClass.replace('text-', '')}">
                    <div class="card-header bg-light">
                        <h6 class="mb-0"><i class="bi ${emissionIcon} ${emissionClass} me-2"></i> Environmental Impact</h6>
                    </div>
                    <div class="card-body">
                        <div class="row align-items-center">
                            <div class="col-md-6">
                                <div class="d-flex align-items-center mb-2">
                                    <div class="me-3">
                                        <span class="fs-4 fw-bold ${emissionClass}">
                                            ${flight.carbon_emissions.difference_percent > 0 ? '+' : ''}${flight.carbon_emissions.difference_percent}%
                                        </span>
                                    </div>
                                    <div>
                                        <div>compared to average</div>
                                        <div class="small text-muted">for this route</div>
                                    </div>
                                </div>
                                <div class="progress" style="height: 10px;">
                                    <div class="progress-bar ${emissionClass.replace('text-', 'bg-')}" 
                                         role="progressbar" 
                                         style="width: ${Math.min(100, Math.max(0, 100 - flight.carbon_emissions.difference_percent))}%"></div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="text-center">
                                    <div class="small text-muted">Carbon Emissions</div>
                                    <div class="d-flex justify-content-center align-items-baseline">
                                        <span class="fs-4 fw-bold">${Math.round(flight.carbon_emissions.this_flight/1000)}</span>
                                        <span class="ms-1">kg CO₂</span>
                                    </div>
                                    <div class="small text-muted">per passenger</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }
        
        // Close the modal
        modalHtml += `
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                                <i class="bi bi-x-circle me-1"></i> Close
                            </button>
                            <a href="https://www.google.com/travel/flights?q=Flights%20to%20${flight.flights[flight.flights.length-1].arrival_airport.id}%20from%20${flight.flights[0].departure_airport.id}%20on%20${flight.flights[0].departure_airport.time.split(' ')[0]}"
                               target="_blank" class="btn btn-success">
                                <i class="bi bi-airplane me-1"></i> Book on Google Flights ($${flight.price})
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        // Add the modal to the page
        const modalContainer = document.createElement('div');
        modalContainer.innerHTML = modalHtml;
        document.body.appendChild(modalContainer);
        
        // Show the modal
        const modal = new bootstrap.Modal(document.getElementById('flightDetailsModal'));
        modal.show();
        
        // Remove the modal from the DOM when it's hidden
        document.getElementById('flightDetailsModal').addEventListener('hidden.bs.modal', function () {
            document.body.removeChild(modalContainer);
        });
    };
    
    // Function to format date range in a user-friendly way
    function formatDateRange(startDate, endDate) {
        if (!startDate || !endDate) return '';
        
        const start = new Date(startDate);
        const end = new Date(endDate);
        
        // Options for date formatting
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        
        // Format the dates
        const formattedStart = start.toLocaleDateString('en-US', options);
        const formattedEnd = end.toLocaleDateString('en-US', options);
        
        return `${formattedStart} to ${formattedEnd}`;
    }
    
    // Function to format the travel plan with some basic Markdown-like parsing
    function formatTravelPlan(planText) {
        // Replace markdown headings with HTML headings
        let formatted = planText
            .replace(/^# (.*$)/gm, '<h2>$1</h2>')
            .replace(/^## (.*$)/gm, '<h3>$1</h3>')
            .replace(/^### (.*$)/gm, '<h4>$1</h4>')
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/- (.*$)/gm, '<li>$1</li>');
        
        // Wrap lists in <ul> tags
        formatted = formatted.replace(/<li>.*?<\/li>/gs, match => {
            return '<ul>' + match + '</ul>';
        });
        
        // Replace double newlines with paragraph breaks
        formatted = formatted.replace(/\n\n/g, '</p><p>');
        
        // Wrap the whole thing in a paragraph
        formatted = '<p>' + formatted + '</p>';
        
        // Fix any double <ul> tags or other issues
        formatted = formatted
            .replace(/<\/ul><ul>/g, '')
            .replace(/<\/p><p><ul>/g, '</p><ul>')
            .replace(/<\/ul><p>/g, '</ul><p>');
        
        return formatted;
    }
});