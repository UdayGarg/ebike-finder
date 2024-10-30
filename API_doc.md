Here's the combined API documentation as requested:

---

# Bluebike E-bike Service API Documentation

## Base URL
```
https://csrlc421nb.execute-api.us-east-2.amazonaws.com/dev
```

## Authentication
This API does not require authentication. It is publicly accessible via the endpoints provided below.

---

### **Endpoint: `/predict`**

#### Description:
The `/predict` endpoint provides predictions about e-bike availability at a specified station. You must provide the `station_id` as a query parameter.

#### HTTP Method:
`GET`

#### Request:

##### Query Parameters:
- `station_id` (required): The ID of the station for which you want to predict e-bike availability. 

##### Example Request:
```
GET /predict?station_id=123
```

##### Headers:
- `Accept: application/json`

#### Response:

##### Success Response (200 OK):
```json
{
  "statusCode": 200,
  "body": "{\"message\":\"No E-bikes available at this moment. I predict that e-bikes will be available in the next 30 minutes at East Somerville Library (Broadway and Illinois) with a High confidence level.\"}",
  "headers": {
    "Content-Type": "application/json"
  }
}
```

##### Error Responses:

- **400 Bad Request**: If the `station_id` query parameter is missing or empty.
  ```json
  {
    "statusCode": 400,
    "body": "{\"error\": \"station_id query parameter is required\"}",
    "headers": {
      "Content-Type": "application/json"
    }
  }
  ```

- **500 Internal Server Error**: If there is an issue processing the prediction.
  ```json
  {
    "statusCode": 500,
    "body": "{\"error\": \"Unable to process the request\"}",
    "headers": {
      "Content-Type": "application/json"
    }
  }
  ```

---

### **Endpoint: `/stations`**

#### Description:
The `/stations` endpoint returns a list of all available bike stations, including their name, location (latitude and longitude), and station ID.

#### HTTP Method:
`GET`

#### Request:

##### Example Request:
```
GET /stations
```

##### Headers:
- `Accept: application/json`

#### Response:

##### Success Response (200 OK):
```json
{
  "statusCode": 200,
  "body": "{\"stations\":[{\"latitude\":42.35352778,\"longitude\":-71.05622222,\"name\":\"High St at Federal St\",\"station_id\":1},{\"latitude\":42.349589423682445,\"longitude\":-71.0794677917329,\"name\":\"Boylston St at Exeter St\",\"station_id\":2}]}"
}
```

##### Error Response:
- **500 Internal Server Error**: If there is an issue retrieving the station data.
  ```json
  {
    "error": "Unable to fetch station data"
  }
  ```

---

## Rate Limiting
There are no explicit rate limits for this API.

---

## Status Codes:
- **200 OK**: The request was successful.
- **400 Bad Request**: The request was invalid.
- **500 Internal Server Error**: The server encountered an error while processing the request.
