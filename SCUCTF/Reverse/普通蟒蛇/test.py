import check
input_flag=input('Please input your flag: ').strip()
if len(input_flag)!=17:
    print('Your flag is too short!')
elif check.check(input_flag):
    print('Congratulations!')
    print('Your flag is SCUCTF{'+input_flag+'}')
else:
    print('noooooooooooo!')