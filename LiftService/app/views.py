from app import app
import requests

sorter = SorterService()

@app.route('/')
@app.route('/index')
def index():
  return "Core Service"

@app.route('/camera_sensor', methods=['POST'])
def camera_sensor():
  packet = Packet()
  sorter.add_packet(packet)
  packet_id = sorter.get_camera_sensor_packets_detected()
  sorter.update_camera_sensor_packets_detected()
  url = app.config['CONNECTION_PROTOCOL']+app.config['BARCODE_SERVICE_URL']+app.config['BARCODE_SERVICE_PORT']+app.config['BARCODE_SERVICE_ENDPOINT']
  headers = {}
  data = {'packet_id':packet_id}
  return requests.post(url, headers=headers, data=data)

@app.route('/barcode', methods=['POST'])
def set_barcode():
  packet_id = requests.json['packet_id']
  barcode = requests.json['barcode']
  packet = sorter.get_packet(packet_id)
  packet.barcode = barcode
  sorter.update_packet(packet_id, packet)

@app.route('/weight_sensor', methods=['POST'])
def weight_sensor():
  packet_id = sorter.get_weight_sensor_packets_detected()
  sorter.update_weight_sensor_packets_detected()
  url = app.config['CONNECTION_PROTOCOL']+app.config['WEIGHT_SERVICE_URL']+app.config['WEIGHT_SERVICE_PORT']+app.config['WEIGHT_SERVICE_ENDPOINT']
  headers = {}
  data = {'packet_id':packet_id}
  return requests.post(url, headers=headers, data=data)

@app.route('/weight', methods=['POST'])
def set_weight():
  packet_id = requests.json['packet_id']
  weight = requests.json['weight']
  packet = sorter.get_packet(packet_id)
  packet.weight = weight
  sorter.update_packet(packet_id, packet)

@app.route('/arm_sensor', methods=['POST'])
def arm_sensor():
  packet_id = sorter.get_arm_sensor_packets_detected()
  sorter.update_arm_sensor_packets_detected()
  url = app.config['CONNECTION_PROTOCOL']+app.config['ARM_SERVICE_URL']+app.config['ARM_SERVICE_PORT']+app.config['ARM_SERVICE_ENDPOINT']
  headers = {}
  data = {'packet_id':packet_id}
  return requests.post(url, headers=headers, date=data)

@app.route('/arm', methods=['POST'])
def set_arm():
  packet_id = requests.json['packet_id']
  arm = requests.json['arm']
  packet = sorter.get_packet(packet_id)
  packet.arm = arm
  sorter.update_packet(packet_id, packet)
