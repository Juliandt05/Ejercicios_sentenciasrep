import os
import time
for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            os.system("clear")
            print(f'{horas,"h"}:{minutos,"m"}:{segundos,"seg"}')
            time.sleep(1)