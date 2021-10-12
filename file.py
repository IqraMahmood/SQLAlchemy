

import classSqlAlchemy as sa
obj = sa.SqlalchemyOop()
obj.return_engine('mysql://root:sqlpassword381@localhost/devnation')
obj.database_connection()
obj.select_query('SELECT * FROM user_details')
res = obj.df()
print(res)

# print("test")
