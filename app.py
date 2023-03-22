from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        package_name = request.form['package_name']
        with open('requirements.txt', 'a') as f:
            f.write(package_name + '\n')
        return 'Package name {} has been added to requirements.txt'.format(package_name)
    else:
        return render_template('index.html.jinja2')


if __name__ == '__main__':
    app.run()
