# import os to use clear console
import os
# import sys to call on sys.exit() function
import sys

from instruction_decode import instr_decode
# instr_decode converts the instruction part of the MIPS code
from register_decode import reg_decode


# converts the register and immediate parts of the MIPS code

# the main conversion function
# example code: add $t0, $t3, $t4


def convert(code):
    # Remove additional characters: ( ) or ,
    code = code.replace('(', ' ')
    code = code.replace(')', ' ')
    code = code.replace(',', ' ')
    code = code.replace("  ", " ")
    # Set argument to the code with single spaces
    arguments = code.split(" ")
    # Set the instruction to the first item of the string, e.g. "addi"
    instruction = arguments[0]

    if instruction == 'exit':
        sys.exit()

    # Call the instr_decode function to return the func_type, opcode and funct
    # E.g. codes = [r, 0, 0x20]
    # codes[0] = func_type
    # codes[1] = opcode
    # codes[2] = funct
    codes = instr_decode(instruction)

    # Set func_type to the first element of the codes array
    # E.g. func_type = r
    func_type = codes[0]

    # Get the numeric value of the registers by calling reg_decode()
    #                 reg_decode(     r   ,   add    ,   $t0, $t3, $t4)
    register_values = reg_decode(func_type, instruction, arguments[1:])
    # reg_decode returns values for [rs, rt, rd, shamt]
    # E.g. register_values = [11, 12, 8, 0]
    if register_values is None:
        print("Not a valid MIPS statement.")
        return

    # execution of r-type functions
    # NOTE: The :05b formatting specification formats the number passed in as binary,
    # with 5 digits, zero padded.
    if func_type == 'r':
        opcode = '{0:06b}'.format(codes[1])
        rs = '{0:05b}'.format(register_values[0])
        rt = '{0:05b}'.format(register_values[1])
        rd = '{0:05b}'.format(register_values[2])
        shamt = '{0:05b}'.format(register_values[3])
        funct = '{0:06b}'.format(codes[2])
        print('Function type: R-Type')
        print('Instruction form: opcode | rs | rt | rd | shamt | funct')
        print('Formatted binary: ' + opcode + '|' + rs + '|' + rt + '|' + rd + '|' + shamt + '|' + funct)
        binary = '0b' + opcode + rs + rt + rd + shamt + funct
        print('Binary:               ' + binary)
        hex_string = '{0:08x}'.format(int(binary, base=2))
        print('Hex:               0x' + hex_string)

    # execution for i-type functions
    elif func_type == 'i':
        opcode = '{0:06b}'.format(codes[1])
        rs = '{0:05b}'.format(register_values[0])
        rt = '{0:05b}'.format(register_values[1])
        imm = '{0:016b}'.format(register_values[2])
        print('Function type: I-Type')
        print('Instruction form: opcode | rs | rt | immediate')
        binary = '0b' + opcode + rs + rt + imm
        print('Binary:          ' + binary)
        hex_string = '{0:08x}'.format(int(binary, base=2))
        print('Hex:                0x' + hex_string)

    elif func_type == 'i':
        # execution for j-type functions
        opcode = '{0:06b}'.format(codes[1])
        imm = '{0:026b}'.format(register_values[0])
        print('Function type: J-Type')
        print('Instruction form: opcode | imm')
        binary = '0b' + opcode + imm
        print('Binary:          ' + binary)
        hex_string = '{0.08x}'.format(int(binary, base=2))
        print('Hex:          0x' + hex_string)

    else:
        print("Not a valid MIPS statement.")
        return

    return


# main code execution
os.system('clear')
print('Welcome to the MIPS decoder!')
print('Type MIPS code below to see it in binary and hex form.')
print('If using hex, use the "0x" label.')
print('Type "exit" to exit.')

while True:
    mips = input('Type MIPS code here: ')
    print()
    convert(mips)
    print('-----------')
