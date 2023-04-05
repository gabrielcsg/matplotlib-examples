data = open('data/bacteria.fasta').read()
output = open('tmp/bacteria.html', 'w')

# data = open('data/human.fasta').read()
# output = open('tmp/human.html', 'w')

cont = {}
values = ['A', 'T', 'C', 'G']

for i in values:
    for j in values:
        cont[i+j] = 0

data = data.replace('\n', '')

for k in range(len(data)-1):
    cont[data[k] + data[k+1]] += 1

i = 1
for k in cont:
    opacity = cont[k]/max(cont.values())
    output.write(
        '<div style="width:100px; border:1px solid #111; height: 100px; float: left; background-color: rgba(0, 0, 0, ' + str(opacity) + '); color: #FFF;">' + k + '</div>')

    if i % 4 == 0:
        output.write('<div style="clear: both;"></div>')

    i += 1


output.close()
