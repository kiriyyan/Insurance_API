
#Insurance_API

Простой API на FastAPI примитивными эндпоинтами GET и POST.  
Проект упакован в Docker-контейнер, что позволяет запускать его без установки Python и зависимостей.

##Requirements
[Docker]
```BASH
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo systemctl start docker
sudo systemctl enable docker
```

##How to use
1. Build Docker image:
```bash
docker build -t my_app .
```

2. Add config.py and input your data 

```python
DB_USER = 'your user'
DB_PASSWORD = 'your password'
DB_HOST = "127.0.0.1"
DB_PORT = 5432
DB_NAME = 'insurance'
```

3. Enable docker container on port 8000:
```
docker run  -p 8000:8000 -d --name InsuranceAPI my_app
```
4. Open http://localhost:8000/docs to get information about endpoints of API

## STRUCTURE
fastapi_project/
├── Routers/            
│   ├── clients.py
│   ├── contracts.py
│   ├── departments.py
│   └── employees.py
├── venv/                
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── lib64/
├── .gitignore           -EXCEPT venv, __pycache__, config.py
├── config.py            
├── database.py          
├── Dockerfile
├── main.py             
├── models.py            
├── README.md
└── requirements.txt 