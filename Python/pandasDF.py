import numpy as np
import pandas as pd
from snowflake.snowpark.functions import udf
@udf(packages=["numpy", "pandas", "xgboost==1.5.0"])
... def compute() -> list:
...     return [np.__version__, pd.__version__]

>>> @udf(packages=["numpy", "pandas", "xgboost==1.5.0"])
... def compute() -> list:
...     return [np.__version__, pd.__version__, xgb.__version__]
print("Hello World!!!!")
def fetch_pandas_old(cur, sql):
    cur.execute(sql)
    rows = 0
    while True:
        dat = cur.fetchmany(50000)
        if not dat:
            break
        df = pd.DataFrame(dat, columns=cur.description)
        rows += df.shape[0]
    print(rows)