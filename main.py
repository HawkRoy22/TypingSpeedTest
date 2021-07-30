import time



def randomParagraphGen():
    x = '''Rain drops the size of bullets thundered on the castle windows for days on end; the lake rose, 
    the flower beds turned into muddy streams, and Hagrid's pumpkins swelled to the size of garden sheds. 
    Oliver Wood's enthusiasm for regular training sessions, however, was not dampened, which was why Harry was to be found, 
    late one stormy Saturday afternoon a few days before Halloween, returning to Gryffindor Tower, drenched to the skin and splattered with mud.'''

    print(x)



def calculateWPM(start, end):
    Gross_WPM = (1000/5)/((end/60)-(start/60))
    print("Your Typing Speed: " + str(Gross_WPM))


def play():
    randomParagraphGen()
    start = time.time()
    input("Start Typing Now! \n")
    end = time.time()
    calculateWPM(start, end)


play()