from flask import Flask, request, jsonify, render_template
from model import answer_query
import time
import os
from flask_cors import CORS

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU (CUDA)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# app = Flask(__name__)

templates_dir = os.path.join(os.getcwd(), 'templates')
static_dir = os.path.join(os.getcwd(), 'static')
app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)

CORS(app)

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json.get("query")
    if not query:
        return jsonify({"error": "No query provided!"}), 400
    response = answer_query(query)
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
