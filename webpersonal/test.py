# myscript.py

from __future__ import print_function

import cx_Oracle

print("Si ejecuto esta linea")
# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("RICARDO", "Ricardo", "localhost:1521/ORCLPDB")

cursor = connection.cursor()
cursor.execute("""
    SELECT first_name, last_name
    FROM employees
    WHERE department_id = :did AND employee_id > :eid""",
               did=50,
               eid=190)
for fname, lname in cursor:
    print("Values:", fname, lname)

print("Si ejecuto esta linea 2")
