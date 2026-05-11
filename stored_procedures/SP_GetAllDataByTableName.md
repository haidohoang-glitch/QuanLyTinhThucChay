# Stored Procedure: `GetAllDataByTableName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 09:12:52.107000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.600000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |
| `@TenChiTiet` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetAllDataByTableName] 
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50),
	@TenChiTiet nvarchar(50)
AS
BEGIN
	Declare @SQLCommand nvarchar(4000)
	Declare @FieldList nvarchar(4000)
	
	IF (@TableName = 'DmSanPham')
	BEGIN
		set @SQLCommand = 'Select DmSanPhamID, TenSanPham, DmSanPhamID [Id], TenSanPham [Ten]  from ' + @TableName + ' Where DeletedStatus <> 1 Order By '+ @TenChiTiet	
	END
	
	ELSE IF (@TableName = 'DmWebsite')
	BEGIN
		set @SQLCommand = 'Select DmWebsiteID, TenWebsite, DmWebsiteID [Id], TenWebsite [Ten]  from ' + @TableName + ' Where DeletedStatus <> 1 Order By '+ @TenChiTiet	
	END
	
	ELSE IF (@TableName = 'DmPhongBan')
	BEGIN
		set @SQLCommand = 'Select DmPhongBanID, TenPhongBan, MaSoPhongBan, DmPhongBanID [Id], TenPhongBan [Ten]  from ' + @TableName + ' Where DeletedStatus <> 1 Order By '+ @TenChiTiet	
	END
	
	ELSE IF (@TableName = 'DmBoPhanNghiepVu')
	BEGIN
		set @SQLCommand = 'Select DmBoPhanNghiepVuID, TenBoPhanNghiepVu, DmPhongBanFK, DmBoPhanNghiepVuID [Id], TenBoPhanNghiepVu [Ten]  from ' + @TableName + ' Where DeletedStatus <> 1 Order By '+ @TenChiTiet	
	END
	
	ELSE IF (@TableName = 'DmNhom')
	BEGIN
		set @SQLCommand = 'Select DmNhomID, TenNhom, DmBoPhanREF, DmNhomID [Id], TenNhom [Ten]  from ' + @TableName + ' Where DeletedStatus <> 1 Order By '+ @TenChiTiet	
	END
	
	--set @SQLCommand = 'Select * from '+@TableName +' Where DeletedStatus <> 1 Order By '+ @TenChiTiet
	exec(@SQLCommand)			
END

```
