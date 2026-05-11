# Stored Procedure: `ThucChay_GGFB_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-24 17:42:15.903000
- **Ngày sửa cuối**: 2025-05-21 18:03:30.817000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql



CREATE PROCEDURE [dbo].[ThucChay_GGFB_Job] 
	
AS
BEGIN

	SET NOCOUNT ON;

    DECLARE @NgayThucHien	DATE, @NgayDanhSoGioiHan DATE
	
	SET @NgayThucHien = CONVERT(DATE, DATEADD(dd, -1, GETDATE()))	
	SET @NgayDanhSoGioiHan = DATEADD(YEAR, -3, @NgayThucHien)

	EXEC [dbo].[ThucChay_GGFB_GhiNhanThayDoi] @NgayThucHien,       
	                                          @NgayThucHien,  
	                                          @NgayDanhSoGioiHan 
	
	EXEC [dbo].[ThucChay_GGFB_GhiNhanPhatSinh] @NgayThucHien ,      
	                                           @NgayDanhSoGioiHan 

	

END

```
