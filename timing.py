import time
import sys

############################################################
ChapterAtom='    <ChapterAtom>\n'
ChapterAtom2='    </ChapterAtom>\n'
ChapterTimeStart='      <ChapterTimeStart>'
ChapterTimeStart2='</ChapterTimeStart>'
ChapterTimeEnd='      <ChapterTimeEnd>'
ChapterTimeEnd2='</ChapterTimeEnd>'
ChapterDisplay='      <ChapterDisplay>'
ChapterDisplay2='      </ChapterDisplay>\n'
ChapterString='        <ChapterString>'
ChapterString2='</ChapterString>'
ChapterLanguage='        <ChapterLanguage>eng</ChapterLanguage>'
ChapterFlagHidden='      <ChapterFlagHidden>0</ChapterFlagHidden>\n'
ChapterFlagEnabled='      <ChapterFlagEnabled>1</ChapterFlagEnabled>\n'
ChapterUID='      <ChapterUID>'
ChapterUID2='</ChapterUID>\n'
##############################################################################

file = sys.argv[1]
app = sys.argv[2]
i = sys.argv[3]
ctr=1
app2= app + " timing.txt"
app=app+".xml"
r = open(file,'r')
f = open(app,'w')
f2 = open(app2,'w')

# start
f.write('<?xml version="1.0"?>\n<!-- <!DOCTYPE Chapters SYSTEM "matroskachapters.dtd"> -->\n<Chapters>\n    <EditionEntry>\n    <EditionFlagDefault>1</EditionFlagDefault>\n    <EditionFlagHidden>0</EditionFlagHidden>\n    <EditionUID>123</EditionUID>\n')
#loop
startTime="00:00:00" #This is for the first time only
#i= raw_input('Enter the number of chapters: ')
while ctr<=int(i):
    f.write(ChapterAtom)
    #Start time
    #timeStemp = raw_input('Enter the start time of this chapter HHMMSS ')
    #timeStemp = timeStemp[0:2] + ':' + timeStemp[2:4] + ':' + timeStemp[4:6]
    #startTime=timeStemp
    arr = r.readline().split("-")
    timeStemp = ChapterTimeStart+startTime + '.000000000'+ChapterTimeStart2+'\n'
    f.write(timeStemp)

    #Chapter name
    name = arr[0]
    chaptname=name

    #End time
    timeStemp = arr[1]
    timeStemp = timeStemp[1:3] + ':' + timeStemp[3:5] + ':' + timeStemp[5:7]
    startTime=timeStemp
    timeStemp = ChapterTimeEnd+timeStemp + '.000000000'+ChapterTimeEnd2+'\n'
    f.write(timeStemp)
    f.write(ChapterDisplay)

    #write the chapter name
    name = '\n' + ChapterString + name + ChapterString2 + '\n' + ChapterLanguage +'\n'
    f.write(name)
    f.write(ChapterDisplay2)
    f.write(ChapterFlagHidden)
    f.write(ChapterFlagEnabled)

    #Chapter UID
    UID = ChapterUID + str(ctr) +ChapterUID2
    f.write(UID)
    ctr= ctr+1
    f.write(ChapterAtom2)
    #TXT timing file
    temp=str(ctr-1) + "." + chaptname + " - " + startTime + "\n"
    f2.write(temp)

#end
f.write('  </EditionEntry>\n</Chapters>')