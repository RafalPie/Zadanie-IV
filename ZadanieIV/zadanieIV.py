import os
from numpy import sqrt
import random
import matplotlib.pyplot as plt
  
nazwa_pierwszego_pliku = input('prosze wpisac sciezke do pierwszego pliku: ')
nazwa_drugiego_pliku =  input('prosze wpisac sciezke do drugiego pliku: ')
rozmiar_pierwszego_pliku=os.path.getsize(nazwa_pierwszego_pliku)
rozmiar_drugiego_pliku=os.path.getsize(nazwa_drugiego_pliku)
print(str(rozmiar_pierwszego_pliku)+ 'to jest drugi plik :' + str(rozmiar_drugiego_pliku))
snrindB_range = range(0, 10)
