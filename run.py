# !/usr/bin/env python3
import os
import time
from termcolor import colored


import long_nozzle as example


def main():
    try:
        geometry = example.geometry

    except:
        geometry = None

    mesh = example.get_mesh()

    mesh.write(output_path=os.path.join('case', 'system', 'blockMeshDict'), geometry=geometry)
    os.system("case/Allrun.mesh")


if __name__ == '__main__':
    s_time = time.time()
    main()
    e_time = time.time()
    print(colored(f"Code run {round((e_time - s_time), 3)}s", 'magenta', attrs=["bold"]))
