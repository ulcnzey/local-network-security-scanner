from flask import Flask, render_template, request, jsonify
from scanner import scan_target

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()

    target = data.get("target", "").strip()

    if not target:
        return jsonify({
            "success": False,
            "error": "Hedef IP adresi girilmedi."
        }), 400

    result = scan_target(target)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
