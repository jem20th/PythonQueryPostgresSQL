#Problem 2 by Harrison Ching
#Insert NHTS
#!/usr/bin/python

import psycopg2
import csv

conn = psycopg2.connect(database="postgres")

print "Opened database successfully"

cur = conn.cursor()
cur.execute('''CREATE TABLE NHTSD
		(HOUSEID_D 	INT,
       	PERSONID_D	TEXT,
        VEHID_D    	INT,
        TDAYDATE_D  INT,
        TRPMILES_D  FLOAT);''')
print "Table D created successfully"

parse = open('DAYV2PUB.CSV')
read_csv = csv.DictReader(parse, delimiter=',')
rownum = 0
for row in read_csv:
	HOUSEID = int(row["HOUSEID"])
	PERSONID = row["PERSONID"]
	VEHID = int(row["VEHID"])
	TDAYDATE = int(row["TDAYDATE"])
	TRPMILES = float(row["TRPMILES"])
	postgres = 'INSERT INTO NHTSD (HOUSEID_D, PERSONID_D, VEHID_D, TDAYDATE_D, TRPMILES_D) VALUES (%s, %s, %s, %s, %s)'
	data = (HOUSEID, PERSONID, VEHID, TDAYDATE, TRPMILES)
	cur.execute(postgres, data)
print "DAYV2 Done"

cur.execute('''CREATE TABLE NHTSV
		(HOUSEID_V	INT,
		VEHID_V		INT,
		TDAYDATE_V	INT,
		EPATMPG_V	FLOAT);''')
print "Table V created successfully"

parse = open('VEHV2PUB.CSV')
read_csv = csv.DictReader(parse, delimiter=',')
rownum = 0
for row in read_csv:
	HOUSEID = int(row["HOUSEID"])
	VEHID = int(row["VEHID"])
	TDAYDATE = int(row["TDAYDATE"])
	EPATMPG = float(row["EPATMPG"])
	postgres = 'INSERT INTO NHTSV (HOUSEID_V, VEHID_V, TDAYDATE_V, EPATMPG_V) VALUES (%s, %s, %s, %s)'
	data = (HOUSEID, VEHID, TDAYDATE, EPATMPG)
	cur.execute(postgres, data)
print "VEHV2 Done"

conn.commit()
conn.close()
