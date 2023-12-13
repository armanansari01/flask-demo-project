from flask import Flask, render_template
app = Flask(__name__)

JOBS = [
  {'id': 1, 'title': 'Python Developer', 'location': 'New York', 'salary': '$100,000'},
  {'id': 2, 'title': 'Web Developer', 'location': 'San Francisco', 'salary': '$120,000'},
  {'id': 3, 'title': 'Data Scientist', 'location': 'Chicago', 'salary': '$90,000'},
  {'id': 4, 'title': 'Backend Engineer', 'location': 'Delhi', 'salary': '$80,000'},
  {'id': 5, 'title': 'Data Engineer', 'location': 'Remote', 'salary': '$50,000'}
]

@app.route('/')
def hello_home():
    return render_template('home.html',jobs=JOBS,company_name= "Internio Careers")

print(__name__)
if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0')