 
FROM python:3.9 

WORKDIR /code 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./app /code/app
COPY ./tests /code/tests

EXPOSE 8000 
 
CMD ["uvicorn", "app.main:app", "--host", "172.17.0.2", "--port", "8000"]

