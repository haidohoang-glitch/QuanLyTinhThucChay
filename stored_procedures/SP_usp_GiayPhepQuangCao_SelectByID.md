# Stored Procedure: `usp_GiayPhepQuangCao_SelectByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:52.243000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.340000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GiayPhepQuangCaoID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_SelectByID]
	@GiayPhepQuangCaoID INT
AS
BEGIN
	SET NOCOUNT ON;
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	
	SELECT [GiayPhepQuangCaoID],
	       [TenGiayPhep],
	       [DmLoaiGiayPhepREF],
	       [DmNhanHangREF],
	       [ThoiGianHieuLuc],
	       [DuongDanFile],
	       [TenFile],
	       [GhiChu],
	       [DataLocked],
	       [CreatedBy],
	       [CreatedAt],
	       [LastModifiedBy],
	       [LastModifiedAt],
	       [DeletedStatus],
	       [PrintStatus],
	       [RecordStatus],
	       [SubmitedBy],
	       [SubmitedAt],
	       [ApprovedBy],
	       [ApprovedAt]
	FROM   [dbo].[GiayPhepQuangCaoNhan]
	WHERE  [GiayPhepQuangCaoID] = @GiayPhepQuangCaoID
	       AND DeletedStatus <> 1;
END

```
