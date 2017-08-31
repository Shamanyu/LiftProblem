from app import app
import requests

lift_manager = LiftManager()

@app.route('/')
@app.route('/index')
def index():
  return "Lift manager"

@app.route('/summon_lift', methods=['POST'])
def summon_lift():
  floor = requests.json['floor']
  direction = requests.json['direction']
  lift_manager.summon_lift(floor, direction)

@app.route('/go_to', methods=['POST'])
def go_to():
  destination_floor = requests.json['destination_floor']
  lift.go_to(floor)

@app.route('/cancel_go_to', methods=['POST'])
def cancel_go_to():
  canceled_floor = requests.json['canceled_floor']
  lift.cancel_go_to(canceled_floor)