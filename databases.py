from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector as mysqlc

db = mysqlc.connect(
    host="localhost",
    user="rounin",
    passwd="Ifnotbuss1",
    database="bdb_portal_kpk"
)
# cursor = db.cursor()
# now = datetime.now()
#
# add_course = ("INSERT INTO salaries "
#                 "(emp_no, salary, from_date, to_date) "
#                 "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
