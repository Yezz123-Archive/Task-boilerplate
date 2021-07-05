#Use Python 3.6 as a base image
FROM python:3.6

# Copy contents into image
COPY . .

# install pip dependencies from requirements file
RUN pip3 install -r requirements.txt

#Add ENV var
ENV PASSWORD="${PASSWORD}"

# Expose correct port
EXPOSE 5000

# Create an entrypoint
ENTRYPOINT ["python3", "app.py"]
