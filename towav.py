

import os
from pydub import AudioSegment

input = "C:/Users/Work/Desktop/SALAMIAUDIO/"
output = "C:\\Users\\Work\\Desktop\\salamiwav"
inlist = os.listdir(input)
print(len(inlist))
print(inlist)


for file in inlist:
    print(file)
    pathin = input+'/'+file
    pathout = output + '/' + file.split(".")[0] + '.wav'
    # convert wav to mp3
    if os.path.exists(pathout):
        print(pathout + ': not twice')
        continue
    else:
        print(pathout + ': success')
        sound = AudioSegment.from_mp3(pathin)
        sound.export(pathout, format="wav")