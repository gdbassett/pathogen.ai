# Initially based off of https://github.com/yefim/flask-heroku-sample

import os

from flask import Flask, render_template, request, redirect, url_for
from flask_restful import reqparse
import logging
# TODO: Set 'False' before launch
use_debugger=False
#from flask.ext.sqlalchemy import SQLAlchemy

# Variables
test_key = "6da80b8abed714cc033779f72ccdbbad"
#pathologists = []
pathologists = ["4843e5c207993ad07e0f3a211a44e9d5",  # Alexa Hudson 
                "75bb0824219e060bd5d4a560d606461d", # Nude Haberdasher
                "b3eb869972c959bdd9642433970ae414", # rob boodis
                "6fbbb157a00d8bf8e3a3b7b1b91a3e38",  # Bhaskar 
                "89c7c9211cd041376d4b1e52d962c1f9",  # Porter
                "73a11c2a1b0b2593fe4ee7e3e5e2fc79",  # baker
                "9d7e1007ecf7445a02f5ed83b32ff32c",  # Jay
                "8312475fe80119819e749b6527dfa534",  # Ally
                "d2c6602d18956acccdf68ebdfe29bb38",  # Tippet
                ] # Pathologist hashes
# TODO: Uncomment core ai hash value
ai_core_hash = "ls0tli4wljauli4ums4xljexll9fls0u" # lower case of: LS0tLi4wLjAuLi4uMS4xLjExLl9fLS0u" # hash of "---..0.0....1.1.11.__--."
#four_pathologists_link = "http://pathogen.ai.s3-website-us-east-1.amazonaws.com/bla"
# TODO: Replace with correct link
four_pathologists_link = "https://s3.amazonaws.com/pathogen.ai/infection_log.8f94829b479a2585e080ab0d4a39df89"
five_pathologists_link = "https://s3.amazonaws.com/pathogen.ai/infection_log.10d410815ce5c064c370a174dc75a44a"
six_plus_pathologists_link = "https://s3.amazonaws.com/pathogen.ai/infection_log.eeda0ec273f57ae84d0b911b6fa3f2f2"

# Flavor Text
alex_hash = "7fc18d46fbc43fe11abc10d71f22fc0e"
david_hash = "e250e4d199da0b089a134a71bf205aa1"

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
  pathologists_submitted = [str(p).lower() for p in pathologists_submitted]
  test_key_submitted = request.args.get("test_key", False)
  noarc = request.args.get('noarc', "false")
  noarc = noarc.lower()
  nofx = request.args.get('nofx', "false")
  nofx = nofx.lower()


  flavor_text = ""
  if alex_hash in pathologists_submitted:
    flavor_text = flavor_text + "console.log('Alex Pinto detected.  Might be a threat if we hadn\\'t planted an infected quadcopter with him last year.  Deploying attack copter.');\n"
  if david_hash in pathologists_submitted:
    flavor_text = flavor_text + "console.log('Darth Null detected.  Deploying obscure cyphertext to his home to occupy him.');\n"

  # look up submitted hashes
  #log.debug(pathologists_submitted)
  #log.debug(pathologists) 
  #TODO: Remove test_key check
  #if test_key_submitted == test_key:
  if 1 == 1:
    pathologists_submitted = set(pathologists_submitted).intersection(pathologists)
  else:
    pathologists_submitted = []
  pathologists_cnt = len(pathologists_submitted)
  #log.debug(pathologists_cnt)
  if pathologists_cnt < 0:
    clrRate=0
  elif pathologists_cnt > 0 and pathologists_cnt < 6:
    clrRate = {0:0.01, 1:0.05, 2:0.25, 3:0.75, 4:0.8, 5:0.95, 6:1}[pathologists_cnt]
  else: # pathologists_cnt >= 6
    clrRate = 1

  # TODO: Swap values and replace hash when ready to initialize project
  initialize_core = "console.log('Initiating AI core {0}')\n".format(ai_core_hash)
  #initialize_core = "console.log('Waiting to initialize AI core');"

  # providing warning of detection
  detect_pathologist = "console.log('Beginning monitoring Global cyberCDC team for cyber pathologists.');\n"
  if pathologists_cnt < 1:
    detect_pathologist = detect_pathologist + "console.log('One insignficiant Cyber Pathologist found. No impact projected.');\n"
  elif pathologists_cnt == 1:
    detect_pathologist = detect_pathologist + "console.log('Significant Cyber Pathologist Detected! Infection rates may be affected. No preventative measures taken yet.');\n"
  elif pathologists_cnt > 1 and pathologists_cnt < 4:
    detect_pathologist = detect_pathologist + "console.log('Significant Cyber Pathologists Detected! Infection rates may be affected. No preventative measures taken yet.');\n"
  else:  # pathologists_cnt > 4
    detect_pathologist = detect_pathologist + "console.log('Significant Cyber Pathologists Detected! Infection rates may be affected.');\n"
  for p in pathologists_submitted:
    detect_pathologist = detect_pathologist + "console.log('Pathologist {0} identified.');\n".format(p)
  if pathologists_cnt == 4:
    detect_pathologist = detect_pathologist + "console.log('Cyber pathologist team has endangered core operations.');\n"
    detect_pathologist = detect_pathologist + "console.log('Duplicating cyber pathogen state {0} to preserve disaster recovery options.');\n".format(four_pathologists_link)
  elif pathologists_cnt == 5:
    detect_pathologist = detect_pathologist + "console.log('Cyber pathologist team has compromised core operations.');\n"
    detect_pathologist = detect_pathologist + "console.log('Duplicating cyber pathogen state {0} to preserve disaster recovery options.');\n".format(five_pathologists_link)
  elif pathologists_cnt >= 6 and pathologists_cnt < 9:
    detect_pathologist = detect_pathologist + "console.log('Cyber pathologist team has disrupted core operations.');\n"
    detect_pathologist = detect_pathologist + "console.log('Imediately duplicating cyber pathogen state {0} to preserve recover viability.  No further mitigations available.');\n".format(six_plus_pathologists_link)
  elif pathologists_cnt >= 9:
    detect_pathologist = detect_pathologist + "console.log('MERCY! I give up!  It was Kevin Thompson!  Kevin was patient zero!  Now won\\'t you just leave me alone!');\n"
    detect_pathologist = detect_pathologist + "console.log('Jerk!');\n"
  # TODO: Comment out below line prior to cover challenge
  #detect_pathologist = ""

  # return correct page
#  return render_template('index.html', users = User.query.all())
  return render_template('index.html', clearRate=clrRate, 
                                       nofx=nofx, 
                                       noarc=noarc, 
                                       detect_pathologist=detect_pathologist, 
                                       initialize_core=initialize_core,
                                       flavor_text=flavor_text) # No pathologists

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
  app.run(host='0.0.0.0', 
          port=port,
          use_debugger=use_debugger,
          debug=use_debugger,
          use_reloader=use_debugger)