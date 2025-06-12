FROM python:3.10.0

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory to the root of the project
WORKDIR /

# Update the CMD to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]