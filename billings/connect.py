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

    cursor.execute("SELECT to_char(l.DTCOMPCUSTO,'MM/YYYY'),l.CDFILIAL,f.NMFILIAL,SUM(l.VRLANCCUST) FROM LANCCCUSTO l INNER JOIN CONTCTBL c ON c.CDCONTCTBL = l.CDCONTCTBL INNER JOIN FILIAL f ON f.CDFILIAL = l.CDFILIAL WHERE l.CDCONTCTBL IN('31102001','31103001')AND l.DTCOMPCUSTO >= ADD_MONTHS(TRUNC(SYSDATE, 'MM'), -3) AND l.DTCOMPCUSTO < TRUNC(SYSDATE, 'MM') GROUP BY to_char(l.DTCOMPCUSTO,'MM/YYYY'),l.CDFILIAL,f.NMFILIAL ORDER BY l.CDFILIAL,to_char(l.DTCOMPCUSTO,'MM/YYYY')")
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)
except oracledb.DatabaseError as e:
    print (e)
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()                          