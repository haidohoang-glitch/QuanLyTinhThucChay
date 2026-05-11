# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_TRUEVIEW_TuNgayDenNgay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-06-15 15:25:56.737000
- **Ngày sửa cuối**: 2022-06-15 15:26:12.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_TRUEVIEW_TuNgayDenNgay] '2018-01-04', '2018-01-08','QC2761217'
*/

CREATE  PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_TRUEVIEW_TuNgayDenNgay]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @SoHopDong NVARCHAR(200)

AS
    BEGIN

        DECLARE @NgayThucHien DATETIME


        SET @NgayThucHien = @StartDate

		WHILE ( @NgayThucHien <= @EndDate )
        BEGIN
		
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ByHopDong] 
			@ID = 99
			, @Case = 4 --TRUE VIEW
			, @NgayThucHien = @NgayThucHien
			, @SoHopDong = @SoHopDong

			SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
        END 


    END


```
