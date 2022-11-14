import os
import time
for hora in range(24):
    for minutos in range(60):
        for segundos in range(60):
            os.system('cls')
            print(f'{hora,"h"}:{minutos,"min"}:{segundos,"seg"}')