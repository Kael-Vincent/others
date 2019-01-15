"""
created by Vincent on 2018-7-12
"""

from app_repr import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'],port=5004)