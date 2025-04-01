from app.models import ProcessTable
from main import db_dependency


class DbQuery:

    @staticmethod
    def get_existing_order(db: db_dependency, payload):
        try:
            existing_order = db.query(ProcessTable).filter(
                ProcessTable.process_id.startswith(payload)
            ).all()
            return {"data": existing_order, "status": 200}
        except Exception as e:
            return {"Error": f"{e}", "status": 500}

