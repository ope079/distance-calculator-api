# Simple API to connect to Google Maps Endpoint

- This API is a post endpoint that takes a  JSON in the following formart
    - {
        origin: origin,
        destination: destination,
        transit_mode: transit_mode,
        unit: unit
    }
   and returns a JSON with the distance and duration of travel between two locations
   provided, the origin, and the destination. It also takes a transit_mode and unit of 
   measurement, being either imperial (miles) or metric (kilometers)

- The application is a fast api python app that is run via docker.

- Below are the steps to run this application (please be aware that a google api key
  with distance matrix api enabled needs to be provided by the user in order for this to run).
    - In the terminal run "docker build -t distancecalcapp ." to build the application
    - The run "docker run -d --name mycontainer -p 8000:8000 distancecalcapp" to start the application
    - Go to "http://127.0.0.1:8000/docs" on the web browser to open the swagger page for the application
    - Input the JSON in the above formart into the "/distance" endpoint.

