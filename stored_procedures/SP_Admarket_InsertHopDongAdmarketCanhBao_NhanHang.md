# Stored Procedure: `Admarket_InsertHopDongAdmarketCanhBao_NhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-14 14:27:00.013000
- **Ngày sửa cuối**: 2016-03-14 14:27:00.013000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(1000)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(1000)` | No |
| `@TK_Admarket` | `nvarchar(1000)` | No |
| `@DmViTri_REF` | `int(4)` | No |
| `@SaleID` | `int(4)` | No |
| `@UserNameSale` | `nvarchar(1000)` | No |
| `@TenSale` | `nvarchar(1000)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoLuong` | `int(4)` | No |
| `@Giatri` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 2016-03-14
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Admarket_InsertHopDongAdmarketCanhBao_NhanHang]
	-- Add the parameters for the stored procedure here
	@HopDongID INT,
	@SoHopDong NVARCHAR(500),
	@HopDongChiTietREF INT ,
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(500),
	@TK_Admarket NVARCHAR(500),
	@DmViTri_REF  INT,
	@SaleID INT,
	@UserNameSale NVARCHAR(500),
	@TenSale       NVARCHAR(500),
	@NgayThucHien DATETIME,
	@SoLuong INT,
	@Giatri FLOAT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO [dbo].[HopDongAdmarketCanhBao_NhanHang]
           ([HopDongID]
           ,[SoHopDong]
           ,[HopDongChiTietID]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[TK_Admarket]
           ,[DmViTriREF]
           ,[TenViTri]
           ,[SaleID]
           ,[UserNameSale]
           ,[TenSale]
           ,[NgayThucHien]
           ,[SoluongThucChay]
           ,[GiaTriThucChay]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[RecordStatus]
           ,[DeletedStatus])
     VALUES
           (
           	@HopDongID,
           	@SoHopDong,
           	@HopDongChiTietREF,
           	@DmSanPhamREF,
           	@TenSanPham,
           	@TK_Admarket,
           	@DmViTri_REF,
           	'',
           	@SaleID,
           	@UserNameSale,
           	@TenSale,
           	@NgayThucHien,
           	@SoLuong,
           	@Giatri,
           	GETDATE(),
           	'ASD',
           	GETDATE(),
           	'ASD',
           	0,
           	0
           	)
	
END

```
