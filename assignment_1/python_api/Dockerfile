FROM python:3.8-slim-buster
WORKDIR /python_api
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=api.py
CMD ["flask", "run", "--host=0.0.0.0"]
