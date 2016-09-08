from datetime import datetime
from task import app, models, db
from flask import jsonify, request
# todo: handle errors


@app.route('/api/departments', methods=['GET'])
def list_of_departments():
    depts = models.Departments.query.all()
    data, errs = models.DepartmentsSchema(many=True).dump(depts)
    return jsonify(data)


@app.route('/api/employees', methods=['GET'])
def list_of_employees():
    start = datetime.now()
    emps = models.Employees.query.all()
    data, errs = models.EmployeesSchema(many=True).dump(emps)
    end = datetime.now()
    print end - start
    return jsonify(data)


@app.route('/api/employees', methods=['POST'])
def add_employees():
    emp = models.Employees(
        id=request.json.get('id'),
        birth_date=request.json.get('birth_date'),
        hire_date=request.json.get('hire_date'),
        first_name=request.json.get('first_name'),
        last_name=request.json.get('last_name'),
        gender=request.json.get('gender')
    )
    db.session.add(emp)
    db.session.commit()
    dept_emp = models.DeptEmp(
        emp_no=emp.id,
        dept_no=request.json.get('dept_no'),
        from_date=request.json.get('hire_date'),
        to_date=request.json.get('hire_date')
    )
    db.session.add(dept_emp)
    db.session.commit()
    emp_ = models.Employees.query.filter(models.Employees.id==request.json.get('id'))
    data, err = models.EmployeesSchema(many=True).dump(emp_)
    return jsonify(data)


@app.route('/api/departments', methods=["POST"])
def add_dept():
    dept = models.Departments(
        id=request.json.get('id'),
        dept_name=request.json.get('dept_name')
    )
    db.session.add(dept)
    db.session.commit()
    return jsonify({
    })