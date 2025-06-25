# Entry point for the Flask app
from inventory.routes import app

if __name__ == "__main__":
    app.run(debug=True)