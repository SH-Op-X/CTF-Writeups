from challenge import StackVM
vm = StackVM()
flag = input("Enter your flag: ")
vm.input_buffer = list(flag)
vm.vm_execute()