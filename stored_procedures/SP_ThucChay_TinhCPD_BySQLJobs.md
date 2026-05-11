# Stored Procedure: `ThucChay_TinhCPD_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-02 13:29:16.160000
- **Ngày sửa cuối**: 2023-06-30 17:35:10.643000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--


CREATE PROCEDURE [dbo].[ThucChay_TinhCPD_BySQLJobs]
	-- Add the parameters for the stored procedure here

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

	--SET @dtStart = '2017-07-07'
	--SET @dtEnd = '2017-07-07'
	--Tinh Thuc Chay CPD
	EXEC dbo.[ThucChay_InsertThucChayDaTinh_CPD_DotChay] @dtStart,@dtEnd

	--Tinh Thuc Chay CPD Khong Dot Chay
	PRINT 'Insert CPD Khong Dot Chay'
	print convert(nvarchar(100),getdate(),120)
	EXEC dbo.[ThucChay_InsertThucChayDaTinh_CPD_KhongDotChay] @dtStart,@dtEnd
	
	--Update gia tri thay doi CPD
	SET @NgayThucHien = CONVERT(date,@dtEnd)
	print convert(nvarchar(100),getdate(),120)
	print 'ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD'
	EXEC dbo.[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD] @NgayThucHien

	print convert(nvarchar(100),getdate(),120)
	print 'ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDonGiaTheoDVT'
	EXEC dbo.[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDonGiaTheoDVT] @NgayThucHien

	--bao gom ca thay doi treo và treo sau
	print convert(nvarchar(100),getdate(),120)
	print 'ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDotChayTD'
	EXEC dbo.[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDotChayTD] @NgayThucHien
	
	--PRINT 'Update gia tri thay doi Khong Dot Chay' --comment do ko thay chay cpd kong dot chay 20210804
	--Thuc hien mo lai CPD Khong Dot chay tu ngay 03/12/2022 do co phat sinh CPD Khong Dot Chay

	----Update gia tri thay doi CPD Khong Dot Chay
	PRINT '[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChay]'
	EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChay] @NgayThucHien
	PRINT '[ThucChay_CheckThucTreoThayDoi_CPDKhongDotChay]'
	EXEC [ThucChay_CheckThucTreoThayDoi_CPDKhongDotChay] @NgayThucHien

	--HAIDH COMMENT THUC HIEN TRIEN KHAI NGÀY 10/10/2022 CHO NHOM CPD DONVIGOI
	print convert(nvarchar(100),getdate(),120)
	print N'ThucChay_InsertThucChayDaTinh_CPD_DonViGoi' 
	EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPD_DonViGoi] 
	@NgayThucHien = @NgayThucHien

	print convert(nvarchar(100),getdate(),120)
	print N'ThucChay_CheckAndUpdateGTTDThucChayDaTinh_CPD_DonViGoi' 
	EXEC [dbo].[ThucChay_CheckAndUpdateGTTDThucChayDaTinh_CPD_DonViGoi] 
	@NgayThucHien = @NgayThucHien

END

```
