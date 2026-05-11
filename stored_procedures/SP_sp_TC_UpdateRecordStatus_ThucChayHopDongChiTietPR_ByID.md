# Stored Procedure: `sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR_ByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-10-23 13:54:40.467000
- **Ngày sửa cuối**: 2018-10-23 13:54:48.057000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDong` | `int(4)` | No |
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR_ByID]
    @NgayThucHien DATETIME,
	@HopDong INT,
	@ThucChayHopDongChiTietPRID INT,
	@DmSanPhamREF INT
AS
    BEGIN
	
	
        UPDATE  dbo.ThucChayHopDongChiTietPR
        SET     RecordStatus = 1
        WHERE ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
		AND HopDongREF= @HopDong
		AND DmSanPhamREF = @DmSanPhamREF
		AND EXISTS (
					
                SELECT DISTINCT DotChayBooking
                FROM    dbo.ThucChayDaTinh
                WHERE  HopDongID = @HopDong
				AND DmSanPhamREF = @DmSanPhamREF
                        AND DmSanPhamREF IN ( 141, 245, 250, 637, 305 )
                        AND NOT ( DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18 ) 
						AND NgayThucHien = @NgayThucHien
						AND DotChayBooking = CONVERT(NVARCHAR(100),ThucChayHopDongChiTietPRID)
				)
                      

    END;



```
