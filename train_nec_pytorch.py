import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

class NeuralEpigeneticClock(nn.Module):
    def __init__(self, input_dim):
        super(NeuralEpigeneticClock, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.1),
            nn.Dropout(0.3),
            nn.Linear(256, 64),
            nn.BatchNorm1d(64),
            nn.LeakyReLU(0.1),
            nn.Dropout(0.2),
            nn.Linear(64, 16),
            nn.LeakyReLU(0.1),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.network(x).squeeze(-1)

def train_nec():
    print("Loading preprocessed matrices for Neural Epigenetic Clock...")
    X = pd.read_parquet("data/processed/X_cpgs.parquet")
    y = pd.read_parquet("data/processed/y_age.parquet")["age"].values

    imputer = SimpleImputer(strategy="median")
    X_imputed = imputer.fit_transform(X)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    train_dataset = TensorDataset(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
    test_dataset = TensorDataset(torch.FloatTensor(X_test), torch.FloatTensor(y_test))

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = NeuralEpigeneticClock(input_dim=X_train.shape[1]).to(device)
    
    criterion = nn.SmoothL1Loss()
    optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=5, factor=0.5)

    print(f"Training NEC Deep Model on {device}...")
    model.train()
    for epoch in range(1, 61):
        total_loss = 0.0
        for batch_x, batch_y in train_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            optimizer.zero_grad()
            preds = model(batch_x)
            loss = criterion(preds, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_loader)
        scheduler.step(avg_loss)

    model.eval()
    all_preds, all_targets = [], []
    with torch.no_grad():
        for batch_x, batch_y in test_loader:
            batch_x = batch_x.to(device)
            preds = model(batch_x)
            all_preds.extend(preds.cpu().numpy())
            all_targets.extend(batch_y.numpy())

    mae = mean_absolute_error(all_targets, all_preds)
    r2 = r2_score(all_targets, all_preds)

    print("\n--- Neural Epigenetic Clock (NEC) Evaluation ---")
    print(f"Deep NEC MAE: {mae:.2f} years")
    print(f"Deep NEC R²:  {r2:.4f}")
    
    os.makedirs("data/processed", exist_ok=True)
    torch.save(model.state_dict(), "data/processed/nec_model.pt")
    print("Saved trained NEC weights to data/processed/nec_model.pt")

if __name__ == "__main__":
    train_nec()
