import streamlit as st

# =================================================================
# CONF IGURASI HALAMAN & CSS GLOBAL
# =================================================================
st.set_page_config(page_title="Tani Pintar - Agrotech Digital", page_icon="🌿", layout="centered")

st.markdown("""<style>
/* Menghilangkan padding bawaan Streamlit agar layout HTML kita mepet rapi */
.block-container { padding-top: 2rem !important; padding-bottom: 0rem !important; }
/* Style Kustom untuk Tabel di Frame C */
table { width: 100% !important; border-collapse: collapse !important; font-family: sans-serif !important; }
th { background-color: #2d5a27 !important; color: white !important; padding: 10px !important; text-align: left !important; }
td { padding: 10px !important; border-bottom: 1px solid #ddd !important; font-size: 0.95rem !important; }
</style>""", unsafe_allow_html=True)


# =================================================================
# --- FRAME A: HERO SECTION (Latar Hijau Tua)                    ---
# =================================================================
# GANTI LINK WA DI BAWAH INI SESUAI NOMOR ANDA
link_wa = "https://wa.me/628xxxxxxxxxx" 

hero_html = f"""<div style="background-color: #2d5a27; padding: 25px; border-radius: 12px; color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 30px; font-family: sans-serif;">
<div style="flex: 1; min-width: 120px; font-size: 1.5rem; font-weight: bold; display: flex; align-items: center; gap: 8px;">🌿 TaniPintar</div>
<div style="flex: 2; min-width: 260px; text-align: center;">
<h1 style="color: white; margin: 0; font-size: 1.8rem; font-weight: 800; line-height: 1.3; border: none; background: none; padding: 0;">Ubah Kebun Anda<br>Menjadi Cerdas</h1>
</div>
<div style="flex: 1; min-width: 160px; text-align: right;">
<a href="{link_wa}" target="_blank" style="background-color: white; color: #2d5a27; padding: 10px 18px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 0.9rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">Konsultasi Gratis (WA)</a>
</div>
</div>"""

