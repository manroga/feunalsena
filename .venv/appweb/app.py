# importa las librerias que se necesitan
import os
import mysql.connector
from flask import Flask, render_template, request, redirect, send_from_directory, session, url_for # metodos para renderizar, requerir, redireccionar, enviar desde directorio, abrir sesiones,
from flaskext.mysql import MySQL #metodo para usar los script de MySQL
from datetime import datetime #metodo para poner tiempo exacto para que las imagenes con nombre duplicado queden diferentes
from werkzeug.utils import secure_filename

# le da nombre a la app por medio de Flask. Siempre se escribe
app=Flask(__name__)
app.secret_key="feunal" 
# conectar a BD
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sitio'
mysql.init_app(app)

# conectar a página INDEX
@app.route('/')
def inicio():
    return render_template('/sitio/index.html')

# imagenes
@app.route('/img/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/img'),imagen)

# imagenes website
@app.route('/img/website/<imagenweb>')
def imageneswebsite(imagenweb):
    print(imagenweb)
    return send_from_directory(os.path.join('templates/sitio/img/website'),imagenweb)

# imagenes Egresados
@app.route('/img/egresados/<imagenegresado>')
def imagenesegresados(imagenegresado):
    print(imagenegresado)
    return send_from_directory(os.path.join('templates/sitio/img/egresados'),imagenegresado)
    
# imagenes Empresas
@app.route('/img/empresas/<imagenempresa>')
def imagenesempresas(imagenempresa):
    print(imagenempresa)
    return send_from_directory(os.path.join('templates/sitio/img/empresas'),imagenempresa)

# cvs
@app.route('/cvs/<cv>')
def cvs(cv):
    print(cv)
    return send_from_directory(os.path.join('templates/sitio/cvs'),cv)

# brcs
@app.route('/brcs/<brc>')
def brcs(brc):
    print(brc)
    return send_from_directory(os.path.join('templates/sitio/brcs'),brc)

# css
@app.route('/css/<archivocss>')
def css_link(archivocss):
    return send_from_directory(os.path.join('templates/sitio/css'),archivocss)

# conectar a página EGRESADOS
@app.route('/egresados')
def egresados():

    # llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `egresados`")
    egresados=cursor.fetchall()
    conexion.commit()
    print(egresados) #solo sirve para verificar la consulta en consola

    # mostrar query en página libros.html del SITIO. Ojo a libros y libros, el primero toma el nombre del segundo
    return render_template('/sitio/egresados.html', egresados=egresados)

# conectar a página EMPRESAS
@app.route('/empresas')
def empresas():

    # llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `empresas`")
    empresas=cursor.fetchall()
    conexion.commit()
    print(empresas) #solo sirve para verificar la consulta en consola

    # mostrar query en página libros.html del SITIO. Ojo a libros y libros, el primero toma el nombre del segundo
    return render_template('/sitio/empresas.html', empresas=empresas)


# conectar a página NOSOTROS
@app.route('/nosotros')
def nosotros():
    return render_template('/sitio/nosotros.html')  

# conectar a página CV
@app.route('/cv')
def cv():

    # llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT `cv` FROM `egresados`")
    cv=cursor.fetchall()
    conexion.commit()
    print(cv) #solo sirve para verificar la consulta en consola

    # mostrar query en página libros.html del SITIO. Ojo a libros y libros, el primero toma el nombre del segundo
    return render_template('/sitio/cv.html', cv=cv) 

# conectar a página INDEX ADMINISTRADOR
@app.route('/admin/')
def admin_index():
    
    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")
    
    return render_template('admin/index.html')
    

# conectar a página LOGIN
@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html') 

