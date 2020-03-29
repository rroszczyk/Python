from skimage import io
from matplotlib import pyplot as plt
import numpy as np
import os
from PIL import Image


def find_secret_on_first_bit(img_filename):
    img_with_secret = np.asarray(Image.open(img_filename))
    mask_for_secret = np.ones_like(img_with_secret)

    secret_info_img = np.bitwise_and(img_with_secret, mask_for_secret)
    secret_info_img *= 255

    display_img(secret_info_img)


def create_image_with_secret(org_img_filename, secret_img_filename, n_bits=1):
    input_img = np.asarray(Image.open(org_img_filename))
    secret_img = np.asarray(Image.open(secret_img_filename))

    hidden_secret_img = hide_image(input_img, secret_img, n_bits)
    save_img_with_prefix_name(hidden_secret_img, "with_secret_", org_img_filename)

    display_img(hidden_secret_img)


def hide_image(img_org, img_secret, n_bits=1):
    img_secret = img_secret // 255

    img_secret = img_secret * (2 ** n_bits - 1)

    img_org = np.right_shift(img_org, n_bits)
    img_org = np.left_shift(img_org, n_bits)

    org_with_secret = np.bitwise_or(img_org, img_secret)

    return org_with_secret


def save_img_with_prefix_name(img, prefix, file_path):
    path, filename = os.path.split(file_path)
    final_name = path + "/" + prefix + filename

    io.imsave(final_name, img)


def display_img(img):
    plt.imshow(img)
    plt.show()


# Ukrywanie informacji (zakomentuj: Odkrywanie informacji)
##########################################################
input_img_filename = "data/mandrill.png"
secret_filename = "data/key.png"
create_image_with_secret(input_img_filename, secret_filename, 1)

# Odkrywanie informacji
#######################
# img_with_secret_filename = "data/with_secret_mandrill.png"
# find_secret_on_first_bit(img_with_secret_filename)
