# Stored Procedure: `usp_InsertThucChayDomainCheck`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-16 11:22:02.673000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayKiemTra` | `datetime(8)` | No |
| `@DomainName` | `nvarchar(100)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertThucChayDomainCheck]
-- Create Date: Friday, May 16, 2014
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertThucChayDomainCheck]
	@ID int,
	@NgayThucHien datetime,
	@NgayKiemTra datetime,
	@DomainName nvarchar(50),
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

INSERT INTO [dbo].[ThucChayDomainCheck] (
	[ID],
	[NgayThucHien],
	[NgayKiemTra],
	[DomainName],
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
	@DomainName,
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
