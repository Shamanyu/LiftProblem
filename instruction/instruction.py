class instruction(object):

  def __init__(self, name, sub_instruction_list=[]):
    self.name = name
    self.sub_instruction_list = sub_instruction_list

  def __str__(self):
    return "\nINSTRUCTION STATE\n" + \
        "Name: " + self.name + "\n" + \
        "Sub instruction list: " + str(self.sub_instruction_list) + "\n"

from nose.tools import assert_equals, assert_raises

class test_instruction(object):

  def test_instruction_instance(self):

    instruction_instance_1 = instruction('inst-1')
    print(instruction_instance_1)

    instruction_instance_2 = instruction('inst-2', [0])
    print(instruction_instance_2)

    instruction_instance_3 = instruction('inst-3')
    print(instruction_instance_3)

    print ("All test cases passed!")


def main():
    test_instruction_instance = test_instruction()
    test_instruction_instance.test_instruction_instance()

if __name__ == '__main__':
    main()
