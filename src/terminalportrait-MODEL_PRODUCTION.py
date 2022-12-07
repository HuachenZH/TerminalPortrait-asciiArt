import numpy as np
from PIL import Image, ImageEnhance
import argparse

#%% functions
def isGrayscale(arr: np.array) -> bool:
    '''
    Check if the rgb matrix is already grayscale. 

    Parameters
    ----------
    arr : np.array uint8
        The rgb matrix.
        Normally it has three dimensions. This function will check again.

    Returns
    -------
    bool
        Return True if array is grayscale. False if array is colored

    '''
    if len(arr.shape) == 2: # if the rgb matrix contains only two dimensions
        return True # then normally it's already gray scale
    # else, three dimensions
    # check for one given pixel, if r, g, b three values are the same
    
    
    # The matrix has 3 dimensions. Check all pixels through the three pages.
    for irow in range(arr.shape[0]):
        for icol in range(arr.shape[1]):
            if arr[irow][icol][0] == arr[irow][icol][1] and arr[irow][icol][1] == arr[irow][icol][2]:
                pass
            else:
                return False # not grayscale
    return True



def color2grayscale(colorArray: np.array) -> np.array:
    '''
    Transform a colored rgb matrix to grayscale.

    Parameters
    ----------
    colorArray : np.array of uint8
        The colored rgb matrix. 
        Normally it has 3 dimensions: 
        Width and height correspond to the pixel size of image. It has three pages, corresponding to the R,G,B three colors.

    Returns
    -------
    np.array of uint8
        The grayscale matrix, two dimensions.

    '''
    # equation color to grayscale : color to greyscale: x = 0.299r + 0.587g + 0.114b.
    return (colorArray[:,:,0]*0.299 + colorArray[:,:,1]*0.587 + colorArray[:,:,2]*0.114).astype(np.uint8)



def grayMatrix(arr: np.array) -> np.array:
    '''
    Create the grayscale matrix.
    Concretly, there are several cases of the input array arr:
        - arr is two dimensional, then normally it s already grayscale
        - arr is three dimensional:
            - arr is already grayscale, the three pages are the same (this is rare but it exists)
            - arr is not grayscale, it s colored
        All of the cases above wil be treated.

    Parameters
    ----------
    arr : np.array
        The numpy array read from input image.

    Returns
    -------
    arr_gray : np.array
        A numpy array in grayscale, two dimensional.

    '''
    if len(arr.shape) == 2: # if the matrix has two dimensions, then normally it's already grayscale
        arr_gray = arr
        print("[*] The input image is already grayscale. Matrix dimension 2")
    elif len(arr.shape) == 3: # the matrix has three dimensions. It's still possible that it's already grayscale
        if isGrayscale(arr): # is grayscale but the matrix has three dimensions.
            print("[*] The input image is already grayscale. However it has three dimensions... Dimensional strike!")
            arr_gray = arr[:,:,0]
            print("[*] Cleared. Target is now two dimensional.")
        else: # is not grayscale. Transform to grayscale by using the equation
            print("[*] The input image is not grayscale. Transforming to grayscale...")
            # transform to grayscale
            arr_gray = color2grayscale(arr)
            print("[*] Done")
    else: # the matrix has one or more than three dimensions. Then raise an error
        print("[!] Matrix dimension incorrect, it's shape of %s" % str(arr.shape))
        raise ValueError("Matrix dimension incorrect. Error with input image. Matrix shape is %s.")
    return arr_gray



def rescaleMatrix(arr_gray: np.array, levels: int) -> np.array:
    '''
    Rescale the grayscale matrix.
    The new values will be 0, 1, 2 ... n 
    with n: number of levels minus 1 

    Parameters
    ----------
    arr_gray : np.array
        The grayscale matrix.
    levels : int
        How many levels are there. Equals to the length of our ink.

    Returns
    -------
    np.array
        The rescaled matrix.

    '''
    # 255//levels+1 might be hard for understanding. 
    # It can also be written as arr_gray//math.ceil(255/levels)
    # The value of arr_rescale varies from 0 to levels-1
    return arr_gray//(255//levels+1) 



