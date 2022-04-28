from scipy.optimize import fsolve
import math

def loop(i):
    """
    In this program, we will solve for the loops in the diagram shown in the homework using the information given
    and returns the KVL equations as arguments within a tuple.
    :param i: this is the tuple containing the args for the 3 different currents
    :return: loops with missing current values into KVL equations
    """
    # First, we assign the appropriate values to our variables
    B1 = 16  # Volts
    B2 = 32  # Volts
    R1 = 2  # ohms
    R2 = R1 # ohms
    R3 = 1  # ohms
    R4 = 4  # ohms
    # Resistors 1 and 2 are in series: Rt = R1 + R2
    R12 = R1 + R2
    # Loops 1 & 2 are my KVL equations for this problem
    loop1 = R12*i[0] + R3*i[2] - B1
    loop2 = R4*i[1] + R3*i[2] - B2
    # KCL: Iin = Iout
    loop3 = -i[0] - i[1] + i[2]
    # Return the above KVLs/KCL as arguments
    return [loop1, loop2, loop3]

def main():
    """
    This program takes the equations of the loops from the loop function above and uses fsolve to solve for the
    currents through each one: I1, I2, and I3.
    :return:
    """
    # Uses fsolve to solve the 3 loops and give the results into the tuple "i"
    i = fsolve(loop, [1, 1, 1])
    # Print clear statements for each current solution within "i"
    print("The currents within the system were determined as follows:")
    print("I1 = {:0.2f} Amps".format(i[0]))
    print("I2 = {:0.2f} Amps".format(i[1]))
    print("I3 = {:0.2f} Amps".format(i[2]))

if __name__ == "__main__":
    main()