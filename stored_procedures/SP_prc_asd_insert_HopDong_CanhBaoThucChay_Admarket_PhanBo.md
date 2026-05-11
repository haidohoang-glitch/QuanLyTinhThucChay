# Stored Procedure: `prc_asd_insert_HopDong_CanhBaoThucChay_Admarket_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 10:59:24.523000
- **Ngày sửa cuối**: 2024-02-28 11:33:57.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(1000)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(1000)` | No |
| `@GiaTriHopDong` | `money(8)` | No |
| `@GiaTriThucChay_HienTai` | `money(8)` | No |
| `@GiaTriThucChay_TraVe` | `money(8)` | No |
| `@Created_By` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[prc_asd_insert_HopDong_CanhBaoThucChay_Admarket_PhanBo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime,
	@SoHopDong nvarchar(50),
	@HopDongChiTietREF int,
	@DmSanPhamREF int,
	@TenSanPham nvarchar(500),
	@DmViTriREF  int,
	@TenViTri nvarchar(500),
	@GiaTriHopDong money,
	@GiaTriThucChay_HienTai money,
	@GiaTriThucChay_TraVe money,
	@Created_By nvarchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

INSERT INTO [dbo].[HopDong_CanhBaoThucChayVuot_Admarket_PhanBo]
           (
		    [NgayThucHien]
           ,[SoHopDong]
		   ,[HopDongChiTietREF]
           ,[DmSanPhamREF]
           ,[TenSanPham]
		   ,DmViTriREF 
		   ,TenViTri 
           ,[GiaTriHopDong]
           ,[GiaTriThucChay_HienTai]
           ,[GiaTriThucChay_TraVe]
           ,[Created_By]
           ,[Created_At]
		   )
     VALUES
           (
		    @NgayThucHien ,
			@SoHopDong ,
			@HopDongChiTietREF,
			@DmSanPhamREF ,
			@TenSanPham,
			@DmViTriREF  ,
			@TenViTri ,
			@GiaTriHopDong ,
			@GiaTriThucChay_HienTai ,
			@GiaTriThucChay_TraVe ,
			@Created_By,
			getdate() 
			)
END




```
