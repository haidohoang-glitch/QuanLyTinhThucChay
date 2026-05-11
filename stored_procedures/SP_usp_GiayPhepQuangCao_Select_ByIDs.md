# Stored Procedure: `usp_GiayPhepQuangCao_Select_ByIDs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:25:34.460000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GiayPhepQuangCaoID` | `varchar(500)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_Select_ByIDs]
	@GiayPhepQuangCaoID VARCHAR(500)
AS
BEGIN
	SET NOCOUNT ON;
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	
	DECLARE @Result NVARCHAR(MAX);
	
	SET @Result = @GiayPhepQuangCaoID;
	
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
		   CASE RecordStatus
				WHEN 0 THEN N'Nháp'
	            WHEN 1 THEN N'Chờ duyệt'
	            WHEN 2 THEN N'Ðã duyệt'
				WHEN 3 THEN N'Từ chối'
	       END AS ReviewStatus,
	       [SubmitedBy],
	       [SubmitedAt],
	       [ApprovedBy],
	       [ApprovedAt]
	FROM   [dbo].[GiayPhepQuangCaoNhan]
	WHERE  [GiayPhepQuangCaoID] IN (SELECT *
	                                FROM   dbo.[Split](@Result, ','))
	       AND DeletedStatus <> 1;
END

```
