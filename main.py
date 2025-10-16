from PIL import Image
from transformers import BlipProcessor,BlipForConditionalGeneration
import gradio as gr
import requests

processor = BlipProcessor.from_pretrained("microsoft/conditional-detr-resnet-50")
model = BlipForConditionalGeneration.from_pretrained("microsoft/conditional-detr-resnet-50")

def genrate_caption(img):
    img_input=Image.fromarray(img) 
    inputs=processor(img_input,return_tensors="pt")
    out= model.generate(**inputs)
    caption=processor.decode(out[0],skip_special_tokens=True)
    return caption

demo=gr.Interface(fn=genrate_caption,
                  title="Image Caption Genrater",
                  inputs=[gr.Image(label="Image")],
                  outputs=[gr.Text(label="Caption"),],)

demo.launch()