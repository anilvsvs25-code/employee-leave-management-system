import os
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD),
    database="employee_leave_db"
)

cursor = conn.cursor()

cursor.execute("SELECT leave_id, emp_id, start_date, end_date, reason, status FROM leaves")
leaves = cursor.fetchall()

print("\nLeave Requests:")
for leave in leaves:
    print(leave)

leave_id = int(input("\nEnter Leave ID to update: "))
new_status = input("Enter new status (APPROVED / REJECTED): ").upper()

update_query = "UPDATE leaves SET status = %s WHERE leave_id = %s"
cursor.execute(update_query, (new_status, leave_id))
conn.commit()

print("✅ Leave status updated successfully")

conn.close()

