from flask import Flask
from .utils.db import connect_to_db, close_db_connection
from .routes.ticket_routes import ticket_bp

app = Flask(__name__)
app.register_blueprint(ticket_bp)

# Initialize database connection
conn, cur = connect_to_db()

# Close database connection on app exit
@app.teardown_appcontext
def close_connection(exception):
    close_db_connection(conn, cur)
