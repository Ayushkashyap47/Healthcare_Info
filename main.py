from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db= yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db["mysql_host"]
app.config['MYSQL_USER'] = db["mysql_user"]
app.config['MYSQL_PASSWORD'] = db["mysql_password"]
app.config['MYSQL_DB'] = db["mysql_db"]

mysql=MySQL(app)
@app.route("/" , methods=["GET","POST"])
def name():
    if request.method == 'POST':
        patientDetails= request.form
        patient_name = patientDetails['patient_name']
        aadhar_number = patientDetails['aadhar_number']
        uhn = patientDetails['uhn']
        symptoms = patientDetails['symptoms']
        medicine_prescribed = patientDetails['medicine_prescribed']
        comments = patientDetails['comments']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO patient_records (patient_name, aadhar_number, uhn, symptoms, medicine_prescribed, comments) VALUES (%s,%s,%s,%s,%s,%s)", (patient_name,aadhar_number ,uhn ,symptoms ,medicine_prescribed,comments ))
        mysql.connection.commit()
        cur.close()
        return "success"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


