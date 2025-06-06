from flask import Flask, render_template, request, redirect, url_for
from functions import (
    is_in_time,
    get_service_status,
    merge,
    search,
    calc_arrtime,
    get_time_ex,
    get_time_shin,
    attach_all_arrival_times,
)

app = Flask("TrainNavi")
ver = "v0.9.1"
debug = True


@app.route("/", methods=["GET", "POST"])
def index():
    """
    index page
    """
    print("index")
    app.logger.info("index, method: %s", request.method)
    if request.method == "POST":
        place, dest = request.form.get("place"), request.form.get("destination")
        return redirect(url_for("result", place=place, destination=dest))
    ret = render_template("index.jinja", ver=ver, status=get_service_status())
    app.logger.info("index, ret: %s", ret)
    return ret


@app.route("/result", methods=["GET"])
def result():
    app.logger.info("result, method: %s", request.method)
    place, dest = request.args.get("place"), request.args.get("destination")
    app.logger.info("place: %s", place)
    app.logger.info("dest: %s", dest)
    return render_template(
        "forhakata.jinja",
        ver=ver,
        timetable=attach_all_arrival_times(
            is_in_time(place, dest), get_time_ex(dest), get_time_shin(dest)
        ),
    )


def start_server(debug):
    app.run(host="localhost", port=5000, debug=debug)


def start_server2(debug):
    print("Starting server at port 5000 from start_server2")
    app.run(host="0.0.0.0", port=5000, debug=debug)


# start_server(debug)
start_server2(debug)
