from flask import Flask, render_template, jsonify
from db import load_jobs
from sqlalchemy import text

app = Flask(__name__)

@app.route('/')
def hello_world():
  jobs_list = load_jobs()
  return render_template('home.html', jobs=jobs_list)

@app.route('/jobs')
def list_jobs():
  return jsonify(job_dict)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
