import os

# Paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, "datasets")
UCM_DIR = os.path.join(DATA_DIR, "UCMerced_LandUse", "Images")
VISDRONE_DIR = os.path.join(DATA_DIR, "VisDrone")
SECRET_DIR = os.path.join(DATA_DIR, "secret_images")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
MODELS_DIR = os.path.join(PROJECT_ROOT, "saved_models")
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")

# Image sizes
COVER_SIZE = 256  # Cover image resize
SECRET_SIZE = 128  # Secret image resize (= COVER_SIZE // 2 after DWT)

# Training
BATCH_SIZE = 8
NUM_EPOCHS = 50
LEARNING_RATE = 1e-3
ALPHA = 1.0  # weight for image (cover vs stego) loss
BETA = 2.0   # weight for secret reconstruction loss
TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1
TEST_SPLIT = 0.1

# Encryption
AES_KEY = b'StegnoProjectKey_2026_SecureX!32'  # 32 bytes = AES-256

# DWT
WAVELET = 'haar'

# Model names
MODEL_NAMES = ['MiniUNet', 'LiteResNet', 'MobileStegNet']

# Device
import torch
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Create directories
for d in [DATA_DIR, SECRET_DIR, RESULTS_DIR, MODELS_DIR, OUTPUTS_DIR,
          os.path.join(OUTPUTS_DIR, "stego_samples"), os.path.join(OUTPUTS_DIR, "plots")]:
    os.makedirs(d, exist_ok=True)
