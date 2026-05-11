# Stored Procedure: `Send_ThuChayDaTinhThayDoi_To_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-01 08:54:13.460000
- **Ngày sửa cuối**: 2016-10-01 09:01:09.893000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 01/12/2015
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Send_ThuChayDaTinhThayDoi_To_ThucChayDaTinh] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO ThucChayDaTinh
	SELECT * FROM ThucChayDaTinh_ThayDoi 
	WHERE 1=1
	AND convert(date,NgayThucHien) = convert(date,@NgayThucHien)
	
	INSERT INTO ThucChayDaTinhAdmarket
	SELECT * FROM ThucChayDaTinhAdmarket_ThayDoi 
	WHERE 1=1 AND convert(date,NgayThucHien) = convert(date,@NgayThucHien)

	--Insert ThucChayDaTinhAdmarket do nhan hang bi chuan hoa

	INSERT INTO dbo.ThucChayDaTinhAdmarket
	SELECT * FROM dbo.ThucChayDaTinhAdmarket_NhanChuanHoa
	WHERE CONVERT(DATE,NgayThucHien) = CONVERT(DATE,@NgayThucHien)

END

```
