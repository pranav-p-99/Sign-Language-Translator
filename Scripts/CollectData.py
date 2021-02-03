import cv2
import numpy as np
import os


if not os.path.exists("../Data"):
    os.makedirs("../Data")
    os.makedirs("../Data/A")
    os.makedirs("../Data/B")
    os.makedirs("../Data/C")
    os.makedirs("../Data/D")
    os.makedirs("../Data/E")
    os.makedirs("../Data/F")
    os.makedirs("../Data/G")
    os.makedirs("../Data/H")
    os.makedirs("../Data/I")
    os.makedirs("../Data/J")
    os.makedirs("../Data/K")
    os.makedirs("../Data/L")
    os.makedirs("../Data/M")
    os.makedirs("../Data/N")
    os.makedirs("../Data/O")
    os.makedirs("../Data/P")
    os.makedirs("../Data/Q")
    os.makedirs("../Data/R")
    os.makedirs("../Data/S")
    os.makedirs("../Data/T")
    os.makedirs("../Data/U")
    os.makedirs("../Data/V")
    os.makedirs("../Data/W")
    os.makedirs("../Data/X")
    os.makedirs("../Data/Y")
    os.makedirs("../Data/Z")
    os.makedirs("../Data/Nothing")

directory = '../Data/'


def func(x):
    pass


cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    count = {
        'A': len(os.listdir(directory+"/A")),
        'B': len(os.listdir(directory+"/B")),
        'C': len(os.listdir(directory+"/C")),
        'D': len(os.listdir(directory+"/D")),
        'E': len(os.listdir(directory+"/E")),
        'F': len(os.listdir(directory+"/F")),
        'G': len(os.listdir(directory+"/G")),
        'H': len(os.listdir(directory+"/H")),
        'I': len(os.listdir(directory+"/I")),
        'J': len(os.listdir(directory+"/J")),
        'K': len(os.listdir(directory+"/K")),
        'L': len(os.listdir(directory+"/L")),
        'M': len(os.listdir(directory+"/M")),
        'N': len(os.listdir(directory+"/N")),
        'O': len(os.listdir(directory+"/O")),
        'P': len(os.listdir(directory+"/P")),
        'Q': len(os.listdir(directory+"/Q")),
        'R': len(os.listdir(directory+"/R")),
        'S': len(os.listdir(directory+"/S")),
        'T': len(os.listdir(directory+"/T")),
        'U': len(os.listdir(directory+"/U")),
        'V': len(os.listdir(directory+"/V")),
        'W': len(os.listdir(directory+"/W")),
        'X': len(os.listdir(directory+"/X")),
        'Y': len(os.listdir(directory+"/Y")),
        'Z': len(os.listdir(directory+"/Z")),
        'Nothing': len(os.listdir(directory+"/Nothing")),
    }

    cv2.putText(frame, "IMAGE COUNT", (10, 80),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "A : "+str(count['A']), (10, 100),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "B : "+str(count['B']), (10, 120),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "C : "+str(count['C']), (10, 140),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "D : "+str(count['D']), (10, 160),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "E : "+str(count['E']), (10, 180),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "F : "+str(count['F']), (10, 200),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "G : "+str(count['G']), (10, 220),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "H : "+str(count['H']), (10, 240),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "I : "+str(count['I']), (10, 260),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "J : "+str(count['J']), (10, 280),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "K : "+str(count['K']), (10, 300),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "L : "+str(count['L']), (10, 320),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "M : "+str(count['M']), (10, 340),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "N : "+str(count['N']), (100, 100),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "O : "+str(count['O']), (100, 120),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "P : "+str(count['P']), (100, 140),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "Q : "+str(count['Q']), (100, 160),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "R : "+str(count['R']), (100, 180),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "S : "+str(count['S']), (100, 200),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "T : "+str(count['T']), (100, 220),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "U : "+str(count['U']), (100, 240),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "V : "+str(count['V']), (100, 260),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "W : "+str(count['W']), (100, 280),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "X : "+str(count['X']), (100, 300),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "Y : "+str(count['Y']), (100, 320),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "Z : "+str(count['Z']), (100, 340),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(frame, "NOTHING : "+str(count['Nothing']), (30, 360),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

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

    cv2.imshow("Frame", frame)
    cv2.imshow("ROI", roi)

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'Nothing/Nothing' +
                    str(count['Nothing'])+'.jpg', roi)
    if interrupt & 0xFF == ord('A'):
        cv2.imwrite(directory+'A/A'+str(count['A'])+'.jpg', roi)
    if interrupt & 0xFF == ord('B'):
        cv2.imwrite(directory+'B/B'+str(count['B'])+'.jpg', roi)
    if interrupt & 0xFF == ord('C'):
        cv2.imwrite(directory+'C/C'+str(count['C'])+'.jpg', roi)
    if interrupt & 0xFF == ord('D'):
        cv2.imwrite(directory+'D/D'+str(count['D'])+'.jpg', roi)
    if interrupt & 0xFF == ord('E'):
        cv2.imwrite(directory+'E/E'+str(count['E'])+'.jpg', roi)
    if interrupt & 0xFF == ord('F'):
        cv2.imwrite(directory+'F/F'+str(count['F'])+'.jpg', roi)
    if interrupt & 0xFF == ord('G'):
        cv2.imwrite(directory+'G/G'+str(count['G'])+'.jpg', roi)
    if interrupt & 0xFF == ord('H'):
        cv2.imwrite(directory+'H/H'+str(count['H'])+'.jpg', roi)
    if interrupt & 0xFF == ord('I'):
        cv2.imwrite(directory+'I/I'+str(count['I'])+'.jpg', roi)
    if interrupt & 0xFF == ord('J'):
        cv2.imwrite(directory+'J/J'+str(count['J'])+'.jpg', roi)
    if interrupt & 0xFF == ord('K'):
        cv2.imwrite(directory+'K/K'+str(count['K'])+'.jpg', roi)
    if interrupt & 0xFF == ord('L'):
        cv2.imwrite(directory+'L/L'+str(count['L'])+'.jpg', roi)
    if interrupt & 0xFF == ord('M'):
        cv2.imwrite(directory+'M/M'+str(count['M'])+'.jpg', roi)
    if interrupt & 0xFF == ord('N'):
        cv2.imwrite(directory+'N/N'+str(count['N'])+'.jpg', roi)
    if interrupt & 0xFF == ord('O'):
        cv2.imwrite(directory+'O/O'+str(count['O'])+'.jpg', roi)
    if interrupt & 0xFF == ord('P'):
        cv2.imwrite(directory+'P/P'+str(count['P'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Q'):
        cv2.imwrite(directory+'Q/Q'+str(count['Q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('R'):
        cv2.imwrite(directory+'R/R'+str(count['R'])+'.jpg', roi)
    if interrupt & 0xFF == ord('S'):
        cv2.imwrite(directory+'S/S'+str(count['S'])+'.jpg', roi)
    if interrupt & 0xFF == ord('T'):
        cv2.imwrite(directory+'T/T'+str(count['T'])+'.jpg', roi)
    if interrupt & 0xFF == ord('U'):
        cv2.imwrite(directory+'U/U'+str(count['U'])+'.jpg', roi)
    if interrupt & 0xFF == ord('V'):
        cv2.imwrite(directory+'V/V'+str(count['V'])+'.jpg', roi)
    if interrupt & 0xFF == ord('W'):
        cv2.imwrite(directory+'W/W'+str(count['W'])+'.jpg', roi)
    if interrupt & 0xFF == ord('X'):
        cv2.imwrite(directory+'X/X'+str(count['X'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Y'):
        cv2.imwrite(directory+'Y/Y'+str(count['Y'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Z'):
        cv2.imwrite(directory+'Z/Z'+str(count['Z'])+'.jpg', roi)

cap.release()
cv2.destroyAllWindows()
