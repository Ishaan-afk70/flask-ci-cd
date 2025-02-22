from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return home()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
