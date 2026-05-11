# Stored Procedure: `prc_QLTC_UpdateLogXuLylaiDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.687000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.687000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@Contract` | `nvarchar(4000)` | No |
| `@Product` | `int(4)` | No |
| `@Table` | `nvarchar(4000)` | No |
| `@HopDongChiTiet` | `int(4)` | No |
| `@TimeExecutedSeconds` | `float(8)` | No |
| `@Message` | `nvarchar` | No |
| `@Status` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[prc_QLTC_UpdateLogXuLylaiDuLieu]
	-- Add the parameters for the stored procedure here
	@FromDate Datetime = NULL,
	@ToDate Datetime = NULL,
	@Contract Nvarchar(2000) = '',
	@Product Int = 0,
	@Table Nvarchar(2000) = '',
	@HopDongChiTiet INT = 0,
	@TimeExecutedSeconds FLOAT,
	@Message NVARCHAR(MAX),
	@Status INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE [dbo].[DataLog_QLTC_XuLylaiDuLieu] SET TimeExecutedSeconds = @TimeExecutedSeconds, Status = @Status, Message = @Message 
	WHERE CAST(FromDate AS Date) = CAST(@FromDate AS Date)
			AND CAST(ToDate AS Date) = CAST(@ToDate AS Date)
			AND (ISNULL(@Contract, '') = ''
					OR SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
			AND (ISNULL(@HopDongChiTiet, 0) = 0
					OR HopDongChiTietREF = @HopDongChiTiet)
			AND (ISNULL(@Product, 0) = 0
					OR DmSanPhamREF = @Product)
			AND Status = 1
END

```
