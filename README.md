# Ebike-finder

## Overview
**Ebike-finder** is a machine learning-powered service that predicts the availability of e-bikes at Bluebikes stations across Boston. The service leverages real-time and historical data to forecast bike availability, helping users plan their trips more efficiently by ensuring they have access to bikes when and where they need them. 

This project is hosted on Hugging Face Spaces and uses Gradio as the frontend interface. You can access the service here: [Ebike-finder on Hugging Face](https://huggingface.co/spaces/UdayG98/ebike-finder).

## Key Features
- **Real-Time Predictions**: Instantly predicts the availability of e-bikes at a selected Bluebikes station.
- **User-Friendly Interface**: The interface, built with Gradio, allows users to easily select a station and view predictions.
- **Scalable & Fast**: Processes incoming data and delivers results with minimal delay, ensuring up-to-date information.
- **Historical Insights**: Incorporates historical data to improve prediction accuracy.

## Use Case
The service is ideal for daily commuters, occasional riders, or tourists who rely on Boston's Bluebikes system for transportation. By predicting e-bike availability, users can plan ahead and avoid situations where bikes may be unavailable at the station closest to them.

### Example Use Case:
A user commuting from **Allston** to **Boston University** can use Ebike-finder to check the predicted availability of e-bikes at the station near **Allston** before leaving home, ensuring an e-bike will be available for their ride, thus improving commute efficiency.

## Architecture

### Backend (Powered by AWS)

The backend infrastructure is designed for scalability, real-time processing, and reliability. It leverages AWS services to handle the data pipeline, model predictions, and API interactions.

1. **Data Collection**:
   - **AWS Lambda Functions**: A Lambda function is responsible for pulling real-time data from the Bluebikes GBFS feed, which includes station information and e-bike availability. 
   - **S3 Data Storage**: The data fetched by Lambda is stored in an AWS S3 bucket, ensuring that the real-time and historical data are both readily available.

2. **Data Processing**:
   - **EC2 Instance**: A virtual server on AWS EC2 processes the data stored in S3 and maintains an **SQLite3 database** to manage structured information about station and e-bike availability. 
   - **XGBoost Model**: The machine learning model for predicting e-bike availability is an XGBoost model, which is optimized for this task. The model is deployed on the EC2 instance for real-time predictions.

3. **Archiving**:
   - The data is periodically moved from the main S3 bucket to an archival bucket using another Lambda function. This ensures historical data is safely stored and can be retrieved in the event of a system failure.

4. **API Gateway**:
   - **AWS API Gateway**: The API Gateway facilitates communication between the Gradio frontend and the backend hosted on EC2. This allows users to interact with the service by selecting stations and receiving predictions in real time.

### Frontend (Gradio Interface)
The frontend interface is built with Gradio and hosted on Hugging Face Spaces. Users can:
- Select a Bluebikes station from a dropdown menu.
- View the predicted e-bike availability for that station based on the machine learning model.
  
The interface is simple and intuitive, ensuring a smooth experience for all users.

## How It Works
1. **Data Collection**: Real-time station data (including bike availability, e-bike status, and station location) is collected from the Bluebikes GBFS feed and stored in an AWS S3 bucket.
2. **Machine Learning Model**: An XGBoost model trained on historical data is used to predict the future availability of e-bikes at each station.
3. **User Input**: Users select a station of interest through the Gradio interface.
4. **Prediction**: The backend processes the input, generates a prediction using the machine learning model, and returns the result to the user through the Gradio interface.

## Installation & Setup (For Developers)

To run the service locally, follow these steps:

### Prerequisites
- Python 3.8 or later
- AWS credentials configured for S3 and Lambda access
- Hugging Face and Gradio accounts (for hosting, if desired)

### Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:UdayGarg/ebike-finder.git