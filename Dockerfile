# Use the Python 3 Slim Bookworm base image
FROM python:3.11-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install the required Python libraries
RUN pip install -r requirements.txt

# Expose the port for the Streamlit app
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "Home.py"]
