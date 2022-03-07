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
        sql = "SELECT * FROM property JOIN ( SELECT sh.* FROM status_history sh INNER JOIN (SELECT property_id, MAX(update_date) last_update FROM status_history sh GROUP BY 1) sh1 ON sh.property_id = sh1.property_id AND sh.update_date = sh1.last_update) sh ON sh.property_id = habi_db.property.id JOIN habi_db.status ON sh.status_id = habi_db.status.id WHERE habi_db.property.city ='{}';".format(id)
            #llamar solo columnas que se necesitan para hacer mas efectiva la busqueda
        try:
            self.cursor.execute(sql)
            prop = self.cursor.fetchall()

            for propertys in prop:
                
                print("Direccion", propertys[1])
                print("Ciudad", propertys[2])
                print("Precio", propertys[3])
                print("Descripcion", propertys[4])
                print("Año", propertys[5])
                print("Estado:", propertys[11])
                print("Descripcion estado:", propertys[12])
                print("_______\n")
                #al llamar solo las columnas necesarias en el SELECT cambian los valores para la impresion
        except Exception as e:
            raise

city=str(input('Ciudad del inmueble:'))
    #cambir por botones que solo tenga las ciudads disponibles
database = DataBase()
database.select_propertys(city)