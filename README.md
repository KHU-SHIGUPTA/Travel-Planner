# Travel Planner 

A travel planning application powered by Google's Gemini 1.5 Flash AI model. This application helps users plan their trips by generating personalized travel itineraries based on their preferences.

## Features

- Generate detailed travel plans based on user inputs
- Personalized recommendations for accommodations, attractions, and activities
- Budget-conscious suggestions
- Day-by-day itinerary planning
- Local food and cultural recommendations
- Travel tips specific to the destination

## User Inputs

The application collects the following information from users:
- Source location
- Destination
- Travel dates
- Budget
- Number of travelers
- Interests and preferences

## Technology Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **AI Model**: Google Gemini 1.5 Flash

## Setup and Installation

1. Clone the repository:
```
git clone <repository-url>
cd travel-planner-ai
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
python app.py
```

5. Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

## Project Structure

```
travel-planner-ai/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/                 # Static files
│   ├── css/
│   │   └── style.css       # Custom CSS styles
│   └── js/
│       └── script.js       # Frontend JavaScript
└── templates/
    └── index.html          # Main HTML template
```

## API Key

The application uses the Gemini 1.5 Flash model. The API key is already included in the code for demonstration purposes. In a production environment, it's recommended to use environment variables to store sensitive information.

