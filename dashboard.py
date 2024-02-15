import os

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from streamlit_option_menu import option_menu


@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

kategori_info = load_data('https://raw.githubusercontent.com/wildanmjjhd29/Dashboard-E-Commerce/main/kategori_info.csv') 

def analisis_wildan(kategori_info):
    
    # Mengubah kolom 'shipping_limit_date' menjadi datetime
    kategori_info['shipping_limit_date'] = pd.to_datetime(kategori_info['shipping_limit_date'])

    # Menghitung jumlah kategori
    count_kategori = kategori_info['product_category'].value_counts()

    # Mencari 5 kategori teratas
    kategori_head = count_kategori.head(5)

    # Mencari 5 kategori terbawah
    kategori_tail = count_kategori.tail(5)

    # Filter data untuk kategori paling banyak terjual
    kategori_terlaris = [kategori_info[kategori_info['product_category'] == kategori] for kategori in kategori_head.index]

    # Buat kolom 'year' untuk menyimpan tahun menggunakan .loc[]
    for kategori in kategori_terlaris:
        kategori.loc[:, 'year'] = kategori['shipping_limit_date'].dt.year

    # trend penjualan top 5 kategori
    sales_trend = [kategori.groupby('year')['jumlah_terjual'].count() for kategori in kategori_terlaris]

    # Gabungkan semua data kategori terlaris ke dalam satu DataFrame
    all_categories = pd.concat(kategori_terlaris)

    # Hitung jumlah penjualan per kategori dan tahun
    sales_trend = all_categories.groupby(['product_category', 'year'])['jumlah_terjual'].count().reset_index()

    # Ubah data menjadi format pivot table
    pivot_table = sales_trend.pivot_table(index='product_category', columns='year', values='jumlah_terjual', fill_value=0)

    st.caption("**1012292 - Wildan Mujjahid Robbani**")
    # ------------------------------------------------------------------------------------------------------------------------------------
    st.subheader("Informasi Yang Ingin Di Sampaikan")
    st.markdown("- **Analisis Terhadap Penjualan Kategori Produk**")
    st.markdown("- **Analisis Terhadap Trend Penjualan 5 Kategori Dengan Penjualan Paling Tinggi**")
    st.markdown("- **Menampilkan Grafik Prediksi Penjualan**")
    
    with st.expander("Tujuan Analisis Infomasi Tersebut"):
        st.markdown("**Analisis Terhadap Penjualan Kategori Produk**")
        st.markdown("Mengidentifikasi 5 kategori produk dengan penjualan tertinggi membantu perusahaan atau pelaku bisnis untuk fokus pada produk-produk yang paling sukses. Ini dapat membimbing keputusan strategis terkait persediaan, pemasaran, dan pengembangan produk.")
        st.markdown("**Analisis Terhadap Trend Penjualan 5 Kategori Dengan Penjualan Paling Tinggi**")
        st.markdown("Dengan mengetahui tren penjualan untuk kategori teratas, perusahaan dapat mengoptimalkan rantai pasokan mereka. Ini mencakup manajemen persediaan, produksi, dan distribusi untuk memenuhi permintaan yang terus meningkat.")
        st.markdown("Mengetahui apakah penjualan dalam kategori tertentu menunjukkan peningkatan, penurunan, atau stabil dapat membimbing keputusan strategis. Misalnya, jika ada penurunan, perusahaan mungkin perlu mengkaji ulang strategi pemasaran atau meningkatkan inovasi produk.")
        st.markdown("**Menampilkan Grafik Prediksi Penjualan**")
        st.markdown("Dengan melibatkan analisis tren penjualan dalam beberapa tahun terakhir, perusahaan dapat menggunakan model prediktif untuk meramalkan penjualan di masa mendatang. Hal ini dapat membantu dalam perencanaan bisnis jangka panjang dan pengambilan keputusan investasi.")
    st.markdown('---')
    #-------------------------------------------------------------------------------------------------------------------------------------
    st.subheader("Grafik Perkembangan Penjualan Per Kategori")
    #  Colom tabel
    col1,col2 = st.columns(2)
    with col1:
        st.write("- **Tabel 5 Kategori Teratas**")
        st.dataframe(kategori_head)
    with col2:
        st.write("- **Tabel 5 Kategori Terbawah**")
        st.dataframe(kategori_tail)
    st.empty()
    # Visualisasi 1 (Bar Chart)
    fig1 = px.bar(x=kategori_head.index, y=kategori_head.values, color=kategori_head.index,
                  title='Grafik 5 Kategori Penjualan Tertinggi',
                  width=400
                )

    # Visualisasi 2 (Bar Chart)
    fig2 = px.bar(x=kategori_tail.index, y=kategori_tail.values, color=kategori_tail.index,
                  title='Grafik 5 Kategori Penjualan Terendah',
                  width=400
                )
 
    # Menghilangkan legend & labl x,y
    fig1.update_traces(showlegend=False)
    fig1.update_xaxes(title_text="")
    fig1.update_yaxes(title_text="")
    fig2.update_traces(showlegend=False)
    fig2.update_xaxes(title_text="")
    fig2.update_yaxes(title_text="")

    col3,col4 = st.columns(2)
    with col3:
        st.plotly_chart(fig1)
    with col4:
        st.plotly_chart(fig2)

    with st.expander("Penjelasana Mengenai Tingkat Penjualan Kategori Produk"):
        st.write('Analisis penjualan kategori produk menyoroti perbedaan yang signifikan antara kategori dengan penjualan tertinggi dan terendah. Kategori seperti perabotan rumah tangga, produk kesehatan & kecantikan, dan perlengkapan olahraga menunjukkan minat tinggi dari pelanggan dan mendominasi pasar.')
        st.write('Sebaliknya, kategori seperti seni & kerajinan, hiburan seperti CD & DVD, dan produk keamanan & layanan menunjukkan performa penjualan yang rendah. Diperlukan strategi perbaikan, termasuk kampanye pemasaran yang lebih agresif, riset pasar untuk memahami kebutuhan pelanggan, dan diversifikasi produk. Peninjauan kembali stok produk juga perlu dilakukan.')
        st.write('Dengan meningkatkan strategi penjualan pada kategori yang rendah, perusahaan dapat memperkuat daya saingnya, meningkatkan pendapatan, dan memperkuat posisinya di pasar. Kesimpulannya, fokus pada pertumbuhan kategori populer dan transformasi strategi pada kategori rendah dapat membantu perusahaan mencapai hasil yang lebih baik.')
    st.markdown('---')
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    st.subheader('Trend Penjualan 5 Kategori Produk Teratas')
    # Visualisasi 3 (Line Chart)
    st.write("- **Tabel Trend Penjualan kategori Produk**")
    st.dataframe(pivot_table)
    
    fig3 = px.line()
    colors = ['blue', 'skyblue', 'red', 'pink', '#15F5BA']
    labels = ['Bed & Bath', 'Health & Beauty', 'Sports & Leisure', 'Furniture & Decor', 'Computers & Accessories']

    for i, trend in enumerate(sales_trend['product_category'].unique()):
        temp = sales_trend[sales_trend['product_category'] == trend]
        fig3.add_scatter(x=temp['year'], y=temp['jumlah_terjual'], mode='lines+markers', name=labels[i], line=dict(color=colors[i]))

    fig3.update_layout(title='Trend Penjualan Top 5 Kategori Produk Terlaris', xaxis_title='Tahun', yaxis_title='Jumlah Penjualan')
    st.plotly_chart(fig3)
    with st.expander("Penjelasan Mengenai Trend Penjualan 5 Kategori Teratas"):
        st.write("Dalam periode 2016 hingga 2018, tren penjualan lima kategori produk menunjukkan dinamika yang beragam. Kategori Bed & Bath menikmati pertumbuhan yang stabil, sementara Computers & Accessories dan Furniture & Decor mengalami pertumbuhan yang lebih rendah. Di sisi lain, Health & Beauty mencatat peningkatan penjualan yang signifikan, menandakan peningkatan minat konsumen terhadap produk kesehatan dan kecantikan. Sementara Sports & Leisure menunjukkan pertumbuhan yang moderat")
        st.write("Secara keseluruhan, semua kategori mencerminkan potensi pertumbuhan dalam berbagai tingkat. Kesimpulannya, analisis tren penjualan ini dapat membantu perusahaan memahami preferensi konsumen dan mengoptimalkan strategi pemasaran untuk memaksimalkan potensi pasar.")

    #---------------------------------------------------------------------------------------------------------------------------------------

    st.markdown('---')
    st.subheader('Korelasi Penjualan 5 Kategori Teratas Dalam 3 Tahun Terakhir')

    heat_map = pivot_table.corr()
    plt.figure(figsize=(8, 6)) 
    sns.heatmap(heat_map, annot=True,cmap='YlGnBu')
    plt.title('Heatmap Penjualan 3 Tahun Terakhir')
    plt.xlabel('Tahun')
    plt.ylabel('Tahun')
    st.dataframe(heat_map)
    st.pyplot(plt)

    with st.expander("Penjelasan Mengenai Heatmap Penjualan"):
        st.write("Dalam Visualisasi Heatmap Di atas Terdapat Keterkaitan Antara Penjualan Pada Tahun 2017 dan 2018, keterkaitan berada pada angka 63%")

    st.markdown('---')
    #-------------------------------------------------------------------------------------------------------------
    st.subheader('Prediksi Penjualan Dengan Linear Regression')
    st.empty()
    # Memilih kolom yang akan digunakan untuk prediksi
    kategori_info = kategori_info[['shipping_limit_date', 'jumlah_terjual']]

    # Ubah 'tanggal' menjadi period dan ambil hanya bulannya
    kategori_info['bulan'] = kategori_info['shipping_limit_date'].dt.to_period('M')

    # Agregasi data per bulan
    monthly_sales = kategori_info.groupby('bulan')['jumlah_terjual'].sum().reset_index()

    # Membuat fitur tambahan berupa jumlah bulan sejak awal data
    monthly_sales['months_since_start'] = (monthly_sales['bulan'] - monthly_sales['bulan'].min()).apply(lambda x: x.n)

    # Memilih fitur dan target
    X = monthly_sales[['months_since_start']]
    y = monthly_sales['jumlah_terjual']

    # Membagi data menjadi set pelatihan dan set pengujian
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inisialisasi model regresi linier
    model = LinearRegression()

    # Pelatihan model
    model.fit(X_train, y_train)

    # Prediksi
    y_pred = model.predict(X_test)

    # Visualisasi hasil prediksi
    plt.figure(figsize=(10, 6))
    plt.scatter(monthly_sales['bulan'].dt.to_timestamp(), monthly_sales['jumlah_terjual'], label='Data Asli')
    plt.plot(monthly_sales['bulan'].dt.to_timestamp(), model.predict(X), color='red', label='Regresi Linier')
    plt.title('Prediksi Penjualan dengan Regresi Linier')
    plt.ylabel('Jumlah Terjual')
    plt.xticks(rotation=90)
    plt.legend()

    # Menampilkan plot di Streamlit
    st.pyplot(plt)

    with st.expander("Penjelasan Mengenai Hasil Prediksi"):
        st.write("Dari hasil regresi linier yang terlihat pada garis merah dalam grafik, kita dapat menyimpulkan bahwa terdapat kecenderungan peningkatan penjualan seiring berjalannya waktu. Peningkatan ini menunjukkan bahwa bisnis secara umum mengalami pertumbuhan yang positif.")
        st.write("Model regresi linier memungkinkan kita untuk membuat prediksi terkait penjualan di masa mendatang berdasarkan tren yang teridentifikasi. Walaupun demikian, penting untuk diingat bahwa prediksi ini mungkin tidak sepenuhnya akurat karena masih ada banyak faktor lain yang dapat mempengaruhi penjualan. Faktor-faktor seperti musim, tren pasar, dan variabel lainnya perlu dipertimbangkan untuk meningkatkan akurasi prediksi.")
    


    st.markdown("---")
    st.caption('10122292 - Wildan Mujjahid Robbani')


with st.sidebar :
    selected = option_menu('Keras',['Dashboard','10122292-Wildan'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    

if (selected=='Dashboard'):
    st.title("DASHBOARD E-COMMERCE KAMI YO BROO AWKWKWKWK")

    image = Image.open('6209783_3195378.jpg')
    st.image(image, caption='E-Comerce Analysis Dashboard',use_column_width=True)
    
elif (selected == '10122292-Wildan') :
    st.header(f"Dashboard Analisis E-Commerce")
    tab1= st.tabs(["Analisis Penjualan Per Kategori"])
    with tab1[0]:
        analisis_wildan(kategori_info)

    

