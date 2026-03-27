# 🏠 Stay Finder

> A full-stack rental booking platform connecting property owners and tenants — built for Tamil Nadu & Bengaluru markets.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-REST_API-red?style=flat)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-black?style=flat&logo=jsonwebtokens)

---

## 🚀 Live Demo
- **Frontend:** [Deployed on Vercel](#)
- **Backend API:** [Deployed on Railway](#)

---

## 📌 Features

### 👤 Three User Roles
- **Owner** — List properties, manage bookings, upload photos
- **Tenant** — Search & book properties, view listings
- **Admin** — Full platform control & user management

### 🔑 Core Functionality
- JWT-based Authentication & Authorization
- Role-Based Access Control (RBAC)
- Property listing with photo uploads (Cloudinary)
- Search & filter rentals by location
- Booking management system
- RESTful API with Django REST Framework

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js, Tailwind CSS |
| Backend | Django, Django REST Framework |
| Database | PostgreSQL |
| Auth | JWT (SimpleJWT) |
| Image Storage | Cloudinary |
| Deployment | Railway (Backend), Vercel (Frontend) |

---

## 📁 Project Structure
```
stay-finder/
├── backend/
│   ├── accounts/        # User auth & roles
│   ├── properties/      # Property listings
│   ├── bookings/        # Booking management
│   └── stay_finder/     # Django settings
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── api/
└── README.md
```

---

## ⚙️ Local Setup

### Backend
```bash
git clone https://github.com/Gytgowtham/stay-finder.git
cd stay-finder/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm start
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | User Registration |
| POST | `/api/auth/login/` | JWT Login |
| GET | `/api/properties/` | List all properties |
| POST | `/api/properties/` | Create listing (Owner) |
| POST | `/api/bookings/` | Book a property |
| GET | `/api/bookings/my/` | View my bookings |

---

## 👨‍💻 Developer

**Gowtham Krish**
- 📧 gowthamkrish4506@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/gowtham-krish-009021276)
- 🐙 [GitHub](https://github.com/Gytgowtham)

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
