# Stored Procedure: `ThucChay_GGFB_Job_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-27 10:50:48.833000
- **Ngày sửa cuối**: 2025-10-27 10:50:54.570000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql

/*
--truoc khi thuc hien phai update trang thai cua 

--update tc
--set tc.IsCaculatedActual = 0
--		FROM dbo.[ADS_Operating_Result_Map_Order] TC
--		WHERE 1=1 and --CAST(TC.LastModificationTime AS DATE) < @NgayGhiNhan OR 
--		     (CAST(TC.LastModificationTime AS DATE) = @NgayGhiNhan AND TC.IsCaculatedActual = 1  
--			 )

select tc.IsCalc_Result_Quantity, tc.LastModificationTime, *

		FROM dbo.[ADS_Operating_Result_Quantity] TC
		WHERE 1=1 and -- CAST(TC.LastModificationTime AS DATE) < @NgayGhiNhan OR 
		     (CAST(TC.LastModificationTime AS DATE) = @NgayGhiNhan --AND TC.IsCalc_Result_Quantity = 1 
			 )

exec [dbo].[ThucChay_GGFB_Job_ByNgayThucHien] 
	@NgayThucHien	= '2025-10-25'
*/

CREATE PROCEDURE [dbo].[ThucChay_GGFB_Job_ByNgayThucHien] 
	@NgayThucHien	DATE
AS
BEGIN

	SET NOCOUNT ON;

    DECLARE  @NgayDanhSoGioiHan DATE
	

	SET @NgayDanhSoGioiHan = DATEADD(YEAR, -3, @NgayThucHien)

	EXEC [dbo].[ThucChay_GGFB_GhiNhanThayDoi] @NgayThucHien,       
	                                          @NgayThucHien,  
	                                          @NgayDanhSoGioiHan 
	
	EXEC [dbo].[ThucChay_GGFB_GhiNhanPhatSinh] @NgayThucHien ,      
	                                           @NgayDanhSoGioiHan 

	

END

```
