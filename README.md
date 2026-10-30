# 013-Riddhi-Internal

### Q1 : Create API For Managing Student data
  - Create student
  - get all students
  - get student by id
  - delete student by id
  - update student by id

### Q2 : Create repo and push all the files in git using commands
   - git init
   - git add .
   - git commit -m "Product-CRUD-Commit"
   - git branch -M main
   - git remote add origin https://github.com/RiddhiDarji07/devops-practical-internal.git
   - git push -u origin main

### Q5 : Deploy FastiAPI on render 

### Q3 : Create CICD PipeLine 
  - using redend deploy hook creare new secret variable and add
  - after push cicd code file in git
  - run cicd pipeline

### Q4 : Perform Docker
  - Create 2 files DockerFile and compose.yml
  - run this 2 files using commands:
    docker build -f DockerFile -t fastapi-app .
    docker run --rm -p 8000:8000 fastapi-app
    docker compose up
  - Create container and give port to run APi
    http://localhost:8000/docs
