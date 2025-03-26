#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pytesseract
import cv2


# In[7]:


import cv2
import pytesseract

# Set the path for Tesseract (make sure it is correct)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image
img = cv2.imread('text.png')

# Convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Apply median blur (to reduce noise)
img = cv2.medianBlur(img, 5)

# Extract text using Tesseract OCR
text = pytesseract.image_to_string(img)

print("Extracted Text:")
print(text)


# In[8]:


import cv2
import pytesseract

# Set the path for Tesseract (make sure it is correct)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image
img = cv2.imread('image.jpg')

# Convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Apply median blur (to reduce noise)
img = cv2.medianBlur(img, 5)

# Extract text using Tesseract OCR
text = pytesseract.image_to_string(img)

print("Extracted Text:")
print(text)


# In[ ]:




