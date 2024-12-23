from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from .models import User
from . import db
import os

bp = Blueprint('main', __name__)


@bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            if not email or not password:
                return jsonify({"error": "Email and password are required"}), 400
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.user_profile', user_id=new_user.id))
        except Exception as e:
            return jsonify({"error": "An error occurred while creating the user."}), 500
    return render_template("home.html")


@bp.route("/user/<int:user_id>")
def user_profile(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        total_users = User.query.count()
        db_size = os.path.getsize('users.db')
        return render_template("user_profile.html", user=user, total_users=total_users, db_size=db_size), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching the user profile."}), 500
