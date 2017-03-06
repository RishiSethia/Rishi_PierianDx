import MySQLdb					# importing module
mutation = open('muataions.txt','w')		# Opening file to write
open_vcf = open('mutect_immediate.vcf','r')	# Opening of input file
vcf = open_vcf.readlines()			# Reading the VCF file
db = MySQLdb.connect("localhost","root","PASSWORD","my_vcf" )	# Replace PASSWORD with your mysql password to access your database created in previous Question 2
cursor = db.cursor()	# prepare a cursor object using cursor() method
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS VCF")
# Create table as per requirement
sql = "CREATE TABLE VCF (Chr VARCHAR(100),Pos INT,ID VARCHAR(20) ,Ref VARCHAR(2) ,Alt VARCHAR(2) ,Qual INT ,Filter VARCHAR(20),Info VARCHAR(20), Sample VARCHAR(20))"
cursor.execute(sql)
# taking entries from input file
for line in vcf:
	if not line.startswith('#'):
		line = line.rstrip()
		split_line = line.split('\t')
		cursor.execute('insert into VCF(Chr,Pos,ID,Ref,Alt,Qual,Filter,Info,Sample)values("%s","%d","%s","%s","%s","%d","%s","%s","%s")' % (split_line[0],int(split_line[1]),split_line[2],split_line[3],split_line[4],int(split_line[5]),split_line[6],split_line[7],split_line[8]))
db.commit()
cursor.execute("SELECT * FROM VCF")
data = cursor.fetchall() # Data variable to print the whole table
cursor.execute("SELECT * from VCF where Qual > 50 and Qual < 500")
query = cursor.fetchall()	# to fetch query
mutation.write(query)	# writing in file
mutation.close()
db.close()		
# Closing Database and file
