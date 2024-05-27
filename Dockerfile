# Base image
FROM python:3.11-slim-bookworm

# Set working directory
WORKDIR /app

# Copy in the requirements file
COPY requirements.txt ./

# Install Streamlit and libraries from requirements.txt
RUN pip install -r requirements.txt

# Copy application files
COPY . /app

# Expose port 8501 for Streamlit
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "Home.py"]
