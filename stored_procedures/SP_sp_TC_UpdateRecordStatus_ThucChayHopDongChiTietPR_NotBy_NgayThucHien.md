# Stored Procedure: `sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR_NotBy_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-11 15:53:30.260000
- **Ngày sửa cuối**: 2018-01-11 15:58:59.107000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@pHopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR_NotBy_NgayThucHien]
    @NgayThucHien DATETIME,
	@pHopDongID INT,
	@DmSanPhamREF INT
AS
    BEGIN
	
	
        UPDATE  ThucChayHopDongChiTietPR
        SET     RecordStatus = 1
        WHERE   ThucChayHopDongChiTietPRID IN (
				
					SELECT tc.ThucChayHopDongChiTietPRID 
					FROM 
					(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
						WHERE HopDongFK = @pHopDongID 
						AND DmSanPhamREF = @DmSanPhamREF 
						AND DeletedStatus = 0
					) hdct
					INNER JOIN dbo.ThucChay_ThongTinHopDongChiTietID_PR tc ON hdct.HopDongChiTietID = tc.HopDongChiTietID
				)
                      

    END;

	

--endregion


```
