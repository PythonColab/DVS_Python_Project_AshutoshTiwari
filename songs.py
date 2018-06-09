# -*- coding: utf-8 -*-
"""
Created on Thu May 24 05:15:59 2018

@author: Ashutosh
"""




from glob import glob


import os
from pygame import mixer


l = glob(os.path.join('E:\\Games\\Eminem\\Recovery\\', '*.mp3'))
print('E:\\Games\\Eminem\\Recovery\\01 Cold Wind Blows.mp3')
l=input("Enter the index of the ")
mixer.init()
mixer.music.load(l[0])
mixer.music.play()
mixer.music.stop()
#for a_file in sorted(files_list):
