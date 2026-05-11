# Stored Procedure: `ThucChayGGFBInput_SearchHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-08 17:52:03.130000
- **Ngày sửa cuối**: 2015-07-08 17:52:03.130000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChayGGFBInput_SearchHopDong] 'N'
CREATE PROCEDURE [dbo].[ThucChayGGFBInput_SearchHopDong]
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT distinct TOP 30 hd.SoHopDong AS id, hd.SoHopDong AS ten
	FROM HopDong hd INNER JOIN 
	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE hd.SoHopDong LIKE '%'+@SoHopDong+'%'
	AND hd.TrangThaiHopDong<>3 AND hd.DeletedStatus = 0
	AND hdct.DmSanPhamREF in (423,306)
	AND hdct.DeletedStatus = 0
	--AND hdct.TrangthaiThucChay <> 3
END

```
