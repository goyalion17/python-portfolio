import json
import os
import smtplib
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from forms import ContactForm
from mailer import mail_configured, send_contact_message
from projects_data import PROJECTS

load_dotenv()

BASE_DIR = Path(__file__).parent
LANGUAGES = ("en", "uk", "de")
DEFAULT_LANG = "en"
AREAS = ("web", "auto", "api", "data", "gui")

app = Flask(__name__)
# In production SECRET_KEY must be set in the environment
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-me")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    area = db.Column(db.String(20), nullable=False)
    tags = db.Column(db.String(200), nullable=False)  # comma-separated
    featured = db.Column(db.Boolean, default=False, nullable=False)
    desc_en = db.Column(db.String(300), nullable=False)
    desc_uk = db.Column(db.String(300), nullable=False)
    desc_de = db.Column(db.String(300), nullable=False)
    code_url = db.Column(db.String(300))
    demo_url = db.Column(db.String(300))
    image = db.Column(db.String(200))  # file name inside static/img/

    def description(self, lang):
        return getattr(self, f"desc_{lang}")

    def tag_list(self):
        return self.tags.split(",")


def load_translations():
    data = {}
    for lang in LANGUAGES:
        with open(BASE_DIR / "translations" / f"{lang}.json", encoding="utf-8") as f:
            data[lang] = json.load(f)
    return data


TRANSLATIONS = load_translations()


with app.app_context():
    db.create_all()
    if db.session.query(Project).first() is None:
        db.session.add_all(Project(**item) for item in PROJECTS)
        db.session.commit()


@app.route("/")
def root():
    # Pick the language from the browser settings, fall back to English
    lang = request.accept_languages.best_match(LANGUAGES, default=DEFAULT_LANG)
    return redirect(url_for("home", lang=lang))


@app.route("/<lang>/", methods=["GET", "POST"])
def home(lang):
    if lang not in LANGUAGES:
        abort(404)

    form = ContactForm()
    if form.validate_on_submit():
        if form.website.data:
            # Honeypot filled in: pretend everything is fine, send nothing
            flash(TRANSLATIONS[lang]["form"]["success"], "success")
            return redirect(url_for("home", lang=lang, _anchor="contact"))
        try:
            if mail_configured():
                send_contact_message(form.name.data, form.email.data, form.message.data)
            elif app.debug:
                # Local development without SMTP settings: show the message in the terminal
                print(f"\n--- contact form ---\n{form.name.data} <{form.email.data}>\n{form.message.data}\n")
            else:
                raise RuntimeError("Mail is not configured")
            flash(TRANSLATIONS[lang]["form"]["success"], "success")
        except (smtplib.SMTPException, OSError, RuntimeError):
            app.logger.exception("Could not send contact message")
            flash(TRANSLATIONS[lang]["form"]["failed"], "error")
        return redirect(url_for("home", lang=lang, _anchor="contact"))

    area = request.args.get("area", "all")
    if area != "all" and area not in AREAS:
        area = "all"

    query = db.select(Project).order_by(Project.id)
    if area != "all":
        query = query.where(Project.area == area)
    projects = db.session.execute(query).scalars().all()

    featured = db.session.execute(
        db.select(Project).where(Project.featured).order_by(Project.id)
    ).scalars().all()

    counts = dict(
        db.session.execute(db.select(Project.area, func.count()).group_by(Project.area)).all()
    )
    counts["all"] = sum(counts.values())

    return render_template(
        "index.html",
        lang=lang,
        t=TRANSLATIONS[lang],
        projects=projects,
        featured=featured,
        areas=("all", *AREAS),
        current_area=area,
        counts=counts,
        form=form,
    )


@app.context_processor
def inject_languages():
    return {"languages": LANGUAGES}


if __name__ == "__main__":
    app.run(debug=True)
