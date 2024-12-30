# segmentation-app

Run the Flask API

`python app.py`

Test the API with curl

`curl -X POST -F "file=@path/to/your/image.jpg" http://127.0.0.1:5001/segment --output segmented_output.png`

Running the Flask API using Docker
From Docker Hub:

`docker pull purukoli/flask-segmentation-app:latest`

From GitHub Container Registry:

`docker pull ghcr.io/pkoli437/segmentation-app/flask-segmentation-app:latest`

Run the Docker container

`docker run --gpus all -p 5001:5001 purukoli/flask-segmentation-app:latest`     (for dockerhub)

Or, if using GitHub Container Registry:

`docker run --gpus all -p 5001:5001 ghcr.io/pkoli437/segmentation-app/flask-segmentation-app:latest`    (for github container)

Test the API using same curl for Docker  

`curl -X POST -F "file=@path/to/your/image.jpg" http://localhost:5001/segment --output segmented_output.png` (Curl command to send requests and interact with API)
