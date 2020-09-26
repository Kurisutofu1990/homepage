"""
CMD Befehle:
set FLASK_APP=server3.py     # Flask_APP ist fester Begriff in Flask. Muss den Namen der auszuführenden Datei bekommen.
python -m flask run         # flask run alleine funktioniert nicht
set FLASK_ENV=development   # öffnet in Debug Mode -> danach wieder python -m flask run
"""
"""
nach free templates css/html googln mashup-template.com, download as html
"""

from flask import Flask, render_template, request, redirect    #render template allows us to send html file
import csv

app = Flask(__name__)

# auch nur @app.route('/') möglich. durch <> gibt man variable url parameters
@app.route('/index.html')
def my_home():
    return render_template("index.html")    # die Datei muss in einem Ordner namens templates sein, damit sie gefunden wird!!


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

"""
def write_to_file(userinput):
    with open("database.txt", "a") as database:
        email = userinput["email"]
        subject = userinput["subject"]
        message = userinput["message"]
        database.write(f"\n {email},  {subject} \n{message}")
"""


def write_to_csv(data):
    with open("database.csv", "a", newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer1 = csv.writer(database2, delimiter=';', quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        csv_writer1.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "did not send to database"
    else:
        return "Failed"