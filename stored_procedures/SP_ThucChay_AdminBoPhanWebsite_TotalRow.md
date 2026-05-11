# Stored Procedure: `ThucChay_AdminBoPhanWebsite_TotalRow`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:17.193000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.680000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmSanPhamREFList` | `nvarchar(400)` | No |
| `@DmWebsiteREFList` | `nvarchar(400)` | No |
| `@DmLoaiDoiTuongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- ThucChay_AdminBoPhanWebsite_TotalRow '','','',1
CREATE PROCEDURE [dbo].[ThucChay_AdminBoPhanWebsite_TotalRow]
	-- Add the parameters for the stored procedure here
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
			COUNT(*) AS TotalRows 
		FROM
		(
			SELECT 
				A.TenDangNhap,
				A.DmSanPhamREF,
				A.TenSanPham,
				A.DmWebsiteREF,
				A.TenWebsite,
				B.TenLoaiDoiTuong,
				ROW_NUMBER() OVER (ORDER BY A.TenDangNhap ASC) AS num
			FROM AdminBoPhanWebsite A
				INNER JOIN DmLoaiDoiTuong B ON B.DmLoaiDoiTuongID = A.DmLoaiDoiTuongREF
			WHERE 1=1 ' + @FilterString + '
		)T
		'

	EXEC (@Sql);
END

```
