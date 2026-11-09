"""Build a static copy of the site for GitHub Pages.

    python freeze.py   ->   build/

Every language page (/en/, /uk/, /de/) is rendered to HTML with Frozen-Flask. The root page picks the
language from the browser settings with a few lines of JavaScript. The contact form needs a server,
so the static copy shows only the email and GitHub links.
"""

import json
import warnings
from pathlib import Path

from flask_frozen import Freezer, MissingURLGeneratorWarning

from main import BASE_DIR, DEFAULT_LANG, LANGUAGES, TRANSLATIONS, app

BUILD_DIR = BASE_DIR / "build"

app.config.update(
    STATIC_BUILD=True,
    FREEZER_DESTINATION=str(BUILD_DIR),
    FREEZER_RELATIVE_URLS=True,       # the site lives under /python-portfolio/, not at the domain root
    FREEZER_REMOVE_EXTRA_FILES=True,
)
# Only the pages listed below: no POST routes, no ?area= links (the filter works in the browser)
freezer = Freezer(app, with_no_argument_rules=False, log_url_for=False)


@freezer.register_generator
def home():
    for lang in LANGUAGES:
        yield {"lang": lang}


ROOT_PAGE = """<!doctype html>
<html lang="{default}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <noscript><meta http-equiv="refresh" content="0; url={default}/"></noscript>
  <script>
    const languages = {languages};
    const preferred = (navigator.languages || [navigator.language])
      .map((code) => code.slice(0, 2).toLowerCase())
      .find((code) => languages.includes(code));
    location.replace((preferred || "{default}") + "/" + location.search + location.hash);
  </script>
  <style>body {{ background: #0A1414; color: #E6F0EE; font-family: system-ui, sans-serif; padding: 24px; }}
  a {{ color: #7CF5C4; }}</style>
</head>
<body>
  <p><a href="en/">English</a> · <a href="uk/">Українська</a> · <a href="de/">Deutsch</a></p>
</body>
</html>
"""


def main():
    with warnings.catch_warnings():
        # "/" only redirects to a language; the root page is written below instead
        warnings.simplefilter("ignore", MissingURLGeneratorWarning)
        freezer.freeze()
    root = ROOT_PAGE.format(default=DEFAULT_LANG, title=TRANSLATIONS[DEFAULT_LANG]["title"],
                            languages=json.dumps(list(LANGUAGES)))
    (BUILD_DIR / "index.html").write_text(root, encoding="utf-8")
    (BUILD_DIR / ".nojekyll").touch()  # serve files as they are, without Jekyll
    pages = sorted(str(p.relative_to(BUILD_DIR)) for p in Path(BUILD_DIR).rglob("*.html"))
    print("Built:", ", ".join(pages))


if __name__ == "__main__":
    main()
