import numpy as np
import cv2

def my_bilinear(img, x, y):
    floorX, floorY = int(x), int(y)

    t, s = x - floorX, y - floorY

    zz = (1 - t) * (1 - s)
    zo = t * (1 - s)
    oz = (1 - t) * s
    oo = t * s

    interVal = img[floorY, floorX, :] * zz + img[floorY, floorX + 1, :] * zo + \
               img[floorY + 1, floorX, :] * oz + img[floorY + 1, floorX + 1, :] * oo

    return interVal

def transformation_backward(img1, M):
    h, w, c = img1.shape
    result = np.zeros((h, w, c))

    for row in range(h):
        for col in range(w):
            xy_prime = np.dot(M, np.array([[col, row, 1]]).T)
            xy = (np.linalg.inv(M)).dot(np.array([[col, row, 1]]).T)

            x_ = xy[0, 0]
            y_ = xy[1, 0]

            if x_ < 0 or y_ < 0 or (x_ + 1) >= w or (y_ + 1) >= h:
                continue

            result[row, col, :] = my_bilinear(img1, x_, y_)

    return result

def get_matching_keypoints(img1, img2, keypoint_num):
    sift = cv2.xfeatures2d.SIFT_create(keypoint_num)

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.DIST_L2)

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    return kp1, kp2, matches

def feature_matching(img1, img2, keypoint_num=None):
    kp1, kp2, matches = get_matching_keypoints(img1, img2, keypoint_num)

    X = my_ls(matches, kp1, kp2)

    M = np.array([[x[0][0], X[1][0], X[2][0]],
                  [X[3][0], X[4][0], X[5][0]],
                  [0, 0, 1]])

    result = backward(img1, M)
    return result.astype(np.uint8)

def main():
    src = cv2.imread('Lena.png')
    src = cv2.resize(src, None, fx=0.5, fy=0.5)
    src2 = cv2.imread('LenaFaceShear.png')
    theta = - 10

    translation = [[1, 0, 350],
                   [0, 1, 350],
                   [0, 0, 1]]
    rotation = [[np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1]]
    scaling = [[2, 0, 0],
               [0, 2, 0],
               [0, 0, 1]]

    M = np.dot(np.dot(translation, rotation), scaling)

    backward = transformation_backward(src, M)

    cv2.imshow("backward", backward)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()