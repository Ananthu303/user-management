# 🧑‍💼 User Management System

A **User Management System** built using **Django REST Framework (DRF)** for the backend and **HTML + JavaScript (jQuery)** for the frontend.  
This project demonstrates **JWT authentication**, **profile management**, and **CRUD operations** with file attachments.

---
## 🚀 Features

### 🔐 Authentication
- User Registration (username, email, password)
- Login & Logout
- Only authenticated users can access profile and CRUD features

### 👤 Profile Management
Each registered user has a profile containing:
- Full Name  
- Date of Birth  
- Email  
- Address  
- Gender  
- Mobile Number  

Users can:
- View their profile  
- Update profile details  
- Change or reset their password  

### 📝 CRUD Module (Notes)
Each authenticated user can manage their own notes:
- **Fields:**  
  - Title  
  - Description  
  - Attachment
  - Created_at 
  - Modified_at
- **APIs:**  
  - Create a new note  
  - View all notes  
  - Update a note  
  - Delete a note  

### 💻 Frontend (Basic)
A simple **JavaScript + jQuery** frontend is included to:
- Register & login users, reset their password
- View and update profiles  
- Perform CRUD operations on notes  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Django, Django REST Framework |
| **Frontend** | HTML, CSS, JavaScript (jQuery) |
| **Database** | SQLite3 |
| **Authentication** | JWT (via `djangorestframework-simplejwt`) |
| **Language** | Python 3.12.8 |


### API Endpoints
- User registration, login, logout,profile update,change password and token refresh.  
- Notes CRUD operations.


## 🚀 Getting Started

Follow the steps below to set up and run the User Management System on your local machine.

---

### 1. Clone the Repository

Start by cloning the project from GitHub:

```bash
git clone https://github.com/Ananthu303/user-management.git
cd user-management
```

### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies for this project. Here’s how to create and activate it:

For **Windows**:
```bash
python -m venv venv

venv\Scripts\activate
```

For **macOS/Linux**:
```bash
python3 -m venv venv

source venv/bin/activate
```

Once activated, your terminal should show something like `(venv)` indicating that the virtual environment is active.

### 3. Install Dependencies

Once the virtual environment is activated, install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Apply the database migrations to set up the necessary database schema:

```bash
python manage.py migrate
```

### 5. Create Superuser (Super Admin)

You need to create a superuser.
Run the following command to create the superuser:

```bash
python manage.py createsuperuser
```

You will be prompted to enter the following information:

- Username
- Email
- Password

This superuser is the SUPERADMIN having full control over the system


### 6. Create .env File

Create a .env file in the project root directory.
By default, the base API URL is set to the hosted version on PythonAnywhere:

BASE_API_URL=https://ananthu66.pythonanywhere.com/

When running locally, update it according to your development port (for example):

BASE_API_URL=http://127.0.0.1:8000

An .env.sample file is provided for reference in the repository.


### 7. Run the Development Server

Once everything is set up, run the Django development server:

```bash
python manage.py runserver
```

Now, you can access the API's at `http://127.0.0.1:8000/`.

---
