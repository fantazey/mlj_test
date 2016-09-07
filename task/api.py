from task import app, models, db
from flask import jsonify, request

@app.route('/api/departments', methods=['GET'])
def list_of_departments():
    depts = models.Departments.query.all()
    return jsonify(depts)

@app.route('/api/employees', methods=['GET'])
def list_of_employees():
    emps = models.Employees.query.all()
    return jsonify(emps)


@app.route('/api/employees', methods=['POST'])
def add_employees():
    emp = models.Employees(
        emp_no=request.json.get('emp_no'),
        birth_date=request.json.get('birth_date'),
        hire_date=request.json.get('hire_date'),
        first_name=request.json.get('first_name'),
        last_name=request.json.get('last_name'),
        gender=request.json.get('gender')
    )
    db.session.add(emp)
    dept_emp = models.DeptEmp(
        emp_no=emp.emp_no,
        dept_no=request.json.get('dept_no'),
        from_date=emp.hire_date,
        to_date=emp.hire_date
    )
    db.session.add(dept_emp)
    db.session.commit()


@app.route('/api/departments', methods=["POST"])
def add_dept():
    dept = models.Departments(
        dept_no=request.json.get('dept_no'),
        dept_name=request.json.get('dept_name')
    )
    db.session.add(dept)
    db.session.commit()