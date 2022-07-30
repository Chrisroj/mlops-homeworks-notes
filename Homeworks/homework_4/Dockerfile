FROM agrigorev/zoomcamp-model:mlops-3.9.7-slim

RUN pip install pipenv 

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system 

COPY ["starter.py", "./"]