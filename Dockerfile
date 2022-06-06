# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY . .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

RUN chmod +x run_server.sh

CMD ["./run_server.sh"]
