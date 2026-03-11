# 🎬 YouTube Thumbnail Hunter

Ever wanted to **grab every thumbnail from a YouTube channel** in **high resolution**, without manually saving each one?  
Well, this Python script does exactly that. It’s like having a **magic thumbnail scraper** in your pocket! 🪄📸

Powered by **Selenium** and **requests**, this script scrolls through the channel, collects all video links, and downloads **non-duplicate max-resolution thumbnails** automatically.  

Perfect for:
- YouTubers who want to archive their content 🎥  
- Researchers building datasets for AI/ML 🧠  
- Designers looking for thumbnail inspiration 🎨  

---

## 🚀 Features

- Scrolls automatically through **all videos** on a channel  
- Extracts **video URLs** without missing a thing  
- Downloads **maxresdefault.jpg thumbnails**  
- Prevents duplicates  
- Saves thumbnails neatly into a local folder `thumbnails/`  
- Beginner-friendly, zero hassle setup  

---

## 🛠 Built With

- **Python 3.x** – The heart of it all  
- **Selenium** – For browser automation 🖥️  
- **WebDriver Manager** – Automatic ChromeDriver setup ⚙️  
- **Requests** – Fetch thumbnails in a snap 📡  

---

## 🔧 Installation

1. Clone this repo:

```bash
git clone https://github.com/SulemanSadat/youtube-thumbnail-downloader.git
cd youtube-thumbnail-hunter
````

2. Install dependencies:

```bash
pip install selenium webdriver-manager requests
```

3. Make sure you have **Google Chrome** installed.

---

## ⚡ How to Use

1. Open `youtube_thumbnail.py` and replace the channel URL:

```python
channel_url = 'https://www.youtube.com/@username/videos'
```

2. Run the script:

```bash
python youtube_thumbnail.py
```

3. Watch the magic happen! All thumbnails will be downloaded to `thumbnails/`.

---

## 🖼 Output Example

```
thumbnails/
├── thumbnail_1.jpg
├── thumbnail_2.jpg
├── thumbnail_3.jpg
...
```

Every thumbnail is **high-quality** and **non-duplicate**. Perfect for datasets, analysis, or archiving your favorite channels.

---

## 💡 Creative Uses

* Build **AI datasets** for computer vision projects 🤖
* Analyze YouTube trends or thumbnail designs 📊
* Backup your own channel thumbnails 🗂️
* Create thumbnail galleries for inspiration 🎨

---

## ⚠️ Notes

* Some videos may not have `maxresdefault.jpg`, in which case you may get a lower-quality thumbnail.
* Works best with **public YouTube channels** (private or age-restricted videos may not load).

---

## 📝 License

Open-source and free to use for **learning, personal, or research projects**.

---
