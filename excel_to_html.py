from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_excel('ai_tools.xlsx')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
