# Stored Procedure: `usp_InsertThucChayProductCheck`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-16 11:22:02.417000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayKiemTra` | `datetime(8)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@Contract` | `nvarchar(100)` | No |
| `@TongClickKiemTra` | `float(8)` | No |
| `@TongViewKiemTra` | `float(8)` | No |
| `@TongClickNguon` | `float(8)` | No |
| `@TongViewNguon` | `float(8)` | No |
| `@ChenhLech_Click` | `float(8)` | No |
| `@ChenhLech_View` | `float(8)` | No |
| `@ChenhLechPhanTram_Click` | `float(8)` | No |
| `@ChenhLechPhanTram_View` | `float(8)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_InsertThucChayProductCheck]
-- Create Date: Friday, May 16, 2014
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertThucChayProductCheck]
	@ID int,
	@NgayThucHien datetime,
	@NgayKiemTra datetime,
	@TenSanPham nvarchar(50),
	@TypeProduct int,
	@Contract nvarchar(50),
	@TongClickKiemTra float,
	@TongViewKiemTra float,
	@TongClickNguon float,
	@TongViewNguon float,
	@ChenhLech_Click float,
	@ChenhLech_View float,
	@ChenhLechPhanTram_Click float,
	@ChenhLechPhanTram_View float
AS

SET NOCOUNT ON

INSERT INTO [dbo].[ThucChayProductCheck] (
	[ID],
	[NgayThucHien],
	[NgayKiemTra],
	[TenSanPham],
	[TypeProduct],
	[Contract],
	[TongClickKiemTra],
	[TongViewKiemTra],
	[TongClickNguon],
	[TongViewNguon],
	[ChenhLech_Click],
	[ChenhLech_View],
	[ChenhLechPhanTram_Click],
	[ChenhLechPhanTram_View]
) VALUES (
	@ID,
	@NgayThucHien,
	@NgayKiemTra,
	@TenSanPham,
	@TypeProduct,
	@Contract,
	@TongClickKiemTra,
	@TongViewKiemTra,
	@TongClickNguon,
	@TongViewNguon,
	@ChenhLech_Click,
	@ChenhLech_View,
	@ChenhLechPhanTram_Click,
	@ChenhLechPhanTram_View
)

--endregion

```
