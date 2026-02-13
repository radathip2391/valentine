import streamlit as st
import streamlit.components.v1 as components

# --- 1. ตั้งค่าหน้าเว็บให้ซ่อนส่วนเกินของ Streamlit ---
st.set_page_config(page_title="My Secret Message ❤️", layout="wide")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            width: 100vw !important;
            height: 100vh !important;
            border: none;
        }
    </style>
    """, unsafe_allow_html=True)

# --- 2. โค้ด HTML + CSS + JS (แก้ไขโครงสร้างหน้า 5 เรียบร้อย) ---
valentine_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;600&family=Fredoka:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
            font-family: 'Kanit', sans-serif; 
            display: flex; align-items: center; justify-content: center; 
            width: 100vw; height: 100vh; overflow: hidden;
        }
        .container { 
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(15px);
            width: 90%; max-width: 420px; 
            padding: 40px 25px; border-radius: 50px; 
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
            text-align: center; z-index: 10;
        }
        .page { display: none; animation: slideUp 0.6s ease-out forwards; }
        .active { display: block; }
        @keyframes slideUp { 
            from { opacity: 0; transform: translateY(30px); } 
            to { opacity: 1; transform: translateY(0); } 
        }
        .img-wrapper { 
            width: 100%; height: 220px; 
            display: flex; justify-content: center; align-items: center; 
            margin-bottom: 20px;
        }
        .main-img { max-width: 100%; max-height: 100%; border-radius: 25px; object-fit: contain; }
        h1 { font-family: 'Fredoka', sans-serif; font-size: 1.8rem; color: #ff4b6d; margin-bottom: 10px; line-height: 1.2; }
        p { color: #7a5c61; line-height: 1.6; margin-bottom: 25px; font-size: 1.1rem; }
        .btn-group { display: flex; justify-content: center; gap: 15px; }
        button { 
            padding: 12px 28px; font-size: 1.1rem; border-radius: 25px; border: none; 
            cursor: pointer; font-weight: 600; transition: 0.3s;
        }
        .primary-btn { background: linear-gradient(45deg, #ff4b6d, #ff8fab); color: white; }
        #noBtn { background: #fff; color: #ff8fab; border: 2px solid #ff8fab; }
        .heart-particle { position: fixed; pointer-events: none; animation: fly 2.5s ease-out forwards; z-index: 1000; }
        @keyframes fly { 0% { transform: translateY(0) scale(0); opacity: 1; } 100% { transform: translateY(-110vh) scale(1.2); opacity: 0; } }
    </style>
</head>
<body>
    <div class="container">
        <div id="page1" class="page active">
            <div class="img-wrapper"><img src="https://files.catbox.moe/c06hs1.png" class="main-img"></div>
            <h1>Special Delivery!</h1>
            <p>ก๊อก ก๊อก ก๊อก... มีดอกไม้มาส่งคั้บ<br>ลองเปิดดูจดหมายข้างในสิ ✨</p>
            <button class="primary-btn" onclick="nextPage(2)">เปิดดูจดหมาย ❤️</button>
        </div>

        <div id="page2" class="page">
            <div class="img-wrapper"><img src="https://files.catbox.moe/nbixs1.jpg" class="main-img"></div>
            <h1>Dear You...</h1>
            <p>วันวาเลนไทน์นี้... <br>มีเค้กแซ่บๆมาเสริฟถึงที่ 🍰</p>
            <button class="primary-btn" onclick="nextPage(3)">อ่านต่อ.. 💌</button>
        </div>

        <div id="page3" class="page">
            <div class="img-wrapper"><img src="https://files.catbox.moe/xus5wq.jpg" class="main-img"></div>
            <h1>Be My Valentine?</h1>
            <p>อยากอยู่ด้วยกันแบบนี้ <br>ไปนานๆมั้ย 🧸</p>
            <div class="btn-group">
                <button class="primary-btn" onclick="nextPage(4); startHearts();">Yes! ❤️</button>
                <button id="noBtn" onclick="nextPage(5); startHearts()">No 😭</button>
            </div>
        </div>

        <div id="page4" class="page">
            <div class="img-wrapper"><img src="https://files.catbox.moe/5itgzz.png" class="main-img"></div>
            <h1 style="font-size: 1.5rem;">Promoted from talk to<br>to can't stop talking to 🥰</h1>
            <p>เย้!<br>น่ารักที่สุดในโลกเลยยย 🥰❤️</p>
            <button class="primary-btn" onclick="nextPage(1)">เริ่มต้นใหม่ 🔄</button>
        </div>

        <div id="page5" class="page">
            <div class="img-wrapper"><img src="https://files.catbox.moe/c6s99m.jpg" class="main-img"></div>
            <h1>End</h1>
            <p>จบบบบบบบ</p>
            <button class="primary-btn" onclick="nextPage(1)">เริ่มต้นใหม่ 🔄</button>
        </div>
    </div> <script>
        function nextPage(n) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById('page' + n).classList.add('active');
        }

        function startHearts() {
            for(let i=0; i<50; i++) {
                setTimeout(() => {
                    const h = document.createElement('div');
                    h.className = 'heart-particle';
                    h.innerHTML = ['❤️', '💖', '💝', '🌸'][Math.floor(Math.random() * 4)];
                    h.style.left = Math.random() * 100 + 'vw';
                    h.style.top = '100vh';
                    h.style.fontSize = (Math.random() * 20 + 20) + 'px';
                    document.body.appendChild(h);
                    setTimeout(() => h.remove(), 2500);
                }, i * 60);
            }
        }
    </script>
</body>
</html>
"""

# --- 3. แสดงผล ---
components.html(valentine_code, height=800, scrolling=False)