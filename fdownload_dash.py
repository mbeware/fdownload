import threading
from flask import Flask, request, render_template, redirect, url_for, jsonify
import logging
import fdownload_scan
import fdownload_download
import fdownload_channels


app = Flask(__name__)

# ---------------------------------------------------------
# Configuration du logger (messages en français)
# ---------------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("yt-app")

# ---------------------------------------------------------
# Données en mémoire (remplacer par DB si nécessaire)
# ---------------------------------------------------------


status_watch = {"status": "idle"} # Dernier statut envoyé par le process "watch"
status_download = {"status": "idle"} # Dernier statut envoyé par le process "download"

# ---------------------------------------------------------
# Fonctions de tâches en arrière-plan
# ---------------------------------------------------------
def watch_channel_worker():
    logger.info("Processus 'watch channel' démarré.")
    fdownload_scan.scan_channels()


def download_videos_worker():
    logger.info("Processus 'download videos' démarré.")
    fdownload_download.download_videos()


# ---------------------------------------------------------
# Interface utilisateur
# ---------------------------------------------------------
@app.route("/")
def index():
    channels = [] # get from DB
    return render_template("index.html", channels=channels)


@app.route("/add_channel", methods=["POST"])
def add_channel():
    # Message en français pour les logs
    url = request.form.get("channel_url")
    if not url:
        logger.warning("Tentative d'ajout de chaîne sans URL.")
        return redirect(url_for("index"))
    urld = {url: None}
    fdownload_channels.channel.create(urld)
    
    logger.info(f"Chaîne ajoutée : {url}")
    return redirect(url_for("index"))


@app.route("/remove_channel", methods=["POST"])
def remove_channel():
    index = request.form.get("channel_index")
    if index is None:
        logger.warning("Tentative de suppression sans index.")
        return redirect(url_for("index"))

    index = int(index)
    if 0 <= index < 0: #len(channels):
#        removed = channels.pop(index)
#        logger.info(f"Chaîne retirée : {removed}")
        logger.error("Not Implemented - remove_channel")
    else:
        logger.warning("Index de chaîne invalide.")
    return redirect(url_for("index"))

tscan = None
tdownload = None
@app.route("/start_watch", methods=["POST"])
def start_watch():
    # On démarre en thread
    global tscan
    if tscan and tscan.is_alive():
        logger.info("Arrêt du thread 'watch channel'.")
        tscan.stop()
        tscan.delete()
        tscan = None
        return redirect(url_for("index"))
    tscan = threading.Thread(target=watch_channel_worker, daemon=True)
    tscan.start()
    logger.info("Thread 'watch channel' lancé.")
    return redirect(url_for("index"))


@app.route("/start_download", methods=["POST"])
def start_download():
    global tdownload
    if tdownload and tdownload.is_alive():
        logger.info("Arrêt du thread 'download videos'.")
        tdownload.stop()
        tdownload.delete()
        tdownload = None
        # Note: Arrêter proprement un thread nécessite une gestion spécifique
        # Ici, on simule juste l'arrêt en ne lançant pas un nouveau thread
        return redirect(url_for("index"))
    tdownload = threading.Thread(target=download_videos_worker, daemon=True)
    tdownload.start()
    logger.info("Thread 'download videos' lancé.")
    return redirect(url_for("index"))


@app.route("/monitor")
def monitor():
    return jsonify({
        "watch": status_watch,
        "download": status_download
    })


# ---------------------------------------------------------
# Routes API pour mise à jour des statuts par les processus
# ---------------------------------------------------------
@app.route("/update_watch_status", methods=["POST"])
def update_watch_status():
    # Processus externes peuvent POST ici
    data = request.get_json(force=True)
    status_watch.update(data)
    logger.info("Statut 'watch' mis à jour.")
    return {"ok": True}


@app.route("/update_download_status", methods=["POST"])
def update_download_status():
    data = request.get_json(force=True)
    status_download.update(data)
    logger.info("Statut 'download' mis à jour.")
    return {"ok": True}

if __name__ == "__main__":
    app.run(debug=True)

