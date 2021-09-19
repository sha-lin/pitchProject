from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user
from . import main
from .forms import UpdateProfile, AddPitch, CommentForm
from ..models import User, Pitch, Comment
from .. import db


# Views
@main.route('/')
def index():
    """
    Function that renders the index.html file
    """
    # pitches = Pitch.query.all()
    users = User.query.all()
    title = 'Welcome to pitches!'
    return render_template('index.html',title = title, users = users)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    pitches = Pitch.query.filter_by(user_id = user.id).all()
    pitches_count = Pitch.count_pitches(uname)
    
    return render_template("profile/profile.html", user=user,pitches=pitches,pitches_count=pitches_count)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form, user = user)




@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def add_pitch():
    form = AddPitch()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data

        # Updated pitch instance
        new_pitch = Pitch(title=title,description=pitch,category=category, user = current_user, upvotes=0,downvotes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html',title = title,pitch_form=form )

@main.route('/pitches/<category>')
def get_pitches_category(category):

    pitches = Pitch.get_pitches(category)

    return render_template("index.html", pitches = pitches)

@main.route('/pitch/<int:id>', methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.posted.strftime('%b %d, %Y')

    if request.args.get("upvote"):
        pitch.upvotes += 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("downvote"):
        pitch.downvotes += 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(content = comment,user = current_user,pitch_id = pitch.id)

        new_comment.save_comment()


    comments = Pitch.get_comments(pitch)

    return render_template("pitch.html", pitch = pitch, comment_form = comment_form, comments = comments, date = posted_date)
