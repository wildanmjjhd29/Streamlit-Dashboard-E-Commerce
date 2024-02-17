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
import plotly.graph_objects as go
from folium.plugins import HeatMap
from streamlit_folium import folium_static
from babel.numbers import format_currency

@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

kategori_info = load_data('https://raw.githubusercontent.com/wildanmjjhd29/Streamlit-Dashboard-E-Commerce/main/kategori_info.csv') 
orders_dataset_df = load_data('https://raw.githubusercontent.com/wildanmjjhd29/Streamlit-Dashboard-E-Commerce/main/orders_dataset.csv') 
orders_sellers_df = load_data('https://raw.githubusercontent.com/wildanmjjhd29/Streamlit-Dashboard-E-Commerce/main/orders_sellers_dataset.csv')
customer_df = load_data("https://raw.githubusercontent.com/wildanmjjhd29/Streamlit-Dashboard-E-Commerce/main/customers_dataset.csv")
count = load_data('https://raw.githubusercontent.com/wildanmjjhd29/Streamlit-Dashboard-E-Commerce/main/Customer.csv')
my_file = "https://raw.githubusercontent.com/wildanmjjhd29/Streamlit-Dashboard-E-Commerce/main/all_data.csv"
all_df = pd.read_csv(my_file)
datetime_columns = ["order_approved_at", "order_delivered_customer_date"]
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)


#WILDAN
def analisis_wildan():

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

def analisis_wildan2(kategori_info):
    
    # Mengubah kolom 'shipping_limit_date' menjadi datetime
    kategori_info['shipping_limit_date'] = pd.to_datetime(kategori_info['shipping_limit_date'])

    # Menghitung jumlah kategori
    count_kategori = kategori_info['product_category'].value_counts()

    # Mencari 5 kategori teratas
    kategori_head = count_kategori.head(5)

    # Mencari 5 kategori terbawah
    kategori_tail = count_kategori.tail(5)

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

def analisis_wildan3(kategori_info):
    # Mengubah kolom 'shipping_limit_date' menjadi datetime
    kategori_info['shipping_limit_date'] = pd.to_datetime(kategori_info['shipping_limit_date'])

    # Menghitung jumlah kategori
    count_kategori = kategori_info['product_category'].value_counts()

    # Mencari 5 kategori teratas
    kategori_head = count_kategori.head(5)

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
    sns.heatmap(heat_map, annot=True,cmap='coolwarm')
    plt.title('Heatmap Penjualan 3 Tahun Terakhir')
    plt.xlabel('Tahun')
    plt.ylabel('Tahun')
    st.dataframe(heat_map)
    st.pyplot(plt)

    with st.expander("Penjelasan Mengenai Heatmap Penjualan"):
        st.write("Dalam Visualisasi Heatmap Di atas Terdapat Keterkaitan Antara Penjualan Pada Tahun 2017 dan 2018, keterkaitan berada pada angka 63%")

def analisis_wildan4(kategori_info):
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
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PUTRI
def analisis_putri_all(orders_dataset_df) :
    orders_dataset_df.isna().sum()

    orders_dataset_df["order_approved_at"].fillna(value="No Date or Related Date", inplace=True)
    orders_dataset_df["order_delivered_carrier_date"].fillna(value="No Date or Related Date", inplace=True)
    orders_dataset_df["order_delivered_customer_date"].fillna(value="No Date or Related Date", inplace=True)

    orders_dataset_df.isna().sum()
    
    st.caption("**10122294 - Putri Aprilia**")
    # ------------------------------------------------------------------------------------------------------------------------------------
    st.subheader("Informasi Yang Ingin Di Sampaikan")
    st.markdown("- **Analisis Terhadap Pengiriman Pesanan Pada Tiap Tahun**")
    st.markdown("- **Menampilkan Diagram Pie Chart Pada Analisis Tiap Tahunnya**")
       
    with st.expander("Tujuan Analisis Infomasi Tersebut"):
        st.markdown("**Analisis Terhadap Pengiriman Pesanan Pada Tiap Tahun**")
        st.markdown("Melalui analisis terhadap pengiriman pesanan pada tiap tahun, kita dapat memahami seberapa efektif operasional pengiriman yang dilakukan dan mengidentifikasi area yang memerlukan perbaikan. Analisis ini fokus pada dua aspek utama: pengiriman tepat waktu dan pengiriman yang terlambat. Menilik setiap tahunnya, analisis ini menelusuri performa pengiriman pesanan dari tahun ke tahun. Data pesanan yang tercatat memberikan informasi tentang jumlah pesanan yang dikirim tepat waktu dan jumlah pesanan yang terlambat pada setiap tahunnya. Dampak dari analisis terhadap pengiriman pesanan pada tiap tahun sangatlah signifikan. Pengiriman yang tepat waktu meningkatkan kepuasan pelanggan, memperkuat reputasi merek, dan meningkatkan loyalitas pelanggan. Di sisi lain, keterlambatan dalam pengiriman dapat mengakibatkan kekecewaan pelanggan, pengembalian barang, dan bahkan potensi kehilangan pelanggan. Oleh karena itu, analisis terhadap pengiriman pesanan pada tiap tahun merupakan instrumen penting dalam pengelolaan operasional e-commerce. Dengan pemahaman yang mendalam tentang performa pengiriman, perusahaan dapat mengidentifikasi tantangan, menerapkan perbaikan yang diperlukan, dan terus meningkatkan kualitas layanan pengiriman untuk memenuhi harapan pelanggan dan menjaga keberlanjutan bisnisnya.")
      
