FROM python:3.10-slim
# set a directory for the app
WORKDIR /usr/src/app
# copy all the files to the container
COPY source dest
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "./app.py"]

