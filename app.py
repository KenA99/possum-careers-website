from flask import Flask, render_template, jsonify

app = Flask(__name__)

job_dict = [
  {
    'id': 1,
    'title': 'Possum Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,000,000'
  },
  {
    'id': 2,
    'title': 'Possum Scientist',
    'location': 'Dehli, India',
    'salary': 'Rs. 15,000,000'
  },
  {
    'id': 3,
    'title': 'Front-end Possum',
    'location': 'San Francisco, USA',
    'salary': '$100,000'
  },
  {
    'id': 4,
    'title': 'Back-end Possum',
    'location': 'Remote',
    # 'salary': 'Rs. 19,000,000'
  }
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=job_dict)

@app.route('/jobs')
def list_jobs():
  return jsonify(job_dict)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
