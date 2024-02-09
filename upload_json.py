import os
import json
from database import Database

def upload_json(path, db: Database):
    with open(os.path.join(path, "patients.json"), "r") as f:
        patients_data = json.load(f)
        for tuple in patients_data["patients"]:
            db.insert_patient_pseudo(tuple["patient_ID"], tuple["patient_pseudo_ID"])

    with open(os.path.join(path, "predictive.json"), "r") as f:
        predictive_data = json.load(f)
        for tuple in predictive_data["predictive"]:
            db.insert_predictive_pseudo(tuple["predictive_number"], tuple["pseudo_number"])

    with open(os.path.join(path, "samples.json"), "r") as f:
        samples_data  = json.load(f)
        for tuple in samples_data["samples"]:
            db.insert_samples_pseudo(tuple["sample_ID"], tuple["pseudo_sample_ID"])

if __name__=="__main__":
    db = Database(
        os.environ["PSQL_NAME"],
        os.environ["PSQL_HOST"],
        os.environ["PSQL_PORT"],
        os.environ["PSQL_USER"],
        os.environ["PSQL_PSSWD"]
    )
    path = os.environ["PSEUDO_TABLE_JSON"]
    upload_json(path, db)