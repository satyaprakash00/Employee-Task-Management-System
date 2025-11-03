# Employee Task Management System

A web-based task management system with AI assistant capabilities built using Flask, PostgreSQL, and TF-IDF for natural language processing.

## Features

- Employee registration and authentication
- Task creation, assignment, and tracking
- Task status updates and priority management
- AI-powered chat assistant for employee queries
- Responsive UI built with Bootstrap

## System Architecture

### Backend
- **Flask**: Web framework
- **PostgreSQL**: Database
- **SQLAlchemy**: ORM
- **Flask-Login**: Authentication

### Frontend
- **Bootstrap 5**: UI framework
- **JavaScript**: Client-side functionality

### AI Assistant
- **TF-IDF**: Text similarity for query matching
- **NLTK**: Natural language processing
- **Local Knowledge Base**: JSON-based knowledge storage

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip

### Installation

1. Clone the repository:
```
git clone <repository-url>
cd employee-task-management
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
```
pip install -r requirements.txt
```

5. Set up environment variables:
Create a `.env` file in the project root with the following:
```
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://username:password@localhost/task_management
```

6. Create the PostgreSQL database:
```
createdb task_management
```

7. Initialize the database:
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

8. Run the application:
```
flask run
```

9. Access the application at `http://localhost:5000`

## Database Schema

### Users Table
- id (PK)
- username
- email
- password_hash
- first_name
- last_name
- role
- department
- created_at

### Tasks Table
- id (PK)
- title
- description
- status
- priority
- due_date
- assignee_id (FK to users.id)
- creator_id (FK to users.id)
- created_at
- updated_at
- completed_at

## AI Assistant

The AI assistant uses TF-IDF (Term Frequency-Inverse Document Frequency) to match user queries with predefined questions and answers stored in a local knowledge base. The system:

1. Preprocesses user queries by tokenizing, removing stopwords, and normalizing text
2. Computes similarity scores between the query and known questions
3. Returns the answer with the highest similarity score

The knowledge base is stored in `knowledge_base/knowledge_base.json` and can be extended with additional Q&A pairs.

## Folder Structure

```
employee-task-management/
├── app.py                  # Main application file
├── requirements.txt        # Dependencies
├── .env                    # Environment variables (create this)
├── models/                 # Database models
│   ├── user.py
│   └── task.py
├── routes/                 # Route handlers
│   ├── auth.py
│   ├── tasks.py
│   └── chat.py
├── forms/                  # Form definitions
│   ├── auth_forms.py
│   └── task_forms.py
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── auth/
│   ├── tasks/
│   └── chat/
├── static/                 # Static assets
│   ├── css/
│   └── js/
├── utils/                  # Utility functions
│   └── ai_assistant.py
└── knowledge_base/         # AI assistant data
    └── knowledge_base.json
```

## Future Enhancements

- Task comments and attachments
- Team management features
- Advanced reporting and analytics
- Enhanced AI capabilities with more sophisticated NLP models
- Mobile application integration