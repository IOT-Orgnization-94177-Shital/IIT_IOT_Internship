import mysql.connector
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="iot_data"
)
cursor = connection.cursor()
id = int(input("Enter Sensor ID to delete: "))
query = "DELETE FROM sensor_data WHERE id = %s"
cursor.execute(query, (id,))
connection.commit()
if cursor.rowcount > 0:
    print("Record deleted successfully")
else:
    print("No record found")
cursor.close()
connection.close()
