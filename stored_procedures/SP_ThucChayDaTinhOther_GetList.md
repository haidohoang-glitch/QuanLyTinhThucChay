# Stored Procedure: `ThucChayDaTinhOther_GetList`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-16 13:39:42.963000
- **Ngày sửa cuối**: 2014-12-16 13:39:42.963000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@RecordCount` | `int(4)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-12-13
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhOther_GetList] 
	-- Add the parameters for the stored procedure here	
	@PageIndex		int,
	@PageSize		int,
	@DmSanPhamREF	int,
	@StartDate		datetime,
	@EndDate		datetime,
	@RecordStatus	INT,
	@RecordCount INT OUTPUT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @sqlCommand	NVARCHAR(MAX),
			@sqlGetList	NVARCHAR(MAX),
			@sqlGetTotalRecords	NVARCHAR(MAX),
			@dauNhay	NVARCHAR(10) = '''',
			@fillterSing	NVARCHAR(MAX)
			
	DECLARE @totalRecord INT
			
	DECLARE @params NVARCHAR(MAX)
	SET @params = '@PageIndexParam		int,
					@PageSizeParam		int,
					@DmSanPhamREFParam	int,
					@StartDateParam		datetime,
					@EndDateParam		datetime,
					@RecordStatusParam	INT'	
					
	DECLARE @ParmTotalRecord nvarchar(MAX);
	SET @ParmTotalRecord = N' 
							@DmSanPhamRefP	INT,
							@StartDateP	DATETIME,
							@EndDateP	DATETIME,
								@RecordCountPOUT varchar(30) OUTPUT';
			
	SET @fillterSing = '';
	
	SET @fillterSing += ' AND NgayThucHien BETWEEN ' + @dauNhay + CONVERT(NVARCHAR(50), @StartDate) + @dauNhay + ' AND ' + @dauNhay 
													+ CONVERT(NVARCHAR(50), @EndDate) + @dauNhay
	IF @DmSanPhamREF > 0
		SET @fillterSing += ' AND A.DmSanPhamREF = ' + CONVERT(NVARCHAR(50), @DmSanPhamREF);
		
	IF @RecordStatus >= 0
		SET @fillterSing += ' AND A.RecordStatus = ' + CONVERT(NVARCHAR(50), @RecordStatus);
			
	SET @sqlCommand = '
			SELECT 
				A.ThucChayDaTinhOtherID ID,
				A.DmSanPhamREF,
				A.TenSanPham,
				A.ThanhTienThucChay,
				A.GhiChu,
				A.Recordstatus,
				A.LastModifiedAt ThoiGianThucHien,
				A.LastModifiedBy NguoiThucHien,
				ROW_NUMBER()OVER (ORDER BY LastModifiedAt DESC) as rowNumber
			FROM ThucChayDaTinhOther A
			WHERE 1=1
				AND A.DeletedStatus = 0 ' + @fillterSing;
			
	SET @sqlGetList = '
		SELECT *
		FROM 
		(' + 
			@sqlCommand + '			
		)T
		WHERE T.rowNumber BETWEEN ' + CONVERT(NVARCHAR(100),((@PageIndex -1) * @PageSize + 1)) 
			+ ' AND ' 
			+ CONVERT(NVARCHAR(100),((((@PageIndex -1) * @PageSize + 1) + @PageSize) - 1));
			
	PRINT '@sqlGetList: ' + @sqlGetList
	
	SET @sqlGetTotalRecords = 
		N'SELECT @RecordCountPOUT = count(*) 
		   FROM 
			(' + 
				@sqlCommand + '			
			)T
		   WHERE 1=1';
	   
	PRINT '@sqlGetTotalRecords: ' + @sqlGetTotalRecords
			
	EXECUTE sp_executesql @sqlGetList, @params, 
		@PageIndexParam		= @PageIndex,
		@PageSizeParam		= @PageSize,
		@DmSanPhamREFParam	= @DmSanPhamREF,
		@StartDateParam		= @StartDate,
		@EndDateParam		= @EndDate,
		@RecordStatusParam	= @RecordStatus--,
		--@RecordCountParam	= @RecordCount OUT
	
	EXECUTE sp_executesql @sqlGetTotalRecords, @ParmTotalRecord, 
		@DmSanPhamRefP		= @DmSanPhamREF,
		@StartDateP			= @StartDate,
		@EndDateP			= @EndDate, 
		@RecordCountPOUT	=@RecordCount OUTPUT;
		
	SELECT @RecordCount;
		
END

```
