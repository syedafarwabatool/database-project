# check_db_connection.py
import pyodbc as odbc
def check_connection():
    try:
        DRIVER_NAME = 'ODBC Driver 18 for SQL Server'
        SERVER = 'patientdb123.database.windows.net'  # Use double backslashes
        DATABASE = 'Pinkeyeflu'
        USERNAME = 'sqladmin'
        PASSWORD = 'Farwa123'
        # connStr = (
        #     f"Driver={{{DRIVER_NAME}}};"
        #     f"Server={SERVER};"
        #     f"Database={DATABASE};"
        #     f"UID={USERNAME};"
        #     f"PWD={PASSWORD};"
        #     "Trusted_Connection=yes;"
        #     "TrustServerCertificate=yes;"  # Added to trust the server certificate
        # )
        connStr=('Driver={ODBC Driver 18 for SQL Server};Server=tcp:patientdb123.database.windows.net,1433;Database=Pinkeyeflu;Uid=sqladmin;Pwd=Farwa123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        connection = odbc.connect(connStr)
        print("Connected to SQL Server Database")
        connection.close()
    except odbc.DatabaseError as e:
        print("There was a problem connecting to the database: ", e)
if __name__ == "__main__":
    check_connection()
