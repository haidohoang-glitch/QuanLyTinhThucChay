# Stored Procedure: `BI_HoSoNhanCha_DanhSachNhanCha`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:14.723000
- **Ngày sửa cuối**: 2015-06-25 16:17:14.723000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNhanHang` | `nvarchar(600)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[BI_HoSoNhanCha_DanhSachNhanCha] N'Yam'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_DanhSachNhanCha] 
(
	@TenNhanHang NVARCHAR(300)	
)
AS
BEGIN
	SELECT * FROM
	(
		SELECT dcnh.DmNhanHangID, dcnh.TenNhanHang
		, dcnh.TenNhanHang + ' (Level=' + CONVERT(NVARCHAR(50),dcnh.Levels) + ')' TenNhanHangShow
		, dcnh.STT
		  FROM DmCaseNhanHang dcnh
		  INNER JOIN DmNhanHang dnh ON dcnh.DmNhanHangID = dnh.DmNhanHangID
		WHERE dnh.RecordStatus = 1 --DANH SACH NHAN HANG DA DUYET
	)A
	WHERE A.TenNhanHang LIKE '%' +@TenNhanHang + '%'
	ORDER BY A.STT, A.TenNhanHang
END

--EXEC [BI_HoSoNhanCha_DanhSachNhanCha]

```
