from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vandyck'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful walk'
        },
        {
            'author': {'username': 'Esther'},
            'body': 'Lovely Site'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


app.run()
