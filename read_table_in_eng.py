__author__="Durgesh kumar,MNNIT ALLAHABAD"
__copyright__="not obtained till now(11/04/2020)"
import androidhelper

droid = androidhelper.Android()
i=1

j=int(droid.dialogGetInput('to read english tables', 'Enter the starting value').result)

maximum=int(droid.dialogGetInput('reading tables', 'Enter the maximum value').result)
while j<=maximum:
    table = str(j)+' '+str(i)+' za '+str(i*j)
    droid.ttsSpeak(table)
    if i==10:
        j+=1
        i=1
    else:
        i+=1