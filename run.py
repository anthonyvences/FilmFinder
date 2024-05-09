from flask import Flask, render_template, request
import main
import sys
sys.path.append('.')

app = Flask(__name__, template_folder='.')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_name = request.form['movie']
        recommendations = main.recommend(movie_name)
        return render_template('index.html', recommendations=recommendations)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

