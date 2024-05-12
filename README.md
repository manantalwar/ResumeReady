# ResumeReady: AI Powered Resume Generator

## Introduction

ResumeReady is web-based AI-powered resume generator application. The aim is to allows users to create customized resumes tailored to specific job descriptions. It is an interplay of three key ideas: CRUD, GPT LLM, and REST APIs. It comprises of an intuitive frontend dashboard with user authentication system for easy navigation and quick access to generated resumes and account information. It utilizes GPT LLM model to craft personalized resumes as an HTML format convertible to PDF for download.

## Installation

To get this project up and running on your local machine, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/manantalwar/ResumeReady.git
```

2. Navigate into the project directory

```bash
cd ResumeReady
```

3. Install dependencies. 

```bash
pip install -r requirements.txt
```

4. Apply migrations to the database. 

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server. 

```bash
python manage.py runserver
```

The app runs at http://127.0.0.1:8000/.

## Configuration 

- Ensure you system has Python3 and pip installed. 
- You may need to set `BASE_DIR` path in `settings.py` in `cs520proj` directory depending on your system configuration. 
- You may need to set `SECRET_KEY` for the application to work correctly.

## Demo Video

- Link: TBD

## Contributors 

- Manan Talwar
- Sonali Palit 
- Arshnoor Kaur Chadha 
- Bhoomika Raj Ethakota 
- Srikiran Kavuri