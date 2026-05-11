# Stored Procedure: `ThucChay_TinhCPD_BySQLJobs_20240920`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-09-30 09:32:32.353000
- **Ngày sửa cuối**: 2024-09-30 09:32:32.353000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Created by:	DWH\haidh
-- Optimized date: 20-09-2024 by DWH\trangtth
-- Description:	chốt thực chạy sản phẩm CPD 
-- =============================================


create PROCEDURE [dbo].[ThucChay_TinhCPD_BySQLJobs_20240920]
AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME, @NgayThucHien DATETIME
	
	SET @dtStart = (
					SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh
						WHERE DmSanPhamREF IN (140,564,549,5082)  
						AND NOT( DmHinhThucQuangCao = 13 OR DmLoaiBannerREF in (17,18))
					)
	
		
	SET @dtEnd = GETDATE()
	
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	
	SET @dtStart = DATEADD(dd,1, @dtStart)

	--Tinh Thuc Chay CPD
	--PRINT ( N'Bat dau ThucChay_InsertThucChayDaTinh_CPD_DotChay_20240920' )
	--PRINT ( GETDATE())
	EXEC dbo.[ThucChay_InsertThucChayDaTinh_CPD_DotChay_20240920] @dtStart,@dtEnd
	--PRINT ( N'Ket thuc ThucChay_InsertThucChayDaTinh_CPD_DotChay_20240920' )
	--PRINT ( GETDATE())

	--Tinh Thuc Chay CPD Khong Dot Chay
	--PRINT ( N'Bat dau ThucChay_InsertThucChayDaTinh_CPD_KhongDotChay_20240920' )
	--PRINT ( GETDATE())
	EXEC dbo.[ThucChay_InsertThucChayDaTinh_CPD_KhongDotChay_20240920] @dtStart,@dtEnd
	--PRINT ( N'Ket thuc ThucChay_InsertThucChayDaTinh_CPD_KhongDotChay_20240920' )
	--PRINT ( GETDATE())

	--Tinh thucchay CPD DVG
	--PRINT ( N'Bat dau ThucChay_InsertThucChayDaTinh_CPD_DonViGoi_20240920' )
	--PRINT ( GETDATE())
	EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPD_DonViGoi_20240920] 
	@NgayThucHien = @NgayThucHien
	--PRINT ( N'Ket thuc ThucChay_InsertThucChayDaTinh_CPD_DonViGoi_20240920' )
	--PRINT ( GETDATE())
	
	--Update gia tri thay doi CPD
	SET @NgayThucHien = CONVERT(date,@dtEnd)
	--PRINT ( N'Bat dau ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD_20240920' )
	--PRINT ( GETDATE())
	EXEC dbo.[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD_20240920] @NgayThucHien
	--PRINT ( N'Ket thuc ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD_20240920' )
	--PRINT ( GETDATE())

	----Update gia tri thay doi CPD Khong Dot Chay
	--PRINT ( N'Bat dau ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChay_20240920' )
	--PRINT ( GETDATE())
	EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChay_20240920] @NgayThucHien
	--PRINT ( N'Ket thuc ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChay_20240920' )
	--PRINT ( GETDATE())

	-- Update gia tri thay doi CPD DVG
	--PRINT ( N'Bat dau ThucChay_CheckAndUpdateGTTDThucChayDaTinh_CPD_DonViGoi_20240920' )
	--PRINT ( GETDATE())
	EXEC [dbo].[ThucChay_CheckAndUpdateGTTDThucChayDaTinh_CPD_DonViGoi_20240920] 
	@NgayThucHien = @NgayThucHien
	--PRINT ( N'Ket thuc ThucChay_CheckAndUpdateGTTDThucChayDaTinh_CPD_DonViGoi_20240920' )
	--PRINT ( GETDATE())

END





```
