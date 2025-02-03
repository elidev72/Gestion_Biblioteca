import bcrypt

if __name__ == '__main__':
    password = "Clave2".encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print(hashed.decode('utf-8'))
