# Starting data for the projects table. Areas: web, auto, api, data, gui.
# Real links and new projects (Day 82-100) get added here or directly in the DB.

PROJECTS = [
    {
        "area": "web", "name": "Blog", "tags": "Flask,SQLAlchemy,Bootstrap", "featured": True,
        "desc_en": "A blog with user registration, comments and post management.",
        "desc_uk": "Блог із реєстрацією, коментарями й керуванням постами.",
        "desc_de": "Ein Blog mit Registrierung, Kommentaren und Beitragsverwaltung.",
    },
    {
        "area": "web", "name": "Top 10 Movies", "tags": "Flask,SQLite,Flask-WTF",
        "desc_en": "A personal movie ranking: add films via an API, edit ratings.",
        "desc_uk": "Особистий рейтинг фільмів: додавання через API, редагування оцінок.",
        "desc_de": "Persönliches Film-Ranking: Filme über eine API hinzufügen, Bewertungen bearbeiten.",
    },
    {
        "area": "web", "name": "Coffee & Wifi", "tags": "Flask,Jinja,Bootstrap",
        "desc_en": "A directory of cafés for working: coffee, Wi-Fi, power sockets.",
        "desc_uk": "Каталог кав’ярень для роботи: кава, Wi‑Fi, розетки.",
        "desc_de": "Verzeichnis von Cafés zum Arbeiten: Kaffee, WLAN, Steckdosen.",
    },
    {
        "area": "auto", "name": "Amazon Price Tracker", "tags": "BeautifulSoup,requests,SMTP", "featured": True,
        "desc_en": "Watches a product price and sends an email when it drops below a threshold.",
        "desc_uk": "Стежить за ціною товару й надсилає лист, коли вона падає нижче порогу.",
        "desc_de": "Beobachtet den Preis eines Produkts und schickt eine E-Mail, wenn er unter eine Schwelle fällt.",
    },
    {
        "area": "auto", "name": "Data Entry Automation", "tags": "BeautifulSoup,Selenium",
        "desc_en": "Scrapes rental listings and fills in a Google Form with them automatically.",
        "desc_uk": "Збирає оголошення про оренду й сама заповнює ними Google-форму.",
        "desc_de": "Sammelt Mietanzeigen und trägt sie automatisch in ein Google-Formular ein.",
    },
    {
        "area": "auto", "name": "Tic Tac Toe", "tags": "Python,CLI,random",
        "desc_en": "A text-based Tic Tac Toe for two players or against a computer that plays random moves.",
        "desc_uk": "Текстова гра «хрестики-нулики» для двох гравців або проти комп’ютера з випадковими ходами.",
        "desc_de": "Textbasiertes Tic-Tac-Toe für zwei Spieler oder gegen einen Computer mit zufälligen Zügen.",
        "code_url": "https://github.com/goyalion17/tic-tac-toe",
        "image": "tic-tac-toe.png",
    },
    {
        "area": "api", "name": "Flight Deal Finder", "tags": "REST API,Google Sheets,SMTP", "featured": True,
        "desc_en": "Searches for cheap flights across a list of destinations and alerts you to deals.",
        "desc_uk": "Шукає дешеві авіаквитки за списком напрямків і сповіщає про знахідки.",
        "desc_de": "Sucht günstige Flüge für eine Liste von Reisezielen und meldet Schnäppchen.",
    },
    {
        "area": "api", "name": "ISS Tracker", "tags": "requests,API,SMTP",
        "desc_en": "Sends an email when the ISS passes overhead at night.",
        "desc_uk": "Надсилає лист, коли МКС уночі пролітає над містом.",
        "desc_de": "Schickt eine E-Mail, wenn die ISS nachts über der Stadt fliegt.",
    },
    {
        "area": "api", "name": "Habit Tracker", "tags": "requests,REST API",
        "desc_en": "Logs daily habits and turns them into a graph via an API.",
        "desc_uk": "Записує щоденні звички й будує з них графік через API.",
        "desc_de": "Erfasst tägliche Gewohnheiten und zeichnet sie über eine API als Diagramm.",
    },
    {
        "area": "data", "name": "House Price Prediction", "tags": "pandas,scikit-learn,Seaborn",
        "desc_en": "A linear regression model that estimates house prices.",
        "desc_uk": "Модель лінійної регресії, що оцінює ціни на житло.",
        "desc_de": "Ein lineares Regressionsmodell, das Immobilienpreise schätzt.",
    },
    {
        "area": "data", "name": "Nobel Prize Analysis", "tags": "pandas,Plotly",
        "desc_en": "An exploration of laureates by year, country and field.",
        "desc_uk": "Дослідження лауреатів за роками, країнами й галузями.",
        "desc_de": "Eine Analyse der Preisträger nach Jahr, Land und Fachgebiet.",
    },
    {
        "area": "data", "name": "LEGO Analysis", "tags": "pandas,matplotlib",
        "desc_en": "How LEGO sets changed over time: themes, part counts, years.",
        "desc_uk": "Як змінювалися набори LEGO: теми, кількість деталей, роки.",
        "desc_de": "Wie sich LEGO-Sets verändert haben: Themen, Teilezahlen, Jahre.",
    },
    {
        "area": "data", "name": "Google Trends", "tags": "pandas,matplotlib",
        "desc_en": "Do search trends relate to real-world data? Correlations and charts.",
        "desc_uk": "Чи пов’язані пошукові тренди з реальними даними — кореляції й графіки.",
        "desc_de": "Hängen Suchtrends mit realen Daten zusammen? Korrelationen und Diagramme.",
    },
    {
        "area": "gui", "name": "Password Manager", "tags": "Tkinter,JSON",
        "desc_en": "Generates and stores passwords, and looks up saved entries.",
        "desc_uk": "Генерує й зберігає паролі, шукає збережені записи.",
        "desc_de": "Erzeugt und speichert Passwörter und sucht gespeicherte Einträge.",
    },
    {
        "area": "gui", "name": "Flash Card App", "tags": "Tkinter,pandas",
        "desc_en": "Flash cards for learning words that remember your progress.",
        "desc_uk": "Картки для вивчення слів, що запам’ятовують прогрес.",
        "desc_de": "Lernkarten für Vokabeln, die den Fortschritt speichern.",
    },
    {
        "area": "gui", "name": "Watermark Studio", "tags": "Tkinter,Pillow",
        "desc_en": "A desktop app that adds a text or logo watermark to photos, with live preview, tiling and batch processing.",
        "desc_uk": "Десктопний застосунок, що додає текстовий або логотипний водяний знак на фото: з превʼю наживо, плиткою й пакетною обробкою.",
        "desc_de": "Eine Desktop-App, die Fotos ein Text- oder Logo-Wasserzeichen hinzufügt: mit Live-Vorschau, Kachelmuster und Stapelverarbeitung.",
        "code_url": "https://github.com/goyalion17/watermark-studio",
        "image": "watermark-studio.png",
    },
]
