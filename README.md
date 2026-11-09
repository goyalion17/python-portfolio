# Python Portfolio

A multilingual (English / Ukrainian / German) portfolio website built with **Python and Flask**.
It showcases my projects from the *100 Days of Code: The Complete Python Pro Bootcamp* and serves as a project in its own right.

## Features

- **Three languages** (`/en/`, `/uk/`, `/de/`): the language is picked from the browser settings and can be switched in the header. Texts live in JSON files.
- **Projects from a database**: SQLAlchemy model with SQLite, featured cards and a server-side filter by area (`?area=web`).
- **Contact form**: Flask-WTF with CSRF protection, validation, a honeypot field against spam bots, and sending via SMTP.
- **Responsive design** with an automatic light and dark theme.

## Tech stack

| Area | Tools |
|---|---|
| Backend | Python, Flask, Jinja2 |
| Database | SQLite, Flask-SQLAlchemy |
| Forms and email | Flask-WTF, WTForms, `smtplib` |
| Config | python-dotenv (environment variables) |
| Frontend | HTML, CSS (no frameworks) |

## Project structure

```
python-portfolio/
├── main.py             # Flask app, routes, database model
├── forms.py            # Contact form
├── mailer.py           # SMTP sending
├── projects_data.py    # Initial project data (seeded into the DB on first run)
├── translations/       # en.json, uk.json, de.json
├── templates/          # base.html, index.html
├── static/css/         # style.css
├── requirements.txt
└── .env.example        # Template for environment variables
```

## Run locally

```bash
git clone https://github.com/goyalion17/python-portfolio.git
cd python-portfolio

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env     # then fill in the values
python main.py
```

Open http://127.0.0.1:5000

On macOS port 5000 is often taken by the AirPlay Receiver. Run the app on another port instead:

```bash
flask --app main run --debug --port 5001
```

and open http://127.0.0.1:5001

### Environment variables

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Signs sessions and CSRF tokens. Generate with `python -c "import secrets; print(secrets.token_hex(32))"` |
| `MAIL_SERVER`, `MAIL_PORT` | SMTP server (default `smtp.gmail.com`, `587`) |
| `MAIL_USER`, `MAIL_PASSWORD` | SMTP login. For Gmail use an app password |
| `MAIL_TO` | Where contact messages arrive (defaults to `MAIL_USER`) |

Without SMTP settings, the contact form prints messages to the terminal in debug mode.

## GitHub Pages

The live site is a static copy built with [Frozen-Flask](https://frozen-flask.readthedocs.io/):

```bash
python freeze.py      # writes the pages for /en/, /uk/, /de/ to build/
```

- The root page picks the language from the browser settings.
- The area filter runs in the browser, so it works without a server (`?area=web` links work too).
- The contact form needs a server, so the static copy shows only the email and GitHub links.

[.github/workflows/pages.yml](.github/workflows/pages.yml) builds and deploys the site on every push to `main`
(Settings → Pages → Source: GitHub Actions).

## Adding a project

Add an entry to [projects_data.py](projects_data.py) (name, area, tags, descriptions in all three languages, optional `code_url` and `demo_url`). For a project whose code is not public, set `"private": True` instead of `code_url`: the card then shows "Private code, available on request".
If the database already exists, delete `instance/portfolio.db` and restart the app so it is seeded again.

## Notes

- Translations are loaded at startup, so restart the server after editing the JSON files.
- Projects without a screenshot show a gradient block with the project name.
