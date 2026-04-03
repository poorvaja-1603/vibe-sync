import os

#datset folder paths
DATASET_FLDR = f'dataset'
trainDiretcory = os.path.join(DATASET_FLDR, "train")
testDirectory = os.path.join(DATASET_FLDR, "test")

#use 10% of train dataset for validation
TRAIN_SIZE = 0.9
VAL_SIZE = 0.1

#training specs
BATCH_SIZE = 16
NUM_OF_EPOCHS = 50
LR = 0.1