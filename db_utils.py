import pyodbc as odbc

def get_connection():
    try:
        # DRIVER_NAME = 'ODBC Driver 18 for SQL Server'
        # SERVER = 'SYEDA-FARWA-BAT\\CLASS'  # Use double backslashes
        # DATABASE = 'Pinkeyeflu'
        DRIVER_NAME = '{ODBC Driver 18 for SQL Server}'
        SERVER='tcp:patientdb123.database.windows.net,1433'
        DB_NAME='Pinkeyeflu'
        USERNAME='sqladmin'
        PASSWORD='Farwa123'
        
        connStr = (
            f'Driver={DRIVER_NAME};'
            f'Server={SERVER};'
            f'Database={DB_NAME};'
            f'Uid={USERNAME};'
            f'Pwd={PASSWORD};'
            'Encrypt=yes;'
            'TrustServerCertificate=no;'
            'Connection Timeout=30;'
        )
        connection = odbc.connect(connStr)
        print("Connected to SQL Server Database")
        # connection.close()
        return connection
    except odbc.DatabaseError as e:
        print("There was a problem connecting to the database: ", e)

def execute_query(query, params=None):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params or [])
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def execute_non_query(query, params=None):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params or [])
    connection.commit()
    cursor.close()
    connection.close()
