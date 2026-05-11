# Stored Procedure: `job_ThucChayDaTinh_ReInsertByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-11-23 16:55:12.140000
- **Ngày sửa cuối**: 2025-04-22 09:32:43.470000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[job_ThucChayDaTinh_ReInsertByHopDong]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = CONVERT(DATE,DATEADD(DD,-1,GETDATE()))
   --SET @NgayThucHien = '2018-05-06'
	--1. SP Thực hiện việc check và tính giá trị thay đổi khi hợp đồng thay đổi thay đổi nội dung
	EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong] @NgayThucHien
	--2. SP thực hiện việc check và tính giá trị thay đổi khi thực treo nhãn hàng thay đổi
	--thay doi ham check nhanhang -> check nhanhang va website khi chi phi thay doi 21/04/2025
	--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang] @NgayThucHien
	EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi] @NgayThucHien
			--------************
	--XU LY HD HUY
    EXEC sp_TC_UpdateGiaTriThayDoi_HDHuy @NgayThucHien,
        @NgayThucHien	
					
	--DECLARE @FromDate DATETIME, @ToDate DATETIME, @NgayThucHien DATETIME
	--SET @FromDate  = '2017-01-01'
	--SET @ToDate = '2017-01-08'
	--SET @NgayThucHien = @FromDate
	--WHILE @NgayThucHien <= @ToDate
	--BEGIN
	--	PRINT @NgayThucHien
	--	--1. SP Thực hiện việc check và tính giá trị thay đổi khi hợp đồng thay đổi thay đổi nội dung
	--	EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong] @NgayThucHien
		----2. SP thực hiện việc check và tính giá trị thay đổi khi thực treo nhãn hàng thay đổi
		--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang] @NgayThucHien
	--	SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
	--END

END

```
