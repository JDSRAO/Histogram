import pypyodbc as ado
import pandas as pd
import matplotlib.pyplot as plt

SERVER_NAME = 'tcp:wa-azgb-te-msq01.database.windows.net'
DATABASE_NAME = 'datamill-des'

# Driver={ODBC Driver 13 for SQL Server};


# tcp:wa-azgb-te-msq01.database.windows.net
# owerthingadmin

# Server=tcp:wa-azgb-dv-msq01.database.windows.net,1433;Initial Catalog=datamill-des;Persist Security Info=False;User ID=powerthingadmin;Password=Wateraid9$#4%;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;

conn = ado.connect("""
    Driver={{SQL Server Native Client 11.0}};
    Server={0};
    Database={1};
    Uid=powerthingadmin;
    Pwd=Wateraid9$#4%;
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
""".format(SERVER_NAME, DATABASE_NAME))

SQL_QUERY = """
SELECT TOP 100 * FROM
[cTNPP].PostedTransaction AS PT
"""

# With headers
df1 = pd.read_sql(SQL_QUERY, conn)
print("#### DF1 ####")
print(df1)

# Without headers
c = conn.cursor()
df2 = pd.DataFrame(c.execute(SQL_QUERY))
print("#### DF2 ####")
print(df2)

# df2.hist()
#pd.DataFrame.plot.hist(df2)

print(df1.shape)
print(df2.shape)

print(df1.dtypes)
print(df2.dtypes)

# for col in df1.columns:
#     print(col)

print("First columns")
print(str(df1.columns[0]))
print(df1.columns[0])

df2.hist(column=str(df1.columns[0]))