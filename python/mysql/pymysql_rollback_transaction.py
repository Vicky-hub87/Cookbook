from pymysql import connect

DB_HOST = 'example.net'  # IP or hostname of database
DB_NAME = 'asdf_test'  # Name of the database to use
DB_USER = 'asdf_test'  # Username for accessing database
DB_PASS = 'asdf'  # Password for database user

db_connection = connect(host=DB_HOST,
	                    user=DB_USER,
	                    password=DB_PASS,
	                    db=DB_NAME)


with db_connection.cursor() as cursor:
    statement = """
        CREATE TABLE IF NOT EXISTS users (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255),
            email VARCHAR(255)
        ) ENGINE=INNODB;
    """
    cursor.execute(statement)

    statement = """
        INSERT INTO users
        (username, password, email)
        VALUES
        ('nanodano', 'mysecret', 'nanodano@devdungeon.com');
    """
    result = cursor.execute(statement)
    print(type(result))  # <class 'int'>
    print(result)  # 1 (number of rows)
    # Get ID of last row inserted
    print(f'Last row ID inserted: {cursor.lastrowid}')

db_connection.rollback()
db_connection.close()
