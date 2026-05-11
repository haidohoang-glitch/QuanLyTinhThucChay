# Stored Procedure: `ThucChayDaTinhAdmarketSale_InsertByDay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-08 19:39:02.940000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.787000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThuchien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-03-27
-- Description:	<Description,,>
-- =============================================
-- EXEC ThucChayDaTinhAdmarketSale_InsertByDay 299, 'CPC Plus Admarket', 'Click', '2014-01-17'
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarketSale_InsertByDay]
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(50),
	@DonViTinh NVARCHAR(50),
	@NgayThuchien DATETIME
AS
BEGIN
	DECLARE @TongView BIGINT, @TongClick BIGINT, @Money FLOAT, @Promotion FLOAT
	
	SELECT @TongView = ISNULL(CAST(SUM(ISNULL(A.[TTV],0)) AS BIGINT),0), @TongClick = ISNULL(CAST(SUM(ISNULL(A.TTC,0)) AS BIGINT),0), @Money =ISNULL(SUM(ISNULL(A.[Money],0 )/1.1),0), @Promotion = ISNULL(SUM(ISNULL(CONVERT(float,A.Promotion),0)/1.1),0)
	FROM ThucChayAdmarket A
	WHERE CreateDate = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF
	
	--SELECT @TongView ttv, @TongClick ttc, @Money tttc, @Promotion ttkm
	INSERT INTO [dbo].[ThucChayDaTinhAdmarketSale]
           ([SoHopDong]
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
           ,[LastModifiedAt])
           
	SELECT
		'-' SoHopDong,
		'1900-01-01' NgayKyHopDong,
		'1900-01-01' NgayDanhSoHopDong,
		0 AS SysNhanVienREF,
		'-' AS TenDangNhap,		
		'-' AS TenNhanVien,
		0 AS DmPhongBanREF,
		'-' AS TenPhongBan,
		0 AS DmBoPhanREF,
		'-' AS TenBoPhan,
		0 AS DmNhomLamViecREF,
		'-' AS TenNhomLamViec,
		0 AS DmDiaDiemLamViecREF,
		'-' AS TenDiaDiemLamViec,
		@DmSanPhamREF,
		@TenSanPham,
		@DonViTinh,
		((SELECT ISNULL(CAST(SUM(ISNULL(TongClickThucChay,0)) AS BIGINT),0) FROM ThucChayDaTinh WHERE convert(date,NgayThucHien) = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF) - @TongClick) TongClick,	
		((SELECT ISNULL(CAST(SUM(ISNULL(TongViewThucChay,0)) AS BIGINT),0) FROM ThucChayDaTinh WHERE convert(date,NgayThucHien) = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF) - @TongView) TongView,
		
		((SELECT ISNULL(SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0)),0) FROM ThucChayDaTinh WHERE convert(date,NgayThucHien) = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF) - @Money) ThanhTienThucChay,
		
		((SELECT ISNULL(SUM(ISNULL(ThanhTienKM,0)),0) FROM ThucChayDaTinh WHERE convert(date,NgayThucHien) = @NgayThucHien AND DmSanPhamREF = @DmSanPhamREF) - @Promotion) ThanhTienThucChayKM,		
		@NgayThucHien,
		'nhatmq' CreatedBy,@NgayThucHien CreatedAt,'nhatmq' LastModifiedBy,@NgayThucHien LastModifiedAt
END

```