#-------------------------------------------------------------------------------------
def analisis_putri_2016(orders_dataset_df) :
    #PERSENTASE PENGIRIMAN 2016
    st.subheader("Grafik Pengiriman Pada Tahun 2016")

    # Filter data
    filter = orders_dataset_df[(orders_dataset_df['order_status'] == "delivered") & (orders_dataset_df['order_delivered_customer_date'] > "2016-01-01") & (orders_dataset_df['order_delivered_customer_date'] < "2016-12-31")]
    filter2 = filter[['order_delivered_customer_date', 'order_estimated_delivery_date']]
    filter3 = filter2[(filter2['order_delivered_customer_date'] > filter2['order_estimated_delivery_date'])]
    filter4 = filter2[(filter2['order_delivered_customer_date'] < filter2['order_estimated_delivery_date'])]

    # Calculate lengths
    jumlah_terlambat_2016 = len(filter3)
    jumlah_tepat_waktu_2016 = len(filter4)
       
    #Pengiriman Tepat Waktu dan Terlambat
    data_keterlambatan = pd.DataFrame({
        'Kategori': ['Tepat Waktu', 'Terlambat'],
        'Jumlah': [jumlah_tepat_waktu_2016,jumlah_terlambat_2016]
    })
       
    st.dataframe(data_keterlambatan)

    # Plot pie chart
    shipped_expose = [0, 0.2]
    warna = ['#25ADE8', '#E55673']
    values = [jumlah_tepat_waktu_2016, jumlah_terlambat_2016]
    labels = ['Tepat Waktu', 'Terlambat']

    fig, ax = plt.subplots()
    ax.pie(values,
        labels=labels,
        autopct='%1.1f%%',
        colors=warna,
        explode=shipped_expose,
        startangle=60)

    st.pyplot(fig)
       
    with st.expander("Penjelasan"):
        st.markdown("**Analisis Keterlamabatan Pengiriman Pesanan pada Tahun 2016**")
        st.markdown("Data di atas menunjukkan bahwa rata-rata pesanan dikirim tepat waktu dengan jumlah 263 pesanan persentase sebesar (98.5%) dan yang dikirim tidak tepat waktu (terlambat) dengan jumlah 4 pesanan persentasenya terhitung sangat kecil sebesar (1.5%), namun guna meningkatkan kenyamanan dan kepuasan pelanggan, perusahaan dapat lebih memperhatikan terkait pengirimannya")

#-------------------------------------------------------------------------------------
def analisis_putri_2017(orders_dataset_df) :
    #PERSENTASE PENGIRIMAN 2017
    st.subheader("Grafik Pengiriman Pada Tahun 2017")
       
    # Filter data
    filter = orders_dataset_df[(orders_dataset_df['order_status'] == "delivered") & (orders_dataset_df['order_delivered_customer_date'] > "2017-01-01") &  (orders_dataset_df['order_delivered_customer_date'] < "2017-12-31")]
    filter2 = filter[['order_delivered_customer_date', 'order_estimated_delivery_date']]
    filter3 = filter2[(filter2['order_delivered_customer_date'] > filter2['order_estimated_delivery_date'])]
    filter4 = filter2[(filter2['order_delivered_customer_date'] < filter2['order_estimated_delivery_date'])]

    # Calculate lengths
    jumlah_terlambat_2017 = len(filter3)
    jumlah_tepat_waktu_2017 = len(filter4)
       
    #Pengiriman Tepat Waktu dan Terlambat
    data_keterlambatan = pd.DataFrame({
        'Kategori': ['Tepat Waktu', 'Terlambat'],
        'Jumlah': [jumlah_tepat_waktu_2017,jumlah_terlambat_2017]
    })
       
    st.dataframe(data_keterlambatan)

    # Plot pie chart
    shipped_expose = [0, 0.2]
    warna = ['#25ADE8', '#E55673']
    values = [jumlah_tepat_waktu_2017, jumlah_terlambat_2017]
    labels = ['Tepat Waktu', 'Terlambat']

    fig, ax = plt.subplots()
    ax.pie(values,
        labels=labels,
        autopct='%1.1f%%',
        colors=warna,
        explode=shipped_expose,
        startangle=60)

    st.pyplot(fig)
       
    with st.expander("Penjelasan"):
        st.markdown("**Analisis Keterlamabatan Pengiriman Pesanan pada Tahun 2017**")
        st.markdown("Data di atas menunjukkan bahwa rata-rata pesanan dikirim tepat waktu dengan jumlah 38.778 pesanan persentase sebesar (94.8%) dan yang dikirim tidak tepat waktu (terlambat) dengan jumlah 2.147 pesanan persentasenya terhitung sangat kecil sebesar (5.2%), namun guna meningkatkan kenyamanan dan kepuasan pelanggan, perusahaan dapat lebih memperhatikan terkait pengirimannya")
       
