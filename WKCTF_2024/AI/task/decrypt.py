import torch
import torch.nn as nn
n=47
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.linear = nn.Linear(n, n*n)
        self.conv=nn.Conv2d(1, 1, (2, 2), stride=1,padding=1)

    def forward(self, x):
        x = self.linear(x)
        x = x.view(1, 1, n, n)
        x=self.conv(x)
        return x
mynet=Net()
mynet.load_state_dict(torch.load('model.pth'))
with open('ciphertext.txt') as f:
    output = f.readlines()
    output = [[float(i) for i in s.split()] for s in output]
    # print(output)

conv_before = []
for i in range(47):
    conv_line = []
    for j in range(47):
        if i == 0 and j == 0:
            conv_line.append((output[i][j]+4)/(-3))
        elif i == 0:
            conv_line.append((output[i][j]+4-conv_line[-1]*(-6))/(-3))
        elif j == 0:
            conv_line.append((output[i][j]+4-conv_before[-1][j]*9)/(-3))
        else:
            conv_line.append((output[i][j]+4-conv_line[-1]*(-6)-conv_before[-1][j]*9-conv_before[-1][j-1]*(-4))/(-3))
    conv_before.append(conv_line)
print(conv_before, len(conv_before), len(conv_before[0]))
linear_after = []
for i in conv_before:
    linear_after += i
from z3 import *
flag = [Int(f'flag{i}') for i in range(0, 47)]

solver = Solver()
for i in range(2209):
    sum = 0
    for j in range(47):
        sum += (mynet.linear.weight[i][j].item() * flag[j])
    solver.add(sum + mynet.linear.bias[i].item() == conv_before[i//47][i%47])
if solver.check() == sat:  # check()方法用来判断是否有解，sat(即satisify)表示满足有解
    ans = solver.model()  # model()方法得到解
    for i in flag:
        print(chr(ans[i].as_long()), end='')