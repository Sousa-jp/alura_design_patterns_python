from connection_factory import ConnectionFactory

connection = ConnectionFactory().get_connection()
cursor = connection.cursor()
cursor.execute('SELECT * FROM tb_funcionario')

connection.close()
