From python:3.11

WORKDIR /code

COPY src/fishmlserv/main.py /code/


RUN pip install git+https://github.com/S00zzang/fishmlserv.git@0.7/manifest

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
