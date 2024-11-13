# 🏆 DIY Room Designer - Hackathon Prize 🏆
**"Most Likely to Be a Business"** — [AI Hacknights with Cloudflare](https://github.com/kristianfreeman/ai-hacknights-cloudflare)

Welcome to **Interactive Room Designer**, the innovative app that lets you design and customize a virtual room with ease. Powered by **ToolHouse**, **OpenAI GPT**, and **Streamlit**, our app generates realistic room images based on user descriptions and provides shopping links for each component, making interior design accessible and interactive!

---

## 📸 Demo
[Hackathon Presentation](https://docs.google.com/presentation/d/1q1e6sRevsFAF9X9173K_BWbJd3BQDpHYqNExA6YyryA/edit?usp=sharing)

[Room Designer Demo](https://drive.google.com/file/d/12foJj8qzN0_oC-O1RjSdIrNj1Xg50nv2/view?usp=sharing)  
*Easily initialize, update, and visualize your custom room!*

---

## 💡 Features

- **Generate Realistic Room Images**: Describe your dream room, and watch it come to life.
- **Dynamic Updates**: Add new components to the room on-the-go, and get updated images in real-time.
- **Shopping Integration**: Browse Amazon links for items in your room, helping you turn your design into reality!
- **Intuitive Interface**: User-friendly layout with easy controls to initialize and update your room.

---

## ⚙️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [OpenAI GPT](https://openai.com/) + [ToolHouse](https://www.toolhouse.com/)
- **Language**: Python

---

## 🚀 Getting Started

Follow these steps to set up and run the app locally:

### Prerequisites
- **Python>= 3.9+**
- **Streamlit**: `pip install streamlit`
- **OpenAI SDK**: `pip install openai`
- **ToolHouse SDK**: `pip install toolhouse`
- OpenAI and ToolHouse API keys

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/interactive-room-designer.git
   cd interactive-room-designer
   ```
2. **Set up API keys: Add your OpenAI and ToolHouse API keys to Streamlit secrets**:
   Create a .streamlit/secrets.toml file in the project root:
   ```bash
    OPENAI_API_KEY = "your_openai_api_key"
    TOOLHOUSE_API_KEY = "your_toolhouse_api_key"
   ```
3. **Run the app**
   ```bash
   streamlit run app.py
   ```
## 📝 Code Walkthrough

The core functionality resides in a few key sections:

1. **Room Initialization**
   - Generates an image based on a user’s initial description.
   - Uses GPT and ToolHouse APIs to produce and display an initial room setup.

2. **Updating Room Components**
   - Dynamically updates the room with new elements as specified by the user.
   - Displays the updated room image with all added components.

3. **Shopping Links**
   - Provides Amazon links for selected room items, helping users find decor and furniture items to bring their room to life.

## 🛠️ Core Functions

- **`initialize_room()`**: Generates the initial room image based on user input.
- **`update_room()`**: Adds new components to the room and updates the displayed image.
- **`extract_image_urls()`**: Extracts and validates image URLs from ToolHouse responses.
- **`get_amazon_link()`**: Links each room component to relevant Amazon search results.

## 🏆 Hackathon Experience

We created **Interactive Room Designer** during the **AI Hacknights Hackathon** and were honored with the **"Most Likely to Be a Business"** award. Our goal was to make interior design accessible, fun, and practical through the power of AI and interactive technology.

## 👥 Contributors

Meet our team! 🎉

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/mpianrhko">
        <img src="https://github.com/mpianrhko.png" width="100px;" alt="mpianrhko"/>
        <br />
        <sub><b>mpianrhko</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/EP04">
        <img src="https://github.com/EP04.png" width="100px;" alt="EP04"/>
        <br />
        <sub><b>EP04</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/victorianwobodo">
        <img src="https://github.com/victorianwobodo.png" width="100px;" alt="victorianwobodo"/>
        <br />
        <sub><b>victorianwobodo</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/srimoyee1212">
        <img src="https://github.com/srimoyee1212.png" width="100px;" alt="srimoyee1212"/>
        <br />
        <sub><b>srimoyee1212</b></sub>
      </a>
    </td>
    <!-- Add more contributors here -->
  </tr>
</table>

## 💬 Feedback

We welcome feedback! If you have ideas for improvements or find any issues, please [open an issue](https://github.com/your-username/interactive-room-designer/issues) or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


