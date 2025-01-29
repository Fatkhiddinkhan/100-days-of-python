import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()



def to_dict(data):
    coffee = {}
    for key, value in data.__dict__.items():
        if not key.startswith('_'):
            coffee[key] = value

    return coffee
@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_coffee():
    cafe = Cafe.query.all()
    # coffees = [coffee.name for coffee in cafe]
    # return coffees[random.randint(0,len(coffees))]
    random_coffee = random.choice(cafe)
    # return jsonify(
    #     coffee={
    #     "id": random_coffee.id,
    #     "name": random_coffee.name,
    #     "map_url": random_coffee.map_url,
    #     "img_url": random_coffee.img_url,
    #     "location": random_coffee.location,
    #     "seats": random_coffee.seats,
    #     "has_toilet": random_coffee.has_toilet,
    #     "has_wifi": random_coffee.has_wifi,
    #     "has_sockets": random_coffee.has_sockets,
    #     "can_take_calls": random_coffee.can_take_calls,
    #     "coffee_price": random_coffee.coffee_price,
    #     }
    # )

    # coffee_data = {key: value for key, value in random_coffee.__dict__.items() if not key.startswith('_')}

    return jsonify(coffee=to_dict(random_coffee))

@app.route("/get_all")
def get_all_cafes():
    cafes = Cafe.query.all()
    all_cafes = []
    for cafe in cafes:
        all_cafes.append(to_dict(cafe))

    return jsonify(cafe=all_cafes)

@app.route("/search", methods=["GET"])
def search_cafe():
    cafes = Cafe.query.all()
    location = request.args.get("loc").title()
    if location:
        all_results = []
        for cafe in cafes:
            if location == cafe.location:
                all_results.append(to_dict(cafe))

        if all_results:
            return jsonify(cafe=all_results)
        else:
            return jsonify(error={
                "Not found": f"Sorry we don't have cafe at {location}."
            })
# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    # if name:
    return jsonify(response={
        "success": "successfully add to cafe list"
    })
    # return jsonify(response={
    #         "failed": "couldn't add data sorry"
    #     })
# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    print(cafe.coffee_price)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["GET", "DELETE"])
def delete_cafe(cafe_id):
    api_key = "mike"
    user_api = request.args.get("api_key")
    if user_api == api_key:
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
if __name__ == '__main__':
    app.run(debug=True)

