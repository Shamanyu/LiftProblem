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

  def sort_commands(self):
    pass

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