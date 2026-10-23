import gradio as gr
from PIL import ImageEnhance, ImageFilter, ImageOps


# Complete the marked steps. The interface is already provided.
def edit_image(image, effect, angle, brightness, flip):
    if image is None:
        return None

    result = image.copy()

    # STEP 1 — Add the three effect branches.
    if effect == "Grayscale":
        result = result
    elif effect == "Blur":
        result = result
    elif effect == "Sharpen":
        result = result

    # STEP 2A — Rotate the image using angle and expand=True.
    result = result

    # The enhancer object is already provided.
    enhancer = ImageEnhance.Brightness(result)

    # STEP 2B — Use enhancer.enhance(...) with the brightness value.
    result = result

    # STEP 3 — Mirror the result only when flip is True.
    if flip:
        result = result

    return result


demo = gr.Interface(
    fn=edit_image,
    inputs=[
        gr.Image(type="pil", label="Upload an alien photo"),
        gr.Dropdown(
            choices=["No Effect", "Grayscale", "Blur", "Sharpen"],
            value="No Effect",
            label="Choose an effect",
        ),
        gr.Slider(
            minimum=-180,
            maximum=180,
            value=0,
            step=15,
            label="Rotation angle",
        ),
        gr.Slider(
            minimum=0.5,
            maximum=1.5,
            value=1.0,
            step=0.1,
            label="Brightness",
        ),
        gr.Checkbox(label="Mirror the image"),
    ],
    outputs=gr.Image(label="Edited photo"),
    title="Alien Photo Editor",
    description="Choose an effect, rotation, brightness, and mirror setting.",
)


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
    )