# validar usuario y contraseña en la página login
@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    _usuario=request.form['txtUsuario'] #pide los datos desde el formulario
    _password=request.form['txtPassword'] #pide los datos desde el formulario
    print (_usuario) #solo sirve para verificar la consulta en consola
    print (_password) #solo sirve para verificar la consulta en consola

    if _usuario=="admin" and _password=="123": #procedimiento para verificar si concuerdan los datos. con BD se pregunta mediante un WHERE usuario == admin y password==123.
        session["login"]=True #si la operacion anterior devuelve un true hace lo que está desde esta linea incluida.
        session["usuario"]="Administrador"
        return redirect ("/admin") #si concuerdan los datos lo envia al inicio de admin

    return render_template('/admin/login.html', mensaje="Acceso Denegado") # No concuerdan los datos lo envia a login de nuevo


# conectar a página ADMIN CERRAR
@app.route('/admin/cerrar')
def admin_login_cerrar():
    session.clear()  # cierra sesion
    return redirect ('/admin/login') # redirecciona a login




  #------------------------------ EGRESADOS -------------------------------------------

  # conectar a página ADMIN EGRESADOS2 consultando BD
@app.route('/admin/egresados2')
def admin_egresados2():

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")

    # llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `egresados`")
    egresados=cursor.fetchall()
    conexion.commit()
    print(egresados) #solo sirve para verificar la consulta en consola
    
    # mostrar query en página egresados.html del admin. Ojo a libros y libros, el primero toma el nombre del segundo
    return render_template('/admin/egresados2.html', egresados=egresados)



    # guardar en BD ADMIN EGRESADOS2 GUARDAR
@app.route('/admin/egresados/guardar2', methods=['POST'])
def admin_egresados_guardar2():

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")
    
    # pide la info del formulario para guardar en BD
    _nombre=request.form['txtNombre']
    _archivo=request.files['txtImagen'] # cambia a files para guardar un archivo en BD
    _cedula=request.form['txtCedula']  
    _cv=request.files['txtCv']  # cambia a files para guardar un archivo en BD 
    print (_cv,_cv.filename)
    

    tiempo=datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')#pone yyhhmmss en un string

    if _archivo.filename!="":
        nuevoNombre=horaActual+"_"+_archivo.filename #une el nombre con la hora actual
        _archivo.save(".venv/appweb/templates/sitio/img/"+nuevoNombre)#atento a la ruta. es relativa, pero debe ser completa a la raiz del sitio


    if _cv.filename!="":
        nuevoNombrecv=horaActual+"_"+_cv.filename #une el nombre con la hora actual
        _cv.save(".venv/appweb/templates/sitio/cvs/"+nuevoNombrecv)#atento a la ruta. es relativa, pero debe ser completa a la raiz del sitio

    # parametrizar query en BD
    sql="INSERT INTO `egresados` (`id`, `nombre`, `imagen`, `cedula`, `cv`) VALUES (NULL, %s, %s, %s, %s);" 
    datos=(_nombre,nuevoNombre,_cedula,nuevoNombrecv) #el nuevonombre se actualizó para que aparezca con la hora actual.
    # conectar con BD
    conexion=mysql.connect() 
    # crear cursor en BD para poder ejecutar
    cursor=conexion.cursor()
    # ejecutar cursor uniendo el query con los datos del formulario hacia la BD
    cursor.execute(sql,datos)
    # ejecutar la conexion a la BD
    conexion.commit()
    #imprime nombre, url y archivo en la consola. (para verificar que esté funcionando) 
    print (_nombre)
    print (_archivo)
    print (_cedula)
    print (_cv)
    
    # redirecionar a la página actualizada en la conexion 'admin/egresados'
    return redirect('/admin/egresados3')  


    # borrar registro en BD ADMIN EGRESADOS BORRAR
