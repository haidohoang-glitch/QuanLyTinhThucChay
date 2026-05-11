# Stored Procedure: `prc_QLTC_InsertLogXuLylaiDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.667000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.667000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(4000)` | No |
| `@BannerREF` | `nvarchar(4000)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Name_Table` | `nvarchar(4000)` | No |
| `@FromDate` | `datetime2(8)` | No |
| `@ToDate` | `datetime2(8)` | No |
| `@UserId` | `int(4)` | No |
| `@HopDongChiTiet` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[prc_QLTC_InsertLogXuLylaiDuLieu]
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(2000),
	@BannerREF NVARCHAR(2000),
	@DmSanPhamREF INT = 0,
	@Name_Table NVARCHAR(2000),
	@FromDate DATETIME2(7),
	@ToDate DATETIME2(7),
	@UserId INT,
	@HopDongChiTiet INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO dbo.DataLog_QLTC_XuLylaiDuLieu
	(
	    SoHopDong,
	    BannerREF,
	    DmSanPhamREF,
	    Name_Table,
	    Message,
	    FromDate,
	    ToDate,
	    TimeExecutedSeconds,
	    Status,
	    creationTime,
	    creatorUserId,
		HopDongChiTietREF
	)
	VALUES(@SoHopDong, @BannerREF, @DmSanPhamREF, @Name_Table, NULL, @FromDate, @ToDate, null, 0, GETDATE(), @UserId, @HopDongChiTiet)
END

```
