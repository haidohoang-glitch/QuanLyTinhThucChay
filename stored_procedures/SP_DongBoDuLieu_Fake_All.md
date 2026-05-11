# Stored Procedure: `DongBoDuLieu_Fake_All`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-12-25 09:44:26.330000
- **Ngày sửa cuối**: 2020-12-25 09:44:42.060000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE DongBoDuLieu_Fake_All 
	
AS
BEGIN
	DECLARE
		@NgayThucHien DATETIME 
		SET @NgayThucHien = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
	--Dong bo du lieu len Database ABM_Data_Release fake
	--USE ABM_Data_ThucChay
	 EXEC [DongBoDuLieu_GGFB_fake] @NgayThucHien,  @NgayThucHien -- lấy all			
	 	
	--use ABM_Data_Release'2020-12-23'
	--   EXEC ThucChayDaTinhBySanPhamThoiGian_InsertData  '2020-12-23',  '2020-12-23'
	--use Reporting_Data
 --   exec rpt_xuly_dulieu_thucchay_fake  '2020-12-23'
END

```
