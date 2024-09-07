from flask import Flask, render_template, request
from travel_logic import process_travel_request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        noe_safar = request.form['trip-type']
        noe_haml = request.form['transport']
        mabda = request.form['origin']
        nafarat = int(request.form['passengers'])
        nights = int(request.form['nights'])
        bodje = int(request.form['budget'])

        results = process_travel_request(noe_safar, noe_haml, mabda, nafarat, nights, bodje)
        return render_template('results.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)