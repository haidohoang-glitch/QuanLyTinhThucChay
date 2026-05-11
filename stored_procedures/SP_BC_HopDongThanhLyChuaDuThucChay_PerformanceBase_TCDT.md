# Stored Procedure: `BC_HopDongThanhLyChuaDuThucChay_PerformanceBase_TCDT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-08 16:14:26.770000
- **Ngày sửa cuối**: 2025-11-03 16:21:10.197000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- Tạo Store Procedure với tham số @ToDate
-- @ToDate: Ngày giới hạn tính 'Thực Chạy' (nếu NULL, sẽ lấy MAX(NgayThucHien) từ bảng)

CREATE PROCEDURE dbo.BC_HopDongThanhLyChuaDuThucChay_PerformanceBase_TCDT
    @ToDate DATETIME = NULL -- Tham số đầu vào tùy chọn
AS
BEGIN
    -- Ngăn chặn hiển thị số lượng dòng bị ảnh hưởng
    SET NOCOUNT ON;
	--DECLARE    @ToDate DATETIME= NULL
    -- Xử lý tham số @ToDate nếu NULL hoặc rỗng
    IF @ToDate IS NULL OR ISNULL(@ToDate, '') = ''
    BEGIN
        SELECT @ToDate = MAX(NgayThucHien)
        FROM dbo.KS_ThucChay_TCDT;
    END
     
    -- Lấy các thông tin hợp đồng và chi tiết hợp đồng
    IF OBJECT_ID('tempdb..#ContractDetails') IS NOT NULL DROP TABLE #ContractDetails;
    SELECT  hd.SoHopDong,
            hd.Nam,
            hd.HopDongID,
            hdct.HopDongChiTietID                         AS PhanBoID,
            hdct.DmLoaiREF                                AS HinhThucQuangCaoID,
            hdct.TenLoai                                  AS TenHinhThucQuangCao,
            hdct.TenSanPham,
            hdct.TenLoaiBanner                            AS LoaiBanner,
            hdct.SoLuong,
            hdct.DonGia,
            hdct.ChietKhau, 
            hdct.NhanHang,                                -- ✅ thêm cột NhanHang
            --ROUND(hdct.ThanhTien, 0)                     AS ThanhTienPhanBo
            CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong * hdct.DonGia
                 ELSE ROUND(hdct.ThanhTien, 0)
            END                                           AS ThanhTien_ThanhTienKM
    INTO #ContractDetails
    FROM dbo.Hopdong hd
    INNER JOIN dbo.HopDongChiTiet hdct 
            ON hd.HopDongID = hdct.HopDongFK AND hdct.DeletedStatus = 0
    WHERE 1 = 1
      AND hd.TrangThaiHopDong NOT IN (0, 3)
      -- HTQC Performance
      AND hdct.DmLoaiREF IN (26, 5010, 5038, 5000)
      -- Tối ưu thêm điều kiện năm (2024 trở đi) ngay tại đây
      AND hd.Nam >= 2024; 

    -- DS hđ có file Thanh ly, Nghiem Thu
    IF OBJECT_ID('tempdb..#Hd_ThanhLy') IS NOT NULL DROP TABLE #Hd_ThanhLy;
    SELECT  hdaf.HopDongREF,
            --MAX(hdaf.DATE_CREATE_DOCUMENT)               AS NgayUpfileThanhLyNghiemThu
            MAX(hdaf.CreatedAt)                           AS NgayUpfileThanhLyNghiemThu
    INTO #Hd_ThanhLy
    FROM HopDongAttachFile hdaf
    WHERE hdaf.HopDongREF > 0
      AND hdaf.HopDongREF IN (SELECT DISTINCT HopDongID FROM #ContractDetails)
      AND (
            hdaf.FileTypeREF IN (7, 21, 51, 52)
            OR hdaf.[fileName] LIKE '%BBTL%'
          )
      AND hdaf.DeletedStatus <> 1
      -- KHông lấy hđ mới up TL trong ngày           
      --AND hdaf.DATE_CREATE_DOCUMENT < DATEADD(DAY, 1, CONVERT(DATE, GETDATE())) -- bỏ qua do lấy ở DB này là chậm 1 ngày rồi
      AND YEAR(hdaf.CreatedAt) >= 2025			
    GROUP BY hdaf.HopDongREF;    

    -- Thuc chay hop dong theo @ToDate    
    IF OBJECT_ID('tempdb..#Thucchay_HD') IS NOT NULL DROP TABLE #Thucchay_HD;
    SELECT  t.HopDongID, 
            t.HopDongChiTietID,
            SUM(CAST(ISNULL(t.ThanhTienThucChayKM,0) AS DECIMAL(19,2)))
          + SUM(CAST(ISNULL(t.ThanhTienThucChay,  0) AS DECIMAL(19,2))) AS ThucChay
    INTO #Thucchay_HD
    FROM dbo.KS_ThucChay_TCDT t        
    -- Sử dụng biến @ToDate đã được xử lý
    WHERE t.HopDongID IN (SELECT DISTINCT HopDongID FROM #ContractDetails)
      AND t.NgayThucHien <= @ToDate		
    GROUP BY t.HopDongID, t.HopDongChiTietID;
		
    -- Câu lệnh SELECT chính
    SELECT  hdct.Nam                                   AS NamDanhSo,
            hdct.SoHopDong,
            hdct.HopDongID,
            hdct.PhanBoID,
            hdct.TenHinhThucQuangCao,
            hdct.TenSanPham,
            hdct.NhanHang,                              -- ✅ hiển thị NhanHang
            hdct.LoaiBanner,
            FORMAT(hdct.SoLuong, '#,##0')               AS SoLuong, --dbo.FormatNumber(hdct.SoLuong)  AS SoLuong,
            FORMAT(hdct.DonGia,  '#,##0')               AS DonGia,  --dbo.FormatNumber(hdct.DonGia)   AS DonGia,
            --FORMAT(CAST(hdct.ChietKhau AS INT), 'N0', 'vi-VN')   AS ChietKhau -- (tuỳ chọn) bỏ .00 cho nhìn gọn
            hdct.ChietKhau,
            FORMAT(CAST(hdct.ThanhTien_ThanhTienKM AS MONEY), '#,##0') AS ThanhTien_ThanhTienKM,			
            FORMAT(ISNULL(c.ThucChay, 0), '#,##0')          AS ThucChay,
            FORMAT(ROUND(hdct.ThanhTien_ThanhTienKM - ISNULL(c.ThucChay, 0), 0), '#,##0') AS [TongTienHD-TongThucChay],           
            tl.NgayUpfileThanhLyNghiemThu,
            DATEDIFF(DAY, tl.NgayUpfileThanhLyNghiemThu, GETDATE())     AS SoNgayDaUpTL
    FROM #ContractDetails hdct 
    LEFT JOIN #Thucchay_HD c 
           ON c.HopDongID = hdct.HopDongID 
          AND c.HopDongChiTietID = hdct.PhanBoID
    -- Chỉ lấy các hợp đồng có file thanh lý/nghiệm thu
    INNER JOIN #Hd_ThanhLy tl 
           ON hdct.HopDongID = tl.HopDongREF
    WHERE 1 = 1
      -- Lọc điều kiện: Giá trị còn lại lớn hơn 1000
      AND ABS(ROUND((hdct.ThanhTien_ThanhTienKM - ISNULL(c.ThucChay, 0)), 0)) > 1000   
      --AND c.HopDongChiTiet_ID = 741913
	  AND ( ROUND(ISNULL(hdct.SoLuong,0),0) <> 0 OR ROUND(ISNULL(hdct.DonGia,0),0) <> 0)
	  AND hdct.ChietKhau <> 100
    ORDER BY hdct.Nam DESC, ROUND(hdct.ThanhTien_ThanhTienKM - ISNULL(c.ThucChay, 0), 0) DESC;
		
    DROP TABLE #Hd_ThanhLy;
    DROP TABLE #Thucchay_HD; 
    DROP TABLE #ContractDetails;
END

```
