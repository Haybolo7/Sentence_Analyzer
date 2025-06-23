from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_word_info(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        try:
            meaning = data[0]['meanings'][0]['definitions'][0]['definition']
            pos = data[0]['meanings'][0]['partOfSpeech']
            return {
                "word": word,
                "meaning": meaning,
                "part_of_speech": pos,
                "length": len(word)
            }
        except (IndexError, KeyError):
            pass

    return {
        "word": word,
        "meaning": "Not found",
        "part_of_speech": "Unknown",
        "length": len(word)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []

    if request.method == 'POST':
        sentence = request.form['sentence']
        words = sentence.strip().split()

        for word in words:
            info = get_word_info(word.strip('.,!?'))
            results.append(info)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
