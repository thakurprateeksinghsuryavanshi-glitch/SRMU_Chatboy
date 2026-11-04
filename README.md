# SRMU Admission Guide Chatbot (Python + Flask)

The chatbot brain is now written in **Python**. The website sends each message
to the Python server (`/api/chat`) and shows the reply.
If the server is not reachable, the page still works using its built-in JavaScript copy.

## Files
- `app.py`           : Flask web server (serves the site + chat API)
- `chatbot.py`       : chatbot logic and course data (edit courses here)
- `static/index.html`: the website design
- `requirements.txt` : Python libraries (flask, gunicorn)
- `Procfile`         : start command for Render/Railway/Heroku
- `.gitignore`       : files Git should ignore

## Run on your computer
```
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000

## Make it live (free): Render.com
1. Upload this whole folder to a GitHub repository.
2. On render.com: New > Web Service > connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Click Deploy. You get a live link like `https://srmu-bot.onrender.com`.

(PythonAnywhere also works: create a Flask web app and upload these files.)

## How to edit
- Add or change courses: the `COURSES` dictionary in `chatbot.py`.
- Change replies or add rules: the `get_reply()` function in `chatbot.py`.

## Important
Course names, eligibility, fees and dates change every year. Always confirm them
on https://www.srmu.ac.in. This is a guidance tool, not an official SRMU product.
