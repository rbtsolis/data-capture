FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install pip --upgrade
RUN pip install -r requirements.txt

# Run pytest when the container launches
CMD ["pytest"]

# To run the file just uncomment the next line and uncomment the last 3 lines on the data_capture.py file
# CMD [python data_capture.py]