@app.route('/admin/egresados/borrar2', methods=['POST'])
def admin_egresados_borrar2():

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")
    
    _id=request.form['txtID']
    print (_id)

    #conectar cursor ejecutar y commit en BD para borrar imégenes
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `egresados` WHERE id=%s", (_id)) #ejecutar selección de imégenes en BD
    egresado=cursor.fetchall() #muestra todos los datos de libros que hay en BD
    conexion.commit()
    print(egresado)

    if os.path.exists(".venv/appweb/templates/sitio/img/"+str(egresado[0][0])): #Verificar si existe la imagen a borrar
        os.unlink(".venv/appweb/templates/sitio/img/"+str(egresado[0][0])) #borra la imagen asociada al registro

    _id=request.form['txtID']
    print (_id)      
    #conectar cursor ejecutar y commit en BD para borrar CVs
    conexion2=mysql.connect()
    cursor2=conexion2.cursor()
    cursor2.execute("SELECT cv FROM `egresados` WHERE id=%s", (_id)) #ejecutar selección de imégenes en BD
    egresado2=cursor2.fetchall() #muestra todos los datos de brochures que hay en BD para ese id
    conexion2.commit()
    print(egresado2)

    if os.path.exists(".venv/appweb/templates/sitio/cvs/"+str(egresado2[0][0])): #Verificar si existe la imagen a borrar
        os.unlink(".venv/appweb/templates/sitio/cvs/"+str(egresado2[0][0])) #borra la imagen asociada al registro

    #conectar cursor ejecutar y commit en BD para borrar registro en BD
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM egresados WHERE id=%s", (_id))
    conexion.commit()
    # redirecionar a la página actualizada en la conexion 'admin/egresados'
    return redirect('/admin/egresados3')



# conectar a página ADMIN EGRESADOS3 consultando BD
@app.route('/admin/egresados3')
def admin_egresados3():

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")

    # llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `egresados`")
    egresados=cursor.fetchall()
    conexion.commit()
    print(egresados) #solo sirve para verificar la consulta en consola
    
    # mostrar query en página egresados.html del admin. Ojo a libros y libros, el primero toma el nombre del segundo
    return render_template('/admin/egresados3.html', egresados=egresados)

# guardar en BD ADMIN EGRESADOS ACTUALIZAR2

@app.route('/admin/egresados/actualizar2/<string:_id>', methods=['POST'])
def admin_egresados_actualizar2(_id):

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")
    
    # pide la info del formulario para guardar en BD
    _id=request.form['txtID']
    _nombre=request.form['txtNombre']
    _archivo=request.files['txtImagen'] # cambia a files para guardar un archivo en BD
    _cedula=request.form['txtCedula']  
    _cv=request.files['txtCv']  # cambia a files para guardar un archivo en BD 
    print (_cv,_cv.filename, _id)
    

    tiempo=datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')#pone yyhhmmss en un string

    if _archivo.filename!="":
        nuevoNombre=horaActual+"_"+_archivo.filename #une el nombre con la hora actual
        _archivo.save(".venv/appweb/templates/sitio/img/"+nuevoNombre)#atento a la ruta. es relativa, pero debe ser completa a la raiz del sitio


    if _cv.filename!="":
        nuevoNombrecv=horaActual+"_"+_cv.filename #une el nombre con la hora actual
        _cv.save(".venv/appweb/templates/sitio/cvs/"+nuevoNombrecv)#atento a la ruta. es relativa, pero debe ser completa a la raiz del sitio

    
    if _nombre and _archivo and _cedula and _cv:
            
            sql="UPDATE egresados SET imagen = %s, nombre = %s, cedula = %s, cv = %s WHERE id=%s"
            datos=(nuevoNombre, _nombre, _cedula, nuevoNombrecv, _id)
    
    # conectar con BD
    conexion=mysql.connect() 
    # crear cursor en BD para poder ejecutar
    cursor=conexion.cursor()
    # ejecutar cursor uniendo el query con los datos del formulario hacia la BD
    cursor.execute(sql,datos)
    # ejecutar la conexion a la BD
    conexion.commit()
    #imprime nombre, url y archivo en la consola. (para verificar que esté funcionando) 
    print (_nombre)
    print (_archivo)
    print (_cedula)
    print (_cv)
    print (_id)
    
    # redirecionar a la página actualizada en la conexion 'admin/egresados'
    return redirect('/admin/egresados3')  



