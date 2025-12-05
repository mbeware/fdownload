class BaseRepository:
    def __init__(self, db, table: str, primary_key: str):
        self.db = db
        self.table = table
        self.primary_key = primary_key

    def create(self, data: dict):
        keys = ", ".join(data.keys())
        placeholders = ", ".join([f":{k}" for k in data])
        sql = f"INSERT INTO {self.table} ({keys}) VALUES ({placeholders})"

        conn = self.db.get_conn()
        conn.execute(sql, data)
        conn.commit()
        print("Enregistrement créé avec succès.")

    def read(self, pk_value):
        sql = f"SELECT * FROM {self.table} WHERE {self.primary_key} = ?"
        row = self.db.get_conn().execute(sql, (pk_value,)).fetchone()
        if row:
            return dict(row)
        print("Aucun enregistrement trouvé.")
        return None

    def update(self, pk_value, updates: dict):
        set_clause = ", ".join([f"{k} = :{k}" for k in updates])
        updates[self.primary_key] = pk_value

        sql = f"UPDATE {self.table} SET {set_clause} WHERE {self.primary_key} = :{self.primary_key}"

        conn = self.db.get_conn()
        cur = conn.execute(sql, updates)
        conn.commit()

        if cur.rowcount == 0:
            print("Aucun enregistrement mis à jour.")
        else:
            print("Enregistrement mis à jour avec succès.")

    def delete(self, pk_value):
        sql = f"DELETE FROM {self.table} WHERE {self.primary_key} = ?"
        conn = self.db.get_conn()
        cur = conn.execute(sql, (pk_value,))
        conn.commit()

        if cur.rowcount == 0:
            print("Aucun enregistrement supprimé.")
        else:
            print("Enregistrement supprimé avec succès.")

    def list_all(self):
        sql = f"SELECT * FROM {self.table}"
        rows = self.db.get_conn().execute(sql).fetchall()
        return [dict(row) for row in rows]
