from fastapi_sqlalchemy import DBSessionMiddleware, db

INITIAL_DATA = {
      'users': [
            {
                  'username': 'superadmin',
                  'email': 'superadmin@superadmin.com',
                  'hashed_password': bcrypt.hashpw('123'.encode('utf-8'), bcrypt.gensalt()).decode('utf8')
            },
            {
                  'username': 'admin',
                  'email': 'admin@example.com',
                  'hashed_password': bcrypt.hashpw('123'.encode('utf-8'), bcrypt.gensalt()).decode('utf8')
            }
      ],
      # 'sometable': [
      #       {'column1': 'value', 'column2': 'value'}
      # ]
}

# This method receives a table, a connection and inserts data to that table.
def initialize_table(target, connection, **kw):
    print("I want to know the value of this: " + '11111')

    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])
