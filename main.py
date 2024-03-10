from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, template_folder='.')

df = pd.read_csv("dictionary.csv")

# Define base URL for GitHub Pages link
BASE_URL = "https://rky5231.github.io/word-api"

@app.route('/')
def index():
    return render_template('index.html', base_url=BASE_URL)

@app.route("/api/v1/<word>")
def api(word):
    try:
        definition_series = df.loc[df['word'] == word]["definition"]
        if not definition_series.empty:
            definition = definition_series.squeeze()
            result_dictionary = {"word": word, "definition": definition}
            return result_dictionary
        else:
            return "Word not found, please check for spelling errors or try another word."

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
