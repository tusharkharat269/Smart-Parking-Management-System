from datetime import datetime


def vehicle_check_in(vehicle_no,conn):

    cursor = conn.cursor()
    values = (vehicle_no,datetime.now())
    query = "INSERT INTO present_vehicles (vehicle_number, check_in_time) VALUES (%s,%s)"

    print("vehicle check in: ",vehicle_no, " time: ", datetime.now())

    cursor.execute(query, values)
    conn.commit()



def search(vehicle_no,conn):

    cursor = conn.cursor()
    query = "SELECT 1 FROM present_vehicles WHERE vehicle_number = %s LIMIT 1"
    cursor.execute(query, (vehicle_no,))
    result = cursor.fetchone()

    return result is not None



def vehicle_check_out(vehicle_no,conn):

    cursor = conn.cursor()

    select_query = "SELECT vehicle_number, check_in_time FROM present_vehicles WHERE vehicle_number = %s LIMIT 1"
    cursor.execute(select_query, (vehicle_no,))
    row = cursor.fetchone()

    if row:
        vehicle_number, checkintime = row
        checkouttime = datetime.now()
        insert_query = """
            INSERT INTO vehicles_history (vehicle_number, check_in_time, check_out_time)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (vehicle_number, checkintime, checkouttime))

        # Step 3: Delete from old table
        delete_query = "DELETE FROM present_vehicles WHERE vehicle_number = %s"
        cursor.execute(delete_query, (vehicle_no,))

        conn.commit()
        print("vehicle check out: ",vehicle_no, " check in time: ", checkintime, " check out time: ",checkouttime)

