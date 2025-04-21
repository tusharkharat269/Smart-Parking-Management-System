import mysql.connector
from mysql.connector import Error

def connect_db():
    try:  
        conn = mysql.connector.connect(
            host="localhost",     
            user="root",
            password="tushar",
            database="smart_parking_management_system"
        )

        if conn.is_connected():
                # print("Connected to MySQL database")
                return conn
        
    except Error as e:
        # print(f"Error while connecting to MySQL: {e}")
        return None
    




# Fetch results
# cursor.execute("SELECT * FROM present_vehicles")
# results = cursor.fetchall()
# for row in results:
#     print(row)



# Close connection
def close_db(conn):
    cursor = conn.cursor()
    cursor.close()
    conn.close()
