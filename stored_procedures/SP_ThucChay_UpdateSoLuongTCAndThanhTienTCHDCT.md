# Stored Procedure: `ThucChay_UpdateSoLuongTCAndThanhTienTCHDCT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-23 17:29:48.320000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.557000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE  PROCEDURE [dbo].[ThucChay_UpdateSoLuongTCAndThanhTienTCHDCT] 
AS
BEGIN
	DECLARE	@SoHopDong NVARCHAR(50),@DmSanPhamREF INT, @HopDongID INT, @TenSanPham NVARCHAR(100)
	DECLARE @SoLuongThucChay INT, @SoLuongThucChayKM INT, @ThanhTienThucChay FLOAT, @ThanhTienThucChayKM FLOAT
	DECLARE @NgayThucHien DATETIME, @HopDongChiTietID INT, @SoLuong INT, @ThanhTien BIGINT, @IsKhuyenMai INT
	DECLARE @ChietKhau INT
	
	
	DECLARE Record_Cursor_HDL CURSOR FOR 
    
	
		SELECT A.SoHopDong, B.*
		, A.SoLuongThucChay, A.SoLuongThucChayKM
		, A.ThanhtienTc
		, A.NgayThucHien
		 FROM 
		(
			SELECT A.*, B.NgayThucHien FROM 
			(
			SELECT tcdt.SoHopDong, tcdt.HopDongID, tcdt.DmSanPhamREF, tcdt.TenSanPham
			, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhtienTc
			, SUM(tcdt.SoLuongThucChay)SoLuongThucChay
			--, SUM(tcdt.ThanhTienThucChayTruocTrietKhau)ThanhTienThucChayTruocTrietKhau
			, SUM(tcdt.SoLuongThucChayKM)SoLuongThucChayKM 
			FROM ThucChayDaTinh tcdt
			WHERE tcdt.DmSanPhamREF IN (231,238,339,240,370)
			GROUP BY tcdt.SoHopDong, tcdt.HopDongID, tcdt.DmSanPhamREF, tcdt.TenSanPham
			)A
			INNER JOIN 
			(
			SELECT * FROM 
			(
			SELECT tcdt.SoHopDong, tcdt.HopDongID, tcdt.DmSanPhamREF, tcdt.TenSanPham
			, MAX(tcdt.NgayThucHien) NgayThucHien
			  FROM ThucChayDaTinh tcdt
			WHERE tcdt.DmSanPhamREF IN (231,238,339,240,370)
			AND tcdt.HopDongChiTietREF = 0
			GROUP BY tcdt.SoHopDong, tcdt.HopDongID, tcdt.DmSanPhamREF, tcdt.TenSanPham
			)B
			WHERE year(b.NgayThucHien) >= 2014
			)B ON A.HopDongID = B.HopDongID AND A.DmSanPhamREF = B.DmSanPhamREF
		)A
		INNER JOIN 
		(
			select hd.HopDongID, hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh) soluong
			, hdct.ThanhTien Thanhtien
			, hdct.IsKhuyenMai
			, hdct.ChietKhau
			 FROM HopDong hd INNER JOIN HopDongChiTiet hdct
			ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.TrangThaiHopDong <> 3
			AND hdct.DmSanPhamREF IN  (231,238,339,240,370)
			AND (hdct.DonViTinh = 'CPM' OR hdct.DonViTinh = 'CPC')
		)B ON A.HopDongID = B.HopDongID AND A.DmSanPhamREF = B.DmSanPhamREF
		ORDER BY B.HopDongID, B.HopDongChiTietID 
	
	OPEN Record_Cursor_HDL

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_HDL INTO @SoHopDong, @HopDongID, @HopDongChiTietID,@DmSanPhamREF, @TenSanPham
	, @SoLuong, @ThanhTien, @IsKhuyenMai, @ChietKhau, @SoLuongThucChay, @SoLuongThucChayKM, @ThanhTienThucChayKM, @ThanhTienThucChay, @NgayThucHien
		
	WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT @SoHopDong
			--INSERT INTO [dbo].[HopDongChiTietThucChayTmp]
   --        ([HopDongChiTietID]
   --        ,[HopDongFK]
   --        ,[DmSanPhamREF]
   --        ,[TenSanPham]
   --        ,[SoLuong]
   --        ,[DonViTinhREF]
   --        ,[DonViTinh]
   --        ,[DonGia]
   --        ,[ChietKhau]
   --        ,[KhuyenMai]
   --        ,[IsKhuyenMai]
   --        ,[ThanhTien]
   --        ,[CreatedBy]
   --        ,[CreatedAt]
   --        ,[SoluongThucChay]
   --        ,[ThanhtienThucChay]
   --        ,[ThucChayDenNgay])
			
	FETCH NEXT FROM Record_Cursor_HDL INTO @SoHopDong, @HopDongID, @HopDongChiTietID,@DmSanPhamREF, @TenSanPham
	, @SoLuong, @ThanhTien, @IsKhuyenMai, @ChietKhau, @SoLuongThucChay, @SoLuongThucChayKM, @ThanhTienThucChayKM, @ThanhTienThucChay, @NgayThucHien
		END
	CLOSE Record_Cursor_HDL
	DEALLOCATE Record_Cursor_HDL
		
	
	SELECT 2
END

--EXEC [ThucChay_UpdateGiaTriThayDoiCPMVuotGTHD] '2014-04-14'

```
