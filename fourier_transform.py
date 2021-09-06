import cv2
import numpy as np
import matplotlib.pyplot as plt


def fourier(img):
    dft = np.fft.fft2(np.float32(img))
    dft_shift = np.fft.fftshift(dft)
    mag = np.abs(dft_shift)
    ang = np.angle(dft_shift)
    return mag, ang

def inverse_fourier(mag, ang):
    combined = np.multiply(mag, np.exp(1j*ang))
    fftx = np.fft.ifftshift(combined)
    ffty = np.fft.ifft2(fftx)
    imgCombined = np.abs(ffty).astype(np.uint8)
    return imgCombined


img = cv2.imread(r'.\imagenes\192.jpg', 0)

mag, ang = fourier(img)
mask = np.zeros(img.shape, dtype=img.dtype)
y,x = mask.shape[0], mask.shape[1]
cx = x//2
cy = y//2

mask[cy-50 : cy+50, cx-50 : cx+50] = 1.
mag = mag * mask
res = inverse_fourier(mag, ang)

mx = np.amax(np.log(mag+0.001))
tmp = np.uint8(255*(mag/mx))

_, ax = plt.subplots(2,2)
ax[0,0].imshow(img, cmap='gray')
ax[0,1].imshow(tmp, cmap='gray')
ax[1,0].imshow(mask, cmap='gray')
ax[1,1].imshow(res, cmap='gray')
plt.show()