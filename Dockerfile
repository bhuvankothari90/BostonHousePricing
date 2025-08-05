# Creating the Base Image of the Environment
FROM python:3.7
# Copying all the files from the project folder to the app (docker folder destination)  
COPY . /app
# Selecting the destination as the Working DIR folder for docker actions
WORKDIR /app
# Running the requirements
RUN pip install -r requirements.txt
# Assigning a Port using Expose function
EXPOSE $PORT
# gunicorn helps to run the complete project inside the DOcker or Heroku
# also assigning the workers to divide the requests and work efficiently
# first app denotes file name (in our case app.py) second name app denotes the app name which we have kept as @app in the file
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app