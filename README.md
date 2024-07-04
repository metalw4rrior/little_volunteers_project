# little project
--to build it:
docker build -t my-app-image .
--to start it:
docker run -d -p 8000:8000 --name my-app-container my-app-image
--to check it:
docker logs my-app-container
