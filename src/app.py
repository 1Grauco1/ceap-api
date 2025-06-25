from flask import Flask
from config.database import init_db, db
from routes.upload_ceap import upload_bp
from routes.deputado_routes import deputado_bp

def create_app():
    app= Flask(__name__)
    init_db(app)

    @app.route('/')
    def index():
        return 'API CEAP conectada com DB PORRA'
    
    app.register_blueprint(upload_bp)
    app.register_blueprint(deputado_bp)

    with app.app_context():
        db.create_all()
    
    return app
if __name__ == '__main__':
    app= create_app()
    app.run(debug=True)
