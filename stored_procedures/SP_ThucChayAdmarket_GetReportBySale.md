# Stored Procedure: `ThucChayAdmarket_GetReportBySale`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:26.673000
- **Ngày sửa cuối**: 2014-10-14 10:39:50.863000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmPhongBanREFList` | `nvarchar(4000)` | No |
| `@DmBoPhanREFList` | `nvarchar(4000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(4000)` | No |
| `@TenNhanVienList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayAdmarket_GetReportBySale]
	@PageIndex int,
	@PageSize int,
	@GroupFieldName nvarchar(50),
	@StartDate DATETIME,
	@EndDate DATETIME,	
	@DmPhongBanREFList nVARCHAR(2000),
	@DmBoPhanREFList nVARCHAR(2000),
	@DmNhomLamViecREFList nVARCHAR(2000),
	@TenNhanVienList nvarchar(2000),
	@TenDangNhap nVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @SqlCommandString nVARCHAR(MAX),
			@SqlSelectString nVARCHAR(MAX),
			@SqlFilterString nVARCHAR(MAX),
			@SqlSecurityString nVARCHAR(MAX),
			@SqlSelectString1 nvarchar(max);
	
	DECLARE @DauNhay nVARCHAR(10)='''';
	DECLARE @GroupByField nvarchar(max);
	DECLARE @OrderByField NVARCHAR(MAX);

	DECLARE @ParmDefinition nvarchar(max) =	  N'@ParamPageIndex int,
												@ParamPageSize int,
												@ParamGroupFieldName nvarchar(50),
												@ParamStartDate DATETIME,
												@ParamEndDate DATETIME,	
												@ParamDmPhongBanREFList nVARCHAR(2000),
												@ParamDmBoPhanREFList nVARCHAR(2000),
												@ParamDmNhomLamViecREFList nVARCHAR(2000),
												@ParamTenNhanVienList nvarchar(2000),
												@ParamTenDangNhap nVARCHAR(50)'

	-- Phan quyen theo cap bac
	SET @SqlSecurityString = '(';
	SET @SqlSecurityString += dbo.GetSecurityDataByTenDangNhap(@StartDate,
																@EndDate,
																@TenDangNhap,
																'NgayThucHien',
																'TenDangNhap');

	SET @SqlSecurityString += ' OR (' + dbo.GetSecurityWebsiteProductAdmarket(@StartDate,
																				@EndDate,@TenDangNhap,
																				'NgayThucHien',
																				'TenDangNhap',
																				'DmSanPhamREF',
																				'DmWebsiteREF') + 
									')';

	SET @SqlSecurityString += ')';

	-- Dieu kien tim kiem theo gia tri truyen vao 
	SET @SqlFilterString = '';
	SET @SqlFilterString += dbo.ThucChayAdmarket_GetCommandFilterString(@DmPhongBanREFList, @DmBoPhanREFList, @DmNhomLamViecREFList, @TenNhanVienList);

	SET @SqlSelectString1 = '
				ROW_NUMBER() OVER (ORDER BY T1.'+ @GroupFieldName + ') AS num,
				T1.TenDangNhap,
				T1.TenNhanVien,
				T1.PhongBoPhanNhomID,
				T1.PhongBoPhanNhom,
				SUM(T1.TongClick) AS TongClick,
				SUM(T1.TongView) AS TongView,
				SUM(T1.TongTienThucChay) AS TongTienThucChay, 
				SUM(T1.TongTienKhuyenMai) AS TongTienKhuyenMai
		';
	
	IF (@PageIndex > 0 AND @PageSize > 0)
		SET @SqlSelectString = '
					T.num AS STT,
					T.TenDangNhap,
					T.TenNhanVien,
					T.PhongBoPhanNhomID,
					T.PhongBoPhanNhom,
					dbo.FormatNumber(T.TongClick) AS TongClick,
					dbo.FormatNumber(T.TongView) AS TongView,
					dbo.FormatNumber(T.TongTienThucChay) AS ThanhTienThucThu, 
					dbo.FormatNumber(T.TongTienKhuyenMai) AS ThanhTienKhuyenMai
			';
	ELSE -- for Print
	BEGIN
		SET @SqlSelectString = '
					T.num AS STT,
					T.TenDangNhap,
					T.TenNhanVien,
					T.PhongBoPhanNhomID,
					T.PhongBoPhanNhom,
					T.TongClick,
					T.TongView,
					T.TongTienThucChay AS ThanhTienThucThu, 
					T.TongTienKhuyenMai AS ThanhTienKhuyenMai
			';
	END

	SET @GroupByField = 'T1.TenDangNhap, T1.TenNhanVien, T1.PhongBoPhanNhomID, T1.PhongBoPhanNhom'
	SET @OrderByField = 'T.TenNhanVien';

	IF @GroupFieldName = 'TenSanPham'
	BEGIN
		SET @SqlSelectString1 += ', T1.DmSanPhamREF, T1.TenSanPham';
		SET @SqlSelectString += ', T.DmSanPhamREF, T.TenSanPham';
					
		SET @GroupByField += ', T1.DmSanPhamREF, T1.TenSanPham';
	END

	SET @SqlCommandString = 
		'
			SELECT ' + @SqlSelectString1 + '
			FROM 
			(' 
				+ dbo.ThucChayAdmarket_GenCommandForReportBySale(@SqlSecurityString, @SqlFilterString) +
			'
			)T1
			GROUP BY ' + @GroupByField;

	SET @SqlCommandString = '
		SELECT ' + @SqlSelectString + '
		FROM
		(' 
			+ @SqlCommandString + 
		'
		)T ';
		
	IF (@PageIndex > 0 AND @PageSize > 0)
		SET @SqlCommandString += 
		'
		WHERE T.num BETWEEN ' + CONVERT(varchar(50),(@PageIndex-1)*@PageSize + 1) + ' AND ' + CONVERT(varchar(50),@PageIndex*@PageSize);
	SET @SqlCommandString += '
		ORDER BY ' + @OrderByField;



	PRINT @SqlCommandString;	

	EXECUTE sp_executesql @SqlCommandString, @ParmDefinition,
							@ParamPageIndex				= @PageIndex,
							@ParamPageSize				= @PageSize,
							@ParamGroupFieldName		= @GroupFieldName,
							@ParamStartDate				= @StartDate,
							@ParamEndDate				= @EndDate,	
							@ParamDmPhongBanREFList		= @DmPhongBanREFList,
							@ParamDmBoPhanREFList		= @DmBoPhanREFList,
							@ParamDmNhomLamViecREFList	= @DmNhomLamViecREFList,
							@ParamTenNhanVienList		= @TenNhanVienList,
							@ParamTenDangNhap			= @TenDangNhap
END

```
