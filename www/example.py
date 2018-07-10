from www import create_application
from www.config import Config

conf = Config()

app = create_application(conf)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
