# Stored Procedure: `LogUserActionFromThucChay_InsertActionLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-10 16:09:41.293000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.523000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@LogTime` | `datetime(8)` | No |
| `@TenBaoCao` | `nvarchar(1024)` | No |
| `@NgayThucHienBatDau` | `datetime(8)` | No |
| `@NgayThucHienKetThuc` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(4000)` | No |
| `@DmPhongBanREF` | `nvarchar(4000)` | No |
| `@DmBoPhanREF` | `nvarchar(4000)` | No |
| `@DmNhomLamViecREF` | `nvarchar(4000)` | No |
| `@SysNhanVienREF` | `nvarchar(4000)` | No |
| `@KhachHangREF` | `nvarchar(1024)` | No |
| `@NhanHang` | `nvarchar(4000)` | No |
| `@DmNhomNganhREF` | `nvarchar(4000)` | No |
| `@DmHinhThucQuangCao` | `nvarchar(4000)` | No |
| `@DmSanPhamREF` | `nvarchar(4000)` | No |
| `@DmViTriREF` | `nvarchar(4000)` | No |
| `@DmWebsiteREF` | `nvarchar(4000)` | No |
| `@TongViewThucChayNoiBo` | `bigint(8)` | No |
| `@TongClickThucChayNoiBo` | `bigint(8)` | No |
| `@TongSoBaiVietNoiBo` | `bigint(8)` | No |
| `@TongSoNgayChayNoiBo` | `bigint(8)` | No |
| `@TongViewThucChayKhuyenMai` | `bigint(8)` | No |
| `@TongClickThucChayKhuyenMai` | `bigint(8)` | No |
| `@TongSoBaiVietKhuyenMai` | `bigint(8)` | No |
| `@TongSoNgayChayKhuyenMai` | `bigint(8)` | No |
| `@TongViewThucChay` | `bigint(8)` | No |
| `@TongClickThucChay` | `bigint(8)` | No |
| `@TongSoBaiViet` | `bigint(8)` | No |
| `@TongSoNgayChay` | `bigint(8)` | No |
| `@TongTienKhuyemMai` | `float(8)` | No |
| `@TongTienNoiBo` | `float(8)` | No |
| `@TongTienThucChaySauCK` | `float(8)` | No |
| `@TongGiaTriThayDoi` | `float(8)` | No |
| `@IsPheDuyet` | `int(4)` | No |
| `@PheDuyetAt` | `datetime(8)` | No |
| `@PheDuyetBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-10
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[LogUserActionFromThucChay_InsertActionLog] 
	@TenDangNhap				NVARCHAR(50),
	@LogTime					DATETIME,
	@TenBaoCao					NVARCHAR(512),
	@NgayThucHienBatDau			DATETIME,
	@NgayThucHienKetThuc		DATETIME,
	@SoHopDong					NVARCHAR(2000),
	@DmPhongBanREF				NVARCHAR(2000),
	@DmBoPhanREF				NVARCHAR(2000),
	@DmNhomLamViecREF			NVARCHAR(2000),
	@SysNhanVienREF				NVARCHAR(2000),
	@KhachHangREF				NVARCHAR(512),
	@NhanHang					NVARCHAR(2000),
	@DmNhomNganhREF				NVARCHAR(2000),
	@DmHinhThucQuangCao			NVARCHAR(2000),
	@DmSanPhamREF				NVARCHAR(2000),
	@DmViTriREF					NVARCHAR(2000),
	@DmWebsiteREF				NVARCHAR(2000),
	@TongViewThucChayNoiBo		BIGINT,
	@TongClickThucChayNoiBo		BIGINT,
	@TongSoBaiVietNoiBo			BIGINT,
	@TongSoNgayChayNoiBo		BIGINT,
	@TongViewThucChayKhuyenMai	BIGINT,
	@TongClickThucChayKhuyenMai	BIGINT,
	@TongSoBaiVietKhuyenMai		BIGINT,
	@TongSoNgayChayKhuyenMai	BIGINT,
	@TongViewThucChay			BIGINT,
	@TongClickThucChay			BIGINT,
	@TongSoBaiViet				BIGINT,
	@TongSoNgayChay				BIGINT,
	@TongTienKhuyemMai			FLOAT,
	@TongTienNoiBo				FLOAT,
	@TongTienThucChaySauCK		FLOAT,
	@TongGiaTriThayDoi			FLOAT,
	@IsPheDuyet					INT,
	@PheDuyetAt					DATETIME,
	@PheDuyetBy					NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    INSERT INTO [dbo].[LogUserActionFromThucChay]
           ([TenDangNhap]
           ,[LogTime]
           ,[TenBaoCao]
           ,[NgayThucHienBatDau]
           ,[NgayThucHienKetThuc]
           ,[SoHopDong]
           ,[DmPhongBanREF]
           ,[DmBoPhanREF]
           ,[DmNhomLamViecREF]
           ,[SysNhanVienREF]
           ,[KhachHangREF]
           ,[NhanHang]
           ,[DmNhomNganhREF]
           ,[DmHinhThucQuangCao]
           ,[DmSanPhamREF]
           ,[DmViTriREF]
           ,[DmWebsiteREF]
           ,[TongViewThucChayNoiBo]
           ,[TongClickThucChayNoiBo]
           ,[TongSoBaiVietNoiBo]
           ,[TongSoNgayChayNoiBo]
           ,[TongViewThucChayKhuyenMai]
           ,[TongClickThucChayKhuyenMai]
           ,[TongSoBaiVietKhuyenMai]
           ,[TongSoNgayChayKhuyenMai]
           ,[TongViewThucChay]
           ,[TongClickThucChay]
           ,[TongSoBaiViet]
           ,[TongSoNgayChay]
           ,[TongThanhTienSauTrietKhauThucChayKhuyenMai]
           ,[TongThanhTienSauTrietKhauThucChayNoiBo]
           ,[TongThanhTienSauTrietKhauThucChay]
           ,[TongGiaTriThayDoi]
           ,[IsPheDuyet]
           ,[PheDuyetBy]
           ,[PheDuyetAt])
     VALUES
           (
           	@TenDangNhap
			,@LogTime
			,@TenBaoCao
			,@NgayThucHienBatDau
			,@NgayThucHienKetThuc
			,@SoHopDong
			,@DmPhongBanREF
			,@DmBoPhanREF
			,@DmNhomLamViecREF
			,@SysNhanVienREF
			,@KhachHangREF
			,@NhanHang
			,@DmNhomNganhREF
			,@DmHinhThucQuangCao
			,@DmSanPhamREF
			,@DmViTriREF	
			,@DmWebsiteREF
			,@TongViewThucChayNoiBo
			,@TongClickThucChayNoiBo
			,@TongSoBaiVietNoiBo
			,@TongSoNgayChayNoiBo
			,@TongViewThucChayKhuyenMai
			,@TongClickThucChayKhuyenMai
			,@TongSoBaiVietKhuyenMai
			,@TongSoNgayChayKhuyenMai
			,@TongViewThucChay
			,@TongClickThucChay
			,@TongSoBaiViet	
			,@TongSoNgayChay	
			,@TongTienKhuyemMai
			,@TongTienNoiBo
			,@TongTienThucChaySauCK
			,@TongGiaTriThayDoi
			,@IsPheDuyet	
			,@PheDuyetAt	
			,@PheDuyetBy	)
END

```
