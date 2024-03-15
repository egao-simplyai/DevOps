#!/usr/bin/env python
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='xxxxx',
    password='Lxxxxx66',
    #account='EIEOOKV.BS67383'
    account='ct46093.ap-southeast-2'
    )
cs = ctx.cursor()
cs.execute("ALTER SESSION SET QUERY_TAG = 'Test_Account_ID'")
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
    cs.execute("USE ROLE ACCOUNTADMIN")
    cs.execute("USE WAREHOUSE tiny_warehouse_mg")
    cs.execute("USE SCHEMA testdb.testschema")
    col1, col2=cs.execute("SELECT * FROM test_table").fetchall()
    print('{0}, {1}'.format(col1, col2))
    #cs.execute("CREATE OR REPLACE TABLE "
    #"grocery (item string, quantity number(7,2))")
    #rows_to_insert = [('milk', 2), ('apple', 3), ('egg', 2)]
    cs.execute("insert into grocery (item, quantity) values ('egg', 2)")
    col1, col2 = cs.execute("SELECT item, quantity FROM grocery").fetchone()
    print('{0}, {1}'.format(col1, col2))
    rows_to_insert=[('milk', 2), ('bread', 3)]
    cs.executemany(
    "insert into grocery (item, quantity) values (?, ?)",
    rows_to_insert)  
    col1, col2 = cs.execute("SELECT item, quantity FROM grocery").fetchone()
    print('{0}, {1}'.format(col1, col2))
finally:
    cs.close()
ctx.close()