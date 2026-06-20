from flask import Flask, render_template
from threading import Thread
from database import create_table
from packet_capture import start_sniffing
from database import get_all_alerts

app = Flask(__name__)

create_table()

@app.route("/")
def dashboard():

    alerts = get_all_alerts()

    total_alerts = len(alerts)

    critical_alerts = len(
        [a for a in alerts if a[3] == "CRITICAL"]
    )

    top_attacker = "N/A"

    if alerts:

        ip_count = {}

        for alert in alerts:

            ip = alert[1]

            ip_count[ip] = ip_count.get(ip, 0) + 1

        top_attacker = max(ip_count, key=ip_count.get)

    return render_template(
        "dashboard.html",
        alerts=alerts,
        total_alerts=total_alerts,
        critical_alerts=critical_alerts,
        top_attacker=top_attacker
    )


def start_ids():

    start_sniffing()


if __name__ == "__main__":

    sniff_thread = Thread(target=start_ids)

    sniff_thread.daemon = True

    sniff_thread.start()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
