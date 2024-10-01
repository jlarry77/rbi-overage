from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html',
                          #data_table=DATA_TABLE,
                          company_name="Roof Brokers, Inc.")

if __name__ == '__main__':
  app.run('0.0.0.0', debug=True) 