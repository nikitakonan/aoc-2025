import unittest
from task_2 import Locker

class TestLocker(unittest.TestCase):
    def test_process_instruction_right_no_wrap(self):
        locker = Locker(initial_pos=50)
        locker.process_instruction("R30")
        self.assertEqual(locker.pos, 80)
        self.assertEqual(locker.code, 0)

    def test_process_instruction_left_no_wrap(self):
        locker = Locker(initial_pos=50)
        locker.process_instruction("L30")
        self.assertEqual(locker.pos, 20)
        self.assertEqual(locker.code, 0)

    def test_process_instruction_right_with_wrap(self):
        locker = Locker(initial_pos=80)
        locker.process_instruction("R30")
        self.assertEqual(locker.pos, 10)
        self.assertEqual(locker.code, 1)

    def test_process_instruction_left_with_wrap(self):
        locker = Locker(initial_pos=20)
        locker.process_instruction("L30")
        self.assertEqual(locker.pos, 90)
        self.assertEqual(locker.code, 1)

    def test_process_instruction_multiple_wraps(self):
        locker = Locker(initial_pos=50)
        locker.process_instruction("R250")
        self.assertEqual(locker.pos, 0)
        self.assertEqual(locker.code, 3)

    def test_multiple_instructions_no_wrap(self):
        locker = Locker(initial_pos=50)
        locker.process_instruction("R10")
        locker.process_instruction("L5")
        self.assertEqual(locker.pos, 55)
        self.assertEqual(locker.code, 0)

    def test_multiple_instructions_with_wraps(self):
        locker = Locker(initial_pos=80)
        locker.process_instruction("R30")  # pos=10, code=1
        locker.process_instruction("R50")  # pos=60, code=1
        locker.process_instruction("R60")  # pos=20, code=2
        self.assertEqual(locker.pos, 20)
        self.assertEqual(locker.code, 2)

    def test_multiple_instructions_alternating_directions(self):
        locker = Locker(initial_pos=50)
        locker.process_instruction("R60")  # pos=10, code=1
        locker.process_instruction("L120")  # pos=90, code=3
        locker.process_instruction("R20")  # pos=10, code=4
        self.assertEqual(locker.pos, 10)
        self.assertEqual(locker.code, 4)

    def test_multiple_instructions_accumulate_code(self):
        locker = Locker(initial_pos=95)
        locker.process_instruction("R10")  # pos=5, code=1
        locker.process_instruction("R200")  # pos=5, code=3
        locker.process_instruction("L110")  # pos=95, code=5
        self.assertEqual(locker.pos, 95)
        self.assertEqual(locker.code, 5)

    def test_multiple_instructions_accumulate_code_2(self):
        locker = Locker(initial_pos=50)
        locker.process_instruction("L68")
        locker.process_instruction("L30")
        locker.process_instruction("R48")
        locker.process_instruction("L5")
        locker.process_instruction("R60")
        locker.process_instruction("L55")
        locker.process_instruction("L1")
        locker.process_instruction("L99")
        locker.process_instruction("R14")
        locker.process_instruction("L82")
        self.assertEqual(locker.pos, 32)
        self.assertEqual(locker.code, 6)

if __name__ == '__main__':
    unittest.main()