# Stored Procedure: `usp_GiayPhepQuangCao_GetListCanDuyetByNhanID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:56:41.157000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_GetListCanDuyetByNhanID]
	@DmNhanHangID INT
AS
BEGIN
	SELECT A.GiayPhepQuangCaoID,
	       A.DmNhanHangREF,
	       A.TenGiayPhep,
	       B.TenLoaiGiayPhep,
	       CONVERT(VARCHAR(10), A.ThoiGianHieuLuc, 103) AS ThoiGianHieuLuc,
	       A.TenFile,
	       A.DuongDanFile,
	       A.GhiChu,
	       A.DataLocked,
	       CASE A.RecordStatus
	            WHEN 1 THEN N'Chờ duyệt'
	            WHEN 2 THEN N'Ðã duyệt'
				WHEN 3 THEN N'Từ chối'
	       END AS RecordStatus,
	       A.RecordStatus AS Status
	FROM   GiayPhepQuangCaoNhan AS A
	       INNER JOIN DmLoaiGiayPhepQuangCao B
	            ON  A.DmLoaiGiayPhepREF = B.DmLoaiGiayPhepID
	WHERE  DmNhanHangREF = @DmNhanHangID
	       AND A.DeletedStatus <> 1
	       AND A.RecordStatus <> 0
END

```
