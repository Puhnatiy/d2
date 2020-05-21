import os
from bottle import route, run, Bottle, request
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
from logger import logger
import env

dns = ''

if os.environ.get("APP_LOCATION") == "heroku":
    dns = os.environ.get("SENTRY_DSN")
else:
    dns = env.SENTRY_DSN

sentry_sdk.init(dsn=dns, integrations=[BottleIntegration()])
#sentry_sdk.init(dsn="https://dbd8333bc9cf458d87de525cf308b05d@o393409.ingest.sentry.io/5242455", integrations=[BottleIntegration()])

app = Bottle()


@app.route('/fail')  
def index():  
    raise RuntimeError("Test - There is an error!")  
    return  
  
  


@app.route("/success")
def index():
    logger.info("Page Success");
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>ДЗ D2</title>
  </head>
  <body>
    <div class="container">
      <h1>Страница Success</h1>
           
    </div>
  </body>
</html>
"""
    return html

@app.route("/")
def index():
    logger.info("Page Main");
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>ДЗ D2</title>
  </head>
  <body>
    <div class="container">
      <h1>Главная страница</h1>
           
    </div>
  </body>
</html>
"""
    return html
    
    
#app.run(host='localhost', port=8080)

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)