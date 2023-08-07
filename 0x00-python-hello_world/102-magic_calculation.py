import dis
def magic_calculation(a, b):
    return 98 + (b ** a)
dis.dis(magic_calculation)
