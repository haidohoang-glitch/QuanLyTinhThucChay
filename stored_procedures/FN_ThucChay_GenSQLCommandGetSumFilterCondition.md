# Function: `ThucChay_GenSQLCommandGetSumFilterCondition`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-29 16:07:40.683000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@GroupByFildID` | `nvarchar(100)` | No |
| `@GroupByFild` | `nvarchar(100)` | No |
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
| `@DmNhomLamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-29
-- Description:	Generate SQL Command GetSumFilterCondition
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandGetSumFilterCondition]
(
	-- Add the parameters for the function here
	@GroupFieldName nvarchar(50),
	@GroupByFildID nvarchar(50),
	@GroupByFild nvarchar(50),
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@TenDangNhap nvarchar(50),
	@DmPhongBanREF int,
	@DmBoPhanREF int,
	@DmNhomLamViecREF int,
	@DmChucDanhREF int
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql VARCHAR(8000)
	DECLARE @DauNhay NVARCHAR(50)
	
	SET @DauNhay='''' 

	SET @Sql = '
			SELECT
				T2.'+ @GroupFieldName+',T2.ID, T2.DonViTinh,
				SUM(T2.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
				SUM(T2.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
				SUM(T2.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
				SUM(T2.SoLuongThucChayNoiBo) SoLuongThucChayNoiBo,
				SUM(T2.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
				SUM(T2.SoLuongThucChayThucThu) SoLuongThucChayThucThu,
				SUM(T2.ThanhTienNoiBo) AS ThanhTienNoiBo,
				SUM(T2.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(T2.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
				SUM(T2.ThanhTienThucThu) AS ThanhTienThucThu,
				ROW_NUMBER() OVER (ORDER BY T2.'+ @GroupFieldName + ') AS num
			FROM
			(
				SELECT
					T1.'+ @GroupFieldName+','+@GroupByFildID+'T1.DonViTinh,SoHopDong AS SHD,
					MAX(T1.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
					MAX(T1.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
					MAX(T1.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
					SUM(T1.SoLuongThucChayNoiBo) SoLuongThucChayNoiBo,
					SUM(T1.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
					SUM(T1.SoLuongThucChayThucThu) SoLuongThucChayThucThu,
					SUM(T1.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
					SUM(T1.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
					SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
					SUM(T1.ThanhTienThucChayThucThu) AS ThanhTienThucThu,
					ROW_NUMBER() OVER (ORDER BY T1.'+ @GroupFieldName + ') AS num
				FROM
				('
					+ dbo.ThucChay_GenSQLCommandForQuery(@StartDate,
														@EndDate,
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
														@DmChucDanhREF) +
				')T1
				GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF
			)T2
			GROUP BY T2.'+ @GroupFieldName+',T2.ID,T2.DonViTinh
	'
	
	RETURN @Sql

END

```
