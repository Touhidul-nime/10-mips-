opcode ={
    "add": "0000",
    "sub": "0001",
    "mul": "0010",
    "div": "0011",
    "and": "0100",
    "or": "0101",
    "not": "0110",
    "addi": "0111",
    "sw": "1000"
}

tregister ={
    "$zero": "00",
    "$t1": "01"
}

sregister ={
    "$s1": "10",
    "$s2": "11"
}

filename = "input.txt"
with open(filename) as file:
    lines = file.readlines()

output=""
for line in lines:
    words= line.split()
    for word in words:
        word=word.strip(',')
        if word in opcode:
            output = opcode[word]
        elif word in tregister:
            output = tregister[word]+" "+output 
        elif word in sregister:
            output = sregister[word]+" "+output 
        else:           
            if "($zero)" in word:
                word = word.strip('($zero)')
            if "($t1)" in word:
                word = word.strip('($t1)')
                output = "01 "+output 
            if "($s1)" in word:
                word = word.strip('($s1)')
                output = "10 "+output 
            if "($s2)" in word:
                word = word.strip('($s2)')
                output = "11 "+output /home/mohit/Downloads/aupu/project.zip
            
            output = str(format(int(word), '02b'))+" "+output 
            


    print(line)  
    print(output)
    print(" ")
    print(" ")
