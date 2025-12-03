with open('./01/input.txt', 'r') as file:
  pos: int = 50
  result = 0
  for line in file:
    l = line.strip()
    direction = l[0]
    value = int(l[1:])
    if direction == 'L':
        pos -= value
    elif direction == 'R':
        pos += value
    pos = pos % 100
    if pos == 0:
      result += 1
  print(result)