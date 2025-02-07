# Use Python base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Clone the repository
RUN git clone https://github.com/stephengpope/no-code-architects-toolkit.git .

# Install Python dependencies
RUN pip install -r requirements.txt

# Replace the s3_toolkit.py with our modified version
COPY s3_toolkit_fixed.py /app/services/s3_toolkit.py

# Expose port
EXPOSE 3000

# Command to run the application
CMD ["python", "app.py"]
