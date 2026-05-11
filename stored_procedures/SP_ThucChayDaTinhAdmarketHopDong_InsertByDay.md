# Stored Procedure: `ThucChayDaTinhAdmarketHopDong_InsertByDay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-08 19:39:03.607000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.100000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC ThucChayDaTinhAdmarketHopDong_InsertByDay 5001,'CPC Admarket', 'Click','2014-04-03'
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarketHopDong_InsertByDay] 
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(50),
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @TongView BIGINT, @TongClick BIGINT, @Money FLOAT
	
	SELECT @TongView = ISNULL(SUM(A.[View]),0), @TongClick = ISNULL(SUM(A.Click),0), @Money = ISNULL(SUM(A.[Money]/1.1),0)
	FROM
	(
		SELECT DISTINCT [Contract],NgayThucHien,DmSanPhamREF,TenSanPham,Click,[View],[Money]
		FROM ThucChayAdmarketHopDong
		WHERE NgayThucHien = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF
	)A
	
	--SELECT @TongView, @TongClick, @Money
	
	INSERT INTO ThucChayDaTinhAdmarketHopDong
	(
		-- ThucChayDaTinhAdmarketHopDongID -- this column value is auto-generated
		[SoHopDong]
        ,[NgayKyHopDong]
        ,[NgayDanhSo]
        ,[SysNhanVienREF]
        ,[TenDangNhap]
        ,[TenNhanVien]
        ,[DmPhongBanREF]
        ,[TenPhongBan]
        ,[DmBoPhanREF]
        ,[TenBoPhan]
        ,[DmNhomLamViecREF]
        ,[TenNhomLamViec]
        ,[DmDiaDiemLamViecREF]
        ,[TenDiaDiemLamViec]
        ,[DmHinhThucQuangCao]
        ,[TenHinhThucQuangCao]
        ,[DmSanPhamREF]
        ,[TenSanPham]
        ,[DonViTinh]
        ,[TongClick]
        ,[TongView]
        ,[TongTienThucChay]
        ,[TongTienKhuyenMai]
        ,[NgayThucHien]
        ,[CreatedBy]
        ,[CreatedAt]
        ,[LastModifiedBy]
        ,[LastModifiedAt]
	)
	
    SELECT 
		'-' SoHopDong,
		'1900-01-01' as NgayKyHopDong,
		'1900-01-01' as NgayDanhSoHopDong,
		0 as SysNhanVienREF,'-' as TenDangNhap, '-' TenNhanVien,
		0 as DmPhongBanREF,'' as TenPhongBan,
		0 as DmBoPhanREF,'' as TenBoPhan,
		0 as DmNhomLamViecREF,'' as TenNhom,
		0 as DmDiaDiemLamViecREF,'' as TenDiaDiemLamViec,		 
		--dbo.ThucChay_GetDmHinhThucQuangCaoByHopDongID(0,@DmSanPhamREF) DmHinhThucQuangCaoREF,
		--dbo.ThucChay_GetTenHinhThucQuangCaoByHopDongID(0,@DmSanPhamREF) TenHinhThucQuangCao,
		CASE WHEN @DmSanPhamREF = 337 THEN 6
				ELSE 7
			END AS DmHinhThucQuangCaoREF,
			CASE WHEN @DmSanPhamREF = 337 THEN 'CPM'
				ELSE 'CPC'
			END AS TenHinhThucQuangCao,
		@DmSanPhamREF as DmSanPhamREF, @TenSanPham as TenSanPham,
		@DonViTinh,
		((SELECT ISNULL(SUM(TongClickThucChay),0) FROM ThucChayDaTinh WHERE convert(date,NgayThucHien) = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF) - @TongClick) TongClick,		
		((SELECT ISNULL(SUM(TongViewThucChay),0) FROM ThucChayDaTinh WHERE convert(date,NgayThucHien) = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF) - @TongView) TongView,		
		((SELECT ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) FROM ThucChayDaTinh WHERE convert(date,NgayThucHien) = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF) - @Money) ThanhTienThucChay,
		0 AS ThanhTienKhuyenMai,
		@NgayThucHien,
		'nhatmq', GETDATE(),'nhatmq', GETDATE()
END

```
