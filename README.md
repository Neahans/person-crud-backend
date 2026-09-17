<div align="center">

# 🐍 Person CRUD Backend

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=30&pause=900&color=0B7A53&center=true&vCenter=true&width=850&lines=Welcome+to+the+Person+CRUD+Backend+%F0%9F%8C%B8;Built+with+Django+%2B+DRF+%F0%9F%90%8D;REST+API+%7C+CRUD+%7C+Image+Upload+%F0%9F%96%BC%EF%B8%8F;Powering+a+React+Frontend+%E2%9A%9B%EF%B8%8F" alt="Typing Animation"/>

<br>

<img src="https://media.giphy.com/media/9C1nyePnovqlpEYFMD/giphy.gif" width="350" alt="Coding Animation"/>

<br><br>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/DRF-A30000?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>

<br><br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B7A53,50:22C55E,100:A7F3D0&height=170&section=header&text=DJANGO%20REST%20API&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=55" width="100%"/>

</div>

---

## 🌸 About The Project

This repository contains the **Django + Django REST Framework backend** for the Person CRUD Full-Stack Application.

The backend provides REST APIs for managing `Person` records with:

```text
👤 Name
🎂 Age
📍 Place
🖼️ Image
```

It handles the CRUD operations and image uploads that are consumed by the React frontend.

---

# ⚡ Full-Stack Architecture

<div align="center">

```text
             ⚛️ React Frontend
                     │
                     │ Axios
                     ▼
             🔗 REST API
                     │
                     ▼
        🐍 Django REST Framework
                     │
                     ▼
                📦 Person
                     │
              ┌──────┴──────┐
              ▼             ▼
          🗄️ Database    🖼️ Media
```

</div>

---

# ✨ Features

```text
➕ Create Person
👀 View Persons
✏️ Update Person
🗑️ Delete Person
🖼️ Image Upload
🔗 RESTful API
📡 React Integration
🌐 CORS Support
```

---

# 🛠️ Technologies

| Technology               | Purpose                |
| ------------------------ | ---------------------- |
| 🐍 Python                | Backend programming    |
| 🌱 Django                | Web framework          |
| 🔗 Django REST Framework | REST API               |
| 🗄️ SQLite               | Database               |
| 🖼️ Pillow               | Image handling         |
| 🌐 django-cors-headers   | Frontend communication |

---

# 📂 Project Structure

```text
person/
│
├── manage.py
│
├── person/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── persona/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── tests.py
│
├── media/
│   └── persons/
│
└── README.md
```

---

# 👤 Person Model

The main entity is `Person`.

```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to="persons/")
```

---

# 🔗 API Endpoints

### Get all persons

```http
GET /api/persona/
```

### Add a person

```http
POST /api/persona/
```

### Get a single person

```http
GET /api/persona/<id>/
```

### Update a person

```http
PATCH /api/persona/<id>/
```

### Delete a person

```http
DELETE /api/persona/<id>/
```

---

# 🔄 CRUD Flow

```text
           👤 PERSON

              │
        ┌─────┼─────┐
        │     │     │
        ▼     ▼     ▼
       ➕     👀    ✏️
     Create   Read  Update
        │     │     │
        └─────┼─────┘
              │
              ▼
           🗑️ Delete
```

---

# 🖼️ Image Upload

The API supports image uploads using Django's `ImageField`.

The React frontend sends the image using `FormData`:

```text
React
  ↓
FormData
  ↓
Axios
  ↓
Django REST Framework
  ↓
media/persons/
```

Uploaded images are exposed during development through Django's media configuration.

---

# ⚙️ Setup

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Neahans/person-crud-backend.git
```

## 2️⃣ Enter the project

```bash
cd person-crud-backend
```

## 3️⃣ Create and activate virtual environment

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

## 4️⃣ Install dependencies

```powershell
pip install django djangorestframework django-cors-headers pillow
```

## 5️⃣ Run migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

## 6️⃣ Start the server

```powershell
python manage.py runserver
```

Backend:

```text
http://127.0.0.1:8000/
```

API:

```text
http://127.0.0.1:8000/api/persona/
```

---

# 🧪 Testing the API

You can open:

```text
http://127.0.0.1:8000/api/persona/
```

to view the Django REST Framework endpoint.

Example response:

```json
[
  {
    "id": 1,
    "name": "Neaha",
    "age": 22,
    "place": "Thrissur",
    "image": "/media/persons/neaha.jpg"
  }
]
```

---

# ⚛️ Frontend Repository

This backend is designed to work with the React frontend:

### 👉 Person CRUD Frontend

**https://github.com/Neahans/person-crud-fullstack**

The frontend uses **Axios** to communicate with this Django REST API.

---

# 🔗 Full Project

<div align="center">

### 🐍 Backend

<a href="https://github.com/Neahans/person-crud-backend">

<img src="https://img.shields.io/badge/Django%20Backend-View%20Repository-092E20?style=for-the-badge&logo=django&logoColor=white"/>

</a>

<br><br>

### ⚛️ Frontend

<a href="https://github.com/Neahans/person-crud-fullstack">

<img src="https://img.shields.io/badge/React%20Frontend-View%20Repository-61DAFB?style=for-the-badge&logo=react&logoColor=black"/>

</a>

</div>

---

# 🌱 What I Learned

```text
🐍 Django Project Structure
🔗 Django REST Framework
📡 REST API Development
📝 Serializers
🧩 ViewSets
🔄 CRUD Operations
🖼️ Image Upload Handling
🌐 CORS Configuration
⚛️ Frontend–Backend Integration
```

---

# 🚀 Future Improvements

```text
🔐 User Authentication
👥 User Management
🔎 Search & Filtering
📄 Pagination
✅ Advanced Validation
☁️ Cloud Image Storage
🚀 Deployment
```

---

# 👩🏻‍💻 Author

<div align="center">

## Neaha N S

💻 Computer Science Graduate
🐍 Python & Django Developer
⚛️ React Developer / Learner
🔐 Cybersecurity Enthusiast

<br>

<a href="https://github.com/Neahans">

<img src="https://img.shields.io/badge/GitHub-Neahans-181717?style=for-the-badge&logo=github"/>

</a>

</div>

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=21&pause=1000&color=0B7A53&center=true&vCenter=true&width=700&lines=Code+%F0%9F%92%BB;Create+%F0%9F%8C%B8;Learn+%F0%9F%9A%80;Keep+Growing+%E2%9C%A8" alt="Footer Animation"/>

<br><br>

💚 **Thanks for visiting the backend repository!**

<br>

Made with 🐍 **Django** + ⚛️ **React**

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B7A53,50:22C55E,100:A7F3D0&height=120&section=footer&animation=fadeIn" width="100%"/>
