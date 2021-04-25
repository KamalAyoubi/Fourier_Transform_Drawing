#%%
import FourierDrawing as FD
#%%
from FourierDrawing import Imagemanip
from FourierDrawing import FourierApprox
from FourierDrawing. import Circles
from FourierDrawing.Animate_FT import Animate
#%%
# Import raw image
url = 'https://raw.githubusercontent.com/KamalAyoubi/Fourier_Transform_Drawing/main/Images/rabbit_raw.jpg'
#img = Imagemanip(url)
img = FD.Imagemanip(url)
#%%
# Show raw image, his format, size and mode. 
raw_image =  img.show()
#%%
#Convert image to single color, Berarize it then convert to black and wight
img.single_color()
img.convert_binary(scale=3, thresh_val=200)
img.black_and_white()
#%%
# Show black and white image 
img.show_black_and_white()

# Get non-zero pixel coordiantes than calcualte distance between each pair of them
img.distance_matrix()
#%%
# Show the image countour, then the splines curves image.
img.contours_search(plot=True)
#%%
img.get_splines(plot=True)
#%%
# Show gif 
DisplayImage(url='./Images/animation5.gif')