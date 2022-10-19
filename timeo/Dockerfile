FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /app

RUN pip install Flask

# Copy the current directory contents into the container at /app
COPY app.py app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
