import os
from live_music_cardiff import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=bool(os.environ.get("DEBUG"))
    )
