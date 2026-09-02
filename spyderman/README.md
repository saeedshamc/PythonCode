# Spyderman

Draw a PNG image as an animated hand-drawn silhouette using OpenCV contour detection and Python Turtle graphics.

## How it works

1. Loads `spyderman.png` with OpenCV.
2. Resizes the image and converts it to grayscale.
3. Applies thresholding to isolate dark shapes from the background.
4. Finds external contours and filters out small noise.
5. Sorts contours by area (largest first) so the main silhouette is drawn before details.
6. Maps pixel coordinates to Turtle screen coordinates and draws each contour with a fill animation.

## Requirements

- Python 3.8+
- [OpenCV](https://opencv.org/) (`opencv-python`)
- Turtle (included in the Python standard library)

## Installation

```bash
pip install opencv-python
```

## Usage

Place your source image as `spyderman.png` in this folder (or change the `IMAGE` constant in `main.py`), then run:

```bash
python main.py
```

A Turtle window opens and draws the image contour by contour.

## Configuration

You can tune behavior in `main.py`:

| Variable       | Default | Description                                      |
|----------------|---------|--------------------------------------------------|
| `IMAGE`        | `spyderman.png` | Path to the input PNG image              |
| `height`       | `700`   | Target image height after resize                 |
| `scale`        | `0.8`   | Scale factor for Turtle coordinates              |
| `UPDATE_EVERY` | `3`     | Screen refresh interval (lower = smoother/slower) |

## Project structure

```
spyderman/
├── main.py          # Main script
├── spyderman.png    # Source image
└── README.md
```

## License

This project is part of the [PythonCode](https://github.com/saeedshamc/PythonCode) repository. See the root [LICENSE](../LICENSE) file for details.
