FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# RUN python -m textblob.download_corpora
EXPOSE 8080
CMD [ "fastapi_app.py" ]
ENTRYPOINT [ "python" ]