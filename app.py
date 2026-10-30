import streamlit as st
import pandas as pd
from data import df_alternatif, df_kriteria
from saw import normalisasi_saw, hitung_preferensi


# =====================================================
# KONFIGURASI APLIKASI
# =====================================================

st.set_page_config(
    page_title="KIP-K Decision Center",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# CUSTOM CSS - WHITE & CYAN EDITION
# =====================================================

st.markdown("""
<style>

/* =====================================================
    GLOBAL
===================================================== */

.stApp {
    background: linear-gradient(
        135deg,
        #F4FDFF 0%,
        #FFFFFF 50%,
        #E9FAFD 100%
    ) !important;
    color: #31596A;
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

[data-testid="stMain"] {
    background: transparent !important;
}

[data-testid="stMainBlockContainer"] {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

[data-testid="stHeader"] {
    background: rgba(255,255,255,0.95) !important;
}

/* =====================================================
    SIDEBAR
===================================================== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #08B8D0 0%,
        #06A9C5 50%,
        #078DAF 100%
    ) !important;
    border-right: 1px solid #079BB5;
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
    padding-top: 2rem;
}

[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
    font-weight: 900 !important;
    letter-spacing: 1px;
}

[data-testid="stSidebar"] p {
    color: #E8FCFF !important;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.3) !important;
}

[data-testid="stSidebar"] .stRadio label {
    color: #FFFFFF !important;
    font-weight: 600;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 9px;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 11px;
    padding: 11px 13px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.28);
    border-color: #FFFFFF;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
    background: #FFFFFF !important;
    border-color: #FFFFFF !important;
    box-shadow: 0 3px 12px rgba(0,70,90,0.15);
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) p {
    color: #0789A8 !important;
    font-weight: 800 !important;
}

.sidebar-method {
    background: #FFFFFF;
    border: 1px solid rgba(255,255,255,0.8);
    border-radius: 12px;
    padding: 14px;
    color: #0789A8;
    font-weight: 800;
    box-shadow: 0 4px 12px rgba(0,70,90,0.08);
}

.sidebar-method small {
    display: block;
    color: #64818D;
    font-size: 11px;
    font-weight: 500;
    margin-top: 5px;
}

/* =====================================================
    HEADING
===================================================== */

h1 {
    color: #0789A8 !important;
    font-weight: 900 !important;
    letter-spacing: -0.8px;
}

h2 {
    color: #087F9B !important;
    font-weight: 800 !important;
}

h3 {
    color: #087F9B !important;
    font-weight: 750 !important;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: #087F9B !important;
}

p {
    color: #52717D;
}

/* =====================================================
    METRIC CARDS
===================================================== */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #FFFFFF 0%,
        #F0FCFE 100%
    ) !important;
    border: 1px solid #A4E7EF;
    border-bottom: 4px solid #12B8D0;
    border-radius: 16px;
    padding: 20px 22px;
    box-shadow: 0 5px 16px rgba(0,160,190,0.08);
    transition: all 0.2s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,160,190,0.14);
}

[data-testid="stMetricLabel"] {
    color: #52717D !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #0789A8 !important;
    font-weight: 900 !important;
}

/* =====================================================
    DATAFRAME
===================================================== */

[data-testid="stDataFrame"] {
    background: #FFFFFF !important;
    border: 1px solid #A4E7EF !important;
    border-radius: 13px;
    overflow: hidden;
    box-shadow: 0 3px 12px rgba(0,150,180,0.06);
}

/* =====================================================
    TABS
===================================================== */

.stTabs [data-baseweb="tab-list"] {
    background: #E5F9FC !important;
    border: 1px solid #A4E7EF;
    border-radius: 12px;
    padding: 6px;
    gap: 6px;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 9px;
    color: #087F9B !important;
    font-weight: 700;
}

.stTabs [aria-selected="true"] {
    background: #FFFFFF !important;
    color: #079CB9 !important;
    box-shadow: 0 2px 7px rgba(0,120,150,0.12);
}

/* =====================================================
    BUTTON
===================================================== */

.stButton button,
.stDownloadButton button {
    background: linear-gradient(
        100deg,
        #08B4CD,
        #04A1C0
    ) !important;
    color: #FFFFFF !important;
    border: 1px solid #079DB9 !important;
    border-radius: 10px;
    padding: 10px 19px;
    font-weight: 800;
    transition: all 0.2s ease;
    box-shadow: 0 3px 10px rgba(0,150,180,0.16);
}

.stButton button:hover,
.stDownloadButton button:hover {
    background: linear-gradient(
        100deg,
        #078CA9,
        #067F9D
    ) !important;
    border-color: #067F9D !important;
    color: #FFFFFF !important;
    box-shadow: 0 5px 15px rgba(0,120,150,0.25);
}

/* =====================================================
    INPUT
===================================================== */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #FFFFFF !important;
    border: 1px solid #8DDFEA !important;
    border-radius: 9px;
    color: #31596A !important;
}

/* =====================================================
    ALERT
===================================================== */

[data-testid="stAlert"] {
    border-radius: 12px;
    border: 1px solid #91DFE9;
}

/* =====================================================
    DIVIDER
===================================================== */

hr {
    border-color: #D0EDF1 !important;
}

/* =====================================================
    CHART
===================================================== */

[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"],
[data-testid="stVegaLiteChartContainer"] {
    background: #FFFFFF !important;
    border: 1px solid #A4E7EF !important;
    border-radius: 14px;
    padding: 12px;
    box-shadow: 0 4px 13px rgba(0,150,180,0.06);
}

/* =====================================================
    CAPTION
===================================================== */

.stCaption {
    color: #64818D !important;
}

/* =====================================================
    DOWNLOAD
===================================================== */

.stDownloadButton {
    margin-top: 10px;
}

/* =====================================================
    SCROLLBAR
===================================================== */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #20C2D8;
    border-radius: 10px;
}

::-webkit-scrollbar-track {
    background: #EAFBFD;
}

/* =====================================================
    CUSTOM COMPONENTS
===================================================== */

.winner-card {
    background: linear-gradient(
        110deg,
        #08B8D0 0%,
        #13C8D9 55%,
        #66E0E8 100%
    );
    border: 1px solid #08B3CA;
    border-radius: 16px;
    padding: 25px 28px;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,160,190,0.15);
}

.winner-label {
    color: #E9FDFF !important;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 1.5px;
}

.winner-name {
    color: #FFFFFF !important;
    font-size: 25px;
    font-weight: 900;
    margin-top: 9px;
}

.winner-score {
    color: #E8FCFF !important;
    font-size: 14px;
    margin-top: 7px;
}

.winner-score b {
    color: #FFFFFF !important;
    font-size: 17px;
}

.info-card {
    background: linear-gradient(
        120deg,
        #FFFFFF,
        #EAFBFD
    );
    border: 1px solid #A4E7EF;
    border-left: 5px solid #08B5CF;
    border-radius: 13px;
    padding: 22px;
    line-height: 1.8;
    color: #416575 !important;
}

.formula-card {
    background: linear-gradient(
        140deg,
        #FFFFFF,
        #F0FCFE
    );
    border: 1px solid #A4E7EF;
    border-radius: 13px;
    padding: 22px;
    min-height: 150px;
    box-shadow: 0 3px 12px rgba(0,150,180,0.05);
}

.formula-title {
    color: #0789A8 !important;
    font-size: 18px;
    font-weight: 900;
}

.formula-description {
    color: #52717D !important;
    margin-top: 10px;
    line-height: 1.7;
}

.stApp,
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"] {
    color-scheme: light;
}

@media (max-width: 768px) {
    [data-testid="stMainBlockContainer"] {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .winner-name {
        font-size: 20px;
    }
    .formula-card {
        min-height: auto;
    }
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# DATA PERHITUNGAN
# =====================================================

normalisasi, ranking = hitung_preferensi()

total_alternatif = len(df_alternatif)
total_kriteria = len(df_kriteria)
total_bobot = df_kriteria["Bobot"].sum()


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:
    st.markdown("### 🎓 KIP-K CENTER")
    st.caption("DECISION SUPPORT SYSTEM")
    st.markdown("---")

    menu = st.radio(
        "Navigasi Utama",
        [
            "Dashboard",
            "Data Alternatif",
            "Data Kriteria",
            "Normalisasi SAW",
            "Hasil Perangkingan"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("**METODE ANALISIS**")
    
    st.markdown(
        """<div class="sidebar-method">
Simple Additive Weighting
<small>Metode pengambilan keputusan</small>
</div>""",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption("© 2026 KIP-K Decision Center")
    st.caption("WHITE & CYAN EDITION")


# =====================================================
# DASHBOARD
# =====================================================

if menu == "Dashboard":
    st.title("Overview Dashboard")
    st.caption(
        "Pusat informasi dan hasil analisis seleksi "
        "calon penerima Beasiswa KIP-K."
    )

    # STATISTIK
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Kandidat",
            total_alternatif,
            help="Jumlah seluruh calon penerima beasiswa."
        )

    with col2:
        st.metric(
            "Total Kriteria",
            total_kriteria,
            help="Jumlah parameter penilaian."
        )

    with col3:
        st.metric(
            "Total Bobot",
            f"{total_bobot:.2f}",
            help="Akumulasi seluruh bobot kriteria."
        )

    st.divider()

    # KANDIDAT TERBAIK
    if not ranking.empty:
        terbaik = ranking.iloc[0]

        st.markdown(
            f"""<div class="winner-card">
<div class="winner-label">🏆 KANDIDAT TERBAIK</div>
<div class="winner-name">{terbaik['Alternatif']}</div>
<div class="winner-score">Nilai Preferensi: <b>{terbaik['Nilai Preferensi']:.3f}</b> &nbsp; | &nbsp; Peringkat 1</div>
</div>""",
            unsafe_allow_html=True
        )

        col_chart, col_table = st.columns([1.3, 1])

        with col_chart:
            st.subheader("Visualisasi Hasil")
            chart_data = ranking.set_index("Alternatif")[["Nilai Preferensi"]]
            st.bar_chart(
                chart_data,
                height=320,
                color="#08B8D0"
            )

        with col_table:
            st.subheader("Top 5 Kandidat")
            st.dataframe(
                ranking.head(5).style.format(
                    {"Nilai Preferensi": "{:.3f}"}
                ),
                use_container_width=True,
                hide_index=True,
                height=320
            )
    else:
        st.info("Belum terdapat data alternatif untuk ditampilkan.")

    st.divider()

    # TENTANG SISTEM
    st.subheader("Tentang Sistem")
    st.markdown(
        """<div class="info-card">
Aplikasi <b style="color:#0789A8;">KIP-K Decision Center</b> merupakan sistem pendukung keputusan yang menggunakan metode <b>Simple Additive Weighting (SAW)</b> untuk membantu proses penilaian dan pemeringkatan calon penerima beasiswa KIP-K berdasarkan kriteria serta bobot yang telah ditentukan.
</div>""",
        unsafe_allow_html=True
    )


# =====================================================
# DATA ALTERNATIF
# =====================================================

elif menu == "Data Alternatif":
    st.title("Data Kandidat")
    st.caption(
        "Daftar alternatif atau calon penerima beasiswa "
        "yang menjadi objek penilaian."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Jumlah Kandidat", total_alternatif)

    with col2:
        st.metric("Jumlah Parameter", total_kriteria)

    st.write("")
    st.subheader("Tabel Data Alternatif")
    st.dataframe(
        df_alternatif,
        use_container_width=True,
        hide_index=True
    )
    st.caption(
        "Data alternatif digunakan sebagai dasar "
        "pembentukan matriks keputusan SAW."
    )


# =====================================================
# DATA KRITERIA
# =====================================================

elif menu == "Data Kriteria":
    st.title("Parameter Penilaian")
    st.caption(
        "Informasi kriteria, bobot kepentingan, "
        "dan jenis perhitungan yang digunakan dalam seleksi."
    )

    st.subheader("Tabel Kriteria")
    st.dataframe(
        df_kriteria,
        use_container_width=True,
        hide_index=True
    )

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Bobot", f"{total_bobot:.2f}")

    with col2:
        status = (
            "Valid"
            if abs(total_bobot - 1.0) < 0.000001
            else "Perlu diperiksa"
        )
        st.metric("Status Bobot", status)

    if abs(total_bobot - 1.0) < 0.000001:
        st.success("Total bobot kriteria sudah berjumlah 1.00.")
    else:
        st.error("Total bobot kriteria harus berjumlah 1.00.")


# =====================================================
# NORMALISASI SAW
# =====================================================

elif menu == "Normalisasi SAW":
    st.title("Proses Normalisasi")
    st.caption(
        "Tahapan transformasi matriks keputusan menjadi "
        "nilai normalisasi berdasarkan jenis kriteria."
    )

    tab1, tab2 = st.tabs(["Matriks Keputusan", "Hasil Normalisasi"])

    # MATRIKS KEPUTUSAN
    with tab1:
        st.subheader("Matriks Keputusan Awal")
        st.dataframe(
            df_alternatif.set_index("Alternatif"),
            use_container_width=True
        )

    # HASIL NORMALISASI
    with tab2:
        st.subheader("Matriks Normalisasi")
        st.dataframe(
            normalisasi.round(3),
            use_container_width=True
        )

        st.download_button(
            label="⬇ Download Normalisasi CSV",
            data=normalisasi.to_csv().encode("utf-8"),
            file_name="normalisasi_saw.csv",
            mime="text/csv"
        )

    st.divider()

    # RUMUS NORMALISASI
    st.subheader("Rumus Normalisasi")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """<div class="formula-card">
<div class="formula-title">BENEFIT</div>
<div class="formula-description">
Nilai alternatif dibagi dengan nilai maksimum pada kriteria.<br><br>
Semakin besar nilai yang diperoleh, semakin baik alternatif tersebut.
</div>
</div>""",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """<div class="formula-card">
<div class="formula-title">COST</div>
<div class="formula-description">
Nilai minimum pada kriteria dibagi dengan nilai alternatif.<br><br>
Semakin kecil nilai awal, semakin baik alternatif tersebut.
</div>
</div>""",
            unsafe_allow_html=True
        )


# =====================================================
# HASIL PERANGKINGAN
# =====================================================

elif menu == "Hasil Perangkingan":
    st.title("Hasil Seleksi Beasiswa")
    st.caption(
        "Pemeringkatan alternatif berdasarkan nilai "
        "preferensi hasil perhitungan metode SAW."
    )

    if ranking.empty:
        st.warning("Belum terdapat data alternatif.")
    else:
        terbaik = ranking.iloc[0]

        # KARTU HASIL TERATAS
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Kandidat Peringkat Pertama", terbaik["Alternatif"])

        with col2:
            st.metric("Nilai Preferensi Tertinggi", f"{terbaik['Nilai Preferensi']:.3f}")

        st.write("")

        # TABEL PERANGKINGAN
        st.subheader("Tabel Hasil Perangkingan")
        st.dataframe(
            ranking.style.format({"Nilai Preferensi": "{:.3f}"}),
            use_container_width=True,
            hide_index=True
        )

        st.write("")

        # GRAFIK PERBANDINGAN
        st.subheader("Grafik Perbandingan Nilai")
        chart_ranking = ranking.set_index("Alternatif")["Nilai Preferensi"]

        st.bar_chart(
            chart_ranking,
            height=350,
            color="#08B8D0"
        )

        # DOWNLOAD HASIL
        st.download_button(
            label="⬇ Unduh Hasil Perangkingan",
            data=ranking.to_csv(index=False).encode("utf-8"),
            file_name="hasil_perangkingan_kipk.csv",
            mime="text/csv"
        )