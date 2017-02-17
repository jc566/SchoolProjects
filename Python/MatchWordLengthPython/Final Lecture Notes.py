

def wordCount(infile, outfile, wordLength):
    inf = open(infile, 'r')
    outf = open(outfile, 'w')

    content = inf.readlines()

    inf.close()
    
    for word in content:
        WORDS = word.split()
        list = []
        for finalWord in WORDS:
            if (len(finalWord) <= wordLength):
                list.append(finalWord)
                listLen = len(list)
                

        outf.write(str(listLen) + '\n')
    outf.close()


wordCount('examQuestion.txt','thisisoutput.txt', 4)
