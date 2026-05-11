# Stored Procedure: `ThucChay_CheckHopDongVaHopDongChiTietThayDoi_PR_GoiHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-04-29 11:48:04.997000
- **Ngày sửa cuối**: 2016-04-29 12:00:56.463000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongVaHopDongChiTietThayDoi_PR_GoiHD] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@ThoiGianBDTinh DATETIME
AS
BEGIN
	DECLARE @HopDongID INT,
	        @NgayDanhSoHopDong DATETIME,
	        @DmNhanVienREF INT,
	        @DmKhachHangREF INT,
	        @DmHinhThucKhachHangREF INT,
	        @TrangThaiHopDong INT,
	        @HopDongChiTietID INT,
	        @DmHinhThucQuangCaoREF INT,
	        @DmSanPhamREF INT,
	        @TrangThaiHopDongChiTiet INT
	
	DECLARE @CONTENT_LOG  NVARCHAR(MAX),
	        @NGUON_LOG    NVARCHAR(MAX),
	        @SoHopDong    NVARCHAR(100),
	        @LoaiThayDoi	INT --0 Khong co thay doi gi ca, 1 Thay doi thong tin, 2 Hopdong huy hoac HopDongChiTiet bi huy

	SET @LoaiThayDoi = 0	        
	
	DECLARE Record_Cursor_hopdong CURSOR  
	FOR
	SELECT hd.HopDongID,
	       hd.NgayDanhSoHopDong,
	       hd.SysNhanVienREF,
	       hd.DmKhachHangREF,
	       hd.DmHinhThucKhachHangREF,
	       hd.TrangThaiHopDong,
	       hdct.HopDongChiTietID,
	       hdct.DmLoaiREF,
	       hdct.DmSanPhamREF,
	       hdct.DeletedStatus
	FROM   HopDong hd
	       INNER JOIN HopDongChiTiet hdct
	            ON  hd.HopDongID = hdct.HopDongFK
	WHERE  (
	           CASE 
	                WHEN hd.LastModifiedAt > hdct.LastModifiedAt THEN CONVERT(date, hd.LastModifiedAt)
	                ELSE CONVERT(date, hdct.LastModifiedAt)
	           END
	       ) = @NgayThucHien

	OPEN Record_Cursor_hopdong
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_hopdong INTO @HopDongID ,
	        @NgayDanhSoHopDong ,
	        @DmNhanVienREF ,
	        @DmKhachHangREF ,
	        @DmHinhThucKhachHangREF ,
	        @TrangThaiHopDong ,
	        @HopDongChiTietID ,
	        @DmHinhThucQuangCaoREF ,
	        @DmSanPhamREF ,
	        @TrangThaiHopDongChiTiet 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @HopDongID
			
	  FETCH NEXT FROM Record_Cursor_hopdong INTO @HopDongID ,
	        @NgayDanhSoHopDong ,
	        @DmNhanVienREF ,
	        @DmKhachHangREF ,
	        @DmHinhThucKhachHangREF ,
	        @TrangThaiHopDong ,
	        @HopDongChiTietID ,
	        @DmHinhThucQuangCaoREF ,
	        @DmSanPhamREF ,
	        @TrangThaiHopDongChiTiet 
	END
	CLOSE Record_Cursor_hopdong
	DEALLOCATE Record_Cursor_hopdong
		       
END



```