#-------------------------------------------------------------------------------------
def analisis_putri_2018(orders_dataset_df) :
    #PERSENTASE PENGIRIMAN 2018
    st.subheader("Grafik Pengiriman Pada Tahun 2018")

    # Filter data
    filter = orders_dataset_df[(orders_dataset_df['order_status'] == "delivered") & (orders_dataset_df['order_delivered_customer_date'] > "2018-01-01") & (orders_dataset_df['order_delivered_customer_date'] < "2018-12-31")]
    filter2 = filter[['order_delivered_customer_date', 'order_estimated_delivery_date']]
    filter3 = filter2[(filter2['order_delivered_customer_date'] > filter2['order_estimated_delivery_date'])]
    filter4 = filter2[(filter2['order_delivered_customer_date'] < filter2['order_estimated_delivery_date'])]

    # Calculate lengths
    jumlah_terlambat_2018 = len(filter3)
    jumlah_tepat_waktu_2018 = len(filter4)
       
    #Pengiriman Tepat Waktu dan Terlambat
    data_keterlambatan = pd.DataFrame({
        'Kategori': ['Tepat Waktu', 'Terlambat'],
        'Jumlah': [jumlah_tepat_waktu_2018,jumlah_terlambat_2018]
    })
       
    st.dataframe(data_keterlambatan)

    # Plot pie chart
    shipped_expose = [0, 0.2]
    warna = ['#25ADE8', '#E55673']
    values = [jumlah_tepat_waktu_2018, jumlah_terlambat_2018]
    labels = ['Tepat Waktu', 'Terlambat']

    fig, ax = plt.subplots()
    ax.pie(values,
        labels=labels,
        autopct='%1.1f%%',
        colors=warna,
        explode=shipped_expose,
        startangle=60)

    st.pyplot(fig)
       
    with st.expander("Penjelasan"):
        st.markdown("**Analisis Keterlamabatan Pengiriman Pesanan pada Tahun 2018**")
        st.markdown("Data di atas menunjukkan bahwa rata-rata pesanan dikirim tepat waktu dengan jumlah 49.598 pesanan persentase sebesar (89.7%), akan tetapi pesanan yang dikirim tidak tepat waktu (telat) juga memiliki persentase yang bisa dibilang cukup besar (10.3%) dengan jumlah 5.675 pesanan yang terlambat. Maka dari itu, data ini dapat digunakan oleh perusahaan guna meningkatkan kualitas pengiriman pesanan sehingga dapat berkurang persentasenya.")

#---------------------------------------------------------------------------------------------
# IMAT
def tingkat_penjualan_2016(all_df):
    df_tingkat_penjualan_2016 = all_df[all_df.order_year == 2016]

    tingkat_penjualan_2016 = df_tingkat_penjualan_2016.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    

    return tingkat_penjualan_2016

def tingkat_penjualan_2017(all_df):
    df_tingkat_penjualan_2017 = all_df[all_df.order_year == 2017]

    tingkat_penjualan_2017 = df_tingkat_penjualan_2017.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    
    return tingkat_penjualan_2017

def tingkat_penjualan_2018(all_df):
    df_tingkat_penjualan_2018 = all_df[all_df.order_year == 2018]

    tingkat_penjualan_2018 = df_tingkat_penjualan_2018.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    
    return tingkat_penjualan_2018

#--------------------------------------------------------------------------------------------
# HILMAN
def cleaningData(df):
    df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])
    df['review_creation_date'] = pd.to_datetime(df['review_creation_date'])
    df.drop(columns=["Unnamed: 0"], inplace=True)
    df['seller_zip_code_prefix'] = df['seller_zip_code_prefix'].astype('object')

def findCounter(df):
    counter = pd.DataFrame(orders_sellers_df.groupby('seller_city').agg({
        'review_score' : 'sum',
        'review_id' : 'count',
        'order_id'  : 'count'
    }).sort_values('review_score',ascending=False))

    return counter

def Graf(Data,color,title):
    fig, ax = plt.subplots()
    bars = ax.bar(Data.index, Data['review_score'], color=color)
    ax.set_xticklabels(Data.index, rotation=65)
    ax.set_title('Kota - Kota Dengan Rating Dan Jumlah penjualan yang '+title)
    ax.set_xlabel('')
    ax.set_ylabel('')
    st.pyplot(fig)

def heatMap(df):
    values = df.groupby('seller_state').agg({
            'seller_city' : 'nunique',
            'seller_id' : 'nunique',
            'review_score' : 'count',
        })
    heat_map = values.corr()
    plt.figure(figsize=(8, 6)) 
    sns.heatmap(heat_map, annot=True,cmap='YlGnBu')
    plt.title('')
    st.dataframe(heat_map)
    st.pyplot(plt)

def GoodReviewsGraf(df,counter):
    rating_counter = pd.DataFrame(orders_sellers_df.groupby('seller_city').review_score.sum().sort_values(ascending=False))
    valid_rating_counter = rating_counter.drop(index=[row for row in rating_counter.index if 5000 > rating_counter.loc[row, 'review_score']])
    review_counter = pd.DataFrame(orders_sellers_df.groupby('seller_city').review_id.count().sort_values(ascending=False))
    valid_review_counter = review_counter.drop(index=[row for row in review_counter.index if 1200 > review_counter.loc[row, 'review_id']])
    ratio = valid_rating_counter / valid_review_counter.values
    overall = pd.DataFrame(ratio.drop(index=[row for row in ratio.index if 4 > ratio.loc[row, 'review_score']]))

    color =["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3"]
    dataTertinggi = overall.sort_values('review_score',ascending= False)
    title = "tinggi"
    st.markdown("- **Kota-kota dengan rating tertinggi**")
    st.dataframe(dataTertinggi)
    Graf(dataTertinggi,color,title)

