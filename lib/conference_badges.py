def badge_maker(name):
    return f"Hello, my name is {name}."

# print(badge_maker("tracy"))

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]
   
# print(batch_badge_creator(["alan"]))

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names, start=1):
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {index}!")
    return room_assignments
        
# print(assign_rooms(["luna"]))

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for item in badges:
        print(item)
    for item in room_assignments:
        print(item)
    
    

print(printer(["hana"]))
