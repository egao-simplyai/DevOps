#!/usr/bin/env python3
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='',
    password='',
    #account='ct46093.ap-southeast-2s.aws'
    #account='eieookv.bs67383.ap-southeast-2s'
    #https://ct46093.ap-southeast-2.snowflakecomputing.com
    #EIEOOKV.BS67383
    account='ORGNAME.ACCOUNTNAME.ap-southeast-2s'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    cs.execute("SELECT 'TESTING!!!!' ")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()
