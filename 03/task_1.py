def join_number(a: int, b: int) -> int:
  return int(f"{a}{b}")

def find_max_joltage(bank: list[int]) -> int:
  max_number = -1
  for i in range(len(bank) - 1):
    for j in range(i + 1, len(bank)):
      candidate = join_number(bank[i], bank[j])
      if candidate > max_number:
        max_number = candidate
  return max_number

with open("./03/input.txt", "r") as f:
  lines = f.readlines()
  banks = map(lambda line: [int(char) for char in line.strip()], lines)
  bank_joltages = [find_max_joltage(bank) for bank in banks]
  result = sum(bank_joltages)
  print(bank_joltages, result)