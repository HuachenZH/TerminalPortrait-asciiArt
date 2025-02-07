import cv2
import numpy as np


def calculate_black_percentage(image_path):
    try:
        arr_image = cv2.imread(image_path)
        if arr_image is None:
            raise FileNotFoundError(f"Image not found or unable to load: {image_path}")

        arr_gray = cv2.cvtColor(arr_image, cv2.COLOR_BGR2GRAY)
        white_pixels = cv2.countNonZero(arr_gray)
        black_pixels = arr_gray.size - white_pixels
        return black_pixels / arr_gray.size

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None



def main():
    # List of image file paths
    image_files = ["../data/chen.jpg",
"../data/chen_t.jpg",
"../data/nnuo.jpg",
"../data/nnuo_t.jpg",
"../data/ran.jpg",
"../data/yi.jpg"]

    # Calculate black percentages for all images
    results = []
    for image_path in image_files:
        percentage = calculate_black_percentage(image_path)
        if percentage is not None:
            results.append((image_path, percentage))

    # Sort by black percentage in descending order
    results.sort(key=lambda x: x[1], reverse=True)

    # Print sorted results
    print("Images sorted by black percentage (descending):")
    for image_path, percentage in results:
        print(f"{image_path}: {percentage:.2%}")


if __name__ == "__main__":
    main()

# ../data/nnuo_t.jpg: 6.20%
# ../data/ran.jpg: 6.06%
# ../data/chen_t.jpg: 5.52%
# ../data/yi.jpg: 5.26%
# ../data/nnuo.jpg: 4.56%
# ../data/chen.jpg: 3.73%

