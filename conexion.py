import psycopg2
# import contextlib

db_params = dict(
    host="localhost",
    database="postgres",
    port=5432,
    user="postgres",
    password="abcd1234"
)

def conect_to_db(db_params):
    print("Connecting to PostgreSQL database...")
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    cur.close()
    conn.close()


def get_db(db_params):
    print("Connecting to PostgreSQL database...")
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    return cur, conn


def get_all_persons():
    connection, con = get_db(db_params)
    connection.execute("select * from persona")
    respuesta = []    
    for persona in connection.fetchall():
        datos = {}
        datos['id'] = persona[0]
        datos['nombre'] = persona[1]
        datos['apellido'] = persona[2]
        datos['email'] = persona[3]
        respuesta.append(datos)
    
    return respuesta

def get_by_id(id):
    connection, con = get_db(db_params)
    connection.execute(f"select * from persona where id = {id}")
    persona = connection.fetchone()
    datos = {}
    datos['id'] = persona[0]
    datos['nombre'] = persona[1]
    datos['apellido'] = persona[2]
    datos['email'] = persona[3]
    
    return datos


def insert_person(name, last_name, email):
    connection, con = get_db(db_params)
    connection.execute(f"insert into persona (name, last_name, email) values ('{name}', '{last_name}', '{email}') returning id")
    persona = connection.fetchone()
    con.commit()
    return persona[0]

# @contextlib.contextmanager
# def database(params):
#     print("Connecting to PostgreSQL database...")
#     # Setup script
#     conn = psycopg2.connect(**params)
#     cur = conn.cursor()
#     try:
#         yield cur
#     finally:
#         # Teardown script
#         cur.close()
#         conn.commit()
#         conn.close()
#         print("Database connection closed.")