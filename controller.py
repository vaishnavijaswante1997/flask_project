from flask import request,render_template,redirect,url_for
from models import app,db,Employee


@app.route('/emp/create/',methods = ['GET','POST'])
def create():
    if request.method == "post":
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = Employee(name= name,age = age,position=position)
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('get_all_emps'))
    else:
        return render_template('createpage.html')
    

@app.route('/all-emps/')
def get_all_emps():
    emps = Employee.query.all()
    return render_template('allemps.html',employee = emps)


@app.route('/emp/<int:id>/')
def get_single_employee(id):
    single_emp = Employee.query.filter_by(id=id).first()
    if single_emp:
        return render_template('emp.html',employee = single_emp)
    return f"Employee with id {id} doesn't exist"
    

@app.route('/emp/<int:id>/update/',methods = ['get','post'])
def update(id):
    emp = Employee.query.filter_by(id=id).first()
    if request.method == "post":
        name = request.form ['name']
        age = request.form ['age']
        position = request.form ['position']
        emp.name = name
        emp.age = age
        emp.position = position
        db.session.commit()
        return redirect('/all-emps/')
    if emp:
        return render_template('update.html',employee = emp)
    
    else:
        return f"Employee ID:{id} Does not exist in database."






if __name__ == "__main__":
    app.run(host = "localhost",port = 5000,debug = True)




