# Stored Procedure: `BaoCaoHDCN_BaoCaoTinhTrangBanCung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-23 12:05:58.063000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.917000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@nameColSort` | `nvarchar(50)` | No |
| `@sort` | `int(4)` | No |
| `@startdate` | `date(3)` | No |
| `@enddate` | `date(3)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DucBM
-- Create date: 23/08/2013
-- Description:	Bao Cao Tình Trạng hợp đồng 
-- =============================================

CREATE PROCEDURE [dbo].[BaoCaoHDCN_BaoCaoTinhTrangBanCung]
	-- Add the parameters for the stored procedure here
	 @PageIndex Int,
	 @RecordCount Int,
	 @nameColSort nvarchar(25),
	 @sort int,
	 @startdate Date,
	 @enddate Date	 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from	
	SET NOCOUNT ON;
	DECLARE @OrderColumn NVARCHAR(500)
	DECLARE @ColumnList NVARCHAR(1000)
	DECLARE @FilterCondition NVARCHAR(1000)
	DECLARE @TableName NVARCHAR(1000)
	DECLARE @StartIndex Int
	DECLARE @MaxRecords Int
	DECLARE @i Int
	DECLARE @PageCount Int
	DECLARE @ApproximatedNumber float	
    DECLARE @SQL NVARCHAR(2000) 
    DECLARE @DauNhay NVARCHAR(50)
    SET @DauNhay = ''''         
    -- SQL Statatement
    
    SET @ColumnList=' SoHopDong,TenNhom,TenNhanVien,NgayNhanHopDongBanCung,NgayChuyenHopDongChoKeToan,GhiChuHopDong,TenMaHopDong '	
	SET @TableName=' HopDong '			
	SET @FilterCondition = ' where DeletedStatus =0 and NgayChuyenHopDongChoKeToan > CONVERT(datetime,'+@DauNhay+'2000/01/01'+@DauNhay+', 120) and NgayNhanHopDongBanCung > CONVERT(datetime,'+@DauNhay+' 2000/01/01'+@DauNhay+', 120)  and TrangThaiHopDong<>3 '	  	
	IF(@startdate <> '')
    BEGIN
       SET @FilterCondition += '  AND NgayDanhSoHopDong >= '+@DauNhay+CONVERT(nvarchar,@startdate)+@DauNhay
    END 
	
	IF(@enddate <> '')
    BEGIN
       SET @FilterCondition +=  '  AND NgayDanhSoHopDong <='+@DauNhay+ CONVERT(nvarchar,@enddate)+@DauNhay
    END        	
    --End SQL Statatement
	--Order	
	IF @sort = 0
	Begin
	    SET @OrderColumn = ' ORDER BY '+@nameColSort+ ' DESC'
	End
    ELSE    
        SET @OrderColumn = ' ORDER BY '+@nameColSort+' ASC'
    --End Order 
	--Phân Trang
    set @ApproximatedNumber=0.49999
	set @i=1
	set @SQL = 'select @MaxRecords=count(*) from '+ @TableName + ' ' + @FilterCondition
	SET @MaxRecords=1
	EXEC sp_executesql @sql, N'@MaxRecords int output', @MaxRecords output	
	
	set @PageCount = round(convert(float,@MaxRecords)/@RecordCount+@ApproximatedNumber,0)
	
	SET @StartIndex = (@PageIndex - 1)*@RecordCount + 1
	Set @MaxRecords = @PageIndex*@RecordCount		
	
	if(@PageCount>=@PageIndex)
	Begin
		SET @SQL = 	'SELECT * FROM 
					(SELECT '+@ColumnList+' , ROW_NUMBER() OVER('+@OrderColumn+')
					 AS rownum from '+@TableName + ' ' + @FilterCondition +') as VitualTable '+
					' WHERE rownum between '+ Convert(nvarchar(50),@StartIndex) + ' and ' + Convert(nvarchar(50),@MaxRecords)			
	END
	ELSE	
		SET @SQL = 'select '+@ColumnList+' from '+@TableName + ' ' + @FilterCondition	
	--End Phân Trang
	EXEC sp_executesql @SQL
	
END

```
