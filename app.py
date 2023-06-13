from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'columns': ['N kort', '60s', '54s', 'Db', 'As', 'Cb', 'Bb', 'Ds', '47b', 'Finish'],
        'rows': [
            ['COG', 342, 88, 124, 347, 124, 355, 219, 16, 259],
            ['TWA', 0, 0, 0, 0, 0, 0, 0, 0, 0] # Empty for calculation
        ],
        'columns2': ['N lang', '60s', '54s', 'Db', 'As', 'Cb', 'Bb', 'Ds', 'As', 'Cb', 'Bb', 'Cb', 'Bb', 'Ds', '47b', 'Finish'],
        'rows2': [
            ['COG', 342, 88, 124, 347, 124, 355, 219, 347, 124, 355, 175, 355, 219, 16, 259],
            ['TWA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Empty for calculation
        ],
        'columns3': ['NO kort', '60s', '47s', 'Db', 'Bb', 'Db', 'Bb', 'Db', 'Bb', 'Finish'],
        'rows3': [
            ['COG', 342,81,196,40,220,40,220,40,255],
            ['TWA', 0, 0, 0, 0, 0, 0, 0, 0, 0] # Empty for calculation
        ],
        'columns4': ['NO lang', '60s', '47s', 'Db', 'Bb', 'Db', 'Bb', 'Db', 'Bb', 'Db', 'Bb', 'Finish'],
        'rows4': [
            ['COG', 342,81,196,40,220,40,220,40,220,40,255],
            ['TWA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Empty for calculation
        ],
        'columns5': ['O kort', '60s', '48b', '47b', '48b', 'Finish'],
        'rows5': [
            ['COG', 342,81,267,40,265],
            ['TWA', 0, 0, 0, 0, 0] # Empty for calculation
        ],
        'columns6': ['O lang', '60s', '46b', '45b', '46b', '45b', '46b', 'Finish'],
        'rows6': [
            ['COG', 342,83,267,87,267,87,264],
            ['TWA', 0, 0, 0, 0, 0, 0, 0] # Empty for calculation
        ],
        'columns7': ['ZO kort', '60s', '49s', 'Cb', 'Ab', 'Cb', 'Ab', 'Cb', 'Ab', 'Finish'],
        'rows7': [
            ['COG', 342,81,108,304,124,304,124,304,243],
            ['TWA', 0, 0, 0, 0, 0, 0, 0, 0, 0] # Empty for calculation
        ],
        'columns8': ['ZO lang', '60s', '49s', 'Cb', 'Ab', 'Cb', 'Ab', 'Cb', 'Ab', 'Cb', 'Ab', 'Cb', 'Ab', 'Finish'],
        'rows8': [
            ['COG', 342,81,108,304,124,304,124,304,124,304,124,304,243],
            ['TWA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Empty for calculation
        ]
    }
    return render_template('table.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
