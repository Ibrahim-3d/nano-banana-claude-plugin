import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_2, NANO_BANANA_PRO


def generate(prompt, output="generated_image.png", images=None, aspect_ratio=None, resolution=None):
    """
    Universal image generation entry point.

    Modes (determined automatically by the flags you pass):
      - Text-to-image   : no --images, no --resolution
      - Image editing   : --images source.png  (one image)
      - Multi-image     : --images a.png b.png ...  (compose, reference, or style transfer
                          – describe what you want in the prompt)
      - High-resolution : --resolution 2K|4K  (can be combined with any mode above;
                          automatically selects the Pro model)
    """
    client = get_client()

    # Use Pro model when a specific resolution is requested
    model = NANO_BANANA_PRO if resolution else NANO_BANANA_2

    # Build multimodal contents list
    contents = [prompt]
    if images:
        for path in images:
            contents.append(Image.open(path))

    # Build optional image config
    image_config_kwargs = {}
    if aspect_ratio:
        image_config_kwargs["aspect_ratio"] = aspect_ratio
    if resolution:
        image_config_kwargs["image_size"] = resolution

    config = None
    if image_config_kwargs:
        config = types.GenerateContentConfig(
            image_config=types.ImageConfig(**image_config_kwargs)
        )

    print(f"Generating image with {model}...")
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=config,
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(output)
            print(f"Image saved to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Nano Banana image generation. "
            "Handles text-to-image, image editing, multi-image composition / style transfer, "
            "and high-resolution generation in a single script."
        )
    )
    parser.add_argument("--prompt", "-p", required=True,
                        help="Text prompt or editing/composition instructions")
    parser.add_argument("--output", "-o", default="generated_image.png",
                        help="Output filename (default: generated_image.png)")
    parser.add_argument("--images", "-i", nargs="+", default=None,
                        help=(
                            "Input image path(s). "
                            "One image → edit mode. "
                            "Two images → composition / style transfer (describe intent in prompt). "
                            "Up to 14 images → multi-reference generation."
                        ))
    parser.add_argument("--aspect-ratio", "-ar", default=None,
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4",
                                 "9:16", "16:9", "21:9"],
                        help="Aspect ratio for the output image")
    parser.add_argument("--resolution", "-r", default=None,
                        choices=["1K", "2K", "4K"],
                        help=(
                            "Output resolution. Triggers the Pro model. "
                            "Omit for standard resolution (Nano Banana 2)."
                        ))
    args = parser.parse_args()

    if args.images and len(args.images) > 14:
        parser.error("Maximum 14 input images are supported.")

    generate(args.prompt, args.output, args.images, args.aspect_ratio, args.resolution)