st.markdown(hero_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME B: SOLUSI PERTANIAN (Latar Putih Bersih)             ---
# =================================================================
st.markdown("### **Satu sistem pintar untuk semua jenis pertanian.**")

frame_b_html = """<div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px; margin-top: 15px; margin-bottom: 40px; font-family: sans-serif;">
<div style="flex: 1; min-width: 280px; background-color: #f0f7f4; padding: 25px; border-radius: 12px; border-left: 5px solid #2d5a27; box-shadow: 0 4px 6px rgba(0,0,0,0.03);">
<div style="font-size: 2rem; margin-bottom: 10px;">🏢</div>
<h3 style="color: #2d5a27; margin: 0 0 15px 0; font-size: 1.25rem; font-weight: bold;">Pertanian Indoor & Hidroponik</h3>
<ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
<li style="margin-bottom: 8px;"><b>Otomatisasi Nutrisi & pH:</b> Sensor menjaga takaran pupuk selalu pas otomatis.</li>
<li style="margin-bottom: 8px;"><b>Kontrol Iklim Mikro:</b> Atur lampu grow led dan kelembapan via HP.</li>
<li><b>Notifikasi Air Kering:</b> Alarm instan WhatsApp jika air tandon menipis.</li>
</ul>
</div>
<div style="flex: 1; min-width: 280px; background-color: #edf4f9; padding: 25px; border-radius: 12px; border-left: 5px solid #2e6f9e; box-shadow: 0 4px 6px rgba(0,0,0,0.03);">
<div style="font-size: 2rem; margin-bottom: 10px;">🚜</div>
<h3 style="color: #2e6f9e; margin: 0 0 15px 0; font-size: 1.25rem; font-weight: bold;">Lahan Terbuka (Outdoor)</h3>
<ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
<li style="margin-bottom: 8px;"><b>Smart Drip Irrigation:</b> Penyiraman otomatis aktif hanya saat tanah kering.</li>
<li style="margin-bottom: 8px;"><b>Prediksi Cuaca Lokal:</b> Sistem menunda siram otomatis jika akan hujan.</li>
<li><b>Deteksi Kesehatan Tanah:</b> Pantau kadar NPK tanah real-time dari dasbor.</li>
</ul>
</div>
</div>"""

st.markdown(frame_b_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME C: PRODUK & HARGA (Dengan Kontak Admin Terintegrasi)---
# =================================================================
# SILAKAN GANTI NOMOR DI BAWAH INI DENGAN NOMOR WHATSAPP ADMIN ANDA
# Format: Gunakan kode negara tanpa tanda +, contoh: 628123456789
nomor_admin_wa = "https://wa.me/628xxxxxxxxxx"
link_youtube_demo = "https://youtube.com" 

# Trik kontainer abu-abu untuk memisahkan section harga
st.markdown("""<div style="background-color: #f8f9fa; padding: 25px; border-radius: 12px; margin-bottom: 40px; font-family: sans-serif;">
<h2 style="margin-top: 0; color: #333; font-weight: bold;">Pilih Paket Sesuai Kebutuhan Anda</h2>
<p style="color: #666; margin-bottom: 20px;">Mulai digitalisasi kebun Anda hari ini demi hasil panen yang berlipat ganda.</p>
</div>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🛒 Beli Langsung", "💬 Tanya Dulu"])

with tab1:
    st.markdown("### **Daftar Paket Tani Pintar**")
    tabel_harga = """
| Nama Paket | Target Pengguna | Fitur Utama |
| :--- | :--- | :--- |
| **Starter 🌱** | Hobi / Rumahan | 2 Sensor Kelembapan + Kontrol Pompa Air Otomatis via HP |
| **Pro 📈** | Kebun Komersil | Paket Starter + Sensor pH, Nutrisi Otomatis + Grafik Analisis |
| **Enterprise 🚜** | Industri / Lahan Luas | Kustomisasi Penuh + Sensor NPK Tanah + Integrasi Cuaca + Garansi 2 Tahun |
"""
    st.markdown(tabel_harga)
    st.write("") 
    
    # Tombol 1: Hubungi Admin untuk pesan
    st.link_button("🟢 Hubungi Admin untuk Pemesanan (WA)", nomor_admin_wa, use_container_width=True)
    # Tombol 2: Lihat demo
    st.link_button("📺 Lihat Demo Alat (YouTube)", link_youtube_demo, use_container_width=True)

with tab2:
    st.markdown("### **Formulir Konsultasi Gratis**")
    st.write("Silakan isi data di bawah ini, tim ahli kami akan segera menghubungi Anda.")
    
    # Membuat formulir input interaktif
    with st.form(key="form_konsultasi"):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("Nomor WhatsApp / Email")
        luas_lahan = st.selectbox("Luas Lahan Pertanian", ["< 100 m² (Rumahan)", "100 - 1000 m²", "> 1000 m² (Skala Industri)"])
        pesan = st.text_area("Ceritakan kendala atau kebutuhan kebun Anda")
        
        submit_button = st.form_submit_button(label="Kirim Pengajuan Konsultasi")
        
        if submit_button:
            if nama and kontak:
                st.success(f"Terima kasih {nama}! Data berhasil dikirim. Tim kami akan menghubungi Anda di {kontak}.")
            else:
                st.warning("Mohon isi Nama dan Kontak Anda terlebih dahulu.")
                
    st.write("")
    st.markdown("---")
    # Alternatif kontak admin cepat di bawah form
    st.markdown("<p style='text-align: center; color: #666;'>Atau ingin respon lebih cepat?</p>", unsafe_allow_html=True)
    st.link_button("💬 Chat Admin Langsung via WhatsApp", nomor_admin_wa, use_container_width=True)

# =================================================================
# --- FRAME D: SOCIAL PROOF & PENUTUP                            ---
# =================================================================
st.write("")
st.markdown("## **Didukung oleh Para Pakar Pertanian**")

frame_d_html = """<div style="font-family: sans-serif; margin-top: 15px;">
<div style="background-color: #f9f9f9; padding: 25px; border-radius: 12px; border-left: 5px solid #2d5a27; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<p style="font-style: italic; color: #555; font-size: 1rem; line-height: 1.6; margin: 0 0 15px 0;">
"Implementasi teknologi IoT dan otomatisasi pada kebun terbukti meningkatkan efisiensi penggunaan pupuk hingga 30% dan mempercepat masa panen secara stabil. Tani Pintar memberikan solusi nyata yang mudah dipahami oleh petani kita."
</p>
<b style="color: #2d5a27; font-size: 0.95rem;">Dr. Ir. Hermawan, M.Sc.</b><br>
<span style="color: #777; font-size: 0.85rem;">Pakar Agronomi & Teknologi Pertanian</span>
</div>

<div style="background-color: #f4f6f4; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 40px;">
<h4 style="margin: 0 0 10px 0; color: #2d5a27;">Pelajari Lebih Lanjut Sistem Tani Pintar</h4>
<p style="margin: 0 0 15px 0; color: #666; font-size: 0.9rem;">Unduh brosur digital dan materi presentasi lengkap mengenai skema alat kami.</p>
<a href="https://google.com" target="_blank" style="background-color: #2d5a27; color: white; padding: 8px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; display: inline-block;">📥 Download Brosur Alat (PDF)</a>
</div>

<div style="background-color: #2d5a27; color: white; padding: 25px 20px; border-radius: 12px 12px 0 0; text-align: center; font-size: 0.85rem; line-height: 1.8; margin-bottom: 0px;">
<b style="font-size: 1rem;">PT Agrotech Digital Indonesia</b><br>
📍 Jl. Kawasan Industri Pertanian Modern No. 45, Indonesia<br>
📞 WhatsApp: +62 8xx-xxxx-xxxx | ✉️ Email: info@tanipintar.com<br>
<hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 15px 0;">
© 2026 Tani Pintar. Hak Cipta Dilindungi Undang-Undang.
</div>
</div>"""

st.markdown(frame_d_html, unsafe_allow_html=True)
