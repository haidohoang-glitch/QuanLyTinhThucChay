# Stored Procedure: `ThucChay_UpdateDmBoPhanIDAndDmPhongBanID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-09 04:54:17.680000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.737000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_UpdateDmBoPhanIDAndDmPhongBanID] 
	-- Add the parameters for the stored procedure here

AS
BEGIN
	update HopDong set
	DmPhongBanREF = dbo.GetIDByTenPhongBan(DmPhongBanREF,TenPhongBan)
	,DmBoPhanREF = dbo.GetIDByTenBoPhanNghiepVu(DmBoPhanREF,TenBoPhan)
END

```
