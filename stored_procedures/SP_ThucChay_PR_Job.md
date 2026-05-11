# Stored Procedure: `ThucChay_PR_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-20 11:12:52.387000
- **Ngày sửa cuối**: 2025-10-24 15:05:30.973000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


--EXEC [dbo].[ThucChay_PR_Job]

CREATE PROCEDURE [dbo].[ThucChay_PR_Job]
AS
BEGIN
	DECLARE @NgayGhiNhan DATE, @NgayDanhSoGioiHan DATE, @NgayCheckThayDoi DATE
	
	--SET @NgayGhiNhan = (
	--					SELECT TOP(1) NgayThucHien FROM ABM_data_thucchay.dbo.ThucChayDaTinh
	--					WHERE DmSanPhamREF IN (141,245,250,637,305)
	--					AND NOT (DmHinhThucQuangCao IN (42, 13) or DmLoaiBannerREF = 18)
	--					ORDER BY NgayThucHien DESC
	--				)

	SET @NgayGhiNhan = DATEADD(DAY, -1, GETDATE())
	SET @NgayCheckThayDoi = @NgayGhiNhan
	SET @NgayDanhSoGioiHan = DATEADD(YEAR, -4, @NgayGhiNhan)
	

	EXEC [dbo].[ThucChay_PR_ThucChayDaTinh] @NgayGhiNhan, @NgayCheckThayDoi, @NgayDanhSoGioiHan
	
END

```
