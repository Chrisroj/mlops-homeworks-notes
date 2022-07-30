FROM agrigorev/zoomcamp-model:3.8.12-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict_to_docker.py", "./"]

# Port where the App will be Exposed
EXPOSE 7878

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:7878", "predict_to_docker:app"]
