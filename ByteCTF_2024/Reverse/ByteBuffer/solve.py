import struct

with open("ByteBuffer.bin", "rb") as f:
    data = f.read()
k = 0x3ac
Edge = []
size = 9
while k < 0x11f0:
    Edge.append(data[k:k+4*size])
    k += 4*size
    if k > 0x10e0:
        size = 8
for i in range(len(Edge)):
    e = Edge[i]
    base = 8
    Edge[i] = (struct.unpack("<I", e[base:base+4])[0], struct.unpack("<I", e[base+4:base+8])[0])
Edge.append((2, 1))     # 手动添加
print(Edge)

k = 0x1230
Dot = []
size = 8
while k < 0x1f80:
    Dot.append(data[k:k+4*size])
    k += 4*size
    if k == 0x14d0:
        size = 7
for i in range(len(Dot)):
    d = Dot[i]
    base = 4
    Dot[i] = (struct.unpack("<I", d[base:base+4])[0], struct.unpack("<I", d[base+4:base+8])[0])
Dot = Dot[::-1]
Dot.insert(1, (25, 75))    # 手动添加
print(Dot)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))
# 绘制点
for point_id, (x, y) in enumerate(Dot):
    plt.scatter(x, y)
    plt.text(x, y, point_id+1)

# 绘制线段
for e in Edge:
    x_values = [Dot[e[0]-1][0], Dot[e[1]-1][0]]
    y_values = [Dot[e[0]-1][1], Dot[e[1]-1][1]]
    plt.plot(x_values, y_values, color='blue', marker='o')
plt.gca().invert_yaxis()
# 添加标签和图例
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Dot and Edge')
plt.legend()
plt.axis('equal')
# 显示图形
plt.show()
