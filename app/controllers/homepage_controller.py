"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 08.29
"""

from app import app
from app.jobs import example_job
from app.utils.response import respond_json
from flask import Blueprint, request, url_for, render_template
from app.models.kerjasama import Kerjasama

mod = Blueprint("homepage_controller", __name__)


@mod.route("/", methods=["GET"])
def index():
    title = "Beranda WebApp"
    return render_template("index.html", title=title)


@mod.route("/dokumentasi", methods=["GET"])
def dokumentasi():
    kerjasama = Kerjasama.query.all()

    title = "Dokumentasi WebApp"
    return render_template("dokumentasi.html", title=title, data=kerjasama)


@mod.route('/dokumentasi/cetak', methods=['GET'])
def cetak_dokumen():
    return respond_json(
        message='Cetak Sukses',
        success=True,
    )


@mod.route("/help", methods=["GET"])
def help():
    func_list = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            func_list.append({
                'rule': rule.rule,
                'methods': [method for method in rule.methods],
            })

    return respond_json(
        message="All URL endpoints",
        success=True,
        data=func_list
    )
