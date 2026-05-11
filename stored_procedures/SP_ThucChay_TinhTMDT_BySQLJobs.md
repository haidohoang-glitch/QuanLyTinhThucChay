# Stored Procedure: `ThucChay_TinhTMDT_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 17:00:23.640000
- **Ngày sửa cuối**: 2015-12-01 10:19:30.660000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_TinhTMDT_BySQLJobs]

CREATE PROCEDURE [dbo].[ThucChay_TinhTMDT_BySQLJobs]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME, @NgayThucHien DATETIME
	-- Tin vip	241
	-- Box nổi bật	264
	-- Box sản phẩm Hot	300
	-- Siêu chăm sóc	268
	-- Tin vip xuyên trang	248
	-- sàn BĐS	270
	-- Tin nổi bật	243
	-- Top giao dịch hot 244
	-- Tin đính 249
	SET @dtStart = (
					SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh
						WHERE DmSanPhamREF IN (241,264,300,268,248,270,243,244,249)  
					)
	
	
	--SET @dtStart = '2014-09-13'
	--SET @dtEnd = '2014-09-13'
	
	SET @dtEnd = GETDATE()
	
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	
	SET @dtStart = DATEADD(dd,1, @dtStart)
	--Tinh Thuc Chay TMDT
	EXEC [ThucChay_InsertThucChayDaTinh_SP_TMDT] @dtStart,@dtEnd
	
	--Update gia tri thay doi TMDT
	SET @NgayThucHien = CONVERT(date,@dtEnd)
	EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_TMDT] @NgayThucHien
	EXEC [ThucChay_CheckThucTreoThayDoi_TMDT] @NgayThucHien

END

```
