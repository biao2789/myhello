from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.models import Message, Test
from sayhello.forms import HelloForm


@app.route('/', methods=["GET"])
def hello():
    return "hello flask!"


@app.route('/index', methods=["GET", "POST"])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    test = Test("biao")
    # print(test.name)
    form = HelloForm()
    # test = 1
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash("commit success!")
        return redirect(url_for("index"))
    return render_template("index.html",
                           form=form,
                           messages=messages,
                           test=test)
