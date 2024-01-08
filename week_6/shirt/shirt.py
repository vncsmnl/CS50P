import sys
import os
from PIL import Image, ImageOps
import argparse

def main():
    parser = argparse.ArgumentParser(description="Overlay a shirt image on another image.")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output image file path")
    args = parser.parse_args()

    validate_arguments(args.input, args.output)

    shirt_image = Image.open("shirt.png")
    try:
        with Image.open(args.input) as input_image:
            input_image = ImageOps.fit(input_image, shirt_image.size)
            input_image.paste(shirt_image, shirt_image)
            input_image.save(args.output)
    except FileNotFoundError:
        sys.exit("Input file does not exist.")

def validate_arguments(input_path, output_path):
    valid_extensions = {".jpg", ".jpeg", ".png"}

    if not (input_path.lower().endswith(tuple(valid_extensions)) and
            output_path.lower().endswith(tuple(valid_extensions))):
        sys.exit("Invalid file extensions in input or output paths.")

    if os.path.splitext(input_path)[1] != os.path.splitext(output_path)[1]:
        sys.exit("Input and output file extensions do not match.")

if __name__ == "__main__":
    main()
