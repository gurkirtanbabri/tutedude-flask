from flask import Flask, render_template, request, redirect, url_for
import requests

BACKEND_API_URL = "http://0.0.0.0:5000"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    data = dict(request.form)
    print(data)
    response = requests.post(BACKEND_API_URL + "/submit", json=data)
    print(response)

    if response.status_code == 200:
      resJson = response.json()
      if (resJson.get("status") == True):
         return redirect(url_for('success'))
      else:
         return render_template('index.html', errorMessage="Submission failed")
    else:
       return render_template('index.html', errorMessage="Submission failed")
    
     
  return render_template('index.html', )

@app.route('/success')
def success():
  return render_template('success.html')



if __name__ == '__main__':
    # You might want to change the port or use a WSGI server for production
    app.run(host="0.0.0.0", port=5001, debug=True)