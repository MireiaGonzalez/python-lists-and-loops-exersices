parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
state = {
    "total_slots": 0,
    "available_slots": 0,
    "occupied_slots": 0
  }
def get_parking_lot(matrix):
  for i in matrix:
    for x in i:
      if i[x] == 1:
        state["occupied_slots"] += 1
      elif i[x] == 2:
        state["available_slots"] += 1
      state["total_slots"] = state["occupied_slots"]+state["available_slots"]
      
  return state

print(get_parking_lot(parking_state))



