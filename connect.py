#build in
import mysql.connector

#fungsi koneksi
def koneksi():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="perpus_berjalan",
        autocommit=True
    )
    if db.is_connected():
        return db
    else:
        print('DB disconnet!')

    
