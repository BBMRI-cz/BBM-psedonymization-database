import psycopg

class Database:
    def __init__(self, database_name, host, port, user, password=None):
        self.conn = psycopg.connect(f"user={user} password={password} host={host} port={port} dbname={database_name}")
        self.c = self.conn.cursor()

    def insert_patient_pseudo(self, patient_id, pseudo_patient_id):
        self.c.execute(
            f"INSERT INTO patients (patient_id, patient_pseudo_id) VALUES (%s, %s)",
            (
                patient_id,
                pseudo_patient_id
            ),
        )
        self.conn.commit()

    def insert_predictive_pseudo(self, predictive_number, pseudo_number):
        self.c.execute(
            f"INSERT INTO predictive (predictive_number, pseudo_number) VALUES (%s, %s)",
            (
                predictive_number,
                pseudo_number
            ),
        )
        self.conn.commit()

    def insert_samples_pseudo(self, sample_id, pseudo_sample_id):
        self.c.execute(
            f"INSERT INTO samples (sample_id, sample_pseudo_id) VALUES (%s, %s)",
            (
                sample_id,
                pseudo_sample_id
            ),
        )
        self.conn.commit()

    def get_patient_pseudo_id(self, patient_id):
        self.c.execute(
            f'SELECT patient_pseudo_id FROM patients WHERE patient_id = %s', (patient_id,)
        )
        row = self.c.fetchone()
        row = row[0] if row is not None else None
        return row

    def get_sample_pseudo_id(self, sample_id):
        self.c.execute(
            f"SELECT sample_pseudo_id FROM samples WHERE sample_id = %s",
            (
                sample_id,
            ),
        )
        row = self.c.fetchone()
        row = row[0] if row is not None else None
        return row
    
    def get_predictive_pseudo_id(self, predictive_number):
        self.c.execute(
            f"SELECT pseudo_number FROM predictive WHERE predictive_number = %s",
            (
                predictive_number,
            ),
        )
        row = self.c.fetchone()
        row = row[0] if row is not None else None
        return row