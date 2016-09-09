from task import db
from marshmallow_jsonapi import Schema, fields
from marshmallow_jsonapi.flask import Relationship


class Employees(db.Model):
    __tablename__ = 'employees'
    id = db.Column('emp_no', db.Integer, primary_key=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.VARCHAR(16), nullable=False)
    last_name = db.Column(db.VARCHAR(16), nullable=False)
    gender = db.Column(db.Enum, nullable=False)


class EmployeesSchema(Schema):
    id = fields.Str(dump_only=True)
    birth_date = fields.Date(required=True)
    hire_date = fields.Date(required=True)
    first_name = fields.Str(required=True)
    gender = fields.Str()

    department = Relationship(
        related_view='department_detail',
        include_data=True,
        type_='departments'
    )

    class Meta:
        type_ = 'employees'


class Departments(db.Model):
    __tablename__ = 'departments'
    id = db.Column('dept_no', db.CHAR(4), primary_key=True, nullable=False)
    dept_name = db.Column(db.Text, unique=True, nullable=False)


class DepartmentsSchema(Schema):
    id = fields.Str(dump_only=True)
    dept_name = fields.Str(required=True)

    employees = Relationship(
        include_data=True,
        type_='employees'
    )

    class Meta:
        type_ = 'departments'


class DeptEmp(db.Model):
    __tablename__ = 'dept_emp'
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'), primary_key=True)
    dept_no = db.Column(db.CHAR(4), db.ForeignKey('departments.dept_no'), primary_key=True)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)


class DeptEmpSchema(Schema):
    id = fields.Str(dump_only=True)
    dept_no = fields.Str(dump_only=True)
    from_date = fields.Date()
    to_date = fields.Date()

    class Meta:
        type_ = 'dept_emp'