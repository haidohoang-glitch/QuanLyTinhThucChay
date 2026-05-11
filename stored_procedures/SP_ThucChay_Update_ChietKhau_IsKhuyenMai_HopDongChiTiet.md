# Stored Procedure: `ThucChay_Update_ChietKhau_IsKhuyenMai_HopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-16 15:07:08.373000
- **Ngày sửa cuối**: 2018-08-16 15:08:22.780000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_Update_ChietKhau_IsKhuyenMai_HopDongChiTiet]
*/
CREATE  PROCEDURE [dbo].[ThucChay_Update_ChietKhau_IsKhuyenMai_HopDongChiTiet] 
AS
BEGIN
	UPDATE dbo.HopDongChiTiet
	SET IsKhuyenMai = 1
	WHERE IsKhuyenMai = 0 AND ChietKhau = 100
	AND DeletedStatus = 0
	AND CONVERT(DATE,LastModifiedAt) >= '2017-01-01'
END



```
