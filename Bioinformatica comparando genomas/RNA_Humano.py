inn = open('18s_humano.fasta').read()
out = open('18s_humano.html','w')

com = {}

for x in ['A','T', 'C','G']:
    for  y in ['A','T','C','G']:
        com[x+y] = 0

inn = inn.replace('\n','')
for s in range(len(inn)-1):
    com[inn[s]+inn[s+1]]+=1

#html
out.write("<div>")
i = 1
for n in com:
    transparencia = com[n]/max(com.values())
    out.write("<div style='width:100px; border:1px solid #111; color:#000; height:100px; float:left; background-color:rgba(0,0,0,"+str(transparencia)+"')>"+n+"</div>")

    if i%4 == 0:
        out.write("<div style='clear:both'></div>")
    i+=1

out.close()