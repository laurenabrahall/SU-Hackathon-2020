import os
from flask import Flask, render_template
from flask import request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index-lauren.html')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/sales-page', methods=('GET', 'POST'))
    def add_product():
        if request.method == 'POST':
            product_to_add = request.form['product_to_add']
            db = get_db()

            db.execute(
                'INSERT INTO user (product_to_add, asdf) VALUES (?, ?)', 
                ('yehaaw', generate_password_hash('asdf'))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        return render_template('index-lauren.html')

    return app