.file   "chal_custom.c"
.text
.section    .rodata
.LC0:
    .string "%s"
.LC1:
    .string "maybe try again!"
.LC2:
    .string "good job!"
.data
target_data:
    .string "TTDv^jrZu`Gg6tXfi+pZojpZSjXmbqbmt.&x"
.text
.globl  main
.type   main, @function
main:
    endbr64
    pushq   %rbp
    movq    %rsp, %rbp
    subq    $96, %rsp
    movq    %fs:40, %rax
    movq    %rax, -8(%rbp)
    xorl    %eax, %eax
    leaq    -80(%rbp), %rax           
    movq    %rax, %rsi
    leaq    .LC0(%rip), %rax
    movq    %rax, %rdi
    movl    $0, %eax
    call    __isoc99_scanf@PLT
    movl    $0, -84(%rbp)             
    leaq    -80(%rbp), %rdi            
    jmp     .L2
.L3:
    movl    -84(%rbp), %eax          
    movl    %eax, %ecx               
    shl     %ecx                      
    movzbl  (%rdi,%rcx), %eax        
    xorb    $7, %al                  
    movb    %al, (%rdi,%rcx)          
    movzbl  1(%rdi,%rcx), %eax        
    subb    $5, %al                    
    movb    %al, 1(%rdi,%rcx)       
    addl    $1, -84(%rbp)           
.L2:
    movl    -84(%rbp), %eax
    imull   $2, %eax                  
    cmpl    $36, %eax                 
    jl      .L3

    leaq    target_data(%rip), %rsi  
    leaq    -80(%rbp), %rdi           
    call    strcmp@PLT
    testl   %eax, %eax
    jne     .L4
    
    leaq    .LC2(%rip), %rax          
    jmp     .L5
.L4:
    leaq    .LC1(%rip), %rax          
.L5:
    movq    %rax, %rdi
    call    puts@PLT

    movl    $0, %eax
    movq    -8(%rbp), %rdx
    subq    %fs:40, %rdx
    je      .L6
    call    __stack_chk_fail@PLT
.L6:
    leave
    ret
.size   main, .-main
.ident  "GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
.section    .note.GNU-stack,"",@progbits
.section    .note.gnu.property,"a"
.align 8
.long   1f - 0f
.long   4f - 1f
.long   5
0:
    .string "GNU"
1:
    .align 8
    .long   0xc0000002
    .long   3f - 2f
2:
    .long   0x3
3:
    .align 8
4:
