# Stored Procedure: `ThucChay_TinhBoxGiaVang_ByJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-02 23:03:59.237000
- **Ngày sửa cuối**: 2020-08-20 17:20:02.240000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_TinhBoxGiaVang_ByJobs]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME
	DECLARE @NgayGioiHanTinh DATETIME
	
	SET @NgayGioiHanTinh = '2014-01-01';
	
	--SET @dtStart = (
	--				SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh
	--					WHERE DmSanPhamREF IN (385,5005 --	Box Lãi suất tiền gửi
	--											, 5006	--Box Tỉ giá ngoại tệ
	--											, 5007 --Box chung khoan
	--											, 5082 --Box tài trợ thông tin 
	--											) 
	--				)
	
	SET @dtStart = DATEADD(dd,-1, GETDATE())

	IF @dtStart IS NULL
		SET @dtStart = @NgayGioiHanTinh
	ELSE
		SET @dtStart = DATEADD(dd,1, @dtStart)
		
	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	--Tinh Thuc Chay Mobile	
	--SELECT @dtStart,@dtEnd
	EXEC [ThucChay_InsertThucChayDaTinh_BoxGiaVang] @dtStart,@dtEnd	
END

```
