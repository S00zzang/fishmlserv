# fishmlserv

### Deploy                                                                         
![deploy_image](https://github.com/user-attachments/assets/d9a3fb4b-672b-47d0-b789-828ac05621b8)

### Run

- dev
- http://localhost:8000/docs
```bash
# uvicorn --help

$ uvicorn src.fishmlserv.main:app --reload
```

- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949 #기본 port는 8000
```
