From s00zzang/isdomi:0.8.2

WORKDIR /code

COPY src/fishmlserv/main.py /code/

#모델서빙만(의존성의 위 BASE 이미지에서 모두 설치함)
RUN pip install --no-cache-dir --upgrade git+https://github.com/S00zzang/fishmlserv.git@1.0/k

#모델서빙을 위해 API 구동을 위한 FastAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
