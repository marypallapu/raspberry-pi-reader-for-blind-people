'''
Raspberry Pi Based Reader for Blind People
------------------------------------------

Main application script that:
- Captures a document image using the camera
- Preprocesses the image for better OCR accuracy
- Extracts text using Tesseract OCR
- Converts text to speech using pyttsx3
- Saves images and extracted text to disk
"""

# ==========================================================
# Imports
# ==========================================================

import cv2
import pytesseract
import pyttsx3
import os
import time
from datetime import datetime

# ==========================================================
# Configuration
# ==========================================================

# Tesseract OCR path (adjust if needed on your system)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Image storage directory
IMAGES_DIR = "images"

# ==========================================================
# Initialize System Components
# ==========================================================

def initialize_system():
    """Initialize TTS, camera, and required directories."""

    print("==> Starting Raspberry Pi Based Reader System")

    print("\n==> Initializing Hardware")

    # Initialize Text-to-Speech Engine
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    print("[OK] Text-to-Speech Engine initialized")

    # Initialize Camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("[ERROR] Camera module not detected.")
        raise RuntimeError("Camera initialization failed")

    print("[OK] Raspberry Pi Camera initialized")

    # OCR Engine info (Tesseract)
    print("[OK] OCR Engine initialized")

    print("\nSystem initialization completed successfully.")

    # Create images folder
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)

    print("[OK] Image storage directory verified")

    return engine, camera


# ==========================================================
# Capture and Preprocess Image
# ==========================================================

def capture_and_preprocess_image(camera):
    """Capture an image from the camera and preprocess it for OCR."""

    # Capture Document Image
    print("\n==> Capturing Document Image")

    time.sleep(2)  # Allow camera to adjust

    ret, frame = camera.read()

    if not ret:
        print("[ERROR] Failed to capture image.")
        raise RuntimeError("Image capture failed")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    image_path = os.path.join(
        IMAGES_DIR,
        f"document_{timestamp}.jpg"
    )

    cv2.imwrite(image_path, frame)

    print("[OK] Image captured successfully")
    print(f"[INFO] Image saved as: {image_path}")

    # Load Captured Image
    print("\n==> Loading Captured Image")

    image = cv2.imread(image_path)

    if image is None:
        print("[ERROR] Unable to load captured image.")
        raise RuntimeError("Unable to load captured image")

    print("[OK] Image loaded successfully")

    # Image Preprocessing
    print("\n==> Processing Image")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    processed = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    processed_path = os.path.join(
        IMAGES_DIR,
        f"processed_{timestamp}.jpg"
    )

    cv2.imwrite(processed_path, processed)

    print("[OK] Image preprocessing completed")
    print(f"[INFO] Processed image saved as: {processed_path}")

    return processed, timestamp


# ==========================================================
# Perform OCR
# ==========================================================

def perform_ocr(processed_image):
    """Run OCR on the preprocessed image and return cleaned text."""

    print("\n==> Performing Optical Character Recognition (OCR)")

    try:
        extracted_text = pytesseract.image_to_string(
            processed_image,
            lang="eng"
        )
    except Exception as error:
        print("[ERROR] OCR processing failed.")
        print(error)
        raise RuntimeError("OCR processing failed") from error

    # Clean Extracted Text
    extracted_text = extracted_text.strip()

    print("[OK] OCR completed successfully")

    # Verify OCR Result
    if extracted_text == "":
        print("[WARNING] No readable text detected.")
        extracted_text = (
            "No readable text was found in the captured document."
        )
    else:
        print("[OK] Readable text detected.")

    return extracted_text


# ==========================================================
# Save and Speak Text
# ==========================================================

def save_and_speak_text(engine, text, timestamp):
    """Save extracted text to file and speak it using TTS."""

    # Display Extracted Text
    print("\nDetected Text")
    print("----------------------------------------")
    print(text)
    print("----------------------------------------")

    # Save Extracted Text
    text_file = os.path.join(
        IMAGES_DIR,
        f"text_{timestamp}.txt"
    )

    with open(text_file, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"[INFO] Text saved as: {text_file}")

    # Speak Text
    print("\n==> Speaking Extracted Text")
    engine.say(text)
    engine.runAndWait()
    print("[OK] Text-to-Speech completed")


# ==========================================================
# Main Application
# ==========================================================

def main():
    """Main entry point for the Raspberry Pi blind reader."""

    engine, camera = initialize_system()

    try:
        processed_image, timestamp = capture_and_preprocess_image(camera)

        extracted_text = perform_ocr(processed_image)

        save_and_speak_text(engine, extracted_text, timestamp)

    except Exception as e:
        print(f"\n[FATAL] Application terminated due to error: {e}")

    finally:
        camera.release()
        print("\n==> Camera released. Exiting.")


if __name__ == "__main__":
    main()
