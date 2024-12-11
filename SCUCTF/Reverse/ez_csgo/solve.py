import hashlib
import uuid

cost = [1, 7, 17, 23, 49, 68, 79, 100]
for a in range(8+1):
    for b in range(6+1):
        for c in range(6+1):
            for d in range(6+1):
                for e in range(6+1):
                    for f in range(6+1):
                        for g in range(7+1):
                            for h in range(8+1):
                                if cost[0]*a+cost[1]*b+cost[2]*c+cost[3]*d+cost[4]*e+cost[5]*f+cost[6]*g+cost[7]*h == 1072:
                                    str_input = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)
                                    if "bd91b333c2c76df11963d2e78255462b" == hashlib.md5(str_input.encode()).hexdigest():
                                        sha1_hash = hashlib.sha1(str_input.encode()).hexdigest()
                                        uuid_v5 = uuid.uuid5(uuid.NAMESPACE_URL, sha1_hash)
                                        print(f"SCUCTF{{{uuid_v5}}}")