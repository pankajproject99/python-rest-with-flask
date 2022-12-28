from flask import Blueprint, render_template, jsonify

second = Blueprint('second', __name__, static_folder="static", template_folder="templates")


@second.route("/home")
@second.route("/")
def home():
    return "Im in Second Router";
