# Stored Procedure: `usp_GiayPhepQuangCao_GetGiayPhepDuyetByNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:26:10.897000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.450000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_GetGiayPhepDuyetByNhanHang]
	@DmNhanHangID INT
AS
BEGIN
	SELECT ROW_NUMBER() OVER(ORDER BY [GiayPhepQuangCaoID] ASC) STT,
	       A.[GiayPhepQuangCaoID],
	       A.[TenGiayPhep],
	       A.[DmLoaiGiayPhepREF],
	       A.[DmNhanHangREF],
	       CONVERT(VARCHAR(10), A.ThoiGianHieuLuc, 103) AS ThoiGianHieuLuc,
	       A.[DuongDanFile],
	       A.[TenFile],
	       A.[GhiChu],
	       A.DataLocked,
	       A.RecordStatus,
	       CASE A.RecordStatus
	            WHEN 0 THEN N'Nháp'
	            WHEN 1 THEN N'Chờ Duyệt'
	            WHEN 2 THEN N'Đã Duyệt'
	            WHEN 3 THEN N'Từ chối'
	       END AS ReviewStatus,
	       B.TenLoaiGiayPhep,
	       A.[SubmitedBy],
	       A.[SubmitedAt],
	       A.[ApprovedBy],
	       A.[ApprovedAt]
	FROM   GiayPhepQuangCaoNhan AS A
	       INNER JOIN DmLoaiGiayPhepQuangCao B
	            ON  A.DmLoaiGiayPhepREF = B.DmLoaiGiayPhepID
	WHERE DmNhanHangREF = @DmNhanHangID AND A.DeletedStatus <> 1 AND A.RecordStatus IN (1,2)
	ORDER BY A.RecordStatus DESC, A.[LastModifiedAt] ASC;
END

```
