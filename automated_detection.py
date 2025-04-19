import cv2
import number_of_vehical as nov
import os


def plate_detection():
    # Load the pre-trained Haar Cascade model for plate detection
    harcascade = "model/haarcascade_russian_plate_number.xml"

    cap = cv2.VideoCapture(0)

    cap.set(3, 640)  # width
    cap.set(4, 480)  # height

    min_area = 500  # Minimum area to consider for a valid plate
    count = 0  # Counter for saved plates

    while True:
        success, img = cap.read()

        # Load the Haar Cascade for plate detection
        plate_cascade = cv2.CascadeClassifier(harcascade)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect plates in the image
        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        for (x, y, w, h) in plates:
            area = w * h

            if area > min_area:
                # Draw a rectangle around the detected plate
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                # Crop the region of interest (ROI)
                img_roi = img[y: y + h, x: x + w]
                
                # Save the image automatically
                filename = f"plates/scaned_img.jpg"
                cv2.imwrite(filename, img_roi)
                print(f"Plate Saved: {filename}")

                # Display a message indicating the plate is saved
                cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
                cv2.imshow("Results", img)
                cv2.waitKey(500)  # Display the "Plate Saved" message for 500 ms
                count += 1

        # Display the result
        cv2.imshow("Result", img)

        image_path = 'plates/scaned_img.jpg'

        if(os.path.exists(image_path)):

            number = nov.vehical_no(image_path)
            if number != -1:
                print("Detected Vehicle Number:",number)
            else:
                print("No license plate-like text detected.")

            os.remove(image_path)
            break

        # Exit the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
