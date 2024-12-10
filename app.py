from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, PollingUnit, AnnouncedPUResults, LGA, AnnouncedLGAResults

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/polling_unit/<int:polling_unit_id>')
def polling_unit_result(polling_unit_id):
    results = AnnouncedPUResults.query.filter_by(polling_unit_uniqueid=polling_unit_id).all()
    return render_template('polling_unit_result.html', results=results)

@app.route('/lga_results', methods=['GET', 'POST'])
def lga_results():
    lgas = LGA.query.filter_by(state_id=25).all()
    if request.method == 'POST':
        lga_id = request.form['lga']
        results = db.session.query(
            AnnouncedPUResults.party_abbreviation,
            db.func.sum(AnnouncedPUResults.party_score).label('total_score')
        ).join(PollingUnit, PollingUnit.uniqueid == AnnouncedPUResults.polling_unit_uniqueid
        ).filter(PollingUnit.lga_id == lga_id
        ).group_by(AnnouncedPUResults.party_abbreviation).all()
        return render_template('lga_result.html', lgas=lgas, results=results)
    return render_template('lga_result.html', lgas=lgas)

@app.route('/new_polling_unit', methods=['GET', 'POST'])
def new_polling_unit():
    if request.method == 'POST':
        # Process form data and save to database
        return redirect(url_for('index'))
    return render_template('new_polling_unit.html')

if __name__ == '__main__':
    app.run(debug=True)