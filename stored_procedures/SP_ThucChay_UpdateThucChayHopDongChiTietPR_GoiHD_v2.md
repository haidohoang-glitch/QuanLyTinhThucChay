# Stored Procedure: `ThucChay_UpdateThucChayHopDongChiTietPR_GoiHD_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-14 09:35:52.650000
- **Ngày sửa cuối**: 2016-03-14 09:42:46.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayHopDongChiTietPR_GoiHD_v2]
	@NgayThucHien datetime
AS

BEGIN
	DECLARE @v_str_thuctreopr NVARCHAR(MAX)
	
	SELECT   @v_str_thuctreopr = COALESCE(@v_str_thuctreopr + ',', '') + CAST(DotChayBooking AS VARCHAR(1000)) 
	FROM ThucChayDaTinh
	WHERE NgayThucHien = @NgayThucHien
	AND DmSanPhamREF IN (141,245,250,637,305)
	AND NOT (DmHinhThucQuangCao = 13 or DmLoaiBannerREF = 18)
	
	SET @v_str_thuctreopr = ISNULL(@v_str_thuctreopr,'')
	
	UPDATE ThucChayHopDongChiTietPR
	SET RecordStatus = 1 
	WHERE ThucChayHopDongChiTietPRID IN (SELECT att.item FROM dbo.ArrayToTable(dbo.Array(@v_str_thuctreopr, ',') ) att)

END

	

--endregion


```