def BadReviewsGraf(df,counter):
    worstCity = pd.DataFrame(counter.drop(index=[row for row in counter.index if 1 < counter.loc[row, 'review_score'] and counter.loc[row, 'review_id'] and counter.loc[row, 'order_id']]))
    color =["#72BCD4"]
    dataTerendah = worstCity.sort_values('review_score',ascending= False)
    title = "rendah"
    st.markdown("- **Kota-kota dengan rating dan penjualan yang rendah**")
    st.dataframe(dataTerendah)
    Graf(dataTerendah,color,title)
    
#---------------------------------------------------------------------------------------------
#DICKY
def AnalisisDicky(df,count):
# Check the loaded data
    if 'count' not in count.columns:
        st.error("Error: 'Count' column not found in the data. Please check your CSV file or data processing code.")
    else:
        # Get top 5 customers
        top5 = count.head(5)

        # Display top 5 customers
        st.write("Top 5 Customers:")
        st.write(top5)

        # Display pie chart
        st.write("Pie Chart:")
        fig, ax = plt.subplots()
        ax.pie(
            x=top5['count'],
            labels=top5['customer_city'],
            autopct='%1.1f%%',
            colors=['#15808E', '#439A97', '#4EB3B0', '#97DECE', '#CBEDD5']
        )
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
        with st.expander("Penjelasan"):
            st.write("disini kita bisa melihat 5 kota dengan jumlah customer terbanyak yaitu dari sao paulo dengan 53.9%, rio de Janeiro dengan 23.9%, belo horizonte dengan 9.6%, Brasilia dengan 7.4%, curtibia 5.3%")
        # Display bar chart
        st.write("Bar Chart:")
        fig, ax = plt.subplots()
        ax.bar(
            x=top5['customer_city'],
            height=top5['count'],
            color=['#15808E', '#439A97', '#4EB3B0', '#97DECE', '#CBEDD5']
        )
        ax.set_xlabel('Customer')
        ax.set_ylabel('Count')
        ax.set_title('Top 5 Customers')
        plt.xticks(rotation=45)
        st.pyplot(fig)
        with st.expander("Penjelasan"):
            st.write("disini kita bisa mengetahui jumlah customer yang ada di kota tersebut")

        #heatmap
        values = df.groupby('customer_state').agg({
            'customer_city' : 'nunique',
            'count' : 'nunique',
        })

        heat_map = values.corr()
        plt.figure(figsize=(8,6))
        sns.heatmap(heat_map, annot=True, cmap='Blues')
        st.dataframe(heat_map)
        st.pyplot(plt)
        with st.expander("Penjelasan"):
            st.write("dalam visualisasi heatmap ada korelasi antara kota kota tersebut dengan banyak nya jumlah customer sebesar 82%")

with st.sidebar :
    selected = option_menu('Keras',['Dashboard','10122292-Wildan','10122293-Imat','10122294-Putri','10122304-Hilman','10122305-Dicky'],
    icons =["easel2", "graph-up","graph-up","pie-chart","bar-chart","bar-chart"],
    menu_icon="cast",
    default_index=0)
    
if (selected=='Dashboard'):
    st.title("DASHBOARD ANALISIS E-COMMERCE")
    st.subheader("KELOMPOK KERAS (IF-8)")
    image_url = 'https://github.com/wildanmjjhd29/Streamlit-Dashboard-E-Commerce/blob/main/db%20kali.png?raw=true'
    st.image(image_url, caption="Dashboard Keras")

elif (selected == '10122292-Wildan') :
    st.header(f"Analsis Penjualan Kategori Produk")
    tab1,tab2,tab3,tab4= st.tabs(["Informasi Analisis","Grafik Penjualan Kategori","Trend Penjualan Kategori","Prediksi Penjualan"])
    with tab1:
        analisis_wildan()
    with tab2:
        analisis_wildan2(kategori_info)
    with tab3:
        analisis_wildan3(kategori_info)
    with tab4:
        analisis_wildan4(kategori_info)
        
elif (selected == '10122294-Putri') :
    st.header(f"Analisis Keterlambatan Pengiriman Pesanan")
    tab1,tab2,tab3,tab4 = st.tabs(["Informasi","2016","2017","2018"])
    with tab1:
        analisis_putri_all(orders_dataset_df)
    with tab2:
        analisis_putri_2016(orders_dataset_df)
    with tab3:
        analisis_putri_2017(orders_dataset_df)
    with tab4:
        analisis_putri_2018(orders_dataset_df)

