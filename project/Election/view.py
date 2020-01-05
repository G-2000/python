from flask import render_template,session,g,redirect,url_for,abort,request,flash,jsonify,json
from Election import app,db
from .model import Course,Student,Student2Dict,Course2Dict

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['name'] != 'zuoye':
            error = 'Invalid username'
        elif request.form['password'] != '666':
             error = 'Invalid password'
        else:
             session['logged_in'] = True
             session['name']=request.form['name']
             flash('You were lgoged in')
             return redirect(url_for('election',username=session.get('name')))
    return render_template('login.html')

@app.route('/feedback')
def feedback(username = None):
    return render_template('feedback.html',user_name=username)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('name', None)
    flash('You have logged out')
    return redirect(url_for('election'))

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('election'))

@app.route('/election/')
@app.route('/election/<username>/')
def election(username = None):
    if session.get('logged_in') is None:
        return render_template('hint.html')
    elif username is None:
        return redirect(url_for('election', username=session.get('name')))
    return render_template('election.html',user_name=username)


#@app.route('/confirm', methods=['POST'])
#def confirm():
#    selected_course = json.loads(request.form.get('courses'))
#    user = Student.query.filter(Student.name == session.get('name')).first()
#    print(type(selected_course))
#    for x in selected_course:
#        print(x)
#    for x in selected_course:
#        tmp_course = Course.query.filter(Course.name==x).first()
#        user.course.append(tmp_course)
#    db.session.commit()
#    return redirect(url_for('election', username=session.get('name')))

@app.route('/election/<username>/selected')
def selected(username = None):
    return render_template('selected.html',user_name=session.get('name'))

@app.route('/election/<username>/feedback')
def feedback2(username = None):
    return render_template('feedback.html',user_name=session.get('name'))

@app.route('/election/<username>/survey')
def survey2(username = None):
    return render_template('survey.html',user_name=session.get('name'))

@app.route('/election/<username>/feedbackbase')
def feedbackbase2(username = None):
    return render_template('feedbackbase.html',user_name=session.get('name'))

@app.route('/election/<username>/result')
def result2(username = None):
    return render_template('result.html',user_name=session.get('name'))





@app.route('/get_selected')
def get_selected():
    course_list = Course.query.filter(Course.student.any(name=session.get('name'))).all()
    return json.dumps(course_list,default=Course2Dict)
