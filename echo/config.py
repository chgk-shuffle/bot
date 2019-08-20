import sqlite3

TG_TOKEN = "822405659:AAHFVHP0-80jXg4uVPrhCyW3Gd447PGzuxk"

def foo(text):
    con = sqlite3.connect('db')
    cur = con.cursor()
    con.commit()
    list = cur.execute(f"""SELECT id_table, id_round
                    FROM Team
                    WHERE id_user IN (
                        SELECT id_user FROM User
                        WHERE name = '{text}'
                    );""").fetchall()
    return list