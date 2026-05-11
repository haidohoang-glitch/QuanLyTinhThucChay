# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhMobileByPhanBoId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-29 08:29:29.170000
- **Ngày sửa cuối**: 2014-11-19 12:25:04.673000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@ContractNo` | `nvarchar(100)` | No |
| `@PhanBoId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC ThucChay_ExcInsertThucChayDaTinhMobileByPhanBoId '2014-05-28','2014-05-28', 'QC950514', 57952

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhMobileByPhanBoId] 
	@StartDate datetime,
	@EndDate DATETIME,
	@ContractNo NVARCHAR(50),
	@PhanBoId	INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong		NVARCHAR(50),  
			@TenWebsite		NVARCHAR(50), 
			@DonViTinh		NVARCHAR(50),
			@BannerType		INT
	
	-- delete du lieu truoc khi insert
	--DELETE FROM ThucChayDaTinh WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND SoHopDong = @ContractNo AND DmSanPhamREF = 342 
	
	set @NgayThucHien = @StartDate
	
	while(@NgayThucHien <= @EndDate)
	BEGIN		
		-- insert data to ThucChayMobileTemp
		--EXEC dbo.ThucChayMobile_InsertToTemp @NgayThucHien, @NgayThucHien
		
		DECLARE Record_Cursor CURSOR FOR 
		SELECT 
			tcm.[Contract],tcm.SiteName, tcm.UnitName, tcm.BannerType
		FROM ThucChayMobileTemp AS tcm
		WHERE tcm.dt			= @NgayThucHien 
			AND tcm.[Contract]	= @ContractNo
			
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TenWebsite, @DonViTinh, @BannerType
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				-- Thuc chay theo don vi tinh CPM, CPC
				 EXEC ThucChayDaTinh_InsertThucChayMobileContractByPhanBoId 
					@NgayThucHien, 
					@SoHopDong, 
					@PhanBoId,
					@TenWebsite, 
					@DonViTinh, 
					@BannerType
				
			FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TenWebsite, @DonViTinh, @BannerType
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		-- Thuc chay khong hop dong
		 --EXEC dbo.ThucChayDaTinh_InsertThucChayMobileNoContract @NgayThucHien
		
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
	
	SELECT '1'
END


```
