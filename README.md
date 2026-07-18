# Raspberry-pi-reader-for-blind-people
A Raspberry Pi-based assistive system that reads printed text aloud for visually impaired people using OCR and Text-to-Speech
# What's New in v2.0
--**Advanced OCR Engine**-The OCR pipeline has been enhanced with improved image preprocessing techniques to deliver more accurate text recognition under different lighting conditions and document types.

--**Voice-Guided Navigation **— Introduces voice-assisted interaction that provides audible prompts, enabling visually impaired users to operate the system more independently.

--**Optimized Processing Pipeline**— Refines the internal workflow to improve processing speed, reduce latency, and provide a smoother user experience on the Raspberry Pi.

--**Improved System Reliability** — Introduces additional error handling and system validation mechanisms to ensure stable and consistent application performance.
# Files
- **main.py** — The primary application that coordinates image capture, Optical Character Recognition (OCR), and Text-to-Speech (TTS) processing on the Raspberry Pi platform.

- **camera.py** — Handles camera initialization and image acquisition, providing high-quality input images for the OCR pipeline.

- **ocr.py** — Implements the Optical Character Recognition (OCR) module responsible for extracting readable text from captured images.

- **tts.py** — Converts the recognized text into natural speech using the integrated Text-to-Speech engine.
# Usage
Main application to run 

```bash
# Navigate to the repository folder
cd raspberry-pi-reader

# Run the main application
python3 main.py
NOTE:
The system requires a configured Raspberry Pi environment with all necessary libraries and hardware connections before execution.
```

Replace ```main.py``` with the actual Python file name used in the project. For example, if the file name is ```reader.py``` or ```blind_reader.py```, use that file name while running the application.
# Terminal output 
```user@raspberrypi:~/raspberry-pi-reader$ python3 main.py

==> Initializing Raspberry Pi Reader System

==> Loading required modules...
[OK] OpenCV loaded
[OK] OCR engine initialized
[OK] Text-to-Speech module ready

==> Initializing camera...
[OK] Camera connected successfully

==> System Ready
Place the document in front of the camera...

[INFO] Capturing image...
[INFO] Processing image...
[INFO] Extracting text using OCR...

Detected Text:
"Welcome to Raspberry Pi Reader"

[INFO] Converting text to speech...
[INFO] Audio output started

*** PROCESS COMPLETED SUCCESSFULLY ***

