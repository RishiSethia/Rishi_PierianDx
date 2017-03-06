import MySQLdb as db 			# Importing mysqldb
con = db.connect("localhost","root","PASSWORD") # Please enter your mysql password to connect it with db
cur = con.cursor()
cur.execute("CREATE DATABASE my_vcf")		# Database created

con.close()		# Connection Closed
