import os

import cv2
cap = cv2.VideoCapture(0)


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100


for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR,str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    done = False
    while not done:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        if not ret:
            print("ERROR: Failed to capture frame")
            break

        print(frame.shape)
        cv2.imshow('frame',frame)
        key = cv2.waitKey(25)
        if key == ord('q'):
            done = True
        
        
        

        
        
    counter = 0
    while counter < dataset_size :
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(25)==ord('q'):
           break
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
