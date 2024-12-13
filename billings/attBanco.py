import oracledb

# configuração user

username = "teknisa"
password = "teknisa"
dsn = "host:1521/teknisa"
def consultaOperador():
    print("############")
    try:
        connection = oracledb.connect(user=username, password=password,
                                    host="192.168.0.91", port=1521, service_name="orclpdb")
        print("############")
        print(connection.version)

        cursor = connection.cursor()

        cursor.execute(f"""
            SELECT CDOPERADOR, NMOPERADOR FROM OPERADOR       
        """)
        rows = cursor.fetchall()
        return rows
    except oracledb.DatabaseError as e:
        print (e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def consultaFiliais():
    print("############")
    try:
        connection = oracledb.connect(user=username, password=password,
                                    host="192.168.0.91", port=1521, service_name="orclpdb")
        print("############")
        print(connection.version)

        cursor = connection.cursor()

        cursor.execute(f"""
            SELECT CDFILIAL, NMFILIAL FROM FILIAL WHERE NMFILIAL NOT LIKE '%INATIVO%' AND NMFILIAL NOT LIKE '%INAT%'     
        """)
        rows = cursor.fetchall()
        return rows
    except oracledb.DatabaseError as e:
        print (e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
def consultaRc():
    print("############")
    try:
        connection = oracledb.connect(user=username, password=password,
                                    host="192.168.0.91", port=1521, service_name="orclpdb")
        print("############")
        print(connection.version)

        cursor = connection.cursor()

        cursor.execute(f"""
            SELECT
            s.CDFILSOLI, s.CDFILLANCA, s.NRSOLICMP, s.DTSOLCMP, o.CDOPERADOR, s.QTITEMSOLIC, m.DSJUSTSOLEXT,
            CASE
            WHEN COUNT(i.CDOPERAPROV) = s.QTITEMSOLIC THEN 'APROVADA'
            WHEN COUNT(i.CDOPERAPROV) < s.QTITEMSOLIC AND COUNT(i.CDOPERAPROV) > 0  THEN 'APROVADA PARCIALMENTE'
            ELSE 'REPROVADA'
            END AS "STATUS"
            FROM SOLICITA s
            INNER JOIN FILIAL f ON f.CDFILIAL = s.CDFILSOLI
            INNER JOIN OPERADOR o ON o.CDOPERADOR = s.CDOPERLANC
            INNER JOIN MOVSOLEXT m ON m.CDFILSOLEXT = s.CDFILSOLI AND m.CDFILLANCEXT = s.CDFILLANCA AND m.NRSOLIMOVEXT = s.NRSOLICMP
            INNER JOIN ITEMSOLI i ON i.CDFILSOLI = s.CDFILSOLI AND i.CDFILLAN = s.CDFILLANCA AND i.NRSOLICMP = s.NRSOLICMP
            WHERE s.DTSOLCMP >= '01/12/2024' AND s.IDSOLEXTRA = 'S'
            GROUP BY
                s.CDFILSOLI,
                f.NMFILIAL,
                s.CDFILLANCA,
                s.NRSOLICMP,
                s.DTSOLCMP,
                o.CDOPERADOR,
                s.QTITEMSOLIC,
                m.DSJUSTSOLEXT
            HAVING 
                COUNT(i.CDOPERAPROV) = s.QTITEMSOLIC
            ORDER BY s.DTSOLCMP, s.CDFILSOLI, s.NRSOLICMP

        """)
        rows = cursor.fetchall()
        return rows
    except oracledb.DatabaseError as e:
        print (e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def consultaItensRc(rc, solicita, destino):
    print("############")
    try:
        connection = oracledb.connect(user=username, password=password,
                                    host="192.168.0.91", port=1521, service_name="orclpdb")
        print("############")
        print(connection.version)

        cursor = connection.cursor()

        cursor.execute(f"""
            SELECT
            s.CDFILSOLI, s.CDFILLANCA, s.NRSOLICMP, s.DTSOLCMP, o.CDOPERADOR, s.QTITEMSOLIC, m.DSJUSTSOLEXT,
            CASE
            WHEN COUNT(i.CDOPERAPROV) = s.QTITEMSOLIC THEN 'APROVADA'
            WHEN COUNT(i.CDOPERAPROV) < s.QTITEMSOLIC AND COUNT(i.CDOPERAPROV) > 0  THEN 'APROVADA PARCIALMENTE'
            ELSE 'REPROVADA'
            END AS "STATUS"
            FROM SOLICITA s
            INNER JOIN FILIAL f ON f.CDFILIAL = s.CDFILSOLI
            INNER JOIN OPERADOR o ON o.CDOPERADOR = s.CDOPERLANC
            INNER JOIN MOVSOLEXT m ON m.CDFILSOLEXT = s.CDFILSOLI AND m.CDFILLANCEXT = s.CDFILLANCA AND m.NRSOLIMOVEXT = s.NRSOLICMP
            INNER JOIN ITEMSOLI i ON i.CDFILSOLI = s.CDFILSOLI AND i.CDFILLAN = s.CDFILLANCA AND i.NRSOLICMP = s.NRSOLICMP
            WHERE s.DTSOLCMP >= '01/12/2024' AND s.IDSOLEXTRA = 'S'
            GROUP BY
                s.CDFILSOLI,
                f.NMFILIAL,
                s.CDFILLANCA,
                s.NRSOLICMP,
                s.DTSOLCMP,
                o.CDOPERADOR,
                s.QTITEMSOLIC,
                m.DSJUSTSOLEXT
            HAVING 
                COUNT(i.CDOPERAPROV) = s.QTITEMSOLIC
            ORDER BY s.DTSOLCMP, s.CDFILSOLI, s.NRSOLICMP

        """)
        rows = cursor.fetchall()
        return rows
    except oracledb.DatabaseError as e:
        print (e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