#---------------------------------------EMPRESAS-------------------------------------------------------------


  # conectar a página ADMIN EMPRESAS2 consultando BD
@app.route('/admin/empresas2')
def admin_empresas2():

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")

    # llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `empresas`")
    empresas=cursor.fetchall()
    conexion.commit()
    print(empresas) #solo sirve para verificar la consulta en consola
    
    # mostrar query en página egresados.html del admin. Ojo a libros y libros, el primero toma el nombre del segundo
    return render_template('/admin/empresas2.html', empresas=empresas)



   # guardar en BD ADMIN EMPRESAS2 GUARDAR
@app.route('/admin/empresas2/guardar2', methods=['POST'])
def admin_empresas_guardar2():

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")
    
    # pide la info del formulario para guardar en BD
    _nombre=request.form['txtNombre']
    _archivo=request.files['txtImagen'] # cambia a files para guardar un archivo en BD
    _nit=request.form['txtNit']  
    _brc=request.files['txtBrc']  # cambia a files para guardar un archivo en BD 
    print (_brc,_brc.filename)
    

    tiempo=datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')#pone yyhhmmss en un string

    if _archivo.filename!="":
        nuevoNombreimg=horaActual+"_"+_archivo.filename #une el nombre con la hora actual
        _archivo.save(".venv/appweb/templates/sitio/img/"+nuevoNombreimg)#atento a la ruta. es relativa, pero debe ser completa a la raiz del sitio


    if _brc.filename!="":
        nuevoNombrebrc=horaActual+"_"+_brc.filename #une el nombre con la hora actual
        _brc.save(".venv/appweb/templates/sitio/brcs/"+nuevoNombrebrc)#atento a la ruta. es relativa, pero debe ser completa a la raiz del sitio

    # parametrizar query en BD
    sql="INSERT INTO `empresas` (`id`, `nombre`, `imagen`, `nit`, `brc`) VALUES (NULL, %s, %s, %s, %s);" 
    datos=(_nombre,nuevoNombreimg,_nit,nuevoNombrebrc) #el nuevonombre se actualizó para que aparezca con la hora actual.
    # conectar con BD
    conexion=mysql.connect() 
    # crear cursor en BD para poder ejecutar
    cursor=conexion.cursor()
    # ejecutar cursor uniendo el query con los datos del formulario hacia la BD
    cursor.execute(sql,datos)
    # ejecutar la conexion a la BD
    conexion.commit()
    #imprime nombre, url y archivo en la consola. (para verificar que esté funcionando) 
    print (_nombre)
    print (_archivo)
    print (_nit)
    print (_brc)
    
    # redirecionar a la página actualizada en la conexion 'admin/egresados'
    return redirect('/admin/empresas3')  




     # conectar a página ADMIN EMPRESAS3 consultando BD
@app.route('/admin/empresas3')
def admin_empresas3():

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")

    # llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `empresas`")
    empresas=cursor.fetchall()
    conexion.commit()
    print(empresas) #solo sirve para verificar la consulta en consola
    
    # mostrar query en página empresas.html del admin. Ojo a libros y libros, el primero toma el nombre del segundo
    return render_template('/admin/empresas3.html', empresas=empresas)


 # borrar registro en BD ADMIN EMPRESAS BORRAR2
