from flask import Flask
from config.database import init_db, db
#from models.entities import Deputado, Despesa

def creat_app():
    app= Flask(__name__)
    init_db(app)

    @app.route('/')
    def index():
        return 'API CEAP conectada com DB PORRA'
    
    with app.app_context():
        db.create_all()
    
    return app
if __name__ == '__main__':
    app= creat_app()
    app.run(debug=True)
