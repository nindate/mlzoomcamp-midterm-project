FROM python:3.8.12-slim

RUN apt update -y && apt install -y python3-pip python3-venv

RUN python3 -m venv mlzoomcamp

RUN . ./mlzoomcamp/bin/activate

WORKDIR /app
COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt

COPY ["predict.py", "cloud-request.py", "xgb_model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "predict:app"]
