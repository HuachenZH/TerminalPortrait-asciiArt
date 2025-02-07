import cv2
import numpy as np

def main():
    try:
        # Load the image from a file
        arr_image = cv2.imread('../data/chen.jpg')
        
        if arr_image is None:
            raise FileNotFoundError("Image not found or unable to load")

        # Convert to grayscale
        arr_gray = cv2.cvtColor(arr_image, cv2.COLOR_BGR2GRAY)

        # Count pixels
        white_pixels = cv2.countNonZero(arr_gray)
        black_pixels = arr_gray.size - white_pixels

        print("Black Pixels:", black_pixels)
        print("White Pixels:", white_pixels)
        print(f"Black Percentage: {black_pixels/arr_gray.size:.2%}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()