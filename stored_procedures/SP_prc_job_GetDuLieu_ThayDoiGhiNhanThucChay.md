# Stored Procedure: `prc_job_GetDuLieu_ThayDoiGhiNhanThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-25 17:47:26.413000
- **Ngày sửa cuối**: 2021-07-01 09:47:02.497000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[prc_job_GetDuLieu_ThayDoiGhiNhanThucChay]
AS
BEGIN
  DECLARE @tmp TABLE(
    FromDate DATE,
    ToDATE DATE
  )

  /* Lấy các config job cần được chạy */
  INSERT INTO @tmp
  (
      FromDate,
      ToDATE
  )
  SELECT CONVERT(DATE, FromDate), CONVERT(DATE, ToDate)
  FROM dbo.ADX_Job_UpdateStatusThayDoiThucChay
  WHERE IsDeleted = 0 AND Status = 1

  /* RETURN DATA */
  SELECT a.Request_key,
    ISNULL(a.RecordStatus, 0) AS Status,
    a.LyDoTuChoi
  FROM dbo.ThucChay_PerformanceBase_ThayDoi a
  WHERE a.DeletedStatus = 0 AND a.RecordStatus <> 0 AND EXISTS (
    SELECT 1
    FROM @tmp b
    WHERE a.LastModifiedAt >= b.FromDate AND a.LastModifiedAt < DATEADD(dd, 1,  b.ToDATE)
  )


END




```
