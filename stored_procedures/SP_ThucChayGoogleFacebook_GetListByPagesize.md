# Stored Procedure: `ThucChayGoogleFacebook_GetListByPagesize`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:22.133000
- **Ngày sửa cuối**: 2015-04-08 10:00:22.133000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@Status` | `int(4)` | No |
| `@RecordCount` | `int(4)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayGoogleFacebook_GetListByPagesize]
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF	int,
	@PageIndex		int,
	@PageSize		int,
	@StartDate		datetime,
	@EndDate		datetime,
	@Status			INT,
	@RecordCount INT OUTPUT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Sql nvarchar(max) = '',
			@DauNhay nvarchar(10) = '''',
			@FilterString nvarchar(max) = ''
	
	IF @DmSanPhamREF <> -1
	BEGIN 
		IF @Status <> -1
		BEGIN
			SELECT @RecordCount = COUNT(*)
			FROM ThucChayGoogleFacebook A
			Where 1=1			
				AND DmSanPhamREF = @DmSanPhamREF
				AND NgayThucHien between @StartDate and @EndDate
			
			SELECT *
			FROM
			(		
				SELECT DmSanPhamREF, TenSanPham, SoNgayChay, Click, ThanhTien,
					A.LastModifiedAt as ThoiGianThucHien, A.CreatedBy as NguoiThucHien,
					ROW_NUMBER()OVER (ORDER BY LastModifiedAt DESC) as rowNumber
				FROM ThucChayGoogleFacebook A
				WHERE 1=1
					AND DmSanPhamREF = @DmSanPhamREF
					AND NgayThucHien between @StartDate and @EndDate
					AND A.DeletedStatus = 0
					AND A.RecordStatus = @RecordCount
			)T
			WHERE T.rowNumber BETWEEN (@PageIndex -1) * @PageSize + 1 AND(((@PageIndex -1) * @PageSize + 1) + @PageSize) - 1
		END
		ELSE
		BEGIN
			SELECT @RecordCount = COUNT(*)
			FROM ThucChayGoogleFacebook A
			Where 1=1			
				AND DmSanPhamREF = @DmSanPhamREF
				AND NgayThucHien between @StartDate and @EndDate
			
			SELECT *
			FROM
			(		
				SELECT DmSanPhamREF, TenSanPham, SoNgayChay, Click, ThanhTien,
					A.LastModifiedAt as ThoiGianThucHien, A.CreatedBy as NguoiThucHien,
					ROW_NUMBER()OVER (ORDER BY LastModifiedAt DESC) as rowNumber
				FROM ThucChayGoogleFacebook A
				WHERE 1=1
					AND DmSanPhamREF = @DmSanPhamREF
					AND NgayThucHien between @StartDate and @EndDate
					AND A.DeletedStatus = 0
			)T
			WHERE T.rowNumber BETWEEN (@PageIndex -1) * @PageSize + 1 AND(((@PageIndex -1) * @PageSize + 1) + @PageSize) - 1
		END
	END
	ELSE
	BEGIN
		IF @Status <> -1 
		BEGIN
			SELECT @RecordCount = COUNT(*)
			FROM ThucChayGoogleFacebook A
			Where 1=1						
				AND NgayThucHien between @StartDate and @EndDate
		
			SELECT *
			FROM
			(		
				SELECT DmSanPhamREF, TenSanPham, SoNgayChay, Click, ThanhTien,
					A.LastModifiedAt as ThoiGianThucHien, A.CreatedBy as NguoiThucHien,
					ROW_NUMBER()OVER (ORDER BY LastModifiedAt DESC) as rowNumber
				FROM ThucChayGoogleFacebook A
				WHERE 1=1				
					AND NgayThucHien between @StartDate and @EndDate
					AND A.DeletedStatus = 0
					AND A.RecordStatus = @Status
			)T
			WHERE T.rowNumber BETWEEN (@PageIndex -1) * @PageSize + 1 AND(((@PageIndex -1) * @PageSize + 1) + @PageSize) - 1	
		END
		ELSE
		BEGIN
			SELECT @RecordCount = COUNT(*)
			FROM ThucChayGoogleFacebook A
			Where 1=1						
				AND NgayThucHien between @StartDate and @EndDate
		
			SELECT *
			FROM
			(		
				SELECT DmSanPhamREF, TenSanPham, SoNgayChay, Click, ThanhTien,
					A.LastModifiedAt as ThoiGianThucHien, A.CreatedBy as NguoiThucHien,
					ROW_NUMBER()OVER (ORDER BY LastModifiedAt DESC) as rowNumber
				FROM ThucChayGoogleFacebook A
				WHERE 1=1				
					AND NgayThucHien between @StartDate and @EndDate
					AND A.DeletedStatus = 0
			)T
			WHERE T.rowNumber BETWEEN (@PageIndex -1) * @PageSize + 1 AND(((@PageIndex -1) * @PageSize + 1) + @PageSize) - 1
		END	
	END
END

```
