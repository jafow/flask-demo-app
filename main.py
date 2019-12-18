"""
for running simple debug flask server without uwsgi
otherwise manage.py will be called by uwsgi
"""
from app import create_app


if __name__ == "__main__":
    print("Running Main app dev server")
    app = create_app()
    app.run(host="0.0.0.0", port=80, debug=True)
