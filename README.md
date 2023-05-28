# kindlespark-ecomm-modem
kindlespark-ecomm-modem

# create virtual environment
python -m venv .venv

# activate virtual environment
.venv/Scripts/activate

# install requirements.txt
pip install -r requirements.txt

# to run uvicorn server
uvicorn main:app --reload