from flask import Flask, jsonify, Response, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/json")
def return_json():
    return jsonify({"status": "success", "message": "Hello from JSON"})

@app.route("/xml")
def return_xml():
    xml_data = "<note><to>User</to><from>Server</from><message>Hello from XML</message></note>"
    return Response(xml_data, mimetype='application/xml')

@app.route("/csv")
def return_csv():
    csv_data = "name,age\nJohn,30\nJane,25"
    return Response(csv_data, mimetype='text/csv')

@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

