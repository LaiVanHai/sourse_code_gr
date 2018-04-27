import os
for file in os.listdir("./wav"):
  os.system("./sfbcep.exe -F PCM16 -f 16000 -p 19 -e -D -A \"./wav/"+file+"\" \"./prm/"+file.split(".") [0]+".prm\"");