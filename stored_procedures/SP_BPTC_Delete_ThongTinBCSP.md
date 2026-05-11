# Stored Procedure: `BPTC_Delete_ThongTinBCSP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.520000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.520000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ReportID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Delete_ThongTinBCSP] ( @ReportID INT )
AS 
    BEGIN	
        UPDATE  dbo.BPTC_BaoCaoTTSanPhamThang
        SET     DeleteStatus = 1
        WHERE   BPTC_BaoCaoTTSanPhamThangID = @ReportID		
    END

```
