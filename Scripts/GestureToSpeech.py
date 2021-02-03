def GTS():
    import cv2
    import tensorflow as tf
    import numpy as np
    import pyttsx3

    temp = ''

    def prepare_data(filepath):
        IMG_SIZE = 64
        new_array = cv2.resize(filepath, (IMG_SIZE, IMG_SIZE))
        new_array = new_array / 255.
        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    json_file = open('../Model/Model.json', "r")
    model_json = json_file.read()
    json_file.close()
    model = tf.keras.models.model_from_json(model_json)
    model.load_weights('../Model/Model.h5')
    print("Model Loaded From Disk!")

    CLASSES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
               'L', 'M', 'N', 'Nothing', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot Open Webcam!")

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        x1 = int(0.5*frame.shape[1])
        y1 = 10
        x2 = frame.shape[1]-10
        y2 = int(0.5*frame.shape[1])
        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (0, 0, 0), 2)
        roi = frame[y1:y2, x1:x2]

        roi = cv2.resize(roi, (128, 128))
        kernel = np.ones((3, 3), np.uint8)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        mask = cv2.dilate(mask, kernel, iterations=3)
        mask = cv2.GaussianBlur(mask, (5, 5), 255)
        roi = cv2.Canny(roi, 100, 100)

        prediction = model.predict([prepare_data(roi)])
        final = (CLASSES[int(np.argmax(prediction[0]))])
        if final == 'Nothing':
            final = ' '
        font = cv2.FONT_HERSHEY_DUPLEX
        blank = np.zeros((128, 128))
        alphabet = np.zeros((128, 128))
        sentence = np.zeros((64, 640))
        cv2.putText(alphabet, final, (32, 90), font, 3,
                    (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(sentence, temp, (40, 40), font,
                    1, (255, 255, 255), 2, cv2.LINE_AA)

        display = np.concatenate(
            (roi, blank, blank, blank, alphabet), axis=1)
        display = np.concatenate((display, sentence), axis=0)

        c = cv2.waitKey(1)
        if c == 27:
            break
        if c == 32:
            temp += final
        if c == 8:
            temp = temp[:-1]
        if c == 13:
            engine = pyttsx3.init()
            engine.say(temp)
            engine.runAndWait()
            engine.setProperty('rate', 80)
            engine.stop()
            print(f' GESTURE TO TEXT : {temp}')
            temp = ''

        cv2.imshow('Frame', frame)
        cv2.imshow('Output', display)

    cap.release()
    cv2.destroyAllWindows()

    print(temp)
