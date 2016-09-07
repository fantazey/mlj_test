from task import db
from flask import jsonify


class Employees(db.Model):
    __tablename__ = 'employees'
    emp_no = db.Column(db.Integer, primary_key=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.VARCHAR(16), nullable=False)
    last_name = db.Column(db.VARCHAR(16), nullable=False)
    gender = db.Column(db.Enum, nullable=False)

    def __repr__(self):
        return jsonify({
            'emp_no': self.emp_no,
            'birth_date': self.birth_date,
            'hire_date': self.hire_date,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender
        })


class Departments(db.Model):
    __tablename__ = 'departments'
    dept_no = db.Column(db.CHAR(4), primary_key=True, nullable=False)
    dept_name = db.Column(db.Text, unique=True, nullable=False)


class DeptEmp(db.Model):
    __tablename__ = 'dept_emp'
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'), primary_key=True)
    dept_no = db.Column(db.CHAR(4), db.ForeignKey('departments.dept_no'), primary_key=True)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return jsonify({
            'emp_no': self.emp_no,
            'dept_no': self.dept_no,
            'from_date': self.from_date,
            'to_date': self.to_date
        })