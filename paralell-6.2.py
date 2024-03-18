
from multiprocessing import Pool
import cv2
import sys
from functools import partial
from timeit import default_timer as timer

THRESH_METHOD = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
DEFAULT_ROWS = 10
DEFAULT_COLS = 10
INPUT_PATH = 'input/'
OUTPUT_PATH = 'output/'


def process_image(name, rows, cols):
    try:
        im = cv2.imread(INPUT_PATH + name)
        height, width, _ = im.shape
        part_height = height // rows
        part_width = width // cols
        parts = []
        for i in range(rows):
            for j in range(cols):
                part = im[i * part_height:(i + 1) * part_height, j * part_width:(j + 1) * part_width]
                parts.append(part)
                output_name = f"{name}_{i}_{j}.png"
                cv2.imwrite(OUTPUT_PATH + output_name, part)
        return parts
    except Exception as e:
        print(f"Error processing image: {e}")
        return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python example6-rm.py <image_file> [rows=<number>] [cols=<number>]")
        sys.exit(1)

    file_name = sys.argv[1]
    rows = DEFAULT_ROWS
    cols = DEFAULT_COLS

    for arg in sys.argv[2:]:
        if arg.startswith("rows="):
            rows = int(arg.split("=")[1])
        elif arg.startswith("cols="):
            cols = int(arg.split("=")[1])

    start = timer()
    parts = process_image(file_name, rows, cols)
    print('Took %.4f seconds.' % (timer() - start))
    print('Done.')
