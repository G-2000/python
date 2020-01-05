from flask import Flask,render_template,session,g,redirect,url_for,abort,request,flash,jsonify,json
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



import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Line

df1 = pd.read_csv("Election/oneenergy.csv", encoding='utf-8')
regions_available = list(df1.观测指标.dropna().unique())
@app.route('/election/',methods=['GET'])
@app.route('/election/<username>/')
def election(username = None):

    data_str = df1.to_html()
    if session.get('logged_in') is None:
        return render_template('hint.html',
                               the_res=data_str,
                               the_select_region=regions_available)
    elif username is None:
        return redirect(url_for('election', username=session.get('name')))
    return render_template('election.html',user_name=username)


@app.route('/hurun', methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df1.query("观测指标=='{}'".format(the_region))
    #     df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
    #     print(df_summary.head(5)) # 在后台检查描述性统计
    #     ## user select
    # print(dfs)
    #     # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="年份", y=["广州市", "深圳市", "佛山市", "揭阳市"], asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    #     # plotly.offline.plot(data, filename='file.html')

    #     with open("render.html", encoding="utf8", mode="r") as f:
    #         plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=regions_available,
                           )


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

@app.route('/election/<username>/result2')
def result2(username = None):
    return render_template('results2.html',user_name=session.get('name'))





@app.route('/get_selected')
def get_selected():
    course_list = Course.query.filter(Course.student.any(name=session.get('name'))).all()
    return json.dumps(course_list,default=Course2Dict)








# 准备工作


# cf.set_config_file(offline=True, theme="ggplot")
# py.offline.init_notebook_mode()




