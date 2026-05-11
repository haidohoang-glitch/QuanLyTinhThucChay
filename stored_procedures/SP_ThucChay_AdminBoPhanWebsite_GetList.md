# Stored Procedure: `ThucChay_AdminBoPhanWebsite_GetList`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:16.940000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.687000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmSanPhamREFList` | `nvarchar(400)` | No |
| `@DmWebsiteREFList` | `nvarchar(400)` | No |
| `@DmLoaiDoiTuongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-18
-- Description:	<Description,,>
-- =============================================
-- dbo.ThucChay_AdminBoPhanWebsite_GetList 1, 10,'-1','','',2
CREATE PROCEDURE [dbo].[ThucChay_AdminBoPhanWebsite_GetList] 
	-- Add the parameters for the stored procedure here
	@PageIndex int,
	@PageSize int,
	@TenDangNhap NVARCHAR(50),
	@DmSanPhamREFList NVARCHAR(200),
	@DmWebsiteREFList NVARCHAR(200),
	@DmLoaiDoiTuongREF INT	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @Sql NVARCHAR(MAX);
	DECLARE @DauNhay NVARCHAR(10)
	DECLARE @FilterString NVARCHAR(MAX)='';
	
	SET @DauNhay = ''''
	
	IF(@TenDangNhap) <> '-1'
		SET @FilterString = ' AND TenDangNhap = ' + @TenDangNhap
	IF (@DmLoaiDoiTuongREF) > 0
		SET @FilterString = @FilterString + ' AND DmLoaiDoiTuongREF = ' + CONVERT(nvarchar(10),@DmLoaiDoiTuongREF)
	
	SET @Sql = '
		SELECT 
			*
		FROM
		(
			SELECT 
				A.AdminBoPhanWebsiteID,
				A.TenDangNhap,
				A.DmSanPhamREF,
				A.TenSanPham,
				A.DmWebsiteREF,
				A.TenWebsite,
				A.DmLoaiDoiTuongREF,
				B.TenLoaiDoiTuong,
				ROW_NUMBER() OVER (ORDER BY A.TenDangNhap ASC) AS num
			FROM AdminBoPhanWebsite A
				INNER JOIN DmLoaiDoiTuong B ON B.DmLoaiDoiTuongID = A.DmLoaiDoiTuongREF
			WHERE 1=1 ' + @FilterString + '
		)T
		WHERE num BETWEEN ' + CONVERT(nvarchar(50),(@PageIndex-1)*@PageSize + 1) + ' AND ' + CONVERT(nvarchar(50), @PageIndex*@PageSize)

	
	PRINT @Sql;
	EXEC (@Sql);
		--AND (A.DmSanPhamREF IS NULL OR A.DmSanPhamREF IN (@DmSanPhamREFList))
		--AND (A.DmWebsiteREF IS NULL OR A.DmWebsiteREF IN (@DmWebsiteREFList))
		--AND (@DmLoaiDoiTuong IS NULL OR A.DmLoaiDoiTuongREF = @DmLoaiDoiTuong)
END

```
