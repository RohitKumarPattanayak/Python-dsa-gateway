create venv
python -m venv .venv

create a server/main.py


create requirements.txt -> fastapi[standard]
pip install -r requirements.txt

uvicorn main:app --reload

pip install "starlette<0.48.0"