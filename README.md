git remote add origin https://github.com/bgtti/mailMockup.git

# MailMockup

A minimal Flask app to visualize and test corporate email template layouts.

**Project under construction**
Please come back later.

## Quickstart

### 1) Create virtual environment & install deps

**Create virtual env**
```powershell
python -m venv env
.\env\Scripts\activate
```

**install dependencies**
```powershell
pip install -r requirements.txt
```
to update dependencies:
```powershell
pip freeze > requirements.txt
```

**run the project**
```powershell
python run.py
```



### 2) Configure environment
Copy the example env and edit:
```bash
cp .env.example .env   # (Windows PowerShell: copy .env.example .env)
```

### 3) Project layout
```
mail_mockup/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── email/
│   ├── templates/
│   │   ├── emails/
│   │   ├── layout.html
│   │   ├── index.html
│   │   └── about.html
│   └── static/
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Notes
- Environment variables are loaded via `python-dotenv` if a `.env` file is present.
- Adjust `SESSION_COOKIE_SECURE`, `REMEMBER_COOKIE_SECURE`, and `PREFERRED_URL_SCHEME` when using HTTPS.