def painting(arr_rescale: np.array, ink: str, inkDensity:int) -> str:
    '''
    Construct the output string.

    Parameters
    ----------
    arr_rescale : np.array
        The rescaled matrix.
    ink : str
        Which characters will we use.
        For example, we can use @ or M for the densest pixels, use - or . for the thinnest pixels.
    inkDensity : int
        Each character will repeat how many times.

    Returns
    -------
    str
        The output string which will be written in a txt file.

    '''
    # construct a mapping dictionary
    mappingDict = {i: ink[i] for i in range(len(ink))}
    # construct the output string
    canvas = ''
    for line in arr_rescale:
        for score in line:
            for i in range(int(inkDensity)):
                canvas += mappingDict[score]
        canvas += '\n'
    return canvas



def getArgs() -> argparse.Namespace:
    '''
    Get arguments from terminal.

    Returns
    -------
    args : argparse.Namespace
        argparse.Namespace object.

    '''
    parser = argparse.ArgumentParser(description='Test Type.')
    parser.add_argument('-i','--input', help='Input file name, with absolute path',required=True)
    parser.add_argument('-o','--output',help='Output file name, with absolute path', required=True)
    parser.add_argument('-l','--levelofink',help='Level of ink (use how many different characters)',required=True)
    parser.add_argument('-d','--densityofink',help='density of ink (each character repeat how many times)',required=True)
    parser.add_argument('-c','--contrastfactor',help='contrast facter. Original is 1. For higher contrast, >1')
    args = parser.parse_args()
    return args



def adjustContrast(img, factor:float):
    '''
    Adjust the contrast of image

    Parameters
    ----------
    img : PIL.Image.Image
        Input image.
    factor : float
        Contrast factor.
        1 for original
        >1 for higher contrast
        <1 for lower contrast

    Returns
    -------
    im_output : PIL.Image.Image
        Contrast adjusted image.

    '''
    enhancer = ImageEnhance.Contrast(img)
    im_output = enhancer.enhance(factor) # type is PIL.Image.Image
    return im_output



#%% main
def main():
    args = getArgs()
    # read image
    # img = Image.open("C:\\Users\\eziod\\Documents\\yy3.jpg") # this works
    # img = Image.open("C:/Users/eziod/Documents/yy3.jpg") # this works
    # img = Image.open(r"C:\Users\eziod\Documents\yy3.jpg") # this works
    img = Image.open(args.input)
    
    if args.contrastfactor is not None: # if contrast factor is set, then adjust contrast level
        img = adjustContrast(img,float(args.contrastfactor))
    
    # image to rgb matrix. The matrix can be three dimensions or two.
    arr = np.array(img)
    # print(arr[0][0])
    print("[*] The shape is %s" % str(arr.shape))
    
    # The grayscale matrix
    arr_gray = grayMatrix(arr)
    
    # prepare ink before painting
    print("[*] Preparing ink.")
    inkPalette = {
                  "14":"@MN§$%¤eo+;:,.",
                  "13":"@MN§$%¤o+;:,.",
                  "12":"@MN$%¤o+;:,.",
                  "11":"@M$%¤o+;:,.",
                  "10":"@M$%¤o+:,.",
                  "9" :"@M$%o+:,.",
                  "8" :"@M$%o:,.",
                  "7" :"@$%o:,.",
                  "6" :"@$o:,.",
                  "5" :"@$o:.",
                  "4" :"@o:.",
                  "3" :"@o:"}
    ink = inkPalette[args.levelofink]
    levels = len(ink) # how many levels are there.
    
    # After preparing the ink, rescale the grayscale matrix.
    arr_rescale = rescaleMatrix(arr_gray, levels)
    
    # construct the output string
    print("[*] Painting...")
    canvas = painting(arr_rescale, ink, args.densityofink)
    print("[*] Done!")
    
    # write to file
    if '\\' in args.output:
        filename = args.output.split('\\').pop()
        outpath = args.output[0:args.output.find(filename)]
    elif '/' in args.output:
        filename = args.output.split('/')[-1]
        outpath = '/'.join(args.output.split('/')[:-1])
    else:
        print('path error')
    # fileName = "Test-Type1.txt"
    text_file = open(filename, "w")
    text_file.write(canvas)
    text_file.close()
    print("Successfully written to %s" % filename)

#%% true main
if __name__ == "__main__":
    main()
# to test the script:
# $ python terminalportrait-TEST_TYPE.py -i "C:\Users\eziod\Documents\yy3.jpg" -o "D:\full_stack\py\TerminalPortrait\src\out.txt" -l 12 -d 2