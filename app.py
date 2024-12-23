from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Запрос случайной цитаты из API
    response = requests.get('https://quoteslate.vercel.app/quotes/random')
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data['quote']
        author = quote_data['author']
    else:
        quote = "Не удалось получить цитату."
        author = ""

    return render_template('index.html', quote=quote, author=author)

if __name__ == "__main__":
    app.run(debug=True)
