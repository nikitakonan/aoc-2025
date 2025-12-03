class Locker:
  def __init__(self, initial_pos: int = 50):
    self.pos = initial_pos
    self.code = 0

  def process_instruction(self, instruction: str):
    direction = instruction[0]
    value = int(instruction[1:])

    if direction == 'L':
      self.pos -= value
    elif direction == 'R':
      self.pos += value

    count = abs(self.pos // 100)

    self.pos = self.pos % 100
    self.code += count

  def get_code(self) -> int:
    return self.code

with open('./01/input.txt', 'r') as f: 
  locker = Locker()

  for line in f:
    locker.process_instruction(line.strip())
      
  print(locker.get_code())

