image = io.imread('../img/skimage-logo.png')

# --- assign each color channel to a different variable ---

r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]
