import os
import torch
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms, datasets
from config import (
    trainDirectory, testDirectory,
    TRAIN_SIZE, BATCH_SIZE
)

# Transforms
train_transforms = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((48, 48)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

test_transforms = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((48, 48)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

# Get DataLoaders
def get_dataloaders():
    # ImageFolder automatically assigns labels based on folder names
    full_train = datasets.ImageFolder(
        root=trainDirectory,
        transform=train_transforms
    )

    test_dataset = datasets.ImageFolder(
        root=testDirectory,
        transform=test_transforms
    )

    print(f"Classes: {full_train.classes}")
    # 90/10 train/val split
    total = len(full_train)
    train_size = int(TRAIN_SIZE * total)
    val_size = total - train_size

    train_dataset, val_dataset = random_split(
        full_train,
        [train_size, val_size],
        generator=torch.Generator().manual_seed(42)
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=0,
        pin_memory=True
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=0,
        pin_memory=True
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=0,
        pin_memory=True
    )

    print(f"Train: {train_size} | Val: {val_size} | Test: {len(test_dataset)}")

    return train_loader, val_loader, test_loader

if __name__ == '__main__':
    train_loader, val_loader, test_loader = get_dataloaders()
    images, labels = next(iter(train_loader))
    print(f"Image shape: {images.shape}") 
    print(f"Labels: {labels}") 