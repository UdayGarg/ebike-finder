import gradio as gr
import json
from fuzzywuzzy import process
import requests

url = "https://csrlc421nb.execute-api.us-east-2.amazonaws.com/dev/predict"


# Load stations data from the JSON file
with open('stations.json') as f:
    stations_data = json.load(f)

stations = stations_data['stations']

# Create a mapping from station name to station ID
station_name_to_id = {station['name']: station['station_id'] for station in stations}

# Define a function to find the closest matching station
def find_station(user_input):
    # Use fuzzy matching to find the top 3 closest station names
    matches = process.extract(user_input, station_name_to_id.keys(), limit=3)
    
    # If the best match has a score of 90 or above, we assume it's a good match
    if matches[0][1] >= 90:
        best_match = matches[0][0]
        station_id = station_name_to_id[best_match]

        response = requests.get(url, params={"station_id": station_id})

        return response.json()
    
    # If ambiguous, return suggestions
    suggestions = [match[0] for match in matches]
    return f"Did you mean one of these stations? {', '.join(suggestions)}"

# Create Gradio interface
station_input = gr.Textbox(label="Enter Station Name")  # Use gr.Textbox for input
output_text = gr.Textbox(label="Station ID or Suggestions")  # Use gr.Textbox for output

# Launch the Gradio interface
gr.Interface(fn=find_station, inputs=station_input, outputs=output_text, title="Ebike Finder").launch()