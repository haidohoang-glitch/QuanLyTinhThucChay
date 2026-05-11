# Function: `ThucChay_GenSQLCommandForDuyetDuLieuQuery`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-09 11:47:11.917000
- **Ngày sửa cuối**: 2015-04-03 13:25:23.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomlamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |
| `@UsingForDoiTac` | `int(4)` | No |
| `@UsingForDuyetDuLieu` | `int(4)` | No |
| `@IsPheDuyet` | `int(4)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-25
-- Description:	ThucChay_GenSQLCommandForQuery 
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandForDuyetDuLieuQuery] 
(
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@TenDangNhap NVARCHAR(50),
	@DmPhongBanREF int,
	@DmBoPhanREF int,
	@DmNhomlamViecREF int,
	@DmChucDanhREF INT,
	@UsingForDoiTac INT,  -- 1: doi tac
	@UsingForDuyetDuLieu INT, -- 1: duyet du lieu
	@IsPheDuyet INT,
	@IsNoiBo INT,
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList NVARCHAR(200)
)
RETURNS VARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql VARCHAR(MAX)
	DECLARE @DauNhay VARCHAR(50)
	DECLARE @FilterString VARCHAR(4000);
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	
	SET @DauNhay = ''''
	SET @ChucDanhID = dbo.NhanSuGetChucDanhByNhanVien(@TenDangNhap)
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)	
	
	SET @FilterString = ' AND '
	SET @FilterString +=  dbo.GetThucChayFilterString(
														@StartDate ,
														@EndDate ,
														@DmSanPhamREFList ,
														@DmWebsiteREFList ,
														@SoHopDongList ,
														@DmPhongBanREFList ,
														@DmBoPhanREFList ,
														@DmNhomLamViecREFList ,
														@TenNhanVienList,
														@TenDangNhap,
														@DmPhongBanREF,
														@DmBoPhanREF,
														@DmNhomLamViecREF,
														@DmChucDanhREF,
														@DmHinhThucQuangCaoList,
														@DmBannerREFList 
													)	
													
	IF @UsingForDoiTac = 1 
		SET @FilterString += ' AND IsPheDuyet = 1 '
	ELSE IF @UsingForDuyetDuLieu = 1
	BEGIN
		IF @IsPheDuyet = 0 	
			SET @FilterString += ' AND IsPheDuyet = 0 '
		ELSE IF @IsPheDuyet = 1
			SET @FilterString += ' AND IsPheDuyet = 1 '
	END
	
	IF @IsNoiBo = 1
		SET @FilterString += ''
	ELSE IF @IsNoiBo = 0
		SET @FilterString += ' AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
		
		 													

	SET @Sql = '
		SELECT DISTINCT
				DmSanPhamREF, TenSanPham, SoHopDong,
				TenWebsite, DmWebsiteREF, 
				TenPhongBan, DmPhongBanREF, 
				TenBoPhan, DmBoPhanREF, 
				TenNhomLamViec, DmNhomLamViecREF,
				TenDangNhap,TenNhanVien
			FROM ThucChayDaTinh 
			WHERE 1=1 AND DmWebsiteREF in (134,182,56,137,254,85)'
		SET @Sql += @FilterString
		SET @Sql += '
				AND TrangThaiHopDong <> 3
				AND (ThanhTienSauTrietKhauThucChay <> 0 OR ThanhTienKM <> 0 OR GiaTriThayDoi <> 0)
				AND (ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) > 1000
	'

	-- Return the result of the function
	RETURN @Sql

END

```
