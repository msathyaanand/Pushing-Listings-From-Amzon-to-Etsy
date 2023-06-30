from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        asin = request.form['asin']
        # You can perform further processing with the ASIN, such as passing it to the backend or performing validation
        return render_template('result.html', asin=asin)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
