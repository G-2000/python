from Election import db
from flask_sqlalchemy import SQLAlchemy


selected = db.Table('selected',
                    db.Column('student_id',db.Integer,db.ForeignKey('student.name')),
                    db.Column('course_id', db.Integer, db.ForeignKey('course.name')),
                    extend_existing=True)


class Student(db.Model):
    __tablename__ = 'student'
    
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR(20), nullable=False)
    password = db.Column(db.VARCHAR(20), nullable=False)
    
    course = db.relationship('Course',secondary=selected, backref='student')
    
    def __int__(self,name,password):
        self.user=name
        self.pwd=password

class Course(db.Model):
    __tablename__ = 'course'
    
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.VARCHAR(20),nullable=False)
    teacher = db.Column(db.VARCHAR(20),nullable=False)
    class_room = db.Column(db.VARCHAR(20),nullable=False)
    score = db.Column(db.VARCHAR(20),nullable=False)
    
    
    def __init__(self,name,teacher,class_room,is_required):
        self.name = name
        self.teacher = teacher
        self.class_room = class_room
        self.required = is_required


class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    student_name = db.Column('student_name',db.Integer,db.ForeignKey('student.name'))
    course_name = db.Column('course_name', db.Integer, db.ForeignKey('course.name'))
    classes = db.Column(db.VARCHAR(140),nullable=False)
    teachers = db.Column(db.VARCHAR(140),nullable=False)


def Student2Dict(std):
    return {
        'id':std.id,
        'name':std.name,
        'password':std.password
}

def Course2Dict(cus):
    return {
        'id':cus.id,
        'name':cus.name,
        'teacher':cus.teacher,
        'class_room':cus.class_room,
        'required':cus.required
}

# std.course.append(some_course)
# db.session.commit()









