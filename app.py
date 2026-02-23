from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_login import current_user
from services.groq_service import get_krishna_response
from services.shloka_service import get_daily_shloka
from models.chat import Chat
from models.conversation import Conversation
from models.reflection import Reflection
from models.user import db, User
from services.krishna_prompt import KRISHNA_PROMPT
from sqlalchemy import inspect, text


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
    return redirect(url_for("dashboard"))

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
    # list user's conversations (for tabs)
    conversations = Conversation.query.filter_by(user_id=current_user.id).order_by(Conversation.created_at.desc()).all()

    # determine selected conversation id (from query param)
    conv_id = request.args.get('conv_id', type=int)

    # if none selected, pick the most recent, or create one if none exist
    if not conv_id:
        if conversations:
            conv_id = conversations[0].id
        else:
            # create a default conversation
            new_conv = Conversation(user_id=current_user.id, title="New Chat")
            db.session.add(new_conv)
            db.session.commit()
            conv_id = new_conv.id
            conversations.insert(0, new_conv)

    # load chats for the selected conversation only
    chats = Chat.query.filter_by(user_id=current_user.id, conversation_id=conv_id).order_by(Chat.id.asc()).all()

    if request.method == "POST":
        user_message = request.form["message"]

        # build messages list for model: system prompt + previous exchanges from this conversation
        messages = [{"role": "system", "content": KRISHNA_PROMPT}]
        for c in chats[-20:]:  # keep last 20 for context
            messages.append({"role": "user", "content": c.user_message})
            messages.append({"role": "assistant", "content": c.ai_response})

        # add the newest user message
        messages.append({"role": "user", "content": user_message})

        # request AI response with conversation history
        response = get_krishna_response(messages)

        # persist message linked to conversation
        chat = Chat(
            user_id=current_user.id,
            conversation_id=conv_id,
            user_message=user_message,
            ai_response=response
        )
        db.session.add(chat)
        db.session.commit()

        # reload chats to include the new one
        chats = Chat.query.filter_by(user_id=current_user.id, conversation_id=conv_id).order_by(Chat.id.asc()).all()

        return render_template("chat.html", chats=chats, conversations=conversations, selected_conv=conv_id)

    return render_template("chat.html", chats=chats, conversations=conversations, selected_conv=conv_id)


@app.route("/chat/new", methods=["POST"])
@login_required
def new_conversation():
    title = request.form.get('title') or "New Chat"
    conv = Conversation(user_id=current_user.id, title=title)
    db.session.add(conv)
    db.session.commit()
    return redirect(url_for('chat', conv_id=conv.id))



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

@app.route("/reflection/delete/<int:reflection_id>", methods=["POST"])
@login_required
def delete_reflection(reflection_id):
    reflection = Reflection.query.get_or_404(reflection_id)

    # Security check: only owner can delete
    if reflection.user_id != current_user.id:
        abort(403)

    db.session.delete(reflection)
    db.session.commit()

    return redirect(url_for("reflection"))


@app.route("/reflection/edit/<int:reflection_id>", methods=["POST"])
@login_required
def edit_reflection(reflection_id):
    reflection = Reflection.query.get_or_404(reflection_id)

    # Security check: only owner can edit
    if reflection.user_id != current_user.id:
        abort(403)

    new_content = request.form.get("content", "").strip()
    if new_content:
        reflection.content = new_content
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
    # create any missing tables
    db.create_all()

    # Ensure older DBs get the new `conversation_id` column on `chat` table
    try:
        inspector = inspect(db.engine)
        cols = [c['name'] for c in inspector.get_columns('chat')]
        if 'conversation_id' not in cols:
            with db.engine.connect() as conn:
                conn.execute(text('ALTER TABLE chat ADD COLUMN conversation_id INTEGER'))
                conn.commit()
            print('Migration: added conversation_id to chat table')
    except Exception as e:
        # If inspection or alter fails, print and continue — user may prefer to run migrations manually
        print('Migration check failed or not applicable:', e)

if __name__ == "__main__":
    app.run(debug=True)