elif (selected == '10122293-Imat'):
    st.title("E-commerce sales performance")
    tab1,tab2,tab3 = st.tabs(["2016","2017","2018"])
    with tab1:
        tingkat_penjualan_2016(all_df)
        tingkat_penjualan_2016 = tingkat_penjualan_2016(all_df)
        col1, col2 = st.columns(2)

        with col1:
            total_orders = tingkat_penjualan_2016.order_id.sum()
            st.metric("Total orders", value=total_orders)
        
        with col2:
            total_revenue = format_currency(tingkat_penjualan_2016.payment_value.sum(), "AUD", locale='es_CO') 
            st.metric("Total Revenue", value=total_revenue)

        with st.container():

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=tingkat_penjualan_2016["order_month_name"],
                y=tingkat_penjualan_2016["order_id"],
                mode='lines+markers',
                marker=dict(
                    color='red',
                    size=8,
                ),
                line=dict(
                    width=3,
                ),
            ))

            for x, y in zip(tingkat_penjualan_2016["order_month_name"], tingkat_penjualan_2016["order_id"]):
                fig.add_annotation(
                    x=x,
                    y=y+15,
                    text=str(y),
                    font=dict(
                        size=12,
                    ),
                    showarrow=False,
                    textangle=0,
                )

            fig.update_layout(
                title="Sales Performance 2016",
                xaxis=dict(
                    title="Order Month",
                    titlefont=dict(
                        size=14,
                    ),
                    tickfont=dict(
                        size=14,
                    ),
                ),
                yaxis=dict(
                    title="Number of orders",
                    titlefont=dict(
                        size=14,
                    ),
                    tickfont=dict(
                        size=14,
                    ),
                ),
                width=650,
                height=400,
            )

            st.plotly_chart(fig)

            with st.expander("Interpretasi", expanded=False):

                # Konten expander
                st.write("Tingkat penjualan di tahun 2016 tidak dapat diamati dengan baik dikarenakan ketidaklengkapan data yang ada. Yaitu hanya terdapat 1 transaksi pada bulan Desember 2016.")
        
    with tab2:
        tingkat_penjualan_2017(all_df)
        tingkat_penjualan_2017 = tingkat_penjualan_2017(all_df)
        col1, col2 = st.columns(2)

        with col1:
            total_orders = tingkat_penjualan_2017.order_id.sum()
            st.metric("Total orders", value=total_orders)
        
        with col2:
            total_revenue = format_currency(tingkat_penjualan_2017.payment_value.sum(), "AUD", locale='es_CO') 
            st.metric("Total Revenue", value=total_revenue)

        fig = go.Figure()

        with st.container():
            fig.add_trace(go.Scatter(
                x=tingkat_penjualan_2017["order_month_name"],
                y=tingkat_penjualan_2017["order_id"],
                mode='lines+markers',
                marker=dict(
                    color='red',
                    size=8,
                ),
                line=dict(
                    width=3,
                ),
            ))

            for x, y in zip(tingkat_penjualan_2017["order_month_name"], tingkat_penjualan_2017["order_id"]):
                fig.add_annotation(
                    x=x,
                    y=y+150,
                    text=str(y),
                    font=dict(
                        size=12,
                    ),
                    showarrow=False,
                    textangle=0,
                )

            fig.update_layout(
                title="Sales Performance 2017",
                xaxis=dict(
                    title="Order Month",
                    titlefont=dict(
                        size=14,
                    ),
                    tickfont=dict(
                        size=14,
                    ),
                ),
                yaxis=dict(
                    title="Number of orders",
                    titlefont=dict(
                        size=14,
                    ),
                    tickfont=dict(
                        size=14,
                    ),
                ),
                width=650,
                height=400,
            )

            st.plotly_chart(fig)

            with st.expander("Interpretasi", expanded=False):

                # Konten expander
                st.write("Tingkat penjualan pada tahun 2017 menunjukan tren pertumbuhan yang baik hingga akhir tahun. Bulan november merupakan bulan yang memiliki jumlah transaksi tertinggi yaitu sebesar 7146 transaksi dengan total penjualan selama 1 tahun sebesar 43352 dan total pemasukan dari keseluruhan transaksi sebesar 8 juta USD atau sekitar 121 milyar rupiah.")

            with st.expander("Saran", expanded=False):

                st.write("- Memanfaatkan Tren Pertumbuhan:")
                st.write("  Memanfaatkan adanya tren pertumbuhan yang baik pada tahun 2017 untuk meningkatkan penjualan di tahun-tahun berikutnya dengan mengidentifikasi faktor-faktor yang berkontribusi terhadap peningkatan penjualan pada bulan November, seperti promosi khusus, produk yang populer, atau strategi pemasaran yang efektif.")
                st.write("- Analisis Bulan November:")
                st.write("  meneliti dengan lebih mendalam mengapa bulan November memiliki jumlah transaksi tertinggi. Apakah ada peristiwa khusus, seperti liburan atau acara penjualan besar, yang mendorong pertumbuhan tersebut. Analisis ini dapat membantu untuk merencanakan kegiatan promosi atau penjualan yang serupa di masa depan.")

    with tab3:
        tingkat_penjualan_2018(all_df)
        tingkat_penjualan_2018 = tingkat_penjualan_2018(all_df)
        col1, col2 = st.columns(2)

        with col1:
            total_orders = tingkat_penjualan_2018.order_id.sum()
            st.metric("Total orders", value=total_orders)
        
        with col2:
            total_revenue = format_currency(tingkat_penjualan_2018.payment_value.sum(), "AUD", locale='es_CO') 
            st.metric("Total Revenue", value=total_revenue)

        fig = go.Figure()

        with st.container():
            fig.add_trace(go.Scatter(
                x=tingkat_penjualan_2018["order_month_name"],
                y=tingkat_penjualan_2018["order_id"],
                mode='lines+markers',
                marker=dict(
                    color='red',
                    size=8,
                ),
                line=dict(
                    width=3,
                ),
            ))

            for x, y in zip(tingkat_penjualan_2018["order_month_name"], tingkat_penjualan_2018["order_id"]):
                fig.add_annotation(
                    x=x,
                    y=y+150,
                    text=str(y),
                    font=dict(
                        size=12,
                    ),
                    showarrow=False,
                    textangle=0,
                )

            fig.update_layout(
                title="Sales Performance 2018",
                xaxis=dict(
                    title="Order Month",
                    titlefont=dict(
                        size=14,
                    ),
                    tickfont=dict(
                        size=14,
                    ),
                ),
                yaxis=dict(
                    title="Number of orders",
                    titlefont=dict(
                        size=14,
                    ),
                    tickfont=dict(
                        size=14,
                    ),
                ),
                width=650,
                height=400,
            )

            st.plotly_chart(fig)

            with st.expander("Interpretasi", expanded=False):

                # Konten expander
                st.write("Tingkat penjualan pada tahun 2018 menujukan tren yang cukup stagnan dan cenderung turun dengan bulan maret menjadi bulan yang memiliki jumlah transaksi tertinggi yaitu sebesar 7085 transaksi.dengan total penjualan selama 1 tahun sebesar 52859 dan total pemasukan dari keseluruhan transaksi sebesar 10 juta USD atau sekitar 151 milyar rupiah.")
            
            with st.expander("Saran", expanded=False):

                # Konten expander
                st.write("- Identifikasi Penyebab Stagnansi dan Penurunan: ")
                st.write("  Meneliti dengan lebih mendalam untuk mengidentifikasi faktor-faktor yang menyebabkan penurunan dan stagnannya tingkat penjualan. Meninjau faktor-faktor internal dan eksternal yang mungkin berperan, seperti perubahan preferensi pelanggan, persaingan yang meningkat, perubahan tren pasar, atau perubahan dalam strategi pemasaran.")

