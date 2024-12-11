import struct
with open("maze", "rb") as f:
    data = f.read()
maze = []
for i in range(0, len(data), 4):
    maze.append(struct.unpack("<i", data[i:i+4])[0])
for i in range(27):
    for j in range(36):
        if maze[36*i+j] != -1 and maze[36*i+j] != 0:
            print(maze[36*i+j], end=" ")
        else:
            print(" ", end=" ")
    print()
s = "ddssdddddddwdddddddddsssdsddddwwwddddwwwdddsss"
print(s.replace("w", "k").replace("s", "j").replace("a", "h").replace("d", "l"))