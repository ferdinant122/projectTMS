from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'Randil Tennskoon',
        'title': 'First Blog Post',
        'content': 'First Blog Content',
        'date_posted': 'March 21st, 2021'
    },
    {
        'author': 'Kasun Bandara',
        'title': 'Second Blog Post',
        'content': 'Second Blog Content',
        'date_posted': 'April 12th, 2021'
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/view')
def view():
    return render_template('view.html', title='View')


if __name__ == '__main__':
    app.run(debug=True)