elif(selected == '10122304-Hilman'):
    cleaningData(orders_sellers_df)
    st.title("ANALISIS KOTA DENGAN RATING TERTINGGI DAN TERENDAH")
    tab1,tab2,tab3,tab4 = st.tabs(["Heads Up","Good Reviews","Bad Reviews","Heat Map"])
    with tab1:
        st.header("INFORMASI YANG AKAN DISAMPAIKAN")
        st.markdown("- **Kota-Kota dengan Rating Tertinggi**")
        with st.expander("Lihat lebih detail"):
            st.write("Analisis ini memberikan gambaran tentang kota-kota yang mencatat rating pelanggan tertinggi dalam dataset. Melalui grafik yang disajikan, kita dapat mengidentifikasi kota-kota yang menonjol dengan layanan unggulan, produk berkualitas, atau pengalaman pembelian yang memuaskan. Warna biru muda pada grafik menandakan kota-kota dengan rating tertinggi, sementara penempatan bar pada grafik memberikan gambaran yang jelas tentang peringkat relatif kota-kota dalam hal rating pelanggan. Analisis ini membantu bisnis untuk mengidentifikasi kota-kota yang dapat menjadi fokus untuk meningkatkan pemasaran dan penjualan lebih lanjut.")
        st.markdown("- **Kota-Kota dengan Rating Terendah**")
        with st.expander("Lihat lebih detail"):
            st.write("Sebaliknya, analisis ini menyoroti kota-kota yang mencatat rating pelanggan terendah dalam dataset. Melalui visualisasi grafik, kita dapat mengidentifikasi kota-kota yang mungkin menghadapi tantangan dalam hal kepuasan pelanggan atau kualitas produk. Warna standar pada grafik menandakan kota-kota dengan rating terendah, memberikan indikasi tentang kinerja kurang memuaskan dalam layanan pelanggan atau produk di wilayah-wilayah tersebut. Analisis ini membantu bisnis untuk mengidentifikasi kota-kota yang memerlukan perhatian lebih dalam upaya untuk meningkatkan kepuasan pelanggan dan performa penjualan di wilayah-wilayah tersebut.")
        st.markdown("- **Korelasi antara Faktor-Faktor Relevan**")
        with st.expander("Lihat lebih detail"):
            st.write("Selain itu, analisis heatmap memberikan pemahaman tambahan tentang hubungan antara faktor-faktor yang relevan dalam dataset, seperti jumlah kota unik, jumlah penjual unik, dan jumlah pesanan. Heatmap menunjukkan korelasi antara variabel-variabel ini, yang membantu dalam mengidentifikasi pola-pola dan hubungan di antara mereka. Informasi ini dapat digunakan untuk mengoptimalkan strategi bisnis dan meningkatkan pemahaman tentang dinamika pasar.")
        st.header("Tujuan")
        with st.expander("Tujuan Analisis"):
            st.write("Analisis ini mengungkapkan insight yang berharga tentang kota-kota dengan kinerja tertinggi dan terendah dalam hal rating pelanggan dan jumlah penjualan pada dataset yang diamati. Dengan fokus pada kota-kota yang mencatat rating tertinggi, grafik-gafik yang disajikan memberikan gambaran yang jelas tentang lokasi-lokasi yang menonjol dengan layanan dan pengalaman pelanggan yang superior. Sementara itu, melalui identifikasi kota-kota dengan rating terendah, analisis ini juga memberikan pemahaman mendalam tentang area-area yang memerlukan perhatian lebih dalam upaya meningkatkan kepuasan pelanggan dan performa penjualan. Selain itu, visualisasi heatmap memperlihatkan korelasi antara faktor-faktor yang relevan dalam dataset, memberikan pemahaman tambahan tentang pola-pola yang mungkin ada di dalamnya. Dengan demikian, analisis ini memberikan landasan yang kuat untuk pengambilan keputusan strategis dalam konteks bisnis e-commerce, memungkinkan perusahaan untuk mengarahkan sumber daya mereka dengan lebih efektif untuk memperkuat kehadiran dan performa mereka di pasar.")
    with tab2:
        st.header("KOTA-KOTA DENGAN RATING DAN JUMLAH PENJUALAN YANG TINGGI")
        GoodReviewsGraf(orders_sellers_df,findCounter(orders_sellers_df))
        with st.expander("Penjelasan Grafik"):
            st.write("Grafik di atas menggambarkan kota-kota dengan rating dan jumlah penjualan tertinggi dalam suatu dataset. Setiap bar pada grafik mewakili satu kota, diurutkan berdasarkan skor rating pelanggan secara menurun dari kiri ke kanan. Warna biru muda pada bar menandakan kota dengan rating tertinggi, sementara warna abu-abu mengindikasikan kota-kota dengan rating yang lebih rendah. Dengan demikian, grafik ini memberikan pemahaman visual yang jelas tentang kota mana yang memiliki reputasi yang baik dalam hal penilaian pelanggan.Analisis grafik ini memberikan wawasan yang berharga bagi bisnis e-commerce atau pengecer untuk mengidentifikasi kota-kota di mana mereka dapat fokus pada upaya pemasaran dan penjualan lebih lanjut. Dengan mengetahui kota-kota yang memiliki rating dan penjualan tinggi, perusahaan dapat mengarahkan sumber daya mereka dengan lebih efektif untuk mempertahankan dan meningkatkan pangsa pasar di daerah-daerah ini. Selain itu, grafik ini juga membantu dalam pemahaman tren dan pola penjualan di berbagai lokasi, yang dapat digunakan untuk mengoptimalkan strategi bisnis dan meningkatkan kepuasan pelanggan secara keseluruhan.")
        st.subheader("Kesimpulan")
        st.write("Grafik tersebut memberikan gambaran tentang kota-kota yang memiliki rating dan jumlah penjualan tertinggi dalam dataset yang diamati. Dari grafik tersebut, dapat disimpulkan beberapa hal: ")
        st.write("1. Kota-kota dengan rating tertinggi cenderung menarik perhatian karena warna biru muda pada grafik menunjukkan keunggulan mereka dalam hal penilaian pelanggan. Ini menandakan bahwa kota-kota tersebut mungkin memiliki layanan pelanggan yang unggul, kualitas produk yang baik, atau pengalaman pembelian yang memuaskan.")
        st.write("2. Penempatan baris pada grafik memberikan pandangan yang jelas tentang peringkat relatif kota-kota dalam hal rating pelanggan. Dengan demikian, bisnis dapat dengan mudah mengidentifikasi kota-kota yang paling sukses dan memfokuskan upaya mereka untuk memperkuat kehadiran mereka di wilayah-wilayah tersebut.")
        st.write("3. Meskipun demikian, grafik ini hanya memberikan gambaran awal dan tidak memberikan informasi tentang faktor-faktor apa yang mendasari peringkat dan penjualan yang tinggi di setiap kota. Oleh karena itu, analisis lebih lanjut mungkin diperlukan untuk memahami secara lebih mendalam mengenai dinamika pasar dan faktor-faktor yang memengaruhinya.")
        st.write("Dengan demikian, grafik ini memberikan gambaran yang berguna tentang kinerja kota-kota dalam dataset tersebut dan dapat digunakan sebagai landasan untuk analisis lebih lanjut dan pengambilan keputusan strategis dalam bisnis e-commerce.")
        
    with tab3:
        st.header("KOTA-KOTA DENGAN RATING DAN JUMLAH PENJUALAN YANG RENDAH")
        BadReviewsGraf(orders_sellers_df,findCounter(orders_sellers_df))
        with st.expander("Penjelasan Grafik"):
            st.write("Grafik tersebut mengilustrasikan kota-kota yang memiliki rating dan jumlah penjualan terendah dalam dataset yang diamati. Dari visualisasi ini, terlihat bahwa beberapa kota menonjol dengan rating yang relatif rendah, ditandai dengan warna standar pada bar grafik. Hal ini memberikan indikasi bahwa kota-kota tersebut mungkin mengalami tantangan dalam hal kepuasan pelanggan atau kualitas produk yang ditawarkan. Dengan memperhatikan penempatan bar pada grafik, perusahaan dapat dengan mudah mengidentifikasi kota-kota yang membutuhkan perhatian lebih dalam upaya meningkatkan performa penjualan dan kepuasan pelanggan di wilayah-wilayah tersebut.")
            st.write("")
            st.write("Grafik tersebut memberikan gambaran awal tentang kota-kota yang memiliki kinerja rendah dalam hal rating dan jumlah penjualan dalam dataset yang diamati. Namun, untuk mendapatkan pemahaman yang lebih mendalam, diperlukan analisis yang lebih rinci. Pertama-tama, perlu dilakukan penelitian untuk memahami preferensi dan perilaku konsumen di setiap kota tersebut. Apakah ada perbedaan dalam preferensi produk atau layanan antara kota yang berperforma baik dan yang berperforma buruk? Selain itu, perlu dievaluasi kualitas layanan dan produk yang disediakan di setiap wilayah. Apakah ada masalah terkait ketersediaan produk, proses pengiriman, atau layanan pelanggan di kota-kota dengan performa rendah?")
            st.write("")
            st.write("Selain itu, penting untuk mempertimbangkan faktor-faktor eksternal yang mungkin memengaruhi performa penjualan, seperti kondisi ekonomi lokal, persaingan pasar, atau tren industri. Apakah ada faktor-faktor eksternal tertentu yang dapat diidentifikasi sebagai penyebab performa rendah di kota-kota tertentu? Dengan menganalisis lebih lanjut faktor-faktor ini, perusahaan dapat mengidentifikasi strategi yang lebih tepat untuk meningkatkan performa mereka di setiap wilayah dan mengatasi tantangan yang mereka hadapi.")
        st.subheader("Kesimpulan")
        st.write("Grafik tersebut memberikan gambaran tentang kota-kota yang memiliki rating dan jumlah penjualan terendah dalam dataset yang diamati. Dari grafik tersebut, dapat disimpulkan beberapa hal: ")
        st.write("1. Ada variasi yang signifikan dalam skor rating antara kota-kota yang tercatat dalam dataset ini. Beberapa kota menonjol dengan rating yang relatif rendah, yang tercermin dalam warna bar pada grafik. Warna standar pada grafik menunjukkan kota-kota dengan rating terendah, memberikan indikasi tentang kinerja kurang memuaskan dalam hal layanan pelanggan atau kualitas produk di wilayah-wilayah tersebut.")
        st.write("2. Penempatan bar pada grafik memberikan gambaran yang jelas tentang peringkat relatif kota-kota dalam hal rating pelanggan. Hal ini memungkinkan bisnis untuk mengidentifikasi kota-kota yang mungkin memerlukan perhatian lebih dalam upaya untuk meningkatkan kepuasan pelanggan dan kinerja penjualan di wilayah-wilayah tersebut.")
        st.write("Meskipun grafik ini memberikan wawasan awal tentang kota-kota dengan kinerja rendah, penting untuk dicatat bahwa analisis lebih lanjut mungkin diperlukan untuk memahami secara lebih mendalam faktor-faktor yang mendasari peringkat dan penjualan yang rendah di setiap kota. Ini dapat mencakup penelitian lebih lanjut tentang kebutuhan dan preferensi pelanggan di wilayah-wilayah tersebut, serta evaluasi terhadap kualitas layanan dan produk yang ditawarkan. Dengan pemahaman yang lebih mendalam tentang faktor-faktor tersebut, bisnis dapat mengambil langkah-langkah yang sesuai untuk meningkatkan kinerja mereka dan memperkuat kehadiran mereka di pasar.")

    with tab4:
        st.header("KORELASI ANTARA SELLER CITY, SELLER ID, DAN REVIEW SCORE")
        heatMap(orders_sellers_df)
        with st.expander("Penjelesan heatmap"):
            st.write("Baik antara seller city dan seller id, seller city dan review score,lalu seller id dan review score memiliki korelasi yang sangat baik karena hasil dari korelasi yang disebutkan sebelumnya dapat menyentuk lebih dari 90% ")

elif (selected == '10122305-Dicky'):
    tab1,tab2 = st.tabs(['Informasi','Analisis'])
    with tab1:
        st.header("INFORMASI YANG AKAN DISAMPAIKAN")
        st.markdown("- **Top 5 kota dengan jumlah customer terbanyak**")
        with st.expander("Tujuan"):
            st.write("Menjaga kepuasan customer dan meningkatkan layanan customer karena Lima kota dengan customer terbanyak memberikan kontribusi signifikan terhadap total persentase customer e-commerce, dengan menjaga kepuasan customer dan meningkatkan pelayanan memungkinkan jumlah customer meningkat.meningkatkan potensi pertumbuhan di luar kota dengan customer terbanyak Meskipun fokus utama mungkin pada lima kota teratas, analisis juga harus mempertimbangkan potensi pertumbuhan di kota-kota lain. Mengetahui tren dan kebutuhan konsumen di kota-kota tersebut dapat membuka peluang untuk meningkatkan strategi yang sama dengan stategi di 5 kota terbesar.")
    with tab2:
        AnalisisDicky(customer_df,count)
