from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_login import current_user
from services.groq_service import get_krishna_response
from services.shloka_service import get_daily_shloka
from models.chat import Chat
from models.reflection import Reflection
from models.user import db, User


app = Flask(__name__)
app.config["SECRET_KEY"] = "krishnai_secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return "KrishnAI is running 🙏"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"]
        )
        user.set_password(request.form["password"])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and user.check_password(request.form["password"]):
            login_user(user)
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    response = None

    if request.method == "POST":
        user_message = request.form["message"]
        response = get_krishna_response(user_message)

        chat = Chat(
            user_id=current_user.id,
            user_message=user_message,
            ai_response=response
        )
        db.session.add(chat)
        db.session.commit()

    return render_template("chat.html", response=response)


@app.route("/daily-shloka")
@login_required
def daily_shloka():
    shloka = get_daily_shloka()
    return render_template("daily_shloka.html", shloka=shloka)

@app.route("/reflection", methods=["GET", "POST"])
@login_required
def reflection():
    if request.method == "POST":
        r = Reflection(
            user_id=current_user.id,
            content=request.form["content"]
        )
        db.session.add(r)
        db.session.commit()
    reflections = Reflection.query.filter_by(user_id=current_user.id).all()
    return render_template("reflection.html", reflections=reflections)

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/about")
@login_required
def about():
    return render_template("about.html")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
