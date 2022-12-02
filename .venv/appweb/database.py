import mysql.connector
mysqlconexion = mysql.connector.connect (user='root', password='', host='localhost', database='sitio')
print(mysqlconexion)


""" 
# conectar a BD
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sitio'
mysql.init_app(app)


# conectar a página EGRESADOS
# llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `egresados`")
    egresados=cursor.fetchall()
    conexion.commit()
    print(egresados) #solo sirve para verificar la consulta en consola

# conectar a página EMPRESAS
# llamar a conectar BD y ejecutar QUERY    
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `empresas`")
    empresas=cursor.fetchall()
    conexion.commit()
    print(empresas) #solo sirve para verificar la consulta en consola


# conectar a página CV
# llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT `cv` FROM `egresados`")
    cv=cursor.fetchall()
    conexion.commit()
    print(cv) #solo sirve para verificar la consulta en consola

 #------------------------------ EGRESADOS -------------------------------------------

# conectar a página ADMIN EMPRESAS2 consultando BD
# llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `empresas`")
    empresas=cursor.fetchall()
    conexion.commit()
    print(empresas) #solo sirve para verificar la consulta en consola

# guardar en BD ADMIN EMPRESAS2 GUARDAR
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

# conectar a página ADMIN EMPRESAS3 consultando BD
# llamar a conectar BD y ejecutar QUERY
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `empresas`")
    empresas=cursor.fetchall()
    conexion.commit()
    print(empresas) #solo sirve para verificar la consulta en consola

 # borrar registro en BD ADMIN EMPRESAS BORRAR2
 #conectar cursor ejecutar y commit en BD para borrar imágenes
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `empresas` WHERE id=%s", (_id)) #ejecutar selección de imégenes en BD
    empresa=cursor.fetchall() #muestra todos los datos de empresa que hay en BD
    conexion.commit()
    print(empresa)
#conectar cursor ejecutar y commit en BD para borrar brochures
    conexion2=mysql.connect()
    cursor2=conexion2.cursor()
    cursor2.execute("SELECT brc FROM `empresas` WHERE id=%s", (_id)) #ejecutar selección de imégenes en BD
    empresa2=cursor2.fetchall() #muestra todos los datos de brochures que hay en BD para ese id
    conexion2.commit()
    print(empresa2)
#conectar cursor ejecutar y commit en BD para borrar registro en BD
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM empresas WHERE id=%s", (_id))
    conexion.commit()
    # redirecionar a la página actualizada en la conexion 'admin/empresas'
    return redirect('/admin/empresas3')

# guardar en BD ADMIN EGRESADOS ACTUALIZAR2
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

"""
