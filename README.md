# API Development

A comprehensive FastAPI-based REST API application featuring user authentication, post management, and PostgreSQL database integration. This project demonstrates modern API development practices with Python, showcasing a clean architecture and secure authentication system.

## Features

- **User Authentication & Authorization**: JWT-based authentication system with secure password hashing
- **User Management**: Complete user registration, login, and profile management
- **Post Management**: Full CRUD operations for posts with user associations
- **Database Integration**: PostgreSQL database with SQLAlchemy ORM
- **Data Validation**: Pydantic schemas for request/response validation
- **Modular Architecture**: Clean separation of concerns with routers, models, and schemas

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT tokens with bcrypt password hashing
- **Data Validation**: Pydantic
- **Environment Management**: python-dotenv

## Project Structure

```
app/
├── __init__.py
├── main.py          # Application entry point
├── database.py      # Database configuration
├── model.py         # SQLAlchemy models
├── schema.py        # Pydantic schemas
├── utilis.py        # Utility functions
└── routers/
    ├── auth.py      # Authentication endpoints
    ├── posts.py     # Post management endpoints
    └── users.py     # User management endpoints
```

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip or conda package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aquashie14/API_Development.git
cd API_Development
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DB_HOST=your_database_host
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- **Interactive API docs**: http://localhost:8000/docs
- **ReDoc documentation**: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /login` - User login
- `POST /register` - User registration

### Users
- `GET /users/{id}` - Get user profile
- `POST /users` - Create new user

### Posts
- `GET /posts` - Get all posts
- `POST /posts` - Create new post
- `GET /posts/{id}` - Get specific post
- `PUT /posts/{id}` - Update post
- `DELETE /posts/{id}` - Delete post

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
