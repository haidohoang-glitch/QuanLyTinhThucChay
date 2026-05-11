# Stored Procedure: `BaoCaoHDCN_HoaDanCanXuatTrongThang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-23 16:28:08.800000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.910000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@NameColSort` | `nvarchar(50)` | No |
| `@Sort` | `int(4)` | No |
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |
| `@KhachHangID` | `int(4)` | No |
| `@NhanVienID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DucBM
-- Create date: 23/08/2013
-- Description:	
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoHDCN_HoaDanCanXuatTrongThang]
	-- Add the parameters for the stored procedure here
	 @PageIndex Int,
	 @RecordCount Int,
	 @NameColSort nvarchar(25),
	 @Sort int,	 
	 @StartDate Date,
	 @EndDate Date,	 
	 @KhachHangID int,
	 @NhanVienID int
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
    DECLARE @SQLSum NVARCHAR(2000)
	SET @DauNhay = ''''         
    
    -- SQL Statatement
    
    SET @ColumnList=' HDHTT.NgayThanhToan , CN.GiaTri as GiaTriHoaDon,CN.NgayXuat,
					  HD.SoHopDong,CN.SoHoaDon, 
					  HDHTT.SoTien as GiaTri, HD.TenNhanVien, HD.TenKhachHang, 
					  ('+@DauNhay+'<FONT color=\"red\"><b>'+@DauNhay+'+ TenPhongBan +'+@DauNhay+'</b></FONT>'+@DauNhay+'+ ISNULL('+@DauNhay+'<br/><FONT color="#4f81bd"><b>'+@DauNhay+'+TenBoPhan+'+@DauNhay+'</b></FONT>'+@DauNhay+','+@DauNhay+@DauNhay+')+ ISNULL('+@DauNhay+'<br/>'+@DauNhay+'+TenNhom,'+@DauNhay+@DauNhay+')) as TenBoPhan ,
					  HD.GiaTriHopDong as TongGiaTriHopDong '	
    
	SET @TableName=' CongNo CN  
					LEFT JOIN HopDong as HD on HD.HopDongId=CN.HopDongREF
					LEFT JOIN HopDongHanThanhToan HDHTT ON HDHTT.HopDongREF = CN.HopDongREF '			

  	SET @FilterCondition = ' Where HD.DeletedStatus = 0  AND HDHTT.NgayThanhToan >='+@DauNhay+ Convert(nvarchar,@StartDate)+@DauNhay+' AND HDHTT.NgayThanhToan <= '+@DauNhay+ Convert(nvarchar,@EndDate) +@DauNhay+' AND (CN.NgayXuat IS NOT NULL)   	
							 AND HD.TrangThaiHopDong <> 3 AND HD.IsBanCung = 1 AND HD.DangSuDung= 1 '	
					
	IF(@KhachHangID <> 0)
    BEGIN
       SET @FilterCondition += '  AND HD.DmKhachHangREF='+CONVERT(nvarchar, @KhachHangID)
    END 
    
    IF(@NhanVienID <> 0)
    BEGIN
       SET @FilterCondition += '  AND HD.SysNhanVienREF='+CONVERT(nvarchar, @NhanVienID)
    END 
	    
	--Order	
	IF @sort = 0
	Begin
	    SET @OrderColumn = ' ORDER BY '+@nameColSort+ ' DESC'
	End
    ELSE    
        SET @OrderColumn = ' ORDER BY '+@nameColSort+' ASC'
    --End Order 
	--Phân Trang
    SET @ApproximatedNumber=0.49999
	SET @i=1
	SET @SQL = 'select @MaxRecords=count(*) from '+ @TableName + ' ' + @FilterCondition
	SET @MaxRecords=1	
	EXEC sp_executesql @sql, N'@MaxRecords int output', @MaxRecords output	
	
	SET @PageCount = round(convert(float,@MaxRecords)/@RecordCount+@ApproximatedNumber,0)
	
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
	--print @SQL
	
	SET @SQLSum='SELECT COUNT(HD.GiaTriHopDong) as SoLuong, SUM( HD.GiaTriHopDong) as Tong from ' + @TableName + ' ' + @FilterCondition	
	EXEC sp_executesql @SQL
	EXEC sp_executesql @SQLSum
END

```
