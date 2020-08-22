from xml.dom import minidom
def lectorXML(archivo):
    doc = minidom.parse(archivo)
    print("==========XML==========")

    empleados = doc.getElementsByTagName("empleado")

    for empleado in empleados:
        nombre = empleado.getElementsByTagName("nombre")[0]
        edad = empleado.getElementsByTagName("edad")[0]
        #sid = empleado.getAttribute("id")
        username = empleado.getElementsByTagName("username")[0]
        password = empleado.getElementsByTagName("password")[0]
        print("nombre:%s" % nombre.firstChild.data)
        print("edad:%s" % edad.firstChild.data)
        print("username:%s" % username.firstChild.data)
        print("password:%s" % password.firstChild.data)
        print("\n")