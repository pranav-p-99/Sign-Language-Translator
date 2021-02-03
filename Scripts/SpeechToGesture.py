def STG():
    import cv2
    import numpy as np
    import speech_recognition as sr

    def prepare_text(text):
        img_array = []
        arr = []
        max_len = 0
        for i in text:
            if i != ' ':
                arr.append(i)
            else:
                img_array.append(arr)
                if len(arr) > max_len:
                    max_len = len(arr)
                arr = []
        if len(arr) > max_len:
            max_len = len(arr)
        img_array.append(arr)

        img_array_new = []
        for i in img_array:
            if len(i) == max_len:
                img_array_new.append(i)
            else:
                temp = i.copy()
                while len(temp) != max_len:
                    temp.append(' ')
                img_array_new.append(temp)

        return img_array_new

    def prepare_image(text, directory):
        img_arr = []
        for i in range(len(text)):
            path = f'{directory}/{text[i][0]}/{text[i][0]}0.jpg'
            img = cv2.imread(path)
            img1 = np.zeros((40, 128, 3), dtype=np.uint8)
            cv2.putText(img1, text[i][0], (50, 30), cv2.FONT_HERSHEY_DUPLEX, 1,
                        (255, 255, 255), 1, cv2.LINE_AA)
            img = np.concatenate((img, img1), axis=0)
            for j in range(len(text[i])):
                if j == 0:
                    continue
                if text[i][j] != ' ':
                    path1 = f'{directory}/{text[i][j]}/{text[i][j]}0.jpg'
                    img1 = cv2.imread(path1)
                    img2 = np.zeros((40, 128, 3), dtype=np.uint8)
                    cv2.putText(img2, text[i][j], (50, 30), cv2.FONT_HERSHEY_DUPLEX, 1,
                                (255, 255, 255), 1, cv2.LINE_AA)
                    img1 = np.concatenate((img1, img2), axis=0)
                    img = np.concatenate((img, img1), axis=1)
                else:
                    img1 = np.zeros((168, 128, 3), dtype=np.uint8)
                    img = np.concatenate((img, img1), axis=1)
            img_arr.append(img)

        final_image = img_arr[0]
        for i in range(1, len(img_arr)):
            final_image = np.concatenate((final_image, img_arr[i]))

        return final_image

    blank = np.zeros((70, 1000), dtype=np.uint8)
    msg = '-------------   SPEAK NOW   -------------'
    cv2.putText(blank, msg, (25, 50), cv2.FONT_HERSHEY_DUPLEX, 1,
                (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('Gestures', blank)
    cv2.waitKey(10)

    directory = '../Data Sample'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('-------------   SPEAK NOW   -------------')
        audio = r.listen(source, timeout=1, phrase_time_limit=10)
        try:
            text = r.recognize_google(audio)
            print(f'SPEECH TO TEXT : {text.upper()}')
            text = r.recognize_google(audio)
        except:
            print('Voice Recognition Failed!')
        try:
            text = text.upper()
            text = list(text)
            text = prepare_text(text)
            image = prepare_image(text, directory)

            cv2.imshow('Gestures', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            print('Text Detection Failed!')
