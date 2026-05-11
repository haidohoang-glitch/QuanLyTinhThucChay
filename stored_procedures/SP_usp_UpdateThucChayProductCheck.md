# Stored Procedure: `usp_UpdateThucChayProductCheck`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-16 11:22:01.900000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.403000

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

CREATE PROCEDURE [dbo].[usp_UpdateThucChayProductCheck](
    @ID                       INT,
    @NgayThucHien             DATETIME,
    @NgayKiemTra              DATETIME,
    @TenSanPham               NVARCHAR(50),
    @TypeProduct              INT,
    @Contract                 NVARCHAR(50),
    @TongClickKiemTra         FLOAT,
    @TongViewKiemTra          FLOAT,
    @TongClickNguon           FLOAT,
    @TongViewNguon            FLOAT,
    @ChenhLech_Click          FLOAT,
    @ChenhLech_View           FLOAT,
    @ChenhLechPhanTram_Click  FLOAT,
    @ChenhLechPhanTram_View   FLOAT
)
AS
	SET NOCOUNT ON 
	
	IF (
	       EXISTS(
	           SELECT [ID]
	           FROM   [ThucChayProductCheck]
	           WHERE  [ID] = @ID
	       )
	   )
	    UPDATE [dbo].[ThucChayProductCheck]
	    SET    [NgayThucHien]             = @NgayThucHien,
	           [NgayKiemTra]              = @NgayKiemTra,
	           [TenSanPham]               = @TenSanPham,
	           [TypeProduct]              = @TypeProduct,
	           [Contract]                 = @Contract,
	           [TongClickKiemTra]         = @TongClickKiemTra,
	           [TongViewKiemTra]          = @TongViewKiemTra,
	           [TongClickNguon]           = @TongClickNguon,
	           [TongViewNguon]            = @TongViewNguon,
	           [ChenhLech_Click]          = @ChenhLech_Click,
	           [ChenhLech_View]           = @ChenhLech_View,
	           [ChenhLechPhanTram_Click]  = @ChenhLechPhanTram_Click,
	           [ChenhLechPhanTram_View]   = @ChenhLechPhanTram_View
	    WHERE  [ID]                       = @ID
	ELSE
	    INSERT INTO [dbo].[ThucChayProductCheck]
	      (
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
	      )
	    VALUES
	      (
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

```
