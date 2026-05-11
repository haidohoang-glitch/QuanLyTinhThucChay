# Stored Procedure: `sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-08 10:47:34.303000
- **Ngày sửa cuối**: 2017-08-31 16:17:35.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@pHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR]
    @NgayThucHien DATETIME,
	@pHopDongID INT
AS
    BEGIN
	
	
        UPDATE  ThucChayHopDongChiTietPR
        SET     RecordStatus = 1
        WHERE   ThucChayHopDongChiTietPRID IN (
                SELECT  DotChayBooking
                FROM    ThucChayDaTinh
                WHERE   NgayThucHien = @NgayThucHien
                        AND DmSanPhamREF IN ( 141, 245, 250, 637, 305 )
						AND (@pHopDongID IS NULL OR HopDongID = @pHopDongID)
                        AND NOT ( DmHinhThucQuangCao = 13
                                  OR DmLoaiBannerREF = 18
                                ) );

    END;

	

--endregion


```
