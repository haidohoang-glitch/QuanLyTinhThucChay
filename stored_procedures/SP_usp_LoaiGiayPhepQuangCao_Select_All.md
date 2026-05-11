# Stored Procedure: `usp_LoaiGiayPhepQuangCao_Select_All`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:23:22.240000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.110000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_LoaiGiayPhepQuangCao_Select_All]
AS
BEGIN
	SELECT DmloaiGiayPhepID,
	       TenLoaiGiayPhep,
	       Ghichu
	FROM   DmLoaiGiayPhepQuangCao
	WHERE  DeletedStatus <> 1
	ORDER BY
	       DmLoaiGiayPhepID ASC
END

```
