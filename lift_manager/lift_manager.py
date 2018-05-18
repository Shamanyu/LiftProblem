from collections import OrderedDict

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
      pass
    instruction_to_process = self.instruction_dict.pop(last=False)
    lift_to_pass_instruction = __get_best_lift(instruction_to_process)
    self.lift_dict[lift_to_pass_instruction].add_instruction(instruction_to_process)
    self.lift_to_instruction_map[lift_to_pass_instruction].append(instruction_to_process)


from nose.tools import assert_equals, assert_raises

class test_lift_manager(object):

  def test_lift_manager_instance(self):
    lift_manager_instance = lift_manager()
    lift_manager_instance_clone = lift_manager()

    # Assert that 'lift_manager' is a singleton class
    assert_equals(lift_manager_instance, lift_manager_instance_clone)

    print ("All test cases passed!")


def main():
    test_lift_manager_instance = test_lift_manager()
    test_lift_manager_instance.test_lift_manager_instance()

if __name__ == '__main__':
    main()
