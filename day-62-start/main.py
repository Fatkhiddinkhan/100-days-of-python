from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe location on Google map', validators=[DataRequired(), URL()])
    open_time = TimeField(label='Open', validators=[DataRequired()])
    close_time = TimeField(label='Close', validators=[DataRequired()])
    coffee = SelectField(label="Coffee",
                         choices=[('1', '☕️'),
                                  ('2', '☕️☕️'),
                                  ('3', '☕️☕️☕️'),
                                  ('4', '☕️☕️☕️☕️️'),
                                  ('5', '☕️☕️☕️☕️☕️')],
                         validators=[DataRequired()])
    wifi = SelectField(label="Wifi",
                       choices=[('1', '🛜'),
                                ('2', '🛜🛜'),
                                ('3', '🛜🛜🛜'),
                                ('4', '🛜🛜🛜🛜️'),
                                ('5', '🛜🛜🛜🛜🛜')],
                       validators=[DataRequired()])
    power = SelectField(label="Power",
                        choices=[('1', '🔌'),
                                 ('2', '🔌🔌'),
                                 ('3', '🔌🔌🔌'),
                                 ('4', '🔌🔌🔌🔌️'),
                                 ('5', '🔌🔌🔌🔌🔌')],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

# Helper function to convert counts to icons
def convert_to_icons(count, icon):
    try:
        count = int(count)
        return icon * count
    except ValueError:
        return '✘'


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{convert_to_icons(form.coffee.data, '☕️')},"
                           f"{convert_to_icons(form.wifi.data, '🛜')},"
                           f"{convert_to_icons(form.power.data, '🔌️')}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
