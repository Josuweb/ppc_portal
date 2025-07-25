class User:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    def authenticate(self, db_cursor):
        db_cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (self.email, self.password))
        result = db_cursor.fetchone()
        if result:
            self.id = result[0]
            return True
        return False
