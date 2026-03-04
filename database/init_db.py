from database.db_connection import get_connection

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Read SQL file and execute
    with open("sql/create_tables.sql", "r") as file:
        sql_script = file.read()
        cursor.execute(sql_script)

    conn.commit()
    cursor.close()
    conn.close()

    print("Database initialized successfully!")
    if __name__ == "__main__":
        initialize_database()