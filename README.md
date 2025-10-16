# 🖼️ Image Caption Generator

This project automatically **generates captions from images** using a pre-trained **BLIP (Bootstrapping Language-Image Pre-training)** model from Hugging Face Transformers. It provides a simple **Gradio web interface** for easy interaction — upload an image, and the model generates a meaningful caption describing it.

---

## 🚀 Features

- 🧠 Uses **BLIP** model for accurate and natural captions  
- 📷 Upload any image and get a caption instantly  
- 💻 Clean **Gradio UI** for quick testing and demos  
- ⚡ Powered by **Transformers** and **PyTorch**

---

## 🧩 Tech Stack

- **Python**
- **Hugging Face Transformers**
- **PIL (Pillow)**
- **Gradio**

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/image-caption-generator.git
   cd image-caption-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   or manually:
   ```bash
   pip install torch torchvision pillow transformers gradio requests
   ```

3. **Run the app**
   ```bash
   python chatgptapi.py
   ```

4. Open the local URL shown in the terminal (e.g. `http://127.0.0.1:7860/`) to use the web app.

---

## 🧠 How It Works

1. The user uploads an image via the Gradio interface.  
2. The **BLIP model** processes the image to extract visual features.  
3. The model generates a **natural language caption** describing the image content.  
4. The generated caption is displayed on the web interface.

---

## 📸 Example

| <img width="1917" height="867" alt="image caption genrator" src="https://github.com/user-attachments/assets/bcba4432-8ace-4f3b-b138-31e8723f4d4e" /> |

---

## 🧾 File Overview

| File | Description |
|------|--------------|
| `chatgptapi.py` | Main Python script that loads the model, defines the caption generation function, and launches the Gradio app. |
| `requirements.txt` | Python dependencies list (optional). |

---

## 💡 Future Enhancements

- Add multilingual caption generation  
- Support for batch image captioning  
- Option to download results as a text file or JSON  
- Integration with camera input  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork this repo and submit a pull request.

---

## 🧑‍💻 Author

**Your Name**  
📧 [das285amit@gmail.com]  
🌐 [(https://amitdas09.github.io/Portfolio-Website/)]

---

**⭐ If you like this project, don’t forget to star it!**
