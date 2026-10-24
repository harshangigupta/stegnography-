# Colour DWT Steganography Lab

A colour-image steganography project exploring **Discrete Wavelet Transform (DWT)** for hiding a secret image inside a cover image. The repository currently includes a browser-based demonstration and Python configuration/dependency files for further development of a lightweight deep-learning pipeline.

> **Project status:** The HTML demo is available to run locally. The broader deep-learning training pipeline and robustness experiments are still under development; results should be treated as experimental until validated.

## Overview

Steganography aims to conceal the existence of a message by embedding it inside an ordinary-looking file. This project experiments with hiding one colour image inside another while measuring the visual difference between the original cover and the resulting stego image.

### Current browser demo

The `colour_dwtsteganography.html` page provides:

- Upload fields for a cover image and a secret image.
- RGB processing with a Haar-style DWT applied independently to the red, green, and blue channels.
- Visualisation of the LL, LH, HL, and HH wavelet sub-bands.
- An adjustable embedding-strength parameter.
- A generated stego image that can be downloaded as PNG.
- A recovery-key JSON file and a metrics CSV export.
- Secret-image extraction using the matching stego PNG and recovery key.
- RGB histogram comparisons.
- Image-quality metrics: Mean Squared Error (MSE), Peak Signal-to-Noise Ratio (PSNR), and Structural Similarity Index (SSIM).

The demo runs in the browser. It does not require a server or upload images to a remote service.

## Methodology

At a high level, the demonstration follows this workflow:

1. **Input:** Select a cover image and a secret image.
2. **Preprocessing:** Read the images as RGB data and resize them to compatible dimensions.
3. **Transform:** Apply a Haar DWT separately to each colour channel to obtain LL, LH, HL, and HH sub-bands.
4. **Embedding:** Embed selected secret-image detail coefficients into corresponding cover-image detail bands, controlled by the embedding-strength setting.
5. **Reconstruction:** Apply the inverse transform to reconstruct the colour stego image.
6. **Evaluation:** Compare cover and stego images using MSE, PSNR, SSIM, and RGB histograms.
7. **Extraction:** Use the generated recovery key with the matching stego PNG to attempt to recover the secret image.

## Repository contents

```text
stegnography-/
├── colour_dwtsteganography.html  # Browser-based colour DWT demo
├── config.py                     # Python project paths and experiment settings
├── requirements.txt              # Python dependencies for the development pipeline
├── README.md
└── .gitignore
```

The Python configuration also defines locations for datasets, results, saved models, and outputs, along with training settings and candidate lightweight model names. These settings do not, by themselves, mean that training or every listed model is already implemented.

## Run the browser demo

No Python setup is needed for the HTML demonstration.

1. Clone the repository:

   ```bash
   git clone https://github.com/harshangigupta/stegnography-.git
   cd stegnography-
   ```

2. Open `colour_dwtsteganography.html` in a modern browser (for example, Chrome, Firefox, or Edge).
3. Upload a cover image and a secret image.
4. Adjust the embedding strength, then select **Apply DWT + Embed**.
5. Download the stego PNG and its matching recovery-key JSON.
6. To test extraction, select both files in the extraction section.

**Important:** Keep the recovery key paired with the exact stego PNG generated alongside it. Store the key securely and do not share it with anyone who should not be able to recover the secret image.

## Python environment

The repository includes `requirements.txt` for the Python-side development work.

```bash
python -m venv .venv
```

Activate the environment:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

Install the listed dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The current repository does not yet document a single Python training or inference command. Run Python scripts only once their entry points and dataset requirements have been added.

## Configuration and datasets

`config.py` contains project paths and settings for image dimensions, training, DWT, and candidate model names. It expects local data under a `datasets/` directory, including the UCMerced Land Use images and secret images.

A possible local layout is:

```text
datasets/
├── UCMerced_LandUse/
│   └── Images/
├── VisDrone/
└── secret_images/
```

Place datasets locally and follow their original licences and terms of use. Large datasets, private images, trained model weights, and generated experiment outputs should not normally be committed to Git.

## Evaluation metrics

| Metric | What it measures | Preferred direction |
|---|---|---|
| **MSE** | Average squared pixel difference between two images | Lower |
| **PSNR** | Signal quality relative to reconstruction error, in dB | Higher |
| **SSIM** | Similarity in image structure, luminance, and contrast | Closer to 1 |
| **UIQI** | Universal Image Quality Index; planned for broader evaluation | Closer to 1 |
| **BER** | Bit Error Rate; relevant when evaluating recovered bit sequences after distortions or attacks | Lower |

The current HTML demo displays MSE, PSNR, and SSIM. UIQI, BER, compression/attack testing, and systematic model comparisons belong to the planned evaluation pipeline and should only be reported after they are implemented and tested.

## Limitations and security notes

- This is an experimental/educational project, not a certified secure communication system.
- The current demo requires a recovery key and is not a blind-extraction method.
- Image recompression, resizing, editing, or format conversion may damage extraction.
- Steganography is not the same as encryption. Do not use the demo to protect highly sensitive information.
- **Never commit real passwords, encryption keys, API tokens, or private data.** If a real secret has already been committed, remove it from the code, rotate/revoke it, and review Git history; adding it to `.gitignore` alone does not remove it from existing commits.
- Check all dataset licences and obtain permission before using images that are not yours.

## Roadmap

- [ ] Finalise the dataset preparation and train/validation/test split.
- [ ] Implement and compare lightweight encoder–decoder architectures.
- [ ] Add UIQI and BER calculations with clear evaluation protocols.
- [ ] Test robustness against selected image distortions and compression.
- [ ] Record reproducible experiments and compare model quality, runtime, and model size.
- [ ] Document tested Python entry points and example results.

## Contributing

Suggestions and improvements are welcome. For substantial changes, open an issue first to discuss the proposed approach. Please do not commit datasets, generated outputs, model checkpoints, or secrets.

## Author

**Harshangi Gupta**

Repository: [harshangigupta/stegnography-](https://github.com/harshangigupta/stegnography-)
