import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "1234",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")

    createTable = '''
	        CREATE TABLE USER (
	            usr VARCHAR(255) PRIMARY KEY,
	            vendor_name VARCHAR(255) NOT NULL
	        )
    '''

    addUsr = '''
			INSERT INTO USUARIO (usr,pwd) VALUES(%s,%s)
    '''

    #cursor.execute(addUsr, ('user1', 'user2',))
    #cursor.execute(addUsr)
    cursor.execute('''
			INSERT INTO public."USUARIO"(
			"user", pwd)
			VALUES (?, ?);
    	''')
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n") 

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")