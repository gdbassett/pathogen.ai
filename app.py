# Initially based off of https://github.com/yefim/flask-heroku-sample

import os

from flask import Flask, render_template, request, redirect, url_for
from flask_restful import reqparse
import logging
#from flask.ext.sqlalchemy import SQLAlchemy

# Variables
pathologists = []
pathologists = ["A", "B", "C", "D", "E", "F"] # Pathologist hashes
#ai_core_hash = "---..0.0....1.1.11.__--."
#four_pathologists_link = "http://pathogen.ai.s3-website-us-east-1.amazonaws.com/bla"
four_pathologists_link = ""
five_pathologists_link = ""
six_plus_pathologists_link = ""

# Argument Parser
#api_parser = reqparse.RequestParser()
#api_parser.add_argument('pathologist', type=str, action='append')

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')
#db = SQLAlchemy(app)

#class User(db.Model):
#  id = db.Column(db.Integer, primary_key=True)
#  name = db.Column(db.String(100))
#  email = db.Column(db.String(100))
#  def __init__(self, name, email):
#    self.name = name
#    self.email = email

@app.route('/')
def index():
  global pathologists

  # Logging
  console = logging.StreamHandler()
  log = logging.getLogger("asdasd")
  log.addHandler(console)
  log.setLevel(logging.DEBUG)

  # Pause a few seconds so people don't brute force (or other brute force protection)

  # Get arguments
  pathologists_submitted = request.args.getlist('pathologist')
  nofx = request.args.get('nofx', "false")
  nofx = nofx.lower()

  # look up submitted hashes
  #log.debug(pathologists_submitted)
  #log.debug(pathologists) 
  pathologists_submitted = set(pathologists_submitted).intersection(pathologists)
  pathologists_cnt = len(pathologists_submitted)
  log.debug(pathologists_cnt)
  clrRate = {0:0.01, 1:0.05, 2:0.25, 3:0.75, 4:0.8, 5:0.95, 6:1}[pathologists_cnt]

  # Swap values and replace hash when ready to initialize project
  #initialize_core = "console.log('Initiating AI core {0}')\n".format(ai_core_hash)
  initialize_core = ""

  # providing warning of detection
  detect_pathologist = "console.log('Beginning monitoring Global cyberCDC team for cyber pathologists.')\n"
  if pathologists_cnt <= 1:
    detect_pathologist = detect_pathologist + "console.log('One insignficiant Cyper Pathologist found. No impact projected.')\n"
  elif pathologists_cnt == 1:
    detect_pathologist = detect_pathologist + "console.log('Significant Cyber Pathologist Detected! Infection rates may be affected.')\n"
  elif pathologists_cnt > 1:
    detect_pathologist = detect_pathologist + "console.log('Significant Cyber Pathologists Detected! Infection rates may be affected.')\n"
  for p in pathologists_submitted:
    detect_pathologist = detect_pathologist + "console.log('Pathologist {0} identified.')\n".format(p)
  if pathologists_cnt == 4:
    detect_pathologist = detect_pathologist + "console.log('Cyber pathologist team has endangered core operations.')\n"
    detect_pathologist = detect_pathologist + "console.log('Duplicating cyber pathogen state 0} to preserve disaster recovery options.')\n".format(four_pathologists_link)
  elif pathologists_cnt == 5:
    detect_pathologist = detect_pathologist + "console.log('Cyber pathologist team has compromised core operations.')\n"
    detect_pathologist = detect_pathologist + "console.log('Duplicating cyber pathogen state {0} to preserve disaster recovery options.')\n".format(four_pathologists_link)
  elif pathologists_cnt >= 6:
    detect_pathologist = detect_pathologist + "console.log('Cyber pathologist team has disrupted core operations.')\n"
    detect_pathologist = detect_pathologist + "console.log('Imediately duplicating cyber pathogen state {0} to preserve recover viability.')\n".format(four_pathologists_link)


  # return correct page
#  return render_template('index.html', users = User.query.all())
  return render_template('index.html', clearRate=clrRate, nofx=nofx, detect_pathologist=detect_pathologist, initialize_core=initialize_core) # No pathologists

#@app.route('/user', methods=['POST'])
#def user():
#  if request.method == 'POST':
#    u = User(request.form['name'], request.form['email'])
#    db.session.add(u)
#    db.session.commit()
#  return redirect(url_for('index'))

if __name__ == '__main__':
#  db.create_all()
  port = int(os.environ.get('PORT',5000))
  app.run(host='0.0.0.0', port=port)