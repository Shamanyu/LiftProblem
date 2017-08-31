from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from app import views

class Lift(object):

  def __init__(self):
    self.pending_commands = list()
    self.current_floor = 0
    self.destination_floor = None
    self.direction = None

  def get_pending_commands(self):
    return self.pending_commands()

  def get_current_floor(self):
    return self.current_floor

  def get_destination_floor(self):
    return self.destination_floor

  def get_direction(self):
    return self.direction

  def go_to(self, floor):
    self.pending_commands.append((go_to, floor))
    self.sort_commands()
    self.process_commands()

  def cancel_go_to(self, floor):
    command = (go_to, floor)
    try:
      self.pending_commands.remove(command)
    except:
      pass
    self.process_commands()

  def process_commands(self):
    if not self.destination_floor:
      command_to_process = self.pending_commands.pop(0)
      self.process_command(command_to_process)

  def process_command(self, command_to_process):
    command, self.destination_floor = command_to_process
    while (self.current_floor > self.destination_floor):
      self.direction = 'down'
      self.move()
      self.current_floor -= 1
    while (self.current_floor < self.destination_floor):
      self.direction = 'up'
      self.move()
      self.current_floor += 1
    self.stop()
    self.process_commands()

  def move(self):
    sleep(1)

  def stop(self):
    sleep(4)
    self.destination_floor = None
    self.direction = None

  def sort_commands(self):
    self.pending_commands.sort(command_sort)

  def command_sort(self, command1, command2):
    command_a, destination_floor_a = command1
    command_b, destination_floor_b = command2
    if (self.current_floor < destination_floor_a and 
      self.current_floor < destination_floor_b and
      self.destination_floor_a < self.destination_floor_b and
      self.direction = 'up'):
      return 1
    elif (self.current_floor < destination_floor_a and 
      self.current_floor < destination_floor_b and
      self.destination_floor_a > self.destination_floor_b
      and self.direction = 'up'):
      return -1
    elif (self.current_floor < destination_floor_a and
      self.current_floor > destination_floor_b and
      self.direction = 'up'):
      return 1
    elif (self.current_floor > destination_floor_a and
      self.current_floor < destination_floor_b and 
      self.direction = 'up'):
      return -1
    elif (self.current_floor > destination_floor_a and
      self.current_floor > destination_floor_b and
      destination_floor_a > destination_floor_b and
      self.direction = 'up'):
      return 1
    elif (self.current_floor > destination_floor_a and
      self.current_floor > destination_floor_b and
      destination_floor_a < destination_floor_b and
      self.direction = 'up'):
      return -1
    if (self.current_floor < destination_floor_a and 
      self.current_floor < destination_floor_b and
      self.destination_floor_a < self.destination_floor_b and
      self.direction = 'down'):
      return -1
    elif (self.current_floor < destination_floor_a and 
      self.current_floor < destination_floor_b and
      self.destination_floor_a > self.destination_floor_b
      and self.direction = 'down'):
      return 1
    elif (self.current_floor < destination_floor_a and
      self.current_floor > destination_floor_b and
      self.direction = 'down'):
      return -1
    elif (self.current_floor > destination_floor_a and
      self.current_floor < destination_floor_b and 
      self.direction = 'down'):
      return 1
    elif (self.current_floor > destination_floor_a and
      self.current_floor > destination_floor_b and
      destination_floor_a > destination_floor_b and
      self.direction = 'down'):
      return -1
    elif (self.current_floor > destination_floor_a and
      self.current_floor > destination_floor_b and
      destination_floor_a < destination_floor_b and
      self.direction = 'down'):
      return 1
    return 0


class LiftManager(object):

  def __init__(self):
    self.lifts = list()

  def add_lift(self, lift):
    self.lifts.append(lift)

  def remove_lift(self, lift):
    self.lifts.remove(lift)

  def summon_lift(self, floor, direction):
    optimal_lift = self.find_optimal_lift(floor, direction)
    optimal_lift.go_to(floor)

  def find_optimal_lift(self, floor, direction):
    optimal_lift = None
    optimal_lift_score = float('inf')
    for lift in optimal_lift:
      if direction == lift.get_direction() and floor > lift.get_current_floor():
        score = floor - lift.get_current_floor()
      elif direction == lift.get_direction() and floor < lift.get_current_floor():
        score = 1000
      elif direction != lift.get_direction() and floor > lift.get_current_floor():
        score = 1000
      elif direction != lift.get_direction() and floor < lift.get_current_floor():
        score = 1000
      else
        pass
      if score < optimal_lift_score:
        optimal_lift = lift
        optimal_lift_score = score
    return optimal_lift
