import oracledb

# configuração user

username = "teknisa"
password = "teknisa"
dsn = "host:1521/teknisa"

try:
    connection = oracledb.connect(user=username, password=password,
                                  host="192.168.0.91", port=1521, service_name="orclpdb")
    print("############")
    print(connection.version)

    cursor = connection.cursor()

except oracledb.DatabaseError as e:
    print (e)
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()