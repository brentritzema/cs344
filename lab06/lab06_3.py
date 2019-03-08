from keras.datasets import boston_housing

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()


def print_structures():
    print(
        "training set \
            \n\tcount: %s} \
            \n\tdimensions: %s \
            \n\tshape: %s \
            \n\tdata type: %s\n\n" % (len(x_train), x_train.ndim, x_train.shape, x_train.dtype),
        "testing set \
            \n\tcount: %s} \
            \n\tdimensions: %s \
            \n\tshape: %s \
            \n\tdata type: %s\n\n" % (len(x_test), x_test.ndim, x_test.shape, x_test.dtype),
    )


print_structures()
