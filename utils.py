import numpy as np


def get_intersection(mask_ann, n_annotators=3):
    intersection = np.zeros(mask_ann[0].shape)
    for mask in mask_ann:
        intersection += mask
        
    intersection = intersection >= n_annotators
    return intersection

def get_union(mask_ann, n_annotators=4):
    union = np.zeros(mask_ann[0].shape)
    mask_ann = mask_ann[:n_annotators]
    for mask in mask_ann:
        union += mask
        
    union = np.where(union>0, True, False)
    return union

    
def normalize(image, MIN_B=-600.0, MAX_B=1500.0):
    # https://stats.stackexchange.com/questions/178626/how-to-normalize-data-between-1-and-1
    image = (image - MIN_B) / (MAX_B - MIN_B)
    image[image>1] = 1.
    image[image<0] = 0.
    return image

def get_pixels_from_hu(slices):
    image = np.stack([s.pixel_array for s in slices])
    # Convert to int16 (from sometimes int16), 
    # should be possible as values should always be low enough (<32k)
    image = image.astype(np.int16)

    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0
    
    # Convert to Hounsfield units (HU)
    for slice_number in range(len(slices)):
        
        intercept = slices[slice_number].RescaleIntercept
        slope = slices[slice_number].RescaleSlope
        
        if slope != 1:
            image[slice_number] = slope * image[slice_number].astype(np.float64)
            image[slice_number] = image[slice_number].astype(np.int16)
            
        image[slice_number] += np.int16(intercept)
    
    image[image > 3072] = 3072
    image[image < -1024] = 1024
    
    return normalize(np.array(image, dtype=np.int16))