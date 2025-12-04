def find_max_joltage(bank: str) -> int:
  """
  Greedy algorithm: O(n * k) where n = len(bank), k = 12
  For each of 12 positions, scan remaining digits and pick the largest
  that still leaves enough digits to complete the selection.
  """
  n = len(bank)
  k = 12 # number of digits to select
  
  result = []
  start_idx = 0

  for position in range(k):
    remaining_needed = k - position - 1

    search_end = n - remaining_needed

    max_digit = '0'
    max_idx = start_idx

    for i in range(start_idx, search_end):
      if bank[i] > max_digit:
        max_digit = bank[i]
        max_idx = i

    result.append(max_digit)
    start_idx = max_idx + 1

  return int("".join(result))

if __name__ == "__main__":
  with open("./03/input.txt", "r") as f:
    lines = f.readlines()
    banks = [line.strip() for line in lines]
    bank_joltages = [find_max_joltage(bank) for bank in banks]
    result = sum(bank_joltages)
    print(bank_joltages, result)