with open("chase.log", "r") as f:
    data = f.readlines()
new_data = []
drop_list = ["$C33F", "$C341", "$C354", "$C356", "$C349", "$C34B", "$C347", "C387", "C38A", "C38B"]
for line in data:
    # if line != "\n":
    #     new_data.append(line)
    if any(drop in line for drop in drop_list):
        continue
    new_data.append(line)
with open("chase.log", "w") as f:
    f.writelines(new_data)