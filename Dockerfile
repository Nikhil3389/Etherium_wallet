FROM python:3.7
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["/app/manage.py", "runserver"]



