"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'horse2zebra_train': 220,
    'horse2zebra_test': 20
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'horse2zebra_train': '.jpg',
    'horse2zebra_test': '.jpg',
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'horse2zebra_train': '/u/home/r/rengel/CycleGAN_TensorFlow/horse2zebra/horse2zebra_train.csv',
    'horse2zebra_test': '/u/home/r/rengel/CycleGAN_TensorFlow/horse2zebra/horse2zebra_test.csv',
}
