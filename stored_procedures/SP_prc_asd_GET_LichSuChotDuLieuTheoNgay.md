# Stored Procedure: `prc_asd_GET_LichSuChotDuLieuTheoNgay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-28 11:38:07.883000
- **Ngày sửa cuối**: 2017-04-28 16:11:59.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `varchar(200)` | No |
| `@SanPham` | `varchar(200)` | No |
| `@NhanHang` | `varchar(200)` | No |
| `@NganhHang` | `varchar(200)` | No |
| `@Sale` | `varchar(200)` | No |
| `@KhachHang` | `varchar(200)` | No |
| `@HTQC` | `varchar(200)` | No |
| `@LoaiBanner` | `varchar(200)` | No |
| `@MuaNgoai` | `bit(1)` | No |
| `@Website` | `varchar(200)` | No |
| `@pageIndex` | `int(4)` | No |
| `@pageSize` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE prc_asd_GET_LichSuChotDuLieuTheoNgay
	-- Add the parameters for the stored procedure here
    @SoHopDong VARCHAR(200) = '',
	@SanPham VARCHAR(200) = '',
	@NhanHang VARCHAR(200) = '',
	@NganhHang VARCHAR(200) = '',
	@Sale VARCHAR(200) = '',
	@KhachHang VARCHAR(200) = '',
	@HTQC VARCHAR(200) = '',
	@LoaiBanner VARCHAR(200) = '',
	@MuaNgoai BIT = '0',
	@Website VARCHAR(200) = '',
	@pageIndex INT = 1,
	@pageSize INT = 20
AS
    BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
        SET NOCOUNT ON;

    -- Insert statements for procedure here
        SELECT 
		@SoHopDong AS SoHopDong,
		@SanPham AS SanPham,
		@NhanHang AS NhanHang,
		@NganhHang AS NganhHang,
		@Sale AS Sale,
		@KhachHang AS KhachHang,
		@HTQC AS HTQC,
		@LoaiBanner AS LoaiBanner,
		@MuaNgoai AS MuaNgoai,
		@Website AS Website,
		GETDATE() AS ChotDenNgay
    END;

```
