# Ebike-finder
## Overview
**Ebike-finder** is a machine learning-powered service that predicts the availability of e-bikes at Bluebikes stations across Boston. 
The service leverages real-time and historical data to forecast bike availability, helping users plan their trips more efficiently by ensuring they have access to bikes when and where they need them. 
This project is hosted on Hugging Face Spaces and uses Gradio as the frontend interface.

You can access the service here: [Ebike-finder on Hugging Face](https://huggingface.co/spaces/UdayG98/ebike-finder).

## Key Features
- **Real-Time Predictions**: Instantly predicts the availability of e-bikes at a selected Bluebikes station.
- **User-Friendly Interface**: The interface, built with Gradio, allows users to easily select a station and view predictions.
- **Scalable & Fast**: Processes incoming data and delivers results with minimal delay, ensuring up-to-date information.
- **Historical Insights**: Incorporates historical data to improve prediction accuracy.

## Use Case
The service is ideal for daily commuters, occasional riders, or tourists who rely on Boston's Bluebikes system for transportation. By predicting e-bike availability, users can plan ahead and avoid situations where bikes may be unavailable at the station closest to them.

### Example Use Case:
- A user who commutes from **Allston** to **Boston University** can use the Ebike-finder service to check the predicted e-bike availability at the station near **Allston** before leaving home. This ensures that an e-bike will be available for their ride, improving commute efficiency.

## How It Works
1. **Data Collection**: The service collects real-time station data from the Bluebikes GBFS feed, including information such as station location, bike availability, and e-bike status.
2. **Machine Learning Model**: A custom LSTM model predicts the availability of e-bikes at a given station using the collected data.
3. **User Input**: Users select their station of interest through an interactive interface.
4. **Prediction**: The service generates a prediction on e-bike availability for the selected station.

## Installation & Setup (For Developers)
To run the service locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:UdayGarg/ebike-finder.git
