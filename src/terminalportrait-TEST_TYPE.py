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

    Returns
    -------
    bool
        Return True if array is grayscale. False if array is colored

    '''
    if len(array.shape) == 2: # if the rgb matrix contains only two dimensions
        return True # then normally it's already gray scale
    # else, three dimensions
    # check for one given pixel, if r, g, b three values are the same
    
    # totalPixel = 1
    # for v in array.shape:
    #     totalPixel *= v
    # totalPixel = totalPixel/3
    # print("Total pixel is %s" % str(totalPixel))
    
    # check all pixels
    for iline in range(arr.shape[0]):
        for icol in range(arr.shape[1]):
            if arr[iline][icol][0] == arr[iline][icol][1] and arr[iline][icol][1] == arr[iline][icol][2]:
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
img = Image.open("C:\\Users\\eziod\\Documents\\yy.jfif")
# image to rgb matrix. The matrix can be three dimensions or two.
arr = np.array(img)
# print(arr[0][0])
print(arr.shape)



# print(arr[719][0])

# if len(arr.shape)==3: # rgb matrix is three dimension
#     # check if the matrix is already grayscaled. If yes, we cant reapply the color to grayscale equation
#     print(isGrayscale(arr))
#     arr2D = arr[:,:,0]
#     arr2D_rescale = arr2D.copy()//37
#     print(np.amax(arr2D_rescale))
# else:
#     arr2D_rescale = arr.copy()//37

# check if the matrix is already grayscale. If not, transform to grayscale. If yes, do nothing.
if isGrayscale(arr)==False: # is not grayscale
    print("[*] The input image is not grayscale. Transforming to grayscale...")
    # transform to grayscale
    arr_gray = color2grayscale(arr)
    print("[*] Done")
else:
    arr_gray = arr
    print("[*] The input image is already grayscale")

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
