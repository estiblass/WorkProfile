from flask import Flask, render_template, request, Response
from os import environ
from dbcontext import db_data, db_delete, db_add, health_check
from person import Person
import logging
import time

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# ---------------------------------------------------------------------------
# 🔄 Wait for the database to become available (retry up to 10×, 5 s each)
# ---------------------------------------------------------------------------
for attempt in range(10):
    try:
        if health_check():
            app.logger.info("✓ Database is ready on attempt %s", attempt + 1)
            break
    except Exception as exc:
        app.logger.warning("⏳ Waiting for database (%s/10): %s", attempt + 1, exc)
        time.sleep(5)
else:
    app.logger.error("❌ Database is not available after 10 attempts – exiting.")
    exit(1)

# ---------------------------------------------------------------------------
# Environment variables
# ---------------------------------------------------------------------------
host_name = environ.get("HOSTNAME") or "no_host"
db_host = environ.get("DB_HOST", "mysql")
backend = environ.get("BACKEND", "http://localhost")

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def main():
    app.logger.info("Entering main route")
    data = db_data()
    return render_template("index.html.jinja", host_name=host_name, db_host=db_host, data=data, backend=backend)

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id: int):
    app.logger.info("Request to delete person with id: %s", id)
    return db_delete(id)

@app.route("/add", methods=["PUT"])
def add():
    body = request.json
    if body is not None:
        app.logger.info("Request to add person with body: %s", body)
        person = Person(0, body["firstName"], body["lastName"], body["age"], body["address"], body["workplace"])
        return db_add(person)
    app.logger.error("Request body is empty")
    return Response(status=404)

@app.route("/health")
def health():
    messages = []
    # Application health
    messages.append("Application: Healthy")

    # Database health
    try:
        db_ok = health_check()
        messages.append("Database: Healthy" if db_ok else "Database: Not Healthy")
        status_code = 200 if db_ok else 503
    except Exception as exc:
        app.logger.error("Database health check failed: %s", exc)
        messages.append("Database: Not Healthy")
        status_code = 503

    return "\n".join(messages), status_code

# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
