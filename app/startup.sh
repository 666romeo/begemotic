chmod +x startup.sh
cd models
alembic upgrade head
cd ..
cd csv_data
python import_data_db.py
cd ..
uvicorn main:app --host 0.0.0.0 --port 8000 --reload