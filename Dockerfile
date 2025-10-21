FROM python:3.9-slim
WORKDIR /usr/src/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Make sure ffmpeg is installed
RUN apt-get update && apt-get install -y ffmpeg

# Copy in the source code
COPY . .

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["python", "main.py"]
