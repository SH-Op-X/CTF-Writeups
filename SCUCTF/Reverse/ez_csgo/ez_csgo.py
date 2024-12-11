import hashlib
import uuid

cost = [1, 7, 17, 23, 49, 68, 79, 100]
num = [8, 6, 6, 6, 6, 6, 7, 8]

def main():
    print("某天，小k闲来无事，翻找自己的库存并卖出了一些东西")
    print("但他没有记录下他卖的东西，现在他求助于你，如果你能告诉他的话他就给你你想要的东西")
    print("要不要猜一下他怎么选的呢？输入8个整数：")
    
    input_values = []
    input_str=input().split()
    for i in range(8):
        try:
            value = int(input_str[i])
            if value < 0 or value > num[i]:
                print("输入数量超出范围，请重新输入")
                return
            input_values.append(value)
        except ValueError:
            print("输入无效，请输入整数")
            return
    
    total_cost = sum(input_values[i] * cost[i] for i in range(8))
    if total_cost != 1072:
        print("你猜错了，gg")
        return
    
    str_input = ''.join(map(str, input_values))
    
    md5_hash = hashlib.md5(str_input.encode()).hexdigest()
    if md5_hash != "bd91b333c2c76df11963d2e78255462b":
        print("你猜错了，gg")
        return
    
    print("你猜对了，恭喜你！")
    
    sha1_hash = hashlib.sha1(str_input.encode()).hexdigest()
    uuid_v5 = uuid.uuid5(uuid.NAMESPACE_URL, sha1_hash)
    
    print(f"SCUCTF{{{uuid_v5}}}")

if __name__ == "__main__":
    main()