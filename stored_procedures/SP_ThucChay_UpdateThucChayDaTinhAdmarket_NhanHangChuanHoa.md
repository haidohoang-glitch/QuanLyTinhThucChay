# Stored Procedure: `ThucChay_UpdateThucChayDaTinhAdmarket_NhanHangChuanHoa`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-09-26 14:00:42.133000
- **Ngày sửa cuối**: 2018-11-07 15:53:03.983000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@IsChuanHoaQK` | `int(4)` | No |
| `@NgayUpdateGiaTriThayDoi` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateThucChayDaTinhAdmarket_NhanHangChuanHoa] '2016-09-09','2016-09-09',1,'2016-10-12'

CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayDaTinhAdmarket_NhanHangChuanHoa] 
	@StartDate datetime,
	@EndDate DATETIME,
	@IsChuanHoaQK INT, --0 Du lieu update gia tri thay doi theo ngay chuan hoa cua nhan
					   --, 1 Du lieu update gia tri thay doi theo ngày @NgayUpdateGiaTriThayDoi
	@NgayUpdateGiaTriThayDoi DATETIME --Ngay thu hien muon update gia tri thay doi

AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @DmNhanHangREF INT, @NhanHang NVARCHAR(200)
	, @TenNhanHang NVARCHAR(200), @DmNhanHangThayDoiREF INT
	, @LastModifiedBy NVARCHAR(50), @LastModifiedAt DATETIME
	, @HopDongID INT, @SoHopDong nvarchar(50)
	, @HopDongChiTietREF int, @DmSanPhamREF int, @TenSanPham nvarchar(100), @DonViTinh NVARCHAR(100)
	, @ThanhTienThucChay BIGINT
	, @SoLuongThucChay	BIGINT
	, @CONTENT_LOG NVARCHAR(Max) = ''
	, @NgayThuHienCapNhat DATETIME

	SET @NgayThucHien = @StartDate
	
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
	
		DECLARE Record_Cursor CURSOR FOR 
		--DANH SACH NHAN HANG BI CHUA HOA SANG NHAN HANG KHAC
		SELECT nh.DmNhanHangID, nh.TenNhanHang, nh.DmNhanHangThayDoiID
		, nh.LastModidfiedBy, nh.LastModifiedAt 
		FROM [192.168.23.217].BRAND.dbo.DmNhanHang nh
		WHERE ISNULL(nh.DmNhanHangThayDoiID,0) <> 0
		AND nh.DeletedStatus = 1
		AND CONVERT(DATE,nh.LastModifiedAt) = @NgayThucHien
		--AND nh.DmNhanHangID = 49081
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @DmNhanHangREF, @TenNhanHang, @DmNhanHangThayDoiREF
		, @LastModifiedBy, @LastModifiedAt
			
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
						EXEC [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinhAdmarket_nhanhang] 
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
			FETCH NEXT FROM Record_Cursor into @DmNhanHangREF, @TenNhanHang, @DmNhanHangThayDoiREF
			, @LastModifiedBy, @LastModifiedAt
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END 
	
	SELECT '1'
END


--EXEC [ThucChay_UpdateThucChayDaTinhAdmarket_NhanHangChuanHoa] '2016-04-21','2016-04-21'

```
