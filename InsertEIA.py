#Problem 2 by Harrison Ching
#Insert EIA
#!/usr/bin/python

import psycopg2
import csv

conn = psycopg2.connect(database="postgres")

print "Opened database successfully"

cur = conn.cursor()
cur.execute('''CREATE TABLE EIA
       (MSN_CE     		TEXT,
        YYYYMM_CE 	 	INT,
        Value_CE    	TEXT,
		Column_Order_CE	INT,
		Description_CE	TEXT,
        Unit_CE     	TEXT,
		MSN_CT     		TEXT,
        YYYYMM_CT 	 	INT,
        Value_CT    	TEXT,
		Column_Order_CT	INT,
		Description_CT	TEXT,
        Unit_CT     	TEXT,
		MSN_MW     		TEXT,
        YYYYMM_MW 	 	INT,
        Value_MW    	TEXT,
		Column_Order_MW	INT,
		Description_MW	TEXT,
        Unit_MW     	TEXT);''')
print "Table created successfully"

parse = open('EIA_CO2_Electric_2014.csv')
read_csv = csv.DictReader(parse, delimiter=',')
rownum = 0
for row in read_csv:
	MSN = row["MSN"]
	YYYYMM = int(row["YYYYMM"])
	Value = row["Value"]
	Column_Order = int(row["Column_Order"])
	Description = row["Description"]
	Unit = row["Unit"]
	postgres = 'INSERT INTO EIA (MSN_CE, YYYYMM_CE, Value_CE, Column_Order_CE, Description_CE, Unit_CE) VALUES (%s, %s, %s, %s, %s, %s)'
	data = (MSN, YYYYMM, Value, Column_Order, Description, Unit)
	cur.execute(postgres, data)
print "EIA CO2 Electric Done"

parse = open('EIA_CO2_Transportation_2014.csv')
read_csv = csv.DictReader(parse, delimiter=',')
rownum = 0
for row in read_csv:
        MSN = row["MSN"]
        YYYYMM = int(row["YYYYMM"])
        Value = row["Value"]
        Column_Order = int(row["Column_Order"])
        Description = row["Description"]
        Unit = row["Unit"]
        postgres = 'INSERT INTO EIA (MSN_CT, YYYYMM_CT, Value_CT, Column_Order_CT, Description_CT, Unit_CT) VALUES (%s, %s, %s, %s, %s, %s)'
        data = (MSN, YYYYMM, Value, Column_Order, Description, Unit)
        cur.execute(postgres, data)
print "EIA CO2 Transportation Done"

parse = open('EIA_MkWh_2014.csv')
read_csv = csv.DictReader(parse, delimiter=',')
rownum = 0
for row in read_csv:
	MSN = row["MSN"]
	YYYYMM = int(row["YYYYMM"])
	Value = row["Value"]
	Column_Order = int(row["Column_Order"])
	Description = row["Description"]
	Unit = row["Unit"]
	postgres = 'INSERT INTO EIA (MSN_MW, YYYYMM_MW, Value_MW, Column_Order_MW, Description_MW, Unit_MW) VALUES (%s, %s, %s, %s, %s, %s)'
	data = (MSN, YYYYMM, Value, Column_Order, Description, Unit)
	cur.execute(postgres, data)
print "EIA MkWh Done"

conn.commit()
conn.close()
