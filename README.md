# 🍹 Ohzu

---
![main](https://user-images.githubusercontent.com/72291860/190209133-1e5cdc33-ab43-48c5-9562-117be0ce8046.png)
![ohzu](https://user-images.githubusercontent.com/72291860/190209889-86e3aa37-f02f-4090-ad2b-e793553a2ee5.png)

당신을 위한 맞춤형 칵테일 추천 서비스, 오쥬

<br/>


## 🥝 Services

1. 매일 랜덤으로 추천받는 다양한 칵테일!
2. 이름 또는 해시태그로 원하는 칵테일 검색! 
3. 해시태그로 제공하는 칵테일에 대한 자세한 정보!
4. 직접 만들어보고 싶은 칵테일 레시피 제공! 
5. 오직 당신만을 위한 맞춤형 추천 칵테일!

<br/>

## 📱 UI/UX
![merge](https://user-images.githubusercontent.com/72291860/190214684-fd63e2a1-6803-4e56-873d-261cf396a50f.png)

![merge_from_ofoct (3)](https://user-images.githubusercontent.com/72291860/190215266-a8532263-554f-4836-9ecd-f9d2b80f39f1.png)

<b> (칵테일 일러스트 이미지의 저작권은 Ohzu 및 Ohzu의 디자이너에게 있습니다) </b>

<br/>

</br>

## 🛠 Tech Stack

### ✔️ Infra

|Docker|Github Actions|
|:---:|:---:|
|<img src = "./images/docker.png" width="50px" title="Docker"/>|<img src="./images/githubactions.png" width="50px" title="Github Actions"/>

### ✔️ DataBase

| MySQL                                                        | RDS                                                     |S3|
|--------------------------------------------------------------|---------------------------------------------------------|---|
|  <img src="./images/mysql.png" width="50px"  title= "MySQL"/> | <img src="./images/rds.png" width="50px"  title="RDS"/> |<img src="./images/s3.png" width="50px"  title="S3" />

### ✔️ Web Server

| EC2                                                      | ELB                                                      | Django                                                         | Nginx                                                        |gunicorn|
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------|---|
|  <img src="./images/ec2.png" width="50px"  title="EC2" /> | <img src="./images/elb.png" width="50px"  title="ELB" /> | <img src="./images/django.png" width="50px"  title="Django" /> | <img src="./images/nginx.png" width="50px"  title="Nginx" /> |<img src="./images/gunicorn.png" width="70px"  title="gunicorn" />



<br/>


## 🏛 Architecture

<img src="./images/architecture.png"  title="architecture" />



<br/>


## 📁 Project Structure

```
├─ .github
├─ config
│  └─ docker
│  └─ nginx
│  └─ scripts
│ 
├─ images
├─ landingpage (앱)
│     ├─ migrations
│     ├─ __init__.py
│     ├─ admin.py
│     ├─ apps.py
│     └─ models.py
│     └─ serializers.py
│     └─ tests.py
│     └─ urls.py
│     └─ views.py
│ 
├─ main (앱)
│     ├─ migrations
│     ├─ __init__.py
│     ├─ admin.py
│     ├─ apps.py
│     └─ models.py
│     └─ serializers.py
│     └─ tests.py
│     └─ urls.py
│     └─ views.py
│ 
├─ Ohzu-BackEnd (프로젝트)
│     ├─ settings
│     ├─ __init__.py
│     ├─ asgi.py
│     ├─ urls.py
│     └─ wsgi.py
│ 
├─ docker-compose.prod.yml
├─ docker-compose.yml
├─ Dockerfile
├─ Dockerfile.prod
├─ manage.py
├─ README.md
├─ requirements.txt

```

<br/>
  
## 😎 Backend Developer

<table>
    <tr align="center">
        <td><B>Backend<B></td>
        <td><B>Backend<B></td>
    </tr>
    <tr align="center">
        <td><B>이수진<B></td>
        <td><B>서수경<B></td>
    </tr>
    <tr align="center">
        <td>
            <img src="https://github.com/ssssujini99.png?size=100">
            <br>
            <a href="https://github.com/ssssujini99"><I>ssssujini99</I></a>
        </td>
        <td>
            <img src="https://github.com/sukyeongs.png?size=100">
            <br>
            <a href="https://github.com/sukyeongs"><I>sukyeongs</I></a>
        </td>
    </tr>
    <tr align="center">
        <td align="center">
            <B>✔️ 프로젝트 세팅 (django)</br>
            <B>✔️ 서버 배포 및 도메인, 기타 세팅 (docker, github action, ec2, rds, aws s3)</br>
            <B>✔️ 칵테일 DB setup</br>
            <B>✔️ 프로젝트 ERD modeling</br>
            <B>✔️ 검색(이름, 태그검색) API 구현</br>
            <B>✔️ 칵테일 세부조회 API 구현</br>
            <B>✔️ 렌딩페이지 ERD modeling</br>
            <B>✔️ 렌딩페이지 서버 세팅 및 배포</br>
            <B>✔️ 렌딩페이지 질문페이지 API 구현</br>
        </td>
        <td align="center">
            <B>✔️ </br>
            <B>✔️ </br>
            <B>✔️ </br>
            <B>✔️ </br>
            <B>✔️ </br>
            <B>✔️ </br>
            <B>✔️ </br>
            <B>✔️ </br>
            <B>✔️ </br>
        </td>
    </tr>
</table>
