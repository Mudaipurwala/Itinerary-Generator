# Use Python 3.7 runtime
FROM python:3.7

# Set the working directory to 
WORKDIR /Documents/Projects/itinerary-generator/

# Copy script and the source folder to 
COPY itinerary.py ./

# Add configuration and requirements.txt 
ADD config.yaml config.yaml
ADD requirements.txt requirements.txt 

# Install any needed packages specified in requirements.txt
RUN pip3.7 install -r requirements.txt

CMD ["python3.7", "./itinerary.py"]