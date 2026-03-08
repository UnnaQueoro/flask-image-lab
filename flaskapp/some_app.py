from flask import Flask, render_template, request
import os
from net import chess_effect, create_histogram

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('simple.html')


@app.route('/process', methods=['POST'])
def process():

    file = request.files['file']
    percent = int(request.form['percent'])

    # сохраняем исходное изображение
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(original_path)

    # создаём шахматное изображение
    result_path = chess_effect(original_path, percent)

    # строим графики
    hist_original = create_histogram(original_path, "original")
    hist_result = create_histogram(result_path, "result")

    return render_template(
        "net.html",
        original=original_path,
        result=result_path,
        hist1=hist_original,
        hist2=hist_result
    )


if __name__ == "__main__":
    app.run(debug=True)