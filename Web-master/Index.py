######################################################
import os, cx_Oracle
from flask import Flask, request, flash, redirect, jsonify
from flask import render_template
import flask_excel as excel

from query.device import QueryDevices
from forms.device import HistorialForm
from forms.excel  import ExcelForm


app = Flask('__main__')
os.environ['PATH'] += r';E:\dbdriver\instantclient_11_2'
app.config['SECRET_KEY'] = 'you-will-never-guess'
excel.init_excel(app)

ip = '10.167.52.241'
port = 1521
SID = 'EPCMABP2'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connection = cx_Oracle.connect('TFADBO77', 'TFADBO77', dsn_tns)

_db_cur = connection.cursor()

query_devices = QueryDevices(connection)



@app.route('/historial', methods=['GET', 'POST'])
def historial():
    title = 'Historial'
    form = HistorialForm()
    if form.validate_on_submit() and request.method == 'POST':
        results = query_devices.getDeviceHistoryBySAPID(form.sap_id.data)
        return render_template('historial.html', title=title, form=form, results=results)
    
    return render_template('historial.html', title=title, form=form)


# print(request.get_array(field_name='file'))
# return jsonify({"result": request.get_array(field_name='file')})
@app.route('/excel-upload', methods=['GET', 'POST'])
def upload():
    form = ExcelForm()
    if form.validate_on_submit():
        f = form.excel_file.name
        
        flying_data = request.get_array(field_name=f)

        return render_template('upload-excel.html',  form=form, results=flying_data)
        #return redirect(url_for('index'))

    return render_template('upload-excel.html', form=form)

@app.route('/')
def index():
    _db_cur.execute("select * from PC9_DEVICE_DISC_RATE")
    for result in _db_cur:
        print (result)

@app.route('/Modificacion')
def Modificacion():
    #Adjunto = tk()
    #Adjunto.filename= filedialog.askopenfilename(filetypes = (("Excel .xls","*.xls"),("All files","*.*")))
    return 'Prueba'

@app.route('/Alta')
def Alta():
    return 'Alta de producto'

@app.route('/Baja')
def Baja():
    return 'Baja de producto'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
