# Stored Procedure: `ThucChay_ReInsertList_GoiHD_PRBySoHopDong_WithNgayThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-27 14:10:05.747000
- **Ngày sửa cuối**: 2017-12-27 14:22:15.497000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ListSoHopDong` | `nvarchar` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_GoiHD_PRBySoHopDong_WithNgayThucChay] 'QC100000', '2015-01-15', 141

--[dbo].[ThucChay_ReInsertList_GoiHD_PRBySoHopDong_WithNgayThucChay] 'QC8571217,QC8561217,QC8551217,QC8541217,QC8531217,NB0211217,QC8521217', '2017-12-31',141

CREATE PROCEDURE [dbo].[ThucChay_ReInsertList_GoiHD_PRBySoHopDong_WithNgayThucChay] 
	@ListSoHopDong NVARCHAR(max),
	@NgayThucHien DateTime,
	@DmSanPhamREF INT
AS
BEGIN

DECLARE @tblSoHopDong table(SoHopDong nvarchar(100))
DECLARE @SoHopDongcur NVARCHAR(100)
	
	DECLARE Record_Cursor_GoiHD CURSOR FOR 
		SELECT [VALUE] FROM [dbo].[ASD_SPLIT](',',@ListSoHopDong)
		OPEN Record_Cursor_GoiHD

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor_GoiHD into @SoHopDongcur
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				PRINT @SoHopDongcur
				EXEC [ThucChay_InsertThucChayDaTinh_GoiHD_PRBySoHopDong_WithNgayThucChay] @SoHopDongcur, @NgayThucHien, @DmSanPhamREF
			FETCH NEXT FROM Record_Cursor_GoiHD into @SoHopDongcur
			END

		CLOSE Record_Cursor_GoiHD
		DEALLOCATE Record_Cursor_GoiHD
END


```
