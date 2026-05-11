# Stored Procedure: `usp_GiayPhepQuangCao_Select_ByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:25:17.230000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GiayPhepQuangCaoID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_Select_ByID]
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
	WHERE  [GiayPhepQuangCaoID] = @GiayPhepQuangCaoID AND DeletedStatus <> 1;
END

```
