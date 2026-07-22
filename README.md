☕ Coffee Shop Sales Analysis & ETL Pipeline
#### 📌 1. Giới thiệu dự án (Project Overview)
Tên dự án: Coffee Shop Sales ETL & Executive Dashboard

Mục tiêu: Xây dựng hệ thống Data Pipeline tự động hóa từ khâu xử lý dữ liệu thô, nạp vào Data Warehouse đến khai thác Insights kinh doanh cho chuỗi cửa hàng cà phê. Dự án giúp giải quyết bài toán tối ưu hóa doanh thu, quản lý ca kíp nhân sự, đánh giá hiệu suất chi nhánh và định hướng chiến lược Combo / Upselling dựa trên dữ liệu giao dịch thực tế.

#### 🏗️ 2. Tổng quan về Dataset & Kiến trúc (Data & Architecture)
Thông tin Dataset: Tập dữ liệu giao dịch bán hàng gồm khoảng 149,000+ dòng và 9 cột thông tin (mã giao dịch, ngày giờ, vị trí cửa hàng, sản phẩm, số lượng, giá bán...).

Tech Stack:

Languages & Libraries: Python 3.x (Pandas, NumPy, Matplotlib, Seaborn)

Database & ORM: MySQL, SQLAlchemy, PyMySQL

Data Visualization: Power BI Desktop

Version Control: Git, GitHub

Sơ đồ kiến trúc (Data Pipeline Flow):

Plaintext
[Raw Data (.xlsx)] ➔ [Staging Area (MySQL - stg_coffee_sales)] 
                          ➔ [ETL Pipeline (Python - 02_etl_pipeline.ipynb)] 
                                ➔ [Data Warehouse (MySQL - fact_sales)] 
                                      ➔ [Deep Analysis (03_data_analysis.ipynb) & Power BI Dashboard]
#### 🌟 3. Tóm tắt Insights & Kết quả chính (Key Findings & Insights)
🏆 Sản phẩm & Menu (Product Performance)
📈 Sản phẩm chủ lực: Nhóm hàng Coffee và Tea đóng góp tỷ trọng doanh thu lớn nhất toàn chuỗi.

💡 Đề xuất: Tối ưu hóa danh mục cho các món thuộc nhóm bán chậm (Low performers) và tập trung Marketing cho các dòng sản phẩm top đầu.

⏰ Thời gian & Khung giờ cao điểm (Peak Hours & Operations)
📈 Khung giờ vàng: Doanh số đạt đỉnh vào khoảng 8h - 10h sáng (đáp ứng nhu cầu mua mang đi trước giờ làm) và tăng nhẹ vào khung giờ nghỉ trưa.

💡 Đề xuất: Tăng cường nhân sự ca sáng để giảm thời gian chờ đợi của khách hàng; chuẩn bị sẵn nguyên vật liệu từ đầu ngày.

🛒 Giá trị đơn hàng trung bình (Average Order Value - AOV)
📈 Hành vi chi tiêu: Phần lớn khách hàng chỉ phát sinh đơn hàng mua 1 món đơn lẻ.

💡 Đề xuất: Triển khai các gói Combo (Nước + Bánh mì/Bánh ngọt) vào khung giờ sáng để kích thích khách hàng chi tiêu nhiều hơn trên mỗi hóa đơn.

📍 Hiệu suất theo Vị trí (Store Location Performance)
📈 Phân hóa chi nhánh: Có sự chênh lệch rõ rệt về mô hình cao điểm giữa các vị trí cửa hàng (Khu văn phòng đông buổi sáng vs Khu thương mại đông buổi tối).

💡 Đề xuất: Điều chỉnh ca làm việc và chương trình khuyến mãi (Happy Hour) linh hoạt riêng cho từng chi nhánh thay vì áp dụng cào bằng.

#### 📈 4. Hình ảnh Dashboard (Dashboard Visuals)
(Lưu ý: Thay tên file dashboard_overview.png bằng tên file ảnh thực tế nằm trong thư mục dashboards/screenshots/ của bạn)

📂 Cấu trúc thư mục (Project Structure)
Plaintext
Coffee Shop Sales/
│
├── dashboards/
│   ├── screenshots/                    # Ảnh chụp màn hình Dashboard sắc nét
│   └── main_dashboard.pbix             # File báo cáo Power BI
│
├── data/
│   ├── raw/                            # Dữ liệu thô ban đầu (Coffee Shop Sales.xlsx)
│   └── processed/                      # Dữ liệu sạch xuất dự phòng (.csv)
│
├── notebooks/
│   ├── 01_initial_eda.ipynb            # [Bước 1] Khảo sát & Thẩm vấn dữ liệu thô
│   ├── 02_etl_pipeline.ipynb           # [Bước 2] Pipeline làm sạch & Nạp vào MySQL
│   └── 03_data_analysis.ipynb          # [Bước 3] Phân tích sâu & Khai thác Insights
│
├── sql/
│   ├── 01_init_schema.sql              # Khởi tạo Schema & Bảng (Staging & Production)
│   └── 02_business_queries.sql        # Truy vấn SQL phục vụ phân tích
│
├── src/                                # Module Python dùng chung (db.py, etl.py)
├── .env                                # Khai báo biến môi trường (Database credentials)
├── .gitignore                          # Cấu hình chặn push file nặng/nhạy cảm
└── README.md                           # Tài liệu tổng quan dự án
#### 🛠️ 5. Hướng dẫn cài đặt & Chạy dự án (How to Run / Installation)
##### 1. Clone repository về máy cục bộ:
Bash
git clone https://github.com/Pham-Minh-Duc/coffee-shop-sales-analysis.git
cd coffee-shop-sales-analysis
##### 2. Cài đặt môi trường & Thư viện:
Bash
# Tạo và kích hoạt môi trường ảo (Khuyên dùng)
python -m venv coffeeShopVenv
source coffeeShopVenv/bin/activate  # Trên Linux/Mac
# coffeeShopVenv\Scripts\activate   # Trên Windows

# Cài đặt thư viện
pip install pandas numpy matplotlib seaborn sqlalchemy pymysql openpyxl python-dotenv
##### 3. Cấu hình Cơ sở dữ liệu MySQL:
Mở MySQL Workbench, chạy file sql/01_init_schema.sql để khởi tạo Database và cấu trúc bảng.

Tạo file .env tại thư mục gốc và điền thông tin kết nối Database của bạn:

Code snippet
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=coffee_shop_db
DB_PORT=3306
4. Thực thi theo thứ tự:
Chạy File Khảo sát: Mở notebooks/01_initial_eda.ipynb để xem đánh giá dữ liệu thô.

Chạy Pipeline ETL: Chạy notebooks/02_etl_pipeline.ipynb để trích xuất, làm sạch và đổ dữ liệu sạch vào bảng fact_sales trong MySQL.

Chạy Phân tích: Mở notebooks/03_data_analysis.ipynb để xem các biểu đồ trực quan và báo cáo Insights.

Mở Dashboard: Dùng Power BI Desktop mở file dashboards/main_dashboard.pbix để tương tác trực quan.