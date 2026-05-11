# Stored Procedure: `usp_SelectDmNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-27 10:19:03.920000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `varchar(1000)` | No |

## Definition (Source Code)

```sql
/************************************************************
 * Code formatted by SoftTree SQL Assistant © v6.0.70
 * Time: 11/21/2013 5:54:41 PM
 ************************************************************/

CREATE PROCEDURE [dbo].[usp_SelectDmNhanHang]
	@DmNhanHangID VARCHAR(1000)
AS
BEGIN
	SET NOCOUNT ON;
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	
	DECLARE @Result NVARCHAR(MAX);
	
	SET @Result = @DmNhanHangID;
	
	SELECT [DmNhanHangID],
	       [TenNhanHang],
	       [DmNghanhHangREF],
	       [NhanSuSoYeuLyLichREF],
	       [DmNhanHangThayDoiID],
	       [TenNghanhHang] = STUFF(
			   (
				   SELECT ',' + md.TenNghanhHang
				   FROM   DmNghanhHang md
				   WHERE md.DeletedStatus <> 1 AND md.DmNghanhHangID IN (SELECT *
												FROM   dbo.Split(DmNhanHang.DmNghanhHangREF, ','))
						  FOR XML PATH(''), TYPE
			   ).value('.', 'NVARCHAR(MAX)'),
			   1,
			   1,
			   ''),
	         [TenNhanSu] = STUFF(
			   (
				   SELECT ';' + ns.HoVaTen
				   FROM   NhanSuSoYeuLyLichFull ns
				   WHERE ns.DeletedStatus <> 1 AND  ns.NhanSuSoYeuLyLichID IN (SELECT *
												FROM   dbo.Split(DmNhanHang.NhanSuSoYeuLyLichREF, ','))
						  FOR XML PATH(''), TYPE
			   ).value('.', 'NVARCHAR(MAX)'),
			   1,
			   1,
			   ''),
	       [CreatedBy],
	       [CreatedAt],
	       [LastModidfiedBy],
	       [LastModifiedAt],
	       [DeletedStatus],
	       [PrintStatus],
	       [RecordStatus]
	FROM   [dbo].[DmNhanHang]
	WHERE  [DmNhanHangID] IN (SELECT *
	                          FROM   dbo.[Split](@Result, ','))
	       AND DeletedStatus <> 1
END

```
