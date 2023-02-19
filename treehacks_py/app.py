import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


# from flask_sqlalchemy import SQLAlchemy

# # create the extension
# db = SQLAlchemy()
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "iris:///SQLAdmin:B!pM7XVUjuj11@k8s-743d0686-a6e900d2-91ad558ada-e138f0bd75318090.elb.us-east-1.amazonaws.com.1972/USER"
# # initialize the app with the extension
# db.init_app(app)

#function for connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'treehacks25'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

#follicle_r int, follicle_l int, weight_gain int, hair_growth int, skin_darkening int, cycle_r int, fast_food float,  pcos int

@app.route('/form', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        follicle_r = request.form['follicle_r']
        follicle_l = request.form['follicle_l']
        weight_gain = request.form['weight_gain']
        hair_growth = request.form['hair_growth']
        skin_darkening = request.form['skin_darkening']
        cycle_r = request.form['cycle_r']
        fast_food = request.form['fast_food']


        if not (follicle_r or follicle_l or weight_gain or hair_growth or skin_darkening or cycle_r or fast_food):
            flash('Question is required!')
        else:

            conn = get_db_connection()
            conn.execute('INSERT INTO pcos (follicle_r, follicle_l, weight_gain, hair_growth, skin_darkening, cycle_r, fast_food) VALUES (?,?,?,?,?,?,?)',
                        (follicle_r, follicle_l, weight_gain, hair_growth, skin_darkening, cycle_r, fast_food))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        
    return render_template('form.html')



# # create the extension
# db = sqlalchemy()
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "iris:///SQLAdmin:password@server.address/USER"
# # initialize the app with the extension
# db.init_app(app)