
import sqlite3
from datetime import datetime


# DATABASE CONFIGURATION

DATABASE = "resume_ranker.db"

# DATABASE CONNECTION

def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

# INITIALIZE DATABASE


def init_db():

    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT NOT NULL,

            candidate_name TEXT,

            email TEXT,

            phone TEXT,

            resume_text TEXT,

            clean_text TEXT,

            tfidf_score REAL DEFAULT 0,

            semantic_score REAL DEFAULT 0,

            overall_score REAL DEFAULT 0,

            status TEXT DEFAULT 'Pending',

            uploaded_at TEXT
        )
    """)

    connection.commit()
    connection.close()


# SAVE CANDIDATE

def save_candidate(
    filename,
    candidate_name,
    email,
    phone,
    resume_text,
    clean_text,
    tfidf_score,
    semantic_score,
    overall_score,
    uploaded_at=None
):

    connection = get_connection()

    # Determine candidate status
    if overall_score >= 70:
        status = "Shortlisted"

    elif overall_score >= 50:
        status = "Under Review"

    else:
        status = "Rejected"

    if uploaded_at is None:
        uploaded_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    connection.execute("""
        INSERT INTO candidates (
            filename,
            candidate_name,
            email,
            phone,
            resume_text,
            clean_text,
            tfidf_score,
            semantic_score,
            overall_score,
            status,
            uploaded_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        filename,
        candidate_name,
        email,
        phone,
        resume_text,
        clean_text,
        tfidf_score,
        semantic_score,
        overall_score,
        status,
        uploaded_at
    ))

    connection.commit()
    connection.close()



# GET ALL CANDIDATES

def get_candidates():

    connection = get_connection()

    candidates = connection.execute("""
        SELECT *
        FROM candidates
        ORDER BY overall_score DESC
    """).fetchall()

    connection.close()

    return candidates


# GET SINGLE CANDIDATE


def get_candidate(candidate_id):

    connection = get_connection()

    candidate = connection.execute("""
        SELECT *
        FROM candidates
        WHERE id = ?
    """, (candidate_id,)).fetchone()

    connection.close()

    return candidate


# SEARCH / FILTER CANDIDATES

def search_candidates(
    search="",
    min_score=0,
    status=""
):

    connection = get_connection()

    query = """
        SELECT *
        FROM candidates
        WHERE overall_score >= ?
    """

    parameters = [min_score]

    # Search by name, email or filename
    if search:

        query += """
            AND (
                candidate_name LIKE ?
                OR email LIKE ?
                OR filename LIKE ?
            )
        """

        value = f"%{search}%"

        parameters.extend([
            value,
            value,
            value
        ])

    # Filter by status
    if status:

        query += """
            AND status = ?
        """

        parameters.append(status)

    query += """
        ORDER BY overall_score DESC
    """

    candidates = connection.execute(
        query,
        parameters
    ).fetchall()

    connection.close()

    return candidates



# UPDATE CANDIDATE STATUS

def update_status(
    candidate_id,
    status
):

    connection = get_connection()

    connection.execute("""
        UPDATE candidates
        SET status = ?
        WHERE id = ?
    """, (
        status,
        candidate_id
    ))

    connection.commit()
    connection.close()

# DELETE CANDIDATE


def delete_candidate(candidate_id):

    connection = get_connection()

    connection.execute("""
        DELETE FROM candidates
        WHERE id = ?
    """, (candidate_id,))

    connection.commit()
    connection.close()

# CLEAR ALL CANDIDATES

def clear_candidates():

    connection = get_connection()

    connection.execute("""
        DELETE FROM candidates
    """)

    connection.commit()
    connection.close()

