# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiCPMVuotGTHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-15 18:37:17.563000
- **Ngày sửa cuối**: 2014-11-19 12:17:00.143000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE  PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiCPMVuotGTHD] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE	@SoHopDong NVARCHAR(50),	@DmSanPhamREF INT
	
	DECLARE Record_Cursor_HDL CURSOR FOR 
    
	SELECT hdl.sohd, hdl.DmSanPhamREF FROM HopDongLech hdl
	
	OPEN Record_Cursor_HDL

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_HDL INTO @SoHopDong,  @DmSanPhamREF
		
	WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT @SoHopDong
			EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinhCPMByNgayThucHien] @NgayThucHien,@SoHopDong,	0, @DmSanPhamREF
		FETCH NEXT FROM Record_Cursor_HDL INTO @SoHopDong,  @DmSanPhamREF
		END
	CLOSE Record_Cursor_HDL
	DEALLOCATE Record_Cursor_HDL
		
	
	SELECT 2
END

--EXEC [ThucChay_UpdateGiaTriThayDoiCPMVuotGTHD] '2014-04-14'

```
