from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from Election import view, model

course1 = model.Course('信息可视化设计','赵景','期末评估','')
course2 = model.Course('线上调查与统计','王子佳','期末评估','')
course3 = model.Course('Python语言', '秦胜伟','期末评估','')
s = model.Student(name='171013057',password='nfu3057')

x = model.Course.query.all()
print(len(x))
y = model.Student.query.all()
print(len(y))
c1 = model.Course.query.filter(model.Course.student.any(name='171013057')).all()
print(len(c1))
z = model.Feedback.query.all()
print(len(z))
