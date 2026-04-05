import os

# dataset folder paths
DATASET_FLDR = 'dataset'
trainDirectory = os.path.join(DATASET_FLDR, "train")
testDirectory = os.path.join(DATASET_FLDR, "test")

# use 10% of train dataset for validation
TRAIN_SIZE = 0.9
VAL_SIZE = 0.1

# training specs
BATCH_SIZE = 16
NUM_OF_EPOCHS = 50
LR = 0.001

# model specs
NUM_OF_CLASSES = 6  # merged angry+disgust
NUM_OF_CHANNELS = 1  # grayscale

# emotions — disgust merged into angry
EMOTIONS = ['angry', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# save path
MODEL_SAVE_PATH = 'emotion_model.pth'