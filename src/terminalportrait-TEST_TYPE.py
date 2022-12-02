import numpy as np
from PIL import Image

#%% functions
def isGrayscale(array: np.array) -> bool:
    '''
    Check if the rgb matrix is already grayscale. 

    Parameters
    ----------
    array : np.array uint8
        The rgb matrix.
        Normally it has three dimensions. This function will check again.

    Returns
    -------
    bool
        Return True if array is grayscale. False if array is colored

    '''
    if len(array.shape) == 2: # if the rgb matrix contains only two dimensions
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


#%% 
# read image
img = Image.open("C:\\Users\\eziod\\Documents\\yy3.jpg")
# image to rgb matrix. The matrix can be three dimensions or two.
arr = np.array(img)
# print(arr[0][0])
print("[*] The shape is %s" % str(arr.shape))




# check grayscale
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
else: # the matrix has one or more than three dimensions
    print("[!] Matrix dimension incorrect. Error with input image. Matrix shape is %s." % str(arr.shape))

# Now the matrix is grayscale, divided by...
ink = '@MX$%=+-;:,.'
inkDensity = 3
levels = len(ink)
arr_rescale = arr_gray//(255//levels+1) # the value of arr_rescale varies from 0 to levels-1

# construct a mapping dictionary
mappingDict = {i: ink[i] for i in range(len(ink))}

# construct the output string
res = ''
for line in arr_rescale:
    for score in line:
        for i in range(inkDensity):
            res += mappingDict[score]
    res += '\n'


# write to file
fileName = "Test-Type.txt"
text_file = open(fileName, "w")
text_file.write(res)
text_file.close()
