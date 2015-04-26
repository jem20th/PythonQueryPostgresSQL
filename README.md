# PythonQueryPostgresSQL
Run SQL queries for database schema, in this case NHTS and EIA

ECS165A Homework 4 by Harrison Ching

Python version 2.7

Directions to use our program:
1. Start the sql postgres server (we used start_postgres).
2. Run the two insertion files without the quotes, NHTS might take a minute:
	'python InsertEIA.py'
	'python InsertNHTS.py'
3. This inserts the three EIA files into one table and two NHTS files in two separate tables.
4. Run the three queries for number 3a, 3b, and 3c without the quotes:
	'python Query3A.py' 
	'python Query3B.py'
	'python Query3C.py'
