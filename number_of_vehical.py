import easyocr
import re


def vehical_no(image_path):
    # Path to the image containing the vehicle number plate
    # image_path = 'plates/scaned_img.jpg'

    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    results = reader.readtext(image_path)

    # Check if any text was detected at all
    if not results:
        print("No text detected in the image.")
    else:
        # Regular expression to match license plate format for partial segments
        plate_segment_pattern = r"[A-Z0-9\s]+"

        # Collect potential license plate segments
        plate_segments = []
        for (bbox, text, confidence) in results:
            # Clean up detected text
            text = text.strip().upper()
            
            # Check if text resembles a license plate segment
            if re.match(plate_segment_pattern, text):
                plate_segments.append(text)

        # If we have segments, concatenate and print as a single license plate
        if plate_segments:
            full_plate = ' '.join(plate_segments)
            return full_plate
            # print(f"Detected Vehicle Number: {full_plate}")
        else:
            return -1
            # print("No license plate-like text detected.")


