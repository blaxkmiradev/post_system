from db import get_connection

def create_post(title, content):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        (title, content)
    )

    conn.commit()
    conn.close()

def get_all_posts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, title, created_at FROM posts ORDER BY id DESC")
    rows = cur.fetchall()

    conn.close()
    return rows

def get_post(post_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM posts WHERE id=?", (post_id,))
    row = cur.fetchone()

    conn.close()
    return row

def delete_post(post_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM posts WHERE id=?", (post_id,))
    conn.commit()
    conn.close()
