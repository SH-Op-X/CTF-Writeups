def dna_to_binary(dna_seq):
    dna_to_binary_map = {
        'A': '00',
        'C': '01',
        'G': '10',
        'T': '11'
    }

    binary_seq = ""
    for base in dna_seq:
        binary_seq += dna_to_binary_map[base]

    return binary_seq


def binary_to_text(binary_seq):
    text = ""
    for i in range(0, len(binary_seq), 8):
        byte = binary_seq[i:i + 8]
        text += chr(int(byte, 2))

    return text


# 假设DNA序列
dna_sequence = "CCCA CACG CAAT CAAT CCCA CACG CTGT ATAC CCTT CTCT ATAC CGTA CGTA CCTT CGCT ATAT CTCA CCTT CTCA CGGA ATAC CTAT CCTT ATCA CTAT CCTT ATCA CCTT CTCA ATCA CTCA CTCA ATAA ATAA CCTT CCCG ATAT CTAG CTGC CCTT CTAT ATAA ATAA CGTG CTTC"  # 这对应的二进制序列应该是 00011011
dna_sequence = dna_sequence.replace(" ", "")
# 解密过程
binary_sequence = dna_to_binary(dna_sequence)
original_text = binary_to_text(binary_sequence)

print("解密后的原文信息:", original_text)
