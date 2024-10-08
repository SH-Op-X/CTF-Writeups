import torch
import torch.nn as nn

flag='ctf{123456789012345678901234567890123456789012}'
flag_list=[]
for i in flag:
    flag_list.append(ord(i))
input=torch.tensor(flag_list, dtype=torch.float32)
n=len(input)
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.linear = nn.Linear(n, n*n)
        self.conv=nn.Conv2d(1, 1, (2, 2), stride=1,padding=1)

    def forward(self, x):
        for i in range(2209):
            sum = 0
            for j in range(47):
                sum += (mynet.linear.weight[i][j].item() * x[j].item())
            sum += mynet.linear.bias[i].item()
            print(sum)
        x = self.linear(x)
        x = x.view(1, 1, n, n)
        x=self.conv(x)
        return x
mynet=Net()
mynet.load_state_dict(torch.load('model.pth'))
output=mynet(input)
with open('ciphertext.txt', 'w') as f:
    for tensor in output:
        for channel in tensor:
            for row in channel:
                f.write(' '.join(map(str, row.tolist())))
                f.write('\n')