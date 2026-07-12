# ☕ Coffee Shop Sales Analysis & ETL Pipeline

## 📌 Tổng quan dự án (Project Overview)
Dự án này tập trung vào việc xây dựng một hệ thống phân tích dữ liệu bán hàng hoàn chỉnh cho một chuỗi cửa hàng cà phê (Coffee Shop Sales). Quy trình bao gồm các bước từ thu thập dữ liệu thô, thiết kế kiến trúc lưu trữ tạm thời (Staging), xây dựng đường ống ETL chuẩn hóa dữ liệu, lưu trữ vào kho dữ liệu (Data Warehouse) trên MySQL, và cuối cùng là khai thác Insights bằng Python (Pandas) cùng Power BI Dashboard.

---

## 📂 Cấu trúc thư mục (Project Structure)
```text
Coffee Shop Sales/
│
├── dashboards/
│   └── Coffee_Shop_Sales_Report.pbix     # Báo cáo trực quan hóa trên Power BI
│
├── data/
│   └── Coffee Shop Sales.xlsx             # File dữ liệu thô ban đầu (Raw Data)
│
├── notebooks/
│   ├── 01_etl_pipeline.ipynb              # Quy trình Extract, Transform, Load vào MySQL
│   └── 02_data_analysis.ipynb             # Phân tích sâu, Feature Engineering & Vẽ biểu đồ
│
├── sql/
│   ├── 01_init_schema.sql               # Tạo cấu trúc bảng (Schema) trong MySQL
│   └── 02_business_queries.sql            # Các câu lệnh SQL truy vấn biểu mẫu
│
├── .gitignore                             # Cấu hình bỏ qua các file dữ liệu nặng khi đẩy lên Git
└── README.md                              # Tài liệu hướng dẫn dự án
```

## 🛠️ Công nghệ sử dụng (Tech Stack)
Ngôn ngữ: Python 3.x

Thư viện phân tích: Pandas, NumPy, Matplotlib, Seaborn

Cơ sở dữ liệu & Kết nối: MySQL, SQLAlchemy, PyMySQL

Công cụ Trực quan hóa: Power BI Desktop

## 🚀 Luồng xử lý dữ liệu (Data Pipeline Flow)
1. Kiến trúc lưu trữ (Data Architecture)
Tầng Staging (Bảng tạm): Dữ liệu thô từ file Excel được đổ trực tiếp vào bảng stg_coffee_sales trong MySQL nhằm đảm bảo tính nguyên bản (Single Source of Truth), toàn bộ các cột giữ nguyên định dạng chuỗi (VARCHAR).

Tầng Production / Data Warehouse: Bảng fact_sales chịu trách nhiệm lưu trữ dữ liệu cốt lõi đã qua xử lý và chuẩn hóa kỹ thuật.

2. Giai đoạn 1: ETL Pipeline (01_etl_pipeline.ipynb)
Extract: Kết nối và trích xuất dữ liệu thô từ tầng Staging của MySQL bằng SQLAlchemy.

Transform:

Kiểm tra và xử lý các giá trị khuyết thiếu (NaN, None).

Ép kiểu dữ liệu chuẩn (transaction_date về datetime64, transaction_id về int).

Sửa lỗi định dạng giờ giấc của cột transaction_time từ dạng phức tạp (timedelta) về chuỗi HH:MM:SS sạch để MySQL không bị lỗi cấu trúc khi nạp.

Load: Sử dụng hàm .to_sql() đẩy toàn bộ dữ liệu sạch vào bảng fact_sales trong Data Warehouse theo cơ chế append an toàn.

3. Giai đoạn 2: Phân tích & Khám phá Insights (02_data_analysis.ipynb)
Dữ liệu sạch được kéo từ fact_sales lên bộ nhớ RAM để tiến hành Feature Engineering và phân tích chuyên sâu mà không làm ảnh hưởng hay thay đổi dữ liệu gốc trong database:

Tạo thêm cột Day_of_Week (Thứ trong tuần) và sắp xếp thứ tự logic tự nhiên từ Thứ 2 đến Chủ Nhật.

Nhóm dữ liệu (groupby) để giải quyết các bài toán kinh doanh trọng tâm.

