# Stored Procedure: `sp_TC_DoiTruVaTinhLaiThucChayDaTinh_CPM_With_DonViTinh_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-06-29 10:15:49.350000
- **Ngày sửa cuối**: 2018-07-02 17:06:04.393000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC  [dbo].[sp_TC_DoiTruVaTinhLaiThucChayDaTinh_CPM_With_DonViTinh_Ngay] '2018-06-14' , '2018-06-29', 1003722, 240, '2018-06-29'
*/
CREATE  PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLaiThucChayDaTinh_CPM_With_DonViTinh_Ngay] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME,
	@HopDongID INT,
	@DmSanPhamREF INT,
	@NgayGhiNhanThucChay DATETIME
AS
    BEGIN
        DECLARE @HopDongREF INT ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietID INT
      
        DECLARE Record_Cursor CURSOR
        FOR
            SELECT DISTINCT
                    hd.HopDongID ,
                    hd.SoHopDong ,
                    hdct.HopDongChiTietID
            FROM    (SELECT * FROM dbo.HopDong WHERE HopDongID = @HopDongID) hd
						INNER JOIN (SELECT HopDongChiTietID, HopDongFK, DmSanPhamREF FROM dbo.HopDongChiTiet 
						WHERE HopDongFK = @HopDongID 
						AND DmSanPhamREF = @DmSanPhamREF
						AND DeletedStatus = 0
						AND DmSanPhamREF IN ( 231, 238, 339, 240, 370, 598, 613, 735, 342 )
						AND NOT ( DmLoaiREF IN ( 13, 42 ) OR DmLoaiBannerREF = 18)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
						AND ( ( [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0,DonViTinh) = 1 ))--DON VI TINH NGAY CUA SAN PHAM CPM
					) hdct ON hdct.HopDongFK = hd.HopDongID
		
        OPEN Record_Cursor

		-- Perform the first fetch.
        FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID
        WHILE @@FETCH_STATUS = 0
            BEGIN
				--PRINT N'Doi tru thuc chay'
				EXEC [dbo].[sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay_ByHopDongChiTietAndNgay]
					@FromDate = @StartDate
				  , @ToDate = @EndDate
				  , @HopDongID = @HopDongID
				  , @HopDongChiTietID = @HopDongChiTietID
				  , @NgayTinh = @NgayGhiNhanThucChay

				----THUC HIEN TINH LAI VAO NGAYTHUCHIEN
				EXEC [dbo].[ThucChay_ReInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_ByHopDongChiTiet_AndNgay] 
					@FromDate = @StartDate,
					@ToDate = @EndDate,
					@pSoHopDong = @SoHopDong,
					@pHopDongChiTietID = @HopDongChiTietID,
					@DmSanPhamREF = @DmSanPhamREF,
					@NgayThucHienGhiNhan = @NgayGhiNhanThucChay
					
                FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID
            END
        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor
        SELECT  2
    END



```
