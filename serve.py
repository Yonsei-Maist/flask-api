from api import create_app
import sys

app = create_app(sys.argv[2])

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