@app.route('/admin/empresas/borrar2', methods=['POST'])
def admin_empresas_borrar2():

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")
    
    _id=request.form['txtID']
    print (_id)

    #conectar cursor ejecutar y commit en BD para borrar imágenes
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `empresas` WHERE id=%s", (_id)) #ejecutar selección de imégenes en BD
    empresa=cursor.fetchall() #muestra todos los datos de libros que hay en BD
    conexion.commit()
    print(empresa)

    if os.path.exists(".venv/appweb/templates/sitio/img/"+str(empresa[0][0])): #Verificar si existe la imagen a borrar
        os.unlink(".venv/appweb/templates/sitio/img/"+str(empresa[0][0])) #borra la imagen asociada al registro

    _id=request.form['txtID']
    print (_id)      
    #conectar cursor ejecutar y commit en BD para borrar brochures
    conexion2=mysql.connect()
    cursor2=conexion2.cursor()
    cursor2.execute("SELECT brc FROM `empresas` WHERE id=%s", (_id)) #ejecutar selección de imégenes en BD
    empresa2=cursor2.fetchall() #muestra todos los datos de brochures que hay en BD para ese id
    conexion2.commit()
    print(empresa2)

    if os.path.exists(".venv/appweb/templates/sitio/brcs/"+str(empresa2[0][0])): #Verificar si existe la imagen a borrar
        os.unlink(".venv/appweb/templates/sitio/brcs/"+str(empresa2[0][0])) #borra la imagen asociada al registro

    #conectar cursor ejecutar y commit en BD para borrar registro en BD
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM empresas WHERE id=%s", (_id))
    conexion.commit()
    # redirecionar a la página actualizada en la conexion 'admin/empresas'
    return redirect('/admin/empresas3')


# guardar en BD ADMIN EGRESADOS ACTUALIZAR2

@app.route('/admin/empresas/actualizar2/<string:_id>', methods=['POST'])
def admin_empresas_actualizar2(_id):

    if not 'login' in session: #verifica que la sesion se haya iniciado. de lo contrario envia al index del administrador
        return redirect("/admin/login")
    
    # pide la info del formulario para guardar en BD
    _id=request.form['txtID']
    _nombre=request.form['txtNombre']
    _archivo=request.files['txtImagen'] # cambia a files para guardar un archivo en BD
    _nit=request.form['txtNit']  
    _brc=request.files['txtBrc']  # cambia a files para guardar un archivo en BD 
    print (_brc,_brc.filename, _id)
    

    tiempo=datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')#pone yyhhmmss en un string

    if _archivo.filename!="":
        nuevoNombreimg=horaActual+"_"+_archivo.filename #une el nombre con la hora actual
        _archivo.save(".venv/appweb/templates/sitio/img/"+nuevoNombreimg)#atento a la ruta. es relativa, pero debe ser completa a la raiz del sitio


    if _brc.filename!="":
        nuevoNombrebrc=horaActual+"_"+_brc.filename #une el nombre con la hora actual
        _brc.save(".venv/appweb/templates/sitio/brcs/"+nuevoNombrebrc)#atento a la ruta. es relativa, pero debe ser completa a la raiz del sitio

    
    if _nombre and _archivo and _nit and _brc: # la condicion falla cuando algún dato falta. 
            
            sql="UPDATE empresas SET imagen = %s, nombre = %s, nit = %s, brc = %s WHERE id=%s"
            datos=(nuevoNombreimg, _nombre, _nit, nuevoNombrebrc, _id)
    
    # conectar con BD
    conexion=mysql.connect() 
    # crear cursor en BD para poder ejecutar
    cursor=conexion.cursor()
    # ejecutar cursor uniendo el query con los datos del formulario hacia la BD
    cursor.execute(sql,datos)
    # ejecutar la conexion a la BD
    conexion.commit()
    #imprime nombre, url y archivo en la consola. (para verificar que esté funcionando) 
    print (_nombre)
    print (_archivo)
    print (_nit)
    print (_brc)
    print (_id)
    
    # redirecionar a la página actualizada en la conexion 'admin/egresados'
    return redirect('/admin/empresas3')  


#----------------------------------------FIN-----------------------------------------------------------------

# llama a la app y la corre. algo asi como el constructor. Siempre se escribe.
if __name__ == '__main__':
    app.run(debug=True)
         