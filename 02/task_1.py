def is_invalid_id(id: str) -> bool:
  if len(id) % 2 != 0:
    return False
  half = len(id) // 2
  first_half = id[:half]
  second_half = id[half:]
  return first_half == second_half

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

