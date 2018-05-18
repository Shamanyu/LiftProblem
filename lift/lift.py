from collections import OrderedDict

class lift(object):

  def __init__(self, name, up_travel_time=10, down_travel_time=10):
    self.name = name
    self.up_travel_time = up_travel_time
    self.down_travel_time = down_travel_time
    self.current_instruction_id = 0
    self.instruction_dict = OrderedDict()

  def add_instruction(self, instruction):
    instruction_id = self.current_instruction_id
    self.current_instruction_id += 1
    self.instruction_dict[instruction_id] = instruction

  def remove_instruction(self, instruction_id):
    del self.instruction_dict[instruction_id]

  def process_instruction(self):
    if len(self.instruction_dict) == 0:
      return
    return self.instruction_dict.popitem(last=False)

  def  __str__(self):
    return "\nLIFT STATE\n" + \
      "Current instruction id: " + str(self.current_instruction_id) + "\n" + \
      "Up travel time: " + str(self.up_travel_time) + "\n" + \
      "Down travel time: " + str(self.down_travel_time) + "\n" + \
      "Instruction dict: " + str(self.instruction_dict) + "\n"


from nose.tools import assert_equals, assert_raises

class test_lift(object):

  def test_lift_instance(self):
    lift_instance = lift('lift-1')

    print(lift_instance)

    lift_instance.add_instruction('inst-1')
    lift_instance.add_instruction('inst-1')
    print(lift_instance)

    lift_instance.remove_instruction(0)
    print(lift_instance)

    lift_instance.add_instruction('inst-3')
    print(lift_instance)

    lift_instance.process_instruction()
    print(lift_instance)

    lift_instance.process_instruction()
    print(lift_instance)

    lift_instance.process_instruction()
    print(lift_instance)

    print ("All test cases passed!")


def main():
    test_lift_instance = test_lift()
    test_lift_instance.test_lift_instance()

if __name__ == '__main__':
    main()
