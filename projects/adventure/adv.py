from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


def travel_maze(player, world, room_graph):
    path = []
    room_stack = []
    room_stack.append(player.current_room.id)  # add starting room to stack
    print(player.current_room.id)
    visited_rooms = set()

    while len(visited_rooms) != len(world.rooms):  # traversal through the rooms
        current_room = room_stack[-1]  # current room is always the first item
        visited_rooms.add(current_room)  # add current room to visted
        connecting_rooms = room_graph[current_room][1]  # checking main maze
        connecting_rooms_queue = []

        for name, con_room in connecting_rooms.items():  # use .items so we can check keys with values
            if con_room not in visited_rooms:
                connecting_rooms_queue.append(
                    con_room)  # add the room to queue

        if len(connecting_rooms_queue) != 0:  # checking the queue as long as its not 0
            # setting next room to first item in queue
            next_room = connecting_rooms_queue[0]
            room_stack.append(next_room)  # adds to stack

        else:  # if queue is empty
            room_stack.pop()  # gets rid of last item on room stack
            # sets the next room to the last item on room stack
            next_room = room_stack[-1]
        for name, con_room in connecting_rooms.items():
            if con_room == next_room:  # if next room is in connecting_rooms
                path.append(name)  # add the name of that room to the path
    return path


traversal_path = travel_maze(player, world, room_graph)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
