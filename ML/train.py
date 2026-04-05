import torch
import torch.nn as nn
import torch.optim as optim
from emotionNet import EmotionNet
from dataset import get_dataloaders
from config import (
    NUM_OF_EPOCHS, LR,
    NUM_OF_CHANNELS, NUM_OF_CLASSES,
    MODEL_SAVE_PATH
)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Training on: {device}")
train_loader, val_loader, test_loader = get_dataloaders()

# Model, Loss, Optimizer, Scheduler
model = EmotionNet(
    numOfChannels=NUM_OF_CHANNELS,
    numOfClasses=NUM_OF_CLASSES
).to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=1e-3,
    weight_decay=1e-4
)

# reduce LR when val loss stops improving
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer,
    mode='min',       # monitor val loss (minimize)
    factor=0.5,       # new_lr = lr * 0.5
    patience=5,       # wait 5 epochs before reducing
)

# Train one epoch
def train_epoch(model, loader, criterion, optimizer):
    model.train()  # dropout ON, batchnorm in train mode
    
    total_loss = 0
    correct = 0
    total = 0

    for batch_idx, (images, labels) in enumerate(loader):
        images = images.to(device)
        labels = labels.to(device)

        # forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # backward pass
        optimizer.zero_grad()   # clear old gradients
        loss.backward()         # compute new gradients
        optimizer.step()        # update weights

        # track stats
        total_loss += loss.item()
        _, predicted = outputs.max(1)   # get highest score index
        correct += predicted.eq(labels).sum().item()
        total += labels.size(0)

        # print progress every 100 batches
        if batch_idx % 100 == 0:
            print(f"  Batch {batch_idx}/{len(loader)} | Loss: {loss.item():.4f}")

    avg_loss = total_loss / len(loader)
    accuracy = 100 * correct / total
    return avg_loss, accuracy

# Evaluate one epoch
def evaluate(model, loader, criterion):
    model.eval()  # dropout OFF, batchnorm in eval mode
    
    total_loss = 0
    correct = 0
    total = 0

    with torch.no_grad():  # no gradient computation needed
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            total_loss += loss.item()
            _, predicted = outputs.max(1)
            correct += predicted.eq(labels).sum().item()
            total += labels.size(0)

    avg_loss = total_loss / len(loader)
    accuracy = 100 * correct / total
    return avg_loss, accuracy

# Main Training Loop
best_val_acc = 0.0

for epoch in range(NUM_OF_EPOCHS):
    print(f"\nEpoch {epoch+1}/{NUM_OF_EPOCHS}")
    print("-" * 40)

    # train
    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer)

    # validate
    val_loss, val_acc = evaluate(model, val_loader, criterion)

    # update scheduler
    scheduler.step(val_loss)

    # print epoch summary
    print(f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.2f}%")
    print(f"Val   Loss: {val_loss:.4f} | Val   Acc: {val_acc:.2f}%")
    print(f"LR: {optimizer.param_groups[0]['lr']}")

    # save best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), MODEL_SAVE_PATH)
        print(f"Saved best model (Val Acc: {val_acc:.2f}%)")

# Final Test Evaluation
print("\n" + "="*40)
print("Final Test Evaluation")
print("="*40)

# load best saved model
model.load_state_dict(torch.load(MODEL_SAVE_PATH))
test_loss, test_acc = evaluate(model, test_loader, criterion)
print(f"Test Loss: {test_loss:.4f} | Test Acc: {test_acc:.2f}%")
print(f"Best Val Acc: {best_val_acc:.2f}%")