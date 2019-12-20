import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="rounin",
    passwd="Ifnotbuss1",
    database="bdb_portal_kpk"
)

if db.is_connected():
    print("Berhasil terhubung ke database")
