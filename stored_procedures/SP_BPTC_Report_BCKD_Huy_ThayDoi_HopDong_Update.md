# Stored Procedure: `BPTC_Report_BCKD_Huy_ThayDoi_HopDong_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.543000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.543000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Huy_ThayDoi_HopDongID` | `int(4)` | No |
| `@Huy_ThayDoi_HopDongBroID` | `int(4)` | No |
| `@LyDoHuy` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Report_BCKD_Huy_ThayDoi_HopDong_Update]
    (
      @Huy_ThayDoi_HopDongID INT ,
      @Huy_ThayDoi_HopDongBroID INT ,
      @LyDoHuy NVARCHAR(500)
    )
AS 
    BEGIN
        
        IF @Huy_ThayDoi_HopDongID > 0 
            BEGIN
                UPDATE  dbo.BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong
                SET     LyDoHuy = @LyDoHuy
                WHERE   BPTC_ThongTinBCKD_Huy_ThayDoi_HopDongID = @Huy_ThayDoi_HopDongID
            END
            
        IF @Huy_ThayDoi_HopDongBroID > 0 
            BEGIN
                UPDATE  dbo.BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong_Bro
                SET     LyDoHuy = @LyDoHuy
                WHERE   BPTC_ThongTinBCKD_Huy_ThayDoi_HopDongID = @Huy_ThayDoi_HopDongBroID
            END
            
    END

```
