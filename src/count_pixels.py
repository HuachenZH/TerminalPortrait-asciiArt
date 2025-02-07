import cv2

# Load the image from a file
image = cv2.imread('../data/qingban.png')

if not image:
    print("Image not found")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarize the image using Otsu's method for automatic thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_LUT)

    # Remove small white regions (using erosion to remove noise)
    kernel = np.ones((3,3), dtype='uint8')
    eroded = cv2.erode(thresh, kernel, iterations=1)

    # Count the number of black and white pixels
    black_pixels = cv2.countNonZero(eroded) if np.isin(255, eroded).any() else 0
    white_pixels = eroded.sum() if not np.isin(0, eroded).any() else 0

    print("Black Pixels:", black_pixels)
    print("White Pixels:", white_pixels)
