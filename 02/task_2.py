def is_invalid_id(s_id: str) -> bool:
  # Check all possible repeating pattern lengths (from 1 to half the string length)
  for part_length in range(1, len(s_id) // 2 + 1):
    if len(s_id) % part_length != 0:
      continue
    pattern = s_id[:part_length]
    if pattern * (len(s_id) // part_length) == s_id:
      return True
  return False


with open("./02/input.txt", "r") as f:
  ranges = f.read().split(",")
  invalid_ids: list[str] = []

  for r in ranges:
    start, end = map(int, r.split("-"))
    for i in range(start, end + 1):
      some_id = str(i)
      if is_invalid_id(some_id):
        invalid_ids.append(some_id)
    
  ids_sum = sum(map(int, invalid_ids))
  print(ids_sum)

