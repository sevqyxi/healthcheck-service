from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)
# Зберігати порядок полів у JSON як у специфікації
app.json.sort_keys = False


def utc_now():
    """Поточний час у UTC у форматі ISO 8601."""
    return datetime.now(timezone.utc).isoformat()


@app.route("/healthz/live", methods=["GET"])
def liveness_check():
    """Liveness: процес застосунку запущений і відповідає."""
    return jsonify({
        "status": "alive",
        "timestamp": utc_now(),
    }), 200


@app.route("/healthz/ready", methods=["GET"])
def readiness_check():
    """Readiness: сервіс готовий приймати трафік."""
    # БД підключатиметься в наступних лабораторних
    return jsonify({
        "status": "ready",
        "database": "not_connected_yet",
        "timestamp": utc_now(),
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
