import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_login import current_user
from services.groq_service import get_krishna_response
from services.shloka_service import get_daily_shloka
from models.chat import Chat
from models.conversation import Conversation
from models.reflection import Reflection
from models.user import db, User

load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "krishnai_dev_secret")

# Use PostgreSQL on production (Render sets DATABASE_URL automatically)
# Falls back to SQLite for local development
database_url = os.environ.get("DATABASE_URL", "sqlite:///database.db")
# Render gives postgres:// URLs but SQLAlchemy needs postgresql://
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
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
    conversations = Conversation.query.filter_by(user_id=current_user.id).order_by(Conversation.created_at).all()

    # Pick conversation: from query param, or the latest one, or create a default
    conv_id = request.args.get("conv_id", type=int)
    selected_conv = None

    if conv_id:
        selected_conv = Conversation.query.filter_by(id=conv_id, user_id=current_user.id).first()

    if not selected_conv and conversations:
        selected_conv = conversations[-1]

    if not selected_conv:
        # Auto-create first conversation
        selected_conv = Conversation(user_id=current_user.id, title="First Chat")
        db.session.add(selected_conv)
        db.session.commit()
        conversations = [selected_conv]

    if request.method == "POST":
        user_message = request.form["message"]
        ai_response = get_krishna_response(user_message)

        new_chat = Chat(
            user_id=current_user.id,
            conversation_id=selected_conv.id,
            user_message=user_message,
            ai_response=ai_response
        )
        db.session.add(new_chat)
        db.session.commit()
        return redirect(url_for("chat", conv_id=selected_conv.id))

    chats = Chat.query.filter_by(conversation_id=selected_conv.id).all()
    return render_template(
        "chat.html",
        chats=chats,
        conversations=conversations,
        selected_conv=selected_conv.id
    )


@app.route("/new-conversation", methods=["POST"])
@login_required
def new_conversation():
    title = request.form.get("title", "").strip() or "New Chat"
    conv = Conversation(user_id=current_user.id, title=title)
    db.session.add(conv)
    db.session.commit()
    return redirect(url_for("chat", conv_id=conv.id))


@app.route("/delete-conversation/<int:conv_id>", methods=["POST"])
@login_required
def delete_conversation(conv_id):
    conv = Conversation.query.filter_by(id=conv_id, user_id=current_user.id).first()
    if conv:
        Chat.query.filter_by(conversation_id=conv_id).delete()
        db.session.delete(conv)
        db.session.commit()
    return redirect(url_for("chat"))


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
        return redirect(url_for("reflection"))
    reflections = Reflection.query.filter_by(user_id=current_user.id).all()
    return render_template("reflection.html", reflections=reflections)


@app.route("/reflection/delete/<int:reflection_id>", methods=["POST"])
@login_required
def delete_reflection(reflection_id):
    r = Reflection.query.filter_by(id=reflection_id, user_id=current_user.id).first()
    if r:
        db.session.delete(r)
        db.session.commit()
    return redirect(url_for("reflection"))


@app.route("/reflection/edit/<int:reflection_id>", methods=["POST"])
@login_required
def edit_reflection(reflection_id):
    r = Reflection.query.filter_by(id=reflection_id, user_id=current_user.id).first()
    if r:
        new_content = request.form.get("content", "").strip()
        if new_content:
            r.content = new_content
            db.session.commit()
    return redirect(url_for("reflection"))

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
