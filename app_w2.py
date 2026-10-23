import gradio as gr
from PIL import ImageOps


# STEP 1 — Replace result = image with a grayscale edit.
def edit_image(image):
    if image is None:
        return None

    result = image

    # STEP 2 — Mirror the edited image from left to right.
    # result = TODO

    return result


# The Gradio interface and launch settings are already provided.
demo = gr.Interface(
    fn=edit_image,
    inputs=gr.Image(type="pil", label="Upload a space photo"),
    outputs=gr.Image(label="Edited photo"),
    title="Space Photo Lab",
    description="Upload a photo, then click Submit to turn it grayscale and mirror it.",
)


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
    )
