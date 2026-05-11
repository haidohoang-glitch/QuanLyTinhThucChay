# Stored Procedure: `usp_NhanHang_SelectByDate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:47.590000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dateSelect` | `varchar(10)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SelectByDate]
	@dateSelect VARCHAR(10)
AS
BEGIN
	SET NOCOUNT ON;
	
	--SET @dateSelect = '21/11/2013';
	
	SELECT DmNhanHangID,dnh.TenNhanHang, dnh.CreatedBy, dnh.CreatedAt,
	       dnh.LastModidfiedBy, dnh.LastModifiedAt, dnh.RecordStatus, dnh.DeletedStatus,
	       [DmNghanhHangREF],DmNhanHangThayDoiID,dnh.RecordStatus,
			[TenNghanhHang] = STUFF(
			   (
				   SELECT ';' + md.TenNghanhHang
				   FROM   DmNghanhHang md
				   WHERE md.DeletedStatus <> 1 AND md.DmNghanhHangID IN (SELECT *
												FROM   dbo.Split(dnh.DmNghanhHangREF, ','))
						  FOR XML PATH(''), TYPE
			   ).value('.', 'NVARCHAR(MAX)'),
			   1,
			   1,
			   '')
	FROM   DmNhanHang dnh
	WHERE  ((
	           CONVERT(VARCHAR(10), CAST(dnh.LastModifiedAt AS DATE), 103) = @dateSelect
	       )
	       OR  (
	               CONVERT(VARCHAR(10), CAST(dnh.CreatedAt AS DATE), 103) = @dateSelect
	       )) AND dnh.DeletedStatus <> 1
	ORDER BY
	       dnh.DmNhanHangID DESC
END

```
