# Stored Procedure: `Notify_warning_brand_input`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-02 16:04:47.377000
- **Ngày sửa cuối**: 2016-11-03 17:12:16.807000

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
/*
EXEC [dbo].[Notify_warning_brand_input]	'2016-10-31'
*/
CREATE PROCEDURE [dbo].[Notify_warning_brand_input]
	@NgayThucHien DATETIME
AS
BEGIN
	
	----***********CHECK THONG TIN DAU VAO************-----------------
	----0. CO DU LIEU DONG BO NGAY THUC HIEN
	----1. DANH SACH CAC SAN PHAM CHAY CO NHAN TINH THEO THUC TREO	

	EXEC [dbo].[Insert_Notify_warning_brand_input]	@NgayThucHien

	------2. DANH SACH CAC SAN PHAM CHAY CO NHAN TINH THEO HOP DONG CHI TIET
	EXEC [dbo].[Insert_Notify_warning_brand_input_contractdetails]	@NgayThucHien

END

```
