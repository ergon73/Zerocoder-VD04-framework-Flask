from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    current_time = datetime.now()
    
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    
    day = current_time.day
    month = months[current_time.month]
    year = current_time.year
    time_str = current_time.strftime("%H:%M:%S")
    formatted_date = f"{day} {month} {year}, {time_str}"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Текущее время</title>
    </head>
    <body>
        <h1>Текущее время</h1>
        <p>Дата и время: {formatted_date}</p>
    </body>
    </html>
    """
    
    return html


if __name__ == "__main__":
    app.run(debug=True)

