# Stored Procedure: `usp_GiayPhepQuangCao_GetByNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:52.990000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `varchar(50)` | No |
| `@UserName` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_GetByNhanHang]
	@DmNhanHangID VARCHAR(50),
	@UserName NVARCHAR(500)
AS
BEGIN
	DECLARE @SQL            NVARCHAR(MAX);
	DECLARE @sUser			NVARCHAR(MAX);	
	
	IF (@UserName <> '')
	    SET @sUser = ' AND A.CreatedBy = ''' + @UserName + '''';
	ELSE 
		SET @sUser = ' ';
		
	SET @SQL = 
	    N'
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
	            WHEN 0 THEN N''Nháp''
	            WHEN 1 THEN N''Chờ Duyệt''
	            WHEN 2 THEN N''Đã Duyệt''
	            WHEN 3 THEN N''Từ chối''
	       END AS ReviewStatus,
	       B.TenLoaiGiayPhep,
	       A.[SubmitedBy],
	       A.[SubmitedAt],
	       A.[ApprovedBy],
	       A.[ApprovedAt]
	FROM   GiayPhepQuangCaoNhan AS A
	       INNER JOIN DmLoaiGiayPhepQuangCao B
	            ON  A.DmLoaiGiayPhepREF = B.DmLoaiGiayPhepID
	WHERE DmNhanHangREF = '+ @DmNhanHangID + ' AND A.DeletedStatus <> 1 ' + @sUser +' ORDER BY A.RecordStatus DESC, A.[LastModifiedAt] DESC;'
--	PRINT @SQL;
	EXEC sp_executesql @SQL;    
END

```
