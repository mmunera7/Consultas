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
        sql = "SELECT * FROM property JOIN ( SELECT sh.* FROM status_history sh INNER JOIN (SELECT property_id, MAX(update_date) last_update FROM status_history sh GROUP BY 1) sh1 ON sh.property_id = sh1.property_id AND sh.update_date = sh1.last_update) sh ON sh.property_id = habi_db.property.id JOIN habi_db.status ON sh.status_id = habi_db.status.id WHERE status.name ='{}';".format(id)
                #llamar solo columnas que se necesitan para hacer mas efectiva la busqueda 
                #agregar condicion para generar solo el ultimo estado disponible
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

status=str(input('ingrese estado del inmueble que sea consultar:'))
    #cambir por botones que solo tenga los estados disponibles
database = DataBase()
database.select_propertys(status)