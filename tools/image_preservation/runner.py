"""Retired PC provider client. Capture traffic belongs to the central server owner."""
RETIRED="PC Archive.org clients are retired; use the central server owner. Follow Bill's current hold/resumption instructions."
def existing_capture(url):raise RuntimeError(RETIRED)
def save_original(url):raise RuntimeError(RETIRED)
def verify_one(info,capture):raise RuntimeError(RETIRED)
def batch(db,directory,limit=10,gap=30,titles=None):raise RuntimeError(RETIRED)
def recover_interrupted(db):
    # Pure legacy ledger repair; never contacts a provider or reschedules verified rows.
    db.execute("UPDATE versions SET status='retry',error='Interrupted before verification; inspect saved capture' WHERE status IN ('saving','checking')")
    db.commit()
