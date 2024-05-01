import psycopg2
from psycopg2 import OperationalError

DB_NAME = "Tickets"
DB_USER = "root"
DB_PASSWORD = "mypassword"
DB_HOST = "localhost"
DB_PORT = 5432

def connect_to_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    create_support_tickets_table(conn, cur)
    return conn, cur

def close_db_connection(conn, cur):
    cur.close()
    conn.close()

def create_support_tickets_table(conn, cur):
    table_name = "support_tickets"
    schema_name = "public"
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (
        id SERIAL PRIMARY KEY,
        email TEXT NOT NULL,
        ticket_title TEXT,
        ticket_description TEXT NOT NULL,
        ticket_priority VARCHAR(50) NOT NULL,
        resolution TEXT,
        isResolved BOOLEAN,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cur.execute(create_table_query)
    conn.commit()

def add_support_ticket(email, ticket_title, ticket_description, ticket_priority, isResolved, resolution=None):
    conn, cur = connect_to_db()
    try:
        cur.execute("""
        INSERT INTO support_tickets (email, ticket_title, ticket_description, ticket_priority, resolution, isResolved)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (email, ticket_title, ticket_description, ticket_priority, resolution, isResolved))
        conn.commit()
    except OperationalError as e:
        print(f"Error: {e}")
    finally:
        close_db_connection(conn, cur)

# Example usage
# add_support_ticket("user@example.com", "Ticket Title", "Ticket Description", "High", False)
