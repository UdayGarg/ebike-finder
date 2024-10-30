import gradio as gr
import json
from fuzzywuzzy import process
import requests
from datetime import datetime

url = "https://csrlc421nb.execute-api.us-east-2.amazonaws.com/dev/predict"

# Load stations data from the JSON file
with open('stations.json') as f:
    stations_data = json.load(f)

stations = stations_data['stations']

# Create a mapping from station name to station ID
station_name_to_id = {station['name']: station['station_id'] for station in stations}

# Define a function to find the closest matching station
def find_station(user_input=None, dropdown_selection=None):
    # Determine which input was provided by the user
    input_station = dropdown_selection if dropdown_selection else user_input
    
    if not input_station:
        return "Please enter a station name or select one from the dropdown."
    
    # Use fuzzy matching to find the top 3 closest station names
    matches = process.extract(input_station, station_name_to_id.keys(), limit=3)
    
    # If the best match has a score of 90 or above, we assume it's a good match
    if matches[0][1] >= 90:
        best_match = matches[0][0]
        station_id = station_name_to_id[best_match]

        # Make a GET request to the API with the station_id
        response = requests.get(url, params={"station_id": station_id})
        data = response.json()
        print(data)
        # Prettify the output
        if data:
            prettified_output = f"""
**Station Information**

- **Station ID**: {data.get('station_id', 'N/A')}
- **Name**: {data.get('name', 'N/A')}
- **Location**: ({data.get('latitude', 'N/A')}, {data.get('longitude', 'N/A')})
- **Capacity**: {data.get('capacity', 'N/A')}
- **E-bike Availability**: {data.get('ebike_availability', 'N/A')}
- **E-bike Range**: {data.get('ebike_range', 'N/A')}
- **Prediction in 30 mins**: {data.get('prediction_30_min', 'N/A')}
- **Confidence**: {data.get('confidence', 'N/A')}
"""
        else:
            prettified_output = "Sorry, there was an issue retrieving the data."

        return prettified_output
    
    # If ambiguous, return suggestions
    suggestions = [match[0] for match in matches]
    return f"Did you mean one of these stations? {', '.join(suggestions)}"

# Create Gradio interface
station_input = gr.Textbox(label="Enter Station Name (optional)")
station_dropdown = gr.Dropdown(choices=list(station_name_to_id.keys()), label="Or Select a Station", interactive=True)
output_text = gr.Markdown(label="Station Information")

# Launch the Gradio interface
gr.Interface(
    fn=find_station, 
    inputs=[station_input, station_dropdown], 
    outputs=output_text, 
    title="E-bike Finder"
).launch()