import re
user = open('.user').readline()
src = open("generatedcode_sample","r").read()
pattern = re.compile("<<<(.*?)>>>", re.DOTALL)

dst = pattern.sub(('00'+user),src)
# print(dst)

f = open("Todotter_ui.py",'a')
f.write(dst)
f.close()
src = open("generatedcode_sample2","r").read()
pattern = re.compile("<<<(.*?)>>>", re.DOTALL)
dst = pattern.sub(('00'+user),src)

src = open("Todotter_ui.py","r").read()
pattern = re.compile("#<<(.*?)>>#", re.DOTALL)
dst2 = pattern.sub(dst,src)

f = open("Todotter_ui.py",'w')
# print(dst2)
f.write(dst2)
# open(".user","w").write((str)(user+1))