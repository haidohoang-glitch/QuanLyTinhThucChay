# Stored Procedure: `ThucChay_PR_Job_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-27 10:11:10.433000
- **Ngày sửa cuối**: 2025-10-27 10:27:58.727000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


/*
 exec [dbo].[ThucChay_PR_Job_ByNgayThucHien]
	 @NgayGhiNhan = '2025-10-25'
*/

CREATE PROCEDURE [dbo].[ThucChay_PR_Job_ByNgayThucHien]
	 @NgayGhiNhan DATE
AS
BEGIN
	DECLARE @NgayDanhSoGioiHan DATE, @NgayCheckThayDoi DATE
	
	--SET @NgayGhiNhan = (
	--					SELECT TOP(1) NgayThucHien FROM ABM_data_thucchay.dbo.ThucChayDaTinh
	--					WHERE DmSanPhamREF IN (141,245,250,637,305)
	--					AND NOT (DmHinhThucQuangCao IN (42, 13) or DmLoaiBannerREF = 18)
	--					ORDER BY NgayThucHien DESC
	--				)


	SET @NgayCheckThayDoi = @NgayGhiNhan
	SET @NgayDanhSoGioiHan = DATEADD(YEAR, -4, @NgayGhiNhan)
	

	EXEC [dbo].[ThucChay_PR_ThucChayDaTinh] @NgayGhiNhan, @NgayCheckThayDoi, @NgayDanhSoGioiHan
	
END

```
