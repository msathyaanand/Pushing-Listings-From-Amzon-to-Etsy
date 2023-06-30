from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@hostname/database_name'
db = SQLAlchemy(app)

class ASIN(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String(10), nullable=False)

@app.route('/', methods=['POST'])
def store_asin():
    asin_id = request.form['asin']
    asin = ASIN(asin=asin_id)
    db.session.add(asin)
    db.session.commit()
    return 'ASIN stored successfully.'

if __name__ == '__main__':
    app.run(debug=True)
