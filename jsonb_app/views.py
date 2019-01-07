from flask import render_template,request,redirect
from jsonb_app import app,db
from  jsonb_app.models import Book

@app.route('/')
@app.route('/list')
def list():
    return  render_template('list.html',books=Book.query.all())

@app.route('/add')
def add_get():
    return render_template('book.html')

@app.route('/add',methods=["POST"])
def add_post():
    form_data={
                "title":request.form["txtTitle"],
                "publish_year":request.form["txtPublishedYear"],
                "genres":request.form.getlist('chkGeneres')
    }
    book = Book(data=form_data)
    db.session.add(book)
    db.session.commit()

    return redirect('/list')

@app.route('/edit/<id_>')
def edit_get(id_):
    book = Book.query.filter_by(id_=id_).first()
    print(book.data['genres'])
    return render_template('edit.html',
                            book=book,
                            genres_list=book.data['genres'])




