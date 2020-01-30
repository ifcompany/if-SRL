from os import system
system('clear')
logp = '''
      \033[0;94m|\033[0;93m	@@@   \033[0;94m|
      \033[0;94m|\033[0;93m	@     \033[0;94m|
      \033[0;94m|\033[0;93m	@@@   \033[0;94m|     |\033[0;93m @@@   \033[0;94m|
      \033[0;94m|\033[0;93m	@     \033[0;94m|\033[0;91m ==\033[0;92m> \033[0;94m|\033[0;93m @@@@  \033[0;94m|
      \033[0;94m|\033[0;93m	@@@@  \033[0;94m|     |\033[0;93m @@@@@ \033[0;94m|
      \033[0;94m|\033[0;93m	@@@@@ \033[0;94m|
      \033[0;94m|\033[0;93m	@@@   \033[0;94m|

    \033[0;95m { \033[0;92mif S R L             \033[0;33mV \033[0;95m}
    \033[0;95m { \033[4;34mwww\033[4;33m.\033[4;34mifcompany\033[4;33m.\033[4;34mir\033[0;33m     2 \033[0;95m}
    \033[0;95m { \033[4;34mgithub\033[4;33m.\033[4;34mcom\033[4;33m/\033[4;34mifcompany\033[0;33m 0 \033[0;95m}
    \033[0;95m { \033[4;34mT\033[4;33m.\033[4;34mme\033[4;33m/\033[4;34mThe\033[4;32mlink\033[4;33mif\033[0;33m       0 \033[0;95m}
    \033[0;95m [ \033[4;33mProgrammer\033[0;36m : \033[0;101m007\033[0;33m       \033[0;95m]\033[0m
'''
print(logp)
length = 0
wordlist = input(" \033[0;32m$ \033[0;36mEnter The Wordlist \033[0;34m\> \033[0;37m")
goodlist = input(" \033[0;32m$ \033[0;36mEnter The Name for Good list \033[0;34m\> \033[0;37m")
length = int(input(" \033[0;32m$ \033[0;36mEnter The Number for length [Default = 0]\033[0;34m\> \033[0;37m"))
ifsetlis = input(" \033[0;32m$ \033[0;36mDo You want Duplicate Member List Removed ? [Y/n]\033[0;34m\> \033[0;37m")

f = open(wordlist+'.txt', "r").read().splitlines()
g = open(goodlist+'.txt', "a")

if (ifsetlis == 'n'):
    print('\033[0;32m[\033[0;33m#\033[0;32m] \033[0;35mPlease Wait ...\033[0m')
    for q in f:
        if (len(q) >= length):
            g.write(q+'\n')
        else:
            pass
    print(' \033[0;31mThe End , Your file \033[0;32m'+goodlist+'.txt\033[0m')
    g.close()
elif (ifsetlis == 'N'):
    print('\033[0;32m[\033[0;33m#\033[0;32m] \033[0;35mPlease Wait ...\033[0m')
    for q in f:
        if (len(q) >= length):
            g.write(q+'\n')
        else:
            pass
    print(' \033[0;31mThe End , Your file \033[0;32m'+goodlist+'.txt\033[0m')
    g.close()
elif (ifsetlis == 'y'):
    setlist = set()
    print('\033[0;32m[\033[0;33m#\033[0;32m] \033[0;35mPlease Wait ...\033[0m')
    for s in f:
        if (len(s) >= length):
            setlist.add(s)
        else:
            pass
    for p in setlist:
        g.write(p+'\n')
    print(' \033[0;31mThe End , Your file \033[0;32m'+goodlist+'.txt\033[0m')
elif (ifsetlis == 'Y'):
    setlist = set()
    print('\033[0;32m[\033[0;33m#\033[0;32m] \033[0;35mPlease Wait ...\033[0m')
    for s in f:
        if (len(s) >= length):
            setlist.add(s)
        else:
            pass
    for p in setlist:
        g.write(p+'\n')
    print(' \033[0;31mThe End , Your file \033[0;32m'+goodlist+'.txt\033[0m')
else:
    print(' Please enter Y/y or n/N')
