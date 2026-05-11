# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-10 09:45:04.457000
- **Ngày sửa cuối**: 2016-10-12 14:01:56.310000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayUpdateGiaTriThayDoi` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan] '2016-10-09'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan] 
	@NgayUpdateGiaTriThayDoi DATETIME --Ngay thu hien muon update gia tri thay doi

AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @DmNhanHangREF INT, @NhanHang NVARCHAR(200),@IsChuanHoaQK INT = 1
	, @TenNhanHang NVARCHAR(200), @DmNhanHangThayDoiREF INT
	, @LastModifiedBy NVARCHAR(50), @LastModifiedAt DATETIME
	, @HopDongID INT, @SoHopDong nvarchar(50)
	, @HopDongChiTietREF int, @DmSanPhamREF int, @TenSanPham nvarchar(100), @DonViTinh NVARCHAR(100)
	, @ThanhTienThucChay BIGINT
	, @SoLuongThucChay	BIGINT
	, @CONTENT_LOG NVARCHAR(Max) = ''
	, @NgayThuHienCapNhat DATETIME

	SET @NgayThucHien = CONVERT(DATE,GETDATE())
	
	TRUNCATE TABLE dbo.ThucChayDaTinhAdmarket_xulynhan

	DECLARE Record_Cursor CURSOR FOR 
	--DANH SACH NHAN HANG BI CHUA HOA SANG NHAN HANG KHAC
		
	SELECT DISTINCT DmNhanHangREF_giam, DmNhanHangDungID_Tang, HopDongID, HopDongChiTietREF 
	FROM ABM_Tuyetnta.[dbo].[NH_PERFORMANCE_DACHUANHOA$]
	--WHERE HopDongChiTietREF = 93048
	--AND nh.DmNhanHangID = 44994
	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor into @DmNhanHangREF, @DmNhanHangThayDoiREF, @HopDongID, @HopDongChiTietREF
	WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT 'Cap nhat gia tri thay doi cho ThucChayDaTinhAdmarket khi nhan hang duoc chuan hoa'
			SET @NgayThuHienCapNhat = @NgayThucHien
			IF(@IsChuanHoaQK = 1)
						SET @NgayThuHienCapNhat = @NgayUpdateGiaTriThayDoi
			--1. Xac nhung hop dong chi tiet nao tren ThucChayDatinhAdmarket co nhan hang cung voi nhan hang thay doi
			--2. Thuc hien update gia tri thay doi cho cac hop dong nay.
			-- de thuc hien update gia tri thay doi cho thucchaydatinh thi phai xac dinh duoc ban ghi cuoi cua nhan do ung voi hop dong chi tiet
			DECLARE Record_Cursor_nhanhang CURSOR FOR
			SELECT * FROM
			(
				SELECT HopDongID, SoHopDong, HopDongChiTietREF, NhanHang
					, DmSanPhamREF, TenSanPham, DonViTinh
					, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ThanhTienThucChay
					, SUM(SoLuongThucChay+ SoLuongThayDoi) SoLuongThucChay
				FROM dbo.ThucChayDaTinhAdmarket
				where 1=1 AND NgayThucHien <= @NgayThuHienCapNhat --HAIDH CHO NAY CAN XEM LAI
				AND NhanHang NOT LIKE('%,%') AND NhanHang <> '' AND NhanHang <> '0'
				GROUP BY  HopDongID, SoHopDong, HopDongChiTietREF
					, DmSanPhamREF, TenSanPham, NhanHang, DonViTinh
			)DS 
			WHERE CONVERT(INT,DS.NhanHang) = @DmNhanHangREF
			AND DS.HopDongID = @HopDongID
			AND DS.HopDongChiTietREF = @HopDongChiTietREF
			OPEN Record_Cursor_nhanhang
				
			FETCH NEXT FROM Record_Cursor_nhanhang into @HopDongID, @SoHopDong, @HopDongChiTietREF, @NhanHang
					, @DmSanPhamREF, @TenSanPham ,@DonViTinh, @ThanhTienThucChay, @SoLuongThucChay
				
			WHILE @@FETCH_STATUS = 0
			BEGIN
				PRINT 'THANH TIEN THUC CHAY: ' + CONVERT(NVARCHAR(100),@ThanhTienThucChay)
				IF(@ThanhTienThucChay <> 0)
				BEGIN
					PRINT 'THUC HIEN CAP NHAT GIA TRI THAY DOI CHO TABLE ThucChayDaTinhAdmarket'
					SET @CONTENT_LOG = N'Ngày' + CONVERT(NVARCHAR(100), @NgayThucHien) + N'Nhãn hàng bị chuẩn hóa tu nhan :' + CONVERT(NVARCHAR(50), @DmNhanHangREF) + ' thành :' + CONVERT(NVARCHAR(50),@DmNhanHangThayDoiREF)
					--EXEC  [dbo].[ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan] 
					EXEC  [dbo].[ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan_v2]
					-- Add the parameters for the stored procedure here
						@NgayThuHienCapNhat ,
						@HopDongID,
						@DmSanPhamREF,
						@HopDongChiTietREF,
						@DonViTinh,
						@DmNhanHangREF,
						@DmNhanHangThayDoiREF,
						@ThanhTienThucChay,
						@SoLuongThucChay,
						@CONTENT_LOG
				END
				
				FETCH NEXT FROM Record_Cursor_nhanhang into @HopDongID, @SoHopDong, @HopDongChiTietREF, @NhanHang
					, @DmSanPhamREF, @TenSanPham, @DonViTinh, @ThanhTienThucChay, @SoLuongThucChay
			END
			CLOSE Record_Cursor_nhanhang
			DEALLOCATE Record_Cursor_nhanhang
		FETCH NEXT FROM Record_Cursor into @DmNhanHangREF, @DmNhanHangThayDoiREF, @HopDongID, @HopDongChiTietREF
		END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
		
	
	SELECT '1'
END


--EXEC [ThucChay_UpdateThucChayDaTinhAdmarket_NhanHangChuanHoa] '2016-04-21','2016-04-21'

```
