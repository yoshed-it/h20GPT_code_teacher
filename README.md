# # Personal Teaching Assistant

A personalized learning and coding assistant built with Flask, H2O GPT, and various other Python libraries. This assistant is designed to help you learn coding concepts, debug code, and follow personalized learning paths tailored to your progress.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This project aims to create an AI-powered coding and learning assistant that serves as a personal teacher for anyone looking to improve their coding skills. The assistant can answer questions, provide coding assistance, and suggest personalized learning paths based on the user's progress.

## Features

- **Interactive Chat Interface**: Engage in a conversation with the assistant to ask coding-related questions or get explanations on various topics.
- **Intelligent Coding Assistance**: Get real-time help with coding tasks, including code suggestions, debugging, and explanations.
- **Personalized Learning Path**: Follow a customized learning plan that adapts to your progress and helps you master new coding skills.
- **Integration with IDEs**: (Planned) Integrate the assistant with popular coding platforms for seamless assistance while coding.

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Frontend**: Jinja2, HTML, CSS, JavaScript
- **AI & NLP**: H2O GPT, Jedi, NLTK/SpaCy
- **Database**: SQLite
- **Deployment**: Docker, Gunicorn

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- (Optional) Docker for containerization

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/personal_teaching_assistant.git
   cd personal_teaching_assistant

2. **Create and Activate a Virtual Env:**
    ```python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**
    ```pip install -r requirements.txt```

4. **Set Up the Database:**
    ```bash
    flask db init
    flask db migrate
    flask db upgrade

5. **Run the Application:**
    ```bash
    flask run

The application will be available at http://127.0.0.1:5000/.


personal_teaching_assistant/
│
├── app/
│   ├── __init__.py            # Initialize Flask app and configurations
│   ├── routes.py              # Application routes
│   ├── models.py              # Database models
│   ├── forms.py               # Form handling and validation
│   ├── utils.py               # Utility functions and helpers
│   ├── static/
│   │   ├── css/
│   │   │   └── main.css       # Custom CSS for styling
│   │   ├── js/
│   │   │   └── main.js        # Custom JavaScript
│   │   └── images/            # Static images
│   ├── templates/
│   │   ├── base.html          # Base template
│   │   ├── index.html         # Homepage template
│   │   ├── learn.html         # Learning path template
│   │   └── code_assistant.html# Coding assistant template
│
├── data/
│   ├── user_data.db           # SQLite database file
│   └── example_data.csv       # Example dataset
│
├── tests/
│   ├── test_routes.py         # Tests for routes
│   ├── test_models.py         # Tests for models
│   └── test_utils.py          # Tests for utilities
│
├── config.py                  # Configuration settings
├── Dockerfile                 # Dockerfile for containerization
├── docker-compose.yml         # Docker Compose file for multi-container setup
├── requirements.txt           # Python dependencies
├── manage.py                  # Script for running the app and managing tasks
└── README.md                  # Project documentation

**Many Thanks to ChatpGPT for help with the file Structure**