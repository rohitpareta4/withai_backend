from core.session import SessionLocal
from services.reminder_service import send_daily_reminder


def main():
    db = SessionLocal()

    try:
        send_daily_reminder(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()
           