from flask import Flask

app = Flask(__name__)


def greet(name: str) -> str:
    return f"Hello, {name}"


@app.get("/")
def index() -> str:
    return f"<h1>{greet('World')}</h1>"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
