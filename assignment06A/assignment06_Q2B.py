import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="iot_data"
)

cursor = connection.cursor()

id = int(input("Enter Sensor ID to update: "))
new_moisture = float(input("Enter new Moisture Level: "))

query = """
UPDATE sensor_data
SET moisture_level = %s
WHERE id = %s
"""

cursor.execute(query, (new_moisture, id))
connection.commit()

if cursor.rowcount > 0:
    print("Record updated successfully")
else:
    print("No record found")

cursor.close()
connection.close()
