# Stored Procedure: `BPTC_Report_BCKD_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.700000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.700000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ReportID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Report_BCKD_Delete] ( @ReportID INT )
AS 
    BEGIN
		--UPDATE BPTC_ThongTinBCKD
        UPDATE  dbo.BPTC_ThongTinBCKD
        SET DeleteStatus = 1
        WHERE   ( BPTC_ThongTinBCKDID = @ReportID
                  OR @ReportID = -1
                )
    END

```
