import pymysql

class DataBase:
    def __init__(self):
            self.connection = pymysql.connect(
                host= '3.130.126.210',
                port= 3309,
                user='pruebas',
                password='VGbt3Day5R',
                db='habi_db',
               
            )
             
            self.cursor = self.connection.cursor()

            print("Conexíon establecida exitosamente")

    def select_propertys(self, id):
        sql = "SELECT * FROM status_history JOIN property ON status_history.property_id = property.id JOIN status ON status_history.status_id = status.id WHERE property.year ={}".format(id)
            #llamar solo columnas que se necesitan para hacer mas efectiva la busqueda
        try:
            self.cursor.execute(sql)
            propertyss = self.cursor.fetchall()

            for propertys in propertyss:

                print("ID", propertys[0])
                print("Direccion", propertys[5])
                print("Ciudad", propertys[6])
                print("Precio", propertys[7])
                print("Descripcion", propertys[8])
                print("Año", propertys[9])
                print("Estado:", propertys[11])
                print("Descripcion estado:", propertys[12])
                print("_______\n")

        except Exception as e:
            raise

year=int(input('Ingrese año de construccion:'))
    #Agregar comentario de años disponibles y condicinal para que el año seleccionado no sea mayor al año actual
database = DataBase()
database.select_propertys(year)