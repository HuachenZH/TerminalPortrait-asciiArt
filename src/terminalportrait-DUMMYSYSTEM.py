import numpy as np
from PIL import Image, ImageEnhance
import argparse
from pathlib import Path



INK_PALETTE = {
    "14": "@MN§$%¤eo+;:,.",
    "13": "@MN§$%¤o+;:,.",
    "12": "@MN$%¤o+;:,.",
    "11": "@M$%¤o+;:,.",
    "10": "@M$%¤o+:,.",
    "9": "@M$%o+:,.",
    "8": "@M$%o:,.",
    "7": "@$%o:,.",
    "6": "@$o:,.",
    "5": "@$o:.",
    "4": "@o:.",
    "3": "@o:",
    "special": "冉伊诺陈"
}


def parse_arguments():
    """Parse and validate command line arguments."""
    parser = argparse.ArgumentParser(description='Convert images to ASCII art')
    parser.add_argument('-i', '--input', required=True, help='Input image file path')
    parser.add_argument('-o', '--output', required=True, help='Output text file path')
    parser.add_argument('-l', '--levels', required=True, choices=INK_PALETTE.keys(),
                       help='Number of grayscale levels (3-14)')
    parser.add_argument('-d', '--density', type=int, required=True,
                       help='Character density (repetition count)')
    parser.add_argument('-c', '--contrast', type=float, default=1.0,
                       help='Contrast adjustment factor (default: 1.0)')
    return parser.parse_args()



def is_grayscale(arr: np.ndarray) -> bool:
    """Check if RGB array is grayscale by comparing color channels."""
    if arr.ndim == 2:
        return True
    return np.allclose(arr[:, :, 0], arr[:, :, 1]) and np.allclose(arr[:, :, 1], arr[:, :, 2])



def resize_image(img: Image.Image, max_width: int = 100) -> Image.Image:
    """Resize image while maintaining aspect ratio.
    
    Args:
        img: Input PIL Image
        max_width: Maximum width for the output image
        
    Returns:
        Resized PIL Image
    """
    width, height = img.size
    if width > max_width:
        ratio = max_width / width
        new_height = int(height * ratio)
        return img.resize((max_width, new_height), Image.LANCZOS)
    return img



def color_to_grayscale(color_array: np.ndarray) -> np.ndarray:
    """Convert RGB array to grayscale using standard weights."""
    return np.dot(color_array[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)



def get_grayscale_matrix(arr: np.ndarray) -> np.ndarray:
    """Convert input array to grayscale, handling various input formats."""
    if arr.ndim == 2:
        print("[*] Input image is already grayscale (2D)")
        return arr
    
    if arr.ndim != 3:
        raise ValueError(f"Invalid array shape: {arr.shape}. Expected 2D or 3D array.")
    
    if is_grayscale(arr):
        print("[*] Input image is grayscale but has 3 dimensions")
        return arr[:, :, 0]
    
    print("[*] Converting color image to grayscale")
    return color_to_grayscale(arr)



def rescale_matrix(arr: np.ndarray, levels: int) -> np.ndarray:
    """Rescale grayscale values to specified number of levels."""
    #return (arr * (levels - 1) / 255).astype(np.uint8)
    return arr//(255//levels+1)



def create_ascii_art(arr: np.ndarray, ink: str, density: int) -> str:
    """Generate ASCII art from grayscale matrix."""
    char_map = {i: char for i, char in enumerate(ink)}
    return "\n".join(
        "".join(char_map[pixel] * density for pixel in row)
        for row in arr
    )



def adjust_contrast(img: Image.Image, factor: float) -> Image.Image:
    """Adjust image contrast using enhancement factor."""
    return ImageEnhance.Contrast(img).enhance(factor)



def main():
    args = parse_arguments()
    
    try:
        # Load and process image
        img = Image.open(args.input)
        print(f"input size is {str(img.size)}")
        img = resize_image(img, 200)
        breakpoint()
        if args.contrast != 1.0:
            img = adjust_contrast(img, args.contrast)
            
        # Convert to grayscale matrix
        arr = np.array(img)
        print(f"[*] Input shape: {arr.shape}")
        grayscale_arr = get_grayscale_matrix(arr)
        
        # Prepare ASCII conversion
        ink = INK_PALETTE[args.levels]
        rescaled_arr = rescale_matrix(grayscale_arr, len(ink))
        
        # Generate and save ASCII art
        print("[*] Generating ASCII art...")
        ascii_art = create_ascii_art(rescaled_arr, ink, args.density)
        
        output_path = Path(args.output)
        output_path.write_text(ascii_art)
        print(f"[*] Successfully saved to {output_path}")
        
    except Exception as e:
        print(f"[!] Error: {str(e)}")
        raise



if __name__ == "__main__":
    main()

# python3 terminalportrait-DUMMYSYSTEM.py -i ../data/marriage_540_x_382.jpg -o ../out/marriage_540_x_382.txt -l special -d 1 -c 1.2
