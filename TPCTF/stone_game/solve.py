import re
from pwn import *


def calculate_move(segments):
    nim_sum = 0
    for s in segments:
        nim_sum ^= s
    if nim_sum == 0:
        # 无必胜策略，随便取一个非零堆取1（出现概率低）
        for i in range(7):
            if segments[i] > 0:
                return [1 if j == i else 0 for j in range(7)]
        return [0] * 7  # 不会触发
    # 寻找需要调整的堆
    highest_bit = 1 << (nim_sum.bit_length() - 1)
    for i in range(7):
        if segments[i] & highest_bit:
            target = i
            break
    # 计算需要移除的数量
    needed = segments[target] ^ nim_sum
    remove = segments[target] - needed
    move = [0] * 7
    move[target] = remove
    return move


def parse_segments(data):
    # 处理可能的换行符问题
    cleaned = data.replace('\r\n', '\n').replace('\r', '\n')
    matches = re.findall(r'Segment \d+: (\d+) stones', cleaned)
    return list(map(int, matches)) if len(matches) == 7 else None

def check_won(data):
    if "won" in data:
        return True

def main():
    conn = remote('1.95.128.179', 3626)  # 修改为实际地址
    conn.recvuntil(b'Press Enter to start...')
    conn.sendline()

    for _ in range(100):
        for i in range(2):
            # 接收数据直到输入提示
            data = conn.recvuntil(b'Enter the number of stones to remove from each segment (space-separated, e.g.: 0 1 0 2 0 0 0):').decode()
            print(data)
            # if check_won(data):
            #     break
            # 解析石子数
            segments = parse_segments(data)[-7:]
            # 计算移动
            # move = calculate_move(segments)
            if i == 0:
                move = segments[:4]+[0]*3
            elif i == 1:
                move = segments
            # data = conn.recvline().decode()
            # if check_won(data):
            #     break
            # data = conn.recvline().decode()
            # if check_won(data):
            #     break
            # 发送移动
            move_str = ' '.join(map(str, move))
            print(f"Sending move: {move_str}")
            conn.sendline(move_str.encode())
            # 接收AI回合结果
            result = conn.recvuntil(b'Current player: AI', timeout=2).decode()
            print(result)


    # 获取最终结果
    print(conn.recv().decode())


if __name__ == '__main__':
    main()