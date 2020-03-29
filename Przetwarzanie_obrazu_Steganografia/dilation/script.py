import numpy as np
from skimage import io
from matplotlib import pyplot as plt


def create_board(n_field=10):
    width = height = 10
    n = full_width = full_height = n_field * width

    board = np.zeros((full_height, full_width), dtype=np.bool)
    idx = np.arange(n).reshape((height, width))[::2].flatten()

    board[idx, :] = True
    board[:, idx] = np.invert(board[:, idx])

    return board


def display_gray(img):
    io.imshow(img, cmap="gray")
    plt.show()


def dilation(img, struct):
    mid_y, mid_x, s_rows, s_cols = info_of_struct_element(struct)

    new_img = expand_img(img, struct)
    img = new_img.__copy__()
    img_rows, img_cols = img.shape

    struct[mid_y, mid_x] = 0  # środek elementu strukturalnego nie będzie uwzględniany w "n_of_matched"

    for i in range(mid_y, img_rows - mid_y):
        for j in range(mid_x, img_cols - mid_x):
            if img[i, j] == 0:
                r = i - mid_y
                c = j - mid_x
                img_part = img[r: r + s_rows, c: c + s_cols]

                n_of_matched = np.count_nonzero(img_part & struct)

                if n_of_matched > 0:
                    new_img[i, j] = 1

    new_img = new_img[mid_y:-mid_y, mid_x:-mid_x]

    return new_img


def expand_img(img, struct):
    mid_y, mid_x, s_rows, s_cols = info_of_struct_element(struct)
    img_rows, img_cols = img.shape

    new_img = np.zeros((img_rows + s_rows - 1, img_cols + s_cols - 1), dtype=np.uint8)
    new_img[mid_y:-mid_y, mid_x:-mid_x] = img

    return new_img


def info_of_struct_element(struct):
    s_rows, s_cols = struct.shape
    mid_y = s_rows // 2
    mid_x = s_cols // 2

    return mid_y, mid_x, s_rows, s_cols


diamond = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]], dtype=np.uint8)

board_10 = create_board()
dilation_10 = dilation(board_10, diamond)
display_gray(dilation_10)
