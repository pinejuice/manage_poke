import sys
sys.dont_write_bytecode = True

from flask import Blueprint, render_template, current_app

calc_status_sv = Blueprint("calc_status_sv", __name__, template_folder="templates")

@calc_status_sv.route("/calc/status/sv", methods=("GET", ))
def display_calc_status_sv():
    print('call')
    return render_template(
        "calc_status_sv.html"
    )
