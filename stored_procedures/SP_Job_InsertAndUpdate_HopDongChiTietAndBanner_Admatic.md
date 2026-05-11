# Stored Procedure: `Job_InsertAndUpdate_HopDongChiTietAndBanner_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-07-06 10:18:43.410000
- **Ngày sửa cuối**: 2017-07-06 10:18:54.740000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[Job_InsertAndUpdate_HopDongChiTietAndBanner_Admatic]
CREATE PROCEDURE [dbo].[Job_InsertAndUpdate_HopDongChiTietAndBanner_Admatic]
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = DATEADD(day,-1,GETDATE())
	EXEC [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic] @NgayThucHien

END

```
