import numpy as np
from PIL import Image

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
            for i in range(inkDensity):
                canvas += mappingDict[score]
        canvas += '\n'
    return canvas


#%% main
def main():
    # read image
    img = Image.open("C:\\Users\\eziod\\Documents\\yy3.jpg")
    # image to rgb matrix. The matrix can be three dimensions or two.
    arr = np.array(img)
    # print(arr[0][0])
    print("[*] The shape is %s" % str(arr.shape))
    
    # The grayscale matrix
    arr_gray = grayMatrix(arr)
    
    # prepare ink before painting
    print("[*] Preparing ink.")
    ink = '@MX$%=+-;:,.'
    inkDensity = 3
    levels = len(ink) # how many levels are there.
    
    # After preparing the ink, rescale the grayscale matrix.
    arr_rescale = rescaleMatrix(arr_gray, levels)
    
    # construct the output string
    print("[*] Painting...")
    canvas = painting(arr_rescale, ink, inkDensity)
    print("[*] Done!")
    
    # write to file
    fileName = "Test-Type.txt"
    text_file = open(fileName, "w")
    text_file.write(canvas)
    text_file.close()
    print("Successfully written to %s" % fileName)

#%% true main
if __name__ == "__main__":
    main()