## 📊 Câu hỏi Kinh doanh & Insights Khai thác (Business Questions)
#### 1.Dòng sản phẩm nào đang là "ngôi sao" của chuỗi cửa hàng ?

Phân tích và trực quan hóa Top 5 sản phẩm bán chạy nhất xét theo cả Số lượng bán ra và Doanh thu ($) mang lại, giúp tối ưu hóa danh mục menu.

#### 2.Thời điểm nào trong tuần cửa hàng đông khách nhất ?

Theo dõi xu hướng lượng khách hàng (số lượng giao dịch) qua các ngày từ Thứ 2 đến Chủ Nhật để tối ưu hóa lịch trình sắp xếp ca làm việc cho nhân viên và chuẩn bị nguyên vật liệu.

#### 3.Khung giờ cao điểm trong ngày ?

Phân nhóm thời gian (Sáng, Chiều, Tối) giúp xác định khoảng thời gian cửa hàng đạt hiệu suất sinh lời cao nhất.

#### 4. Hóa đơn trung bình của 1 khách hàng là bao nhiêu ?

AOV (Average Order Value): giá trị đơn hàng trung bình:
    Đánh giá hành vi chi tiêu và định vị khách hàng: 1 khách hàng sẵn sàng chi bao nhiêu tiền cho 1 lần ghé thăm
    Thước đó cho chiến lược "Upselling" và "Cross-selling": Đây là chỉ số kiểm tra xem nhân viên có làm tốt việc gợi ý khách hàng mua thêm hay không
    Tối ưu hóa doanh thu mà không cần tìm khách hàng mới: 
        Để tăng tổng doanh thu thì quán có 2 cách: Kiếm thêm nhiều khách mới(tốn chi phí marketing) và Khiến mỗi khách hiện tại chi tiền nhiều hơn trên 1 hóa đơn (tăng AOV)
        -> biết được chỉ số này giúp quán đưa ra các quyết định combo hợp lý 

#### 5. Vị trí cửa hàng ảnh hưởng như thế nào đến doanh số ?

Đánh giá tính hiệu quả của mặt bằng và định vị khách hàng tiềm năng
Tối ưu hóa phân bổ nguồn lực và logicstic
Cở sở để ra quyết định mở rộng chuỗi hoặc đóng bớt cửa hàng

#### 6. Khung giờ cao điểm của từng cửa hàng có khác nhau không ?

Tối ưu hóa ca làm việc của nhân viên
Quản lí chuỗi cung ứng và chuẩn bị nguyên vật liệu 
Lên chiến dịch khuyến mãi nhắm trúng đích

## 📈 Kết quả Trực quan hóa (Dashboards)
File Coffee_Shop_Sales_Report.pbix cung cấp một góc nhìn tương tác đa chiều (Interactive Dashboard) cho các nhà quản lý, bao gồm:

Thống kê doanh thu theo thời gian thực (Daily/Weekly/Monthly Sales Trends).

Bản đồ phân bổ doanh thu theo vị trí cửa hàng (Store Location Performance).

Cơ cấu tỷ trọng đóng góp doanh thu của từng nhóm sản phẩm.

## 📝 Hướng dẫn cài đặt & Chạy dự án (Setup & Installation)
#### 1.Clone repository này về máy cục bộ:

Bash
git clone [https://github.com/your-username/coffee-shop-sales.git](https://github.com/your-username/coffee-shop-sales.git)
#### 2.Cài đặt các thư viện cần thiết:

Bash
pip install pandas numpy matplotlib seaborn sqlalchemy pymysql openpyxl
#### 3.Cấu hình Cơ sở dữ liệu:

Chạy file 01_create_tables.sql trong MySQL Workbench để khởi tạo database.

Thay đổi thông số kết nối (USER, PASSWORD, HOST, DB_NAME) trong các file Notebook cho khớp với môi trường máy của bạn.

#### 4.Thực thi:

Chạy lần lượt file 01_etl_pipeline.ipynb để nạp dữ liệu sạch vào MySQL.

Chạy file 02_data_analysis.ipynb để xem các báo cáo phân tích và biểu đồ.