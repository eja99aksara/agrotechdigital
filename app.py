import streamlit as st

# =================================================================
# CONFIGURASI HALAMAN & CSS GLOBAL
# =================================================================
st.set_page_config(page_title="Tani Pintar - Agrotech Digital", page_icon="🌿", layout="centered")

st.markdown("""<style>
/* Menghilangkan padding bawaan Streamlit agar tampilan penuh */
.block-container { padding-top: 2rem !important; padding-bottom: 0rem !important; }

/* Style Kustom untuk Tabel di Frame C agar serasi */
table { width: 100% !important; border-collapse: collapse !important; font-family: sans-serif !important; }
th { background-color: rgba(45, 90, 39, 0.85) !important; color: white !important; padding: 10px !important; text-align: left !important; }
td { padding: 10px !important; border-bottom: 1px solid rgba(0,0,0,0.1) !important; font-size: 0.95rem !important; background-color: rgba(255,255,255,0.6) !important; }

/* Transparansi Wadah Tab Streamlit */
div[data-testid="stTabs"] {
    background-color: rgba(255, 255, 255, 0.6) !important; 
    padding: 15px; 
    border-radius: 12px;
    backdrop-filter: blur(8px);
}
div[role="tabpanel"] {
    background-color: transparent !important;
}
</style>""", unsafe_allow_html=True)

# 🔗 CONFIGURASI LINK UTAMA (Silakan ubah sesuai kebutuhan Anda)
nomor_admin_wa = "https://wa.me/628xxxxxxxxxx"
link_youtube_demo = "https://youtube.com" 
link_toko_online = "https://tokopedia.com" 

# =================================================================
# --- FRAME A: HERO SECTION (Menggunakan Gambar Sawah Data)      ---
# =================================================================
# Memanggil gambar sawah terasering digital dari repositori Anda
hero_html = f"""<div style="background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://raw.githubusercontent.com/eja99aksara/tani_pirntar/main/1781366738720.png'); background-size: cover; background-position: center; background-repeat: no-repeat; min-height: 200px; padding: 35px 20px; border-radius: 12px; color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 30px; font-family: sans-serif;">
<div style="flex: 1; min-width: 120px; font-size: 1.5rem; font-weight: bold; display: flex; align-items: center; gap: 8px; text-shadow: 1px 1px 4px rgba(0,0,0,0.6);">🌿 TaniPintar</div>
<div style="flex: 3; min-width: 250px; text-align: center;">
<h1 style="color: white; margin: 0; font-size: 1.8rem; font-weight: 800; line-height: 1.3; text-shadow: 2px 2px 6px rgba(0,0,0,0.7); border: none; background: none; padding: 0;">Ubah Kebun Anda<br>Menjadi Cerdas</h1>
</div>
<div style="flex: 1; min-width: 180px; text-align: right;">
<a href="{nomor_admin_wa}" target="_blank" style="background-color: white; color: #2d5a27; padding: 12px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 0.9rem; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">Konsultasi Gratis (WA)</a>
</div>
</div>"""

# CRITICAL: Baris ini wajib menggunakan unsafe_allow_html=True agar tidak bocor sebagai teks biasa
st.markdown(hero_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME B: SOLUSI PERTANIAN (Menggunakan Infografis)         ---
# =================================================================
st.markdown("## **Satu sistem pintar untuk semua jenis pertanian.**")

# Memasukkan kartu infografis pertanian indoor dan outdoor
frame_b_html = """<div style="background-color: #f7f9f6; padding: 15px; border-radius: 12px; margin-bottom: 40px; font-family: sans-serif;">
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; min-width: 280px; background-color: rgba(255, 255, 255, 0.95); padding: 20px; border-radius: 12px; border-top: 5px solid #2d5a27; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <img src="https://raw.githubusercontent.com/eja99aksara/tani_pirntar/main/1781366663615.png" style="width: 100%; border-radius: 8px; margin-bottom: 15px;" alt="Infografis Indoor">
            <h3 style="color: #2d5a27; margin: 0 0 10px 0; font-size: 1.25rem; font-weight: bold;">Pertanian Indoor & Hidroponik</h3>
            <ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
                <li style="margin-bottom: 6px;"><b>Otomatisasi Nutrisi & pH:</b> Sensor pintar menjaga takaran pupuk selalu pas otomatis.</li>
                <li style="margin-bottom: 6px;"><b>Kontrol Iklim Mikro:</b> Atur lampu grow led dan kelembapan via HP.</li>
                <li><b>Notifikasi Air Kering:</b> Alarm instan WhatsApp jika air tandon menipis.</li>
            </ul>
        </div>
        <div style="flex: 1; min-width: 280px; background-color: rgba(255, 255, 255, 0.95); padding: 20px; border-radius: 12px; border-top: 5px solid #2e6f9e; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <img src="https://raw.githubusercontent.com/eja99aksara/tani_pirntar/main/1781366599354.png" style="width: 100%; border-radius: 8px; margin-bottom: 15px;" alt="Infografis Outdoor">
            <h3 style="color: #2e6f9e; margin: 0 0 10px 0; font-size: 1.25rem; font-weight: bold;">Lahan Terbuka (Outdoor)</h3>
            <ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
                <li style="margin-bottom: 6px;"><b>Smart Drip Irrigation:</b> Penyiraman otomatis aktif saat tanah mendeteksi kekeringan.</li>
                <li style="margin-bottom: 6px;"><b>Prediksi Cuaca Lokal:</b> Sistem otomatis menunda penyiraman jika akan hujan.</li>
                <li><b>Deteksi Kesehatan Tanah:</b> Analisis kandungan NPK tanah secara real-time.</li>
            </ul>
        </div>
    </div>
</div>"""

st.markdown(frame_b_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME C: PRODUK & HARGA (Menggunakan Background IoT Sensor)---
# =================================================================
st.markdown("""<div style="background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://raw.githubusercontent.com/eja99aksara/tani_pirntar/main/smart-farming-soil-sensor-digital-monitoring-greenhouse-modern-scene-featuring-iot-emitting-data-visualizations-to-445872804.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat; padding: 40px 25px; border-radius: 12px; margin-bottom: 15px; font-family: sans-serif;">
<h2 style="margin-top: 0; color: white; font-weight: bold; text-shadow: 2px 2px 5px rgba(0,0,0,0.8); border: none; background: none; padding: 0;">Pilih Paket Sesuai Kebutuhan Anda</h2>
<p style="color: #fff; margin-bottom: 0; font-weight: 500; text-shadow: 1px 1px 4px rgba(0,0,0,0.7);">Mulai digitalisasi kebun Anda hari ini demi hasil panen yang berlipat ganda.</p>
</div>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🛒 Beli Langsung", "💬 Tanya Dulu"])

with tab1:
    st.markdown("### **Daftar Paket Tani Pintar**")
    tabel_harga = """
| Nama Paket | Target Pengguna | Fitur Utama |
| :--- | :--- | :--- |
| **Starter 🌱** | Hobi / Rumahan | 2 Sensor Kelembapan + Kontrol Pompa Air Otomatis via HP |
| **Pro 📈** | Kebun Komersil | Paket Starter + Sensor pH, Nutrisi Otomatis + Grafik Analisis |
| **Enterprise 🚜** | Industri / Lahan Luas | Kustomisasi Penuh + Sensor NPK Tanah + Integrasi Cuaca |
"""
    st.markdown(tabel_harga)
    st.write("") 
    
    kolom_kiri, kolom_kanan = st.columns(2)
    with kolom_kiri:
        st.link_button("🛍️ Toko Online Official", link_toko_online, use_container_width=True)
    with kolom_kanan:
        st.link_button("📺 Lihat Demo Alat (YouTube)", link_youtube_demo, use_container_width=True)
        
    st.link_button("🟢 Hubungi Admin untuk Pemesanan Paket (WA)", nomor_admin_wa, use_container_width=True)

with tab2:
    st.markdown("### **Formulir Konsultasi Gratis**")
    with st.form(key="form_konsultasi"):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("Nomor WhatsApp / Email")
        luas_lahan = st.selectbox("Luas Lahan Pertanian", ["< 100 m² (Rumahan)", "100 - 1000 m²", "> 1000 m² (Skala Industri)"])
        pesan = st.text_area("Ceritakan kendala atau kebutuhan kebun Anda")
        submit_button = st.form_submit_button(label="Kirim Pengajuan")
        if submit_button:
            if nama and kontak:
                st.success(f"Terima kasih {nama}! Data berhasil dikirim.")
            else:
                st.warning("Mohon isi Nama dan Kontak Anda.")


# =================================================================
# --- FRAME D: SOCIAL PROOF (Menggunakan Petani Drone & VR)     ---
# =================================================================
st.write("")
st.markdown("## **Social Proof & Penutup**")

frame_d_html = """<div style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://raw.githubusercontent.com/eja99aksara/tani_pirntar/main/farmer-using-vr-drones-smart-farming.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat; padding: 40px 15px; border-radius: 12px; font-family: sans-serif; margin-bottom: 30px;">
<div style="background-color: rgba(255,255,255,0.92); padding: 25px; border-radius: 12px; border-left: 5px solid #2d5a27; box-shadow: 0 4px 15px rgba(0,0,0,0.15); backdrop-filter: blur(4px);">
<p style="font-style: italic; color: #111; font-size: 1rem; line-height: 1.6; margin: 0 0 15px 0;">
"Implementasi teknologi IoT dan otomatisasi pada kebun terbukti meningkatkan efisiensi penggunaan pupuk hingga 30% dan mempercepat masa panen secara stabil. Tani Pintar memberikan solusi nyata."
</p>
<b style="color: #2d5a27; font-size: 0.95rem;">Dr. Ir. Hermawan, M.Sc.</b><br>
<span style="color: #444; font-size: 0.85rem;">Pakar Agronomi & Teknologi Pertanian</span>
</div>
</div>"""

st.markdown(frame_d_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME E: PUSTAKA & DOKUMENTASI (Menggunakan Laboratorium Hidroponik) ---
# =================================================================
st.markdown("## **Pelajari Lebih Lanjut Sistem Tani Pintar**")

st.markdown("""<img src="https://raw.githubusercontent.com/eja99aksara/tani_pirntar/main/1781370872828.png" style="width: 100%; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" alt="Dokumentasi Lab">""", unsafe_allow_html=True)

tab_pustaka, tab_berita = st.tabs(["📚 Download Pustaka", "📰 Berita Tani Pintar"])

with tab_pustaka:
    st.markdown("""<div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 12px; text-align: center; font-family: sans-serif; border: 1px solid rgba(0,0,0,0.05);">
<h4 style="margin: 0 0 10px 0; color: #2d5a27;">Katalog Produk & Spesifikasi Hardware IoT</h4>
<p style="margin: 0 0 15px 0; color: #232323; font-size: 0.9rem;">Unduh brosur digital dan materi presentasi lengkap mengenai skema alat kami.</p>
<a href="https://google.com" target="_blank" style="background-color: #2d5a27; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; display: inline-block;">📥 Download Brosur Alat (PDF)</a>
</div>""", unsafe_allow_html=True)

with tab_berita:
    st.markdown("### **Aktivitas Lapangan Terbaru**")
    st.markdown("""<div style="font-family: sans-serif; background-color: rgba(255,255,255,0.5); padding: 15px; border-radius: 12px;">
<span style="color: #2d5a27; font-size: 0.8rem; font-weight: bold;">📅 JUNI 2026</span>
<h4 style="margin: 5px 0; color: #111;">Modernisasi Greenhouse Hidroponik Selada</h4>
<p style="margin: 5px 0; color: #333; font-size: 0.9rem;">Pemasangan pompa nutrisi dosing otomatis berbasis pembacaan pH & EC secara real-time di area Lembang.</p>
</div>""", unsafe_allow_html=True)


# =================================================================
# --- FOOTER HALAMAN
# =================================================================
st.write("")
st.markdown("""<div style="background-color: #2d5a27; color: white; padding: 25px 20px; border-radius: 12px; text-align: center; font-size: 0.85rem; line-height: 1.8; font-family: sans-serif; margin-top: 30px;">
<b style="font-size: 1rem;">PT Agrotech Digital Indonesia</b><br>
📍 Jl. Kawasan Industri Pertanian Modern No. 45, Indonesia<br>
📞 WhatsApp: +62 8xx-xxxx-xxxx | ✉️ Email: info@tanipintar.com<br>
<hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 15px 0;">
© 2026 Tani Pintar. Hak Cipta Dilindungi Undang-Undang.
</div>""", unsafe_allow_html=True)
