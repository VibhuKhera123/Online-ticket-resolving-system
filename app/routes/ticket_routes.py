from flask import Blueprint, request, jsonify
from ..services.ticket_service import TicketService
from ..utils.db import connect_to_db,close_db_connection
ticket_bp = Blueprint("ticket_bp", __name__, url_prefix="/ticket")
ticket_service = TicketService()

@ticket_bp.route("/predict", methods=["POST"])
def predict_ticket():
    data = request.get_json()
    title = data.get('title')
    description = data.get("description")
    email = data.get("email")
    if not description:
        return jsonify({"error": "Missing description in request body"}), 400

    predicted_priority, suggested_solution = ticket_service.predict_ticket(title,description, email)

    return jsonify({
        "predicted_priority": predicted_priority,
        "suggested_solution": suggested_solution
    })

@ticket_bp.route("/tickets", methods=["GET"])
def get_tickets():
    conn, cur = connect_to_db()
    cur.execute("SELECT * FROM support_tickets")
    tickets = cur.fetchall()
    close_db_connection(conn, cur)

    ticket_list = []
    for ticket in tickets:
        ticket_dict = {
            "id": ticket[0],
            "email": ticket[1],
            "ticket_title": ticket[2],
            "ticket_description": ticket[3],
            "ticket_priority": ticket[4],
            "resolution": ticket[5],
            "isResolved": ticket[6],
            "created_at": ticket[7]
        }
        ticket_list.append(ticket_dict)

    return jsonify({"tickets": ticket_list})

@ticket_bp.route("/lowTickets", methods=["GET"])
def get_low_tickets():
    conn, cur = connect_to_db()
    cur.execute("SELECT * FROM support_tickets WHERE ticket_priority = 'Low'")
    tickets = cur.fetchall()
    close_db_connection(conn, cur)

    ticket_list = []
    for ticket in tickets:
        ticket_dict = {
            "id": ticket[0],
            "email": ticket[1],
            "ticket_title": ticket[2],
            "ticket_description": ticket[3],
            "ticket_priority": ticket[4],
            "resolution": ticket[5],
            "isResolved": ticket[6],
            "created_at": ticket[7]
        }
        ticket_list.append(ticket_dict)

    return jsonify({"tickets": ticket_list})

@ticket_bp.route("/mediumTickets", methods=["GET"])
def get_medium_tickets():
    conn, cur = connect_to_db()
    cur.execute("SELECT * FROM support_tickets WHERE ticket_priority = 'Medium'")
    tickets = cur.fetchall()
    close_db_connection(conn, cur)

    ticket_list = []
    for ticket in tickets:
        ticket_dict = {
            "id": ticket[0],
            "email": ticket[1],
            "ticket_title": ticket[2],
            "ticket_description": ticket[3],
            "ticket_priority": ticket[4],
            "resolution": ticket[5],
            "isResolved": ticket[6],
            "created_at": ticket[7]
        }
        ticket_list.append(ticket_dict)

    return jsonify({"tickets": ticket_list})

@ticket_bp.route("/highTickets", methods=["GET"])
def get_high_tickets():
    conn, cur = connect_to_db()
    cur.execute("SELECT * FROM support_tickets WHERE ticket_priority = 'High'")
    tickets = cur.fetchall()
    close_db_connection(conn, cur)

    ticket_list = []
    for ticket in tickets:
        ticket_dict = {
            "id": ticket[0],
            "email": ticket[1],
            "ticket_title": ticket[2],
            "ticket_description": ticket[3],
            "ticket_priority": ticket[4],
            "resolution": ticket[5],
            "isResolved": ticket[6],
            "created_at": ticket[7]
        }
        ticket_list.append(ticket_dict)

    return jsonify({"tickets": ticket_list})

@ticket_bp.route("/criticalTickets", methods=["GET"])
def get_critical_tickets():
    conn, cur = connect_to_db()
    cur.execute("SELECT * FROM support_tickets WHERE ticket_priority = 'Critical'")
    tickets = cur.fetchall()
    close_db_connection(conn, cur)

    ticket_list = []
    for ticket in tickets:
        ticket_dict = {
            "id": ticket[0],
            "email": ticket[1],
            "ticket_title": ticket[2],
            "ticket_description": ticket[3],
            "ticket_priority": ticket[4],
            "resolution": ticket[5],
            "isResolved": ticket[6],
            "created_at": ticket[7]
        }
        ticket_list.append(ticket_dict)

    return jsonify({"tickets": ticket_list})

@ticket_bp.route("/resolvedTickets", methods=["GET"])
def get_resolved_tickets():
    conn, cur = connect_to_db()
    cur.execute("SELECT * FROM support_tickets WHERE isResolved = TRUE")
    tickets = cur.fetchall()
    close_db_connection(conn, cur)

    ticket_list = []
    for ticket in tickets:
        ticket_dict = {
            "id": ticket[0],
            "email": ticket[1],
            "ticket_title": ticket[2],
            "ticket_description": ticket[3],
            "ticket_priority": ticket[4],
            "resolution": ticket[5],
            "isResolved": ticket[6],
            "created_at": ticket[7]
        }
        ticket_list.append(ticket_dict)

    return jsonify({"tickets": ticket_list})

@ticket_bp.route("/unresolvedTickets", methods=["GET"])
def get_unresolved_tickets():
    conn, cur = connect_to_db()
    cur.execute("SELECT * FROM support_tickets WHERE isResolved = FALSE")
    tickets = cur.fetchall()
    close_db_connection(conn, cur)

    ticket_list = []
    for ticket in tickets:
        ticket_dict = {
            "id": ticket[0],
            "email": ticket[1],
            "ticket_title": ticket[2],
            "ticket_description": ticket[3],
            "ticket_priority": ticket[4],
            "resolution": ticket[5],
            "isResolved": ticket[6],
            "created_at": ticket[7]
        }
        ticket_list.append(ticket_dict)

    return jsonify({"tickets": ticket_list})

@ticket_bp.route("/resolveTicket", methods=["POST"])
def resolve_ticket():
    data = request.get_json()
    ticket_id = data.get("id")
    resolution = data.get("resolution")
    if not ticket_id:
        return jsonify({"error": "Missing ticket ID in request body"}), 400
    if not resolution:
        return jsonify({"error": "Missing resolution in request body"}), 400

    conn, cur = connect_to_db()
    cur.execute("UPDATE support_tickets SET resolution = %s, isResolved = TRUE WHERE id = %s", (resolution, ticket_id))
    conn.commit()
    close_db_connection(conn, cur)

    return jsonify({"message": "Ticket resolved successfully"})

@ticket_bp.route("/deleteTicket", methods=["POST"])
def delete_ticket():
    data = request.get_json()
    ticket_id = data.get("id")
    if not ticket_id:
        return jsonify({"error": "Missing ticket ID in request body"}), 400

    conn, cur = connect_to_db()
    cur.execute("DELETE FROM support_tickets WHERE id = %s", (ticket_id,))
    conn.commit()
    close_db_connection(conn, cur)

    return jsonify({"message": "Ticket deleted successfully"})

