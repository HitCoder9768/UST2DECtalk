import os, sys, pyutau

# check for oto in cli args
fn = sys.argv[-1]
if os.path.exists(fn):
    ust = pyutau.UtauPlugin(sys.argv[-1])
else:
    print("ust not specified")
    quit()

decscript = "[:phoneme on]\n["

tempo = float(ust.settings['Tempo'])
barlen = 240000/tempo

for note in ust.get_notes():
    lyric = note.get_lyric()
    num = note.get_note_num()-35
    length = barlen*(note.get_length()/1920)
    decscript = decscript + (lyric+"<"+str(round(length))+","+str(round(num))+">")

decscript = decscript + "]."

outscript = open(os.path.basename(sys.argv[-1]).replace(".ust","_DEC.txt"),"w")
outscript.write(decscript)
outscript.close()