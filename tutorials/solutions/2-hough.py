# Hough transform

from skimage import data, feature
from skimage.transform import hough_circle
from skimage.draw import circle_perimeter

image = data.coins()[0:95, 180:370]
edges = feature.canny(image, sigma=3, low_threshold=10, high_threshold=60)

hough_radii = np.arange(15, 30, 2)
hough_response = hough_circle(edges, hough_radii)

centers = []
likelihood = []
radii = []
# Your code here

for idx, resp in enumerate(hough_response):
        # Find the local peaks:
    peaks = feature.peak_local_max(resp)
    centers.extend(peaks)
    # The likelihood for each of these peaks is given by the Hough response:
    likelihood.extend(resp[peaks[:, 0], peaks[:, 1]])
    # Radius is given by the array index, but we need to save the radius for
    # every peak we added to the list above. So we create an array of equal
    # length (`peaks.shape[0]`)
    radii.extend(np.ones(peaks.shape[0]) * hough_radii[idx])

# Make a copy of the image so we can draw on it without messing up the original
im = image.copy()

# Sort the likelihood array from low to high. We're interested in the entries
# with highest likelihood - so we need to look at the end of the array.
# However, we don't really care about the actual likelihood values. What we
# care about is the indices at which these max likelihood values occur. We can
# use `np.argsort` for that:
for i in np.argsort(likelihood)[-3:]:
        # Look up circle center:
    row, column = centers[i]
    # Draw a black circle at the center with given radius:
    r_circle, c_circle = circle_perimeter(row, column, int(radii[i]))
    im[r_circle, c_circle] = 0
    # Plot:
    plt.imshow(im)
    plt.plot(column, row, 'ko')
