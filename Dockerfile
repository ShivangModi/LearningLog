FROM python:3.11

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /LearningLog

# Set the working directory to /LearningLog
WORKDIR /LearningLog

# Copy the current directory contents into the container at /music_service
ADD . /LearningLog/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
