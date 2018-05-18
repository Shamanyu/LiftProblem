from collections import OrderedDict
import random

class lift_manager(object):

  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(lift_manager, cls).__new__(cls, *args, **kwargs)
    return cls._instance

  def __init__(self):
    self.current_lift_id = 0
    self.lift_dict = dict()
    self.current_instruction_id = 0
    self.instruction_dict = OrderedDict()
    self.lift_to_instruction_map = dict()

  def add_lift(self, lift):
    lift_id = self.current_lift_id
    self.lift_dict[lift_id] = lift
    self.current_lift_id += 1
    return lift_id

  def remove_lift(self, lift_id):
    del self.lift_dict[lift_id]

  def add_instruction(self, instruction):
    instruction_id = self.current_instruction_id
    self.instruction_dict[instruction_id] = instruction
    self.current_instruction_id += 1
    return instruction_id

  def remove_instruction(self, instruction_id):
    del self.instruction_dict[instruction_id]

  def process_instructions(self):
    if len(self.instruction_dict) == 0:
      return
    instruction_to_process, _ = self.instruction_dict.popitem(last=False)
    lift_to_pass_instruction = self.__get_best_lift(instruction_to_process)
    # Send instruction to chosen lift
    # self.lift_dict[lift_to_pass_instruction].add_instruction(instruction_to_process)
    # self.lift_to_instruction_map[lift_to_pass_instruction].append(instruction_to_process)

  def __get_best_lift(self, instruction):
    return random.choice(list(self.lift_dict.keys()))

  def __str__(self):
    return "\nLIFT MANAGER STATE\n" + \
      "Current lift ID: " + str(self.current_lift_id) + "\n" + \
      "Lift dict: " + str(self.lift_dict) + "\n" + \
      "Current instruction ID: " + str(self.current_instruction_id) + "\n" + \
      "Instruction dict: " + str(self.instruction_dict) + "\n" + \
      "Lift to instruction map: " + str(self.lift_to_instruction_map)


from nose.tools import assert_equals, assert_raises

class test_lift_manager(object):

  def test_lift_manager_instance(self):
    lift_manager_instance = lift_manager()
    lift_manager_instance_clone = lift_manager()

    # Assert that 'lift_manager' is a singleton class
    assert_equals(lift_manager_instance, lift_manager_instance_clone)

    print (lift_manager_instance)

    lift_manager_instance.add_lift('lift-1')
    print (lift_manager_instance)

    lift_manager_instance.add_lift('lift-2')
    print (lift_manager_instance)

    lift_manager_instance.add_instruction('inst-1')
    print (lift_manager_instance)

    lift_manager_instance.add_instruction('inst-2')
    print (lift_manager_instance)

    lift_manager_instance.process_instructions()
    print (lift_manager_instance)

    lift_manager_instance.add_lift('lift-3')
    print (lift_manager_instance)

    lift_manager_instance.remove_lift(0)
    print (lift_manager_instance)

    lift_manager_instance.process_instructions()
    print (lift_manager_instance)

    lift_manager_instance.add_instruction('inst-3')
    print (lift_manager_instance)

    lift_manager_instance.add_instruction('inst-4')
    print (lift_manager_instance)

    lift_manager_instance.remove_instruction(2)
    print (lift_manager_instance)

    lift_manager_instance.process_instructions()
    print (lift_manager_instance)

    lift_manager_instance.process_instructions()
    print (lift_manager_instance)

    lift_manager_instance.process_instructions()
    print (lift_manager_instance)

    lift_manager_instance.process_instructions()
    print (lift_manager_instance)

    print ("All test cases passed!")


def main():
    test_lift_manager_instance = test_lift_manager()
    test_lift_manager_instance.test_lift_manager_instance()

if __name__ == '__main__':
    main()
