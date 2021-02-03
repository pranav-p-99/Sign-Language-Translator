import os

while True:
    print('\n\n'+'-'*117 + '\n')
    print('*'*50 + '  W E L C O M E  ' + '*'*50)
    print('\n'+'-'*117 + '\n\n')

    print('.'*24+'\n')
    print('        M E N U        ')
    print('\n'+'.'*24+'\n')

    print('GTS -> Gesture To Speech')
    print('STG -> Speech To Gesture')

    option = input('Enter Option : ')

    option = option.upper()

    if option == 'GTS':
        print('\n'+'* '*21 + '  G E S T U R E  T O  S P E E C H  ' + ' *'*21+'\n\n')
        os.system('python GestureToSpeech.py')
    elif option == 'STG':
        print('\n'+'* '*21 + '   S P E E C H  T O  S P E E C H   ' + ' *'*21+'\n\n')
        os.system('python SpeechToGesture.py')
    else:
        print('\n'+'x '*21 + '   I N V A L I D   O P T I O N   ' + ' x'*21+'\n')

    cont = input('Do You Want To Continue? (YES/NO): ')
    cont = cont.upper()
    if cont == 'NO':
        print('\n'+'X-X-'*10 +
              '  A P P L I C A T I O N   C L O S E D  ' + '-X-X'*10+'\n')
        break
