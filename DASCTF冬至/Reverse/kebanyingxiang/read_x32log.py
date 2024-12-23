# 读取文件并提取每列的数据
class CODE:
    def __init__(self, index, eip, asm, dis):
        self.index = index
        self.eip = eip
        self.asm = asm
        self.dis = dis
def extract_columns_from_file(file_path):
    # 打开文件并读取所有行
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    codes = []
    # 处理每一行，提取每一列的数据
    for i in range(len(lines)):
        line = lines[i]
        # 去除行首尾的空白符，并按'|'分割
        parts = line.strip().split('|')
        # 确保行包含至少7个部分，防止异常
        if len(parts) >= 6:
            #column1.append(parts[0].strip())
            eip = int(parts[1].strip(), 16)
            asm = parts[2].strip().replace(" ", "")
            dis = parts[3].strip()
            code = CODE(i, eip, asm, dis)
            codes.append(code)
            # 返回每列的数据作为结果
    return codes

file_path = 'babyenc.log'
codes = extract_columns_from_file(file_path)

final_codes = []
final_codes.append(codes[0x5])
for i in range(0x16, len(codes) - 1):
    insert1 = 0
    insert2 = 0
    code = codes[i]
    #普通的指令
    if codes[i - 1].dis == "popad" and codes[i + 1].dis == "pushad":
        insert1 = 1
        # for k in range(len(final_codes)):
        #     if final_codes[k].eip == code.eip:
        #         insert1 = 0
        #         break
    #跳转指令
    if codes[i - 2].dis == "pushfd" and codes[i + 1].dis == "popfd":
        insert2 = 1
        # for k in range(len(final_codes)):
        #     if final_codes[k].eip == code.eip:
        #         insert2 = 0
        #         break
    if insert1 == 1 or insert2 == 1:
        final_codes.append(code)
final_codes.append(codes[len(codes)- 1])
for i in range(len(final_codes)):
    code = final_codes[i]
    print(f"{(code.eip):X} {code.asm} {code.dis}")