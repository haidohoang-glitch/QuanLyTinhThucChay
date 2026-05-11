# Stored Procedure: `sp_TC_CapNhatThuTuTrongSoThucChayHopDongChiTietPR_ByHopDongSanPham_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-10-31 15:15:26.893000
- **Ngày sửa cuối**: 2018-10-31 15:15:26.893000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@pHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[sp_TC_CapNhatThuTuTrongSoThucChayHopDongChiTietPR_ByHopDongSanPham_dev]  '2018-10-14', 141 , 1005948
*/

CREATE PROCEDURE [dbo].[sp_TC_CapNhatThuTuTrongSoThucChayHopDongChiTietPR_ByHopDongSanPham_dev]
    @EndDate DATETIME ,
	@DmSanPhamREF INT,
    @pHopDongID INT
AS
    BEGIN

        DECLARE  @NgayGioiHanTinh DATETIME;
        SET @NgayGioiHanTinh = '2014-01-01';
		
       DECLARE @ThucChayHopDongChiTietPRID INT ,
            @HopDongREF INT ,
            @ChietKhau FLOAT ,
            @ThucChayHopDongChiTietPrREF INT ,
            @HopDongChiTietREF INT ,
            @DmHinhThucQuangCaoREF INT ,
            @DmWebsiteREF INT ,
            @GiaTien BIGINT ,
            @SoLuong INT
		
		--XOA THONG TIN THU TU THUC TREO CUA PR

		DELETE FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_HopDong]
		WHERE HopDongREF = @pHopDongID

        DECLARE icursor CURSOR
        FOR
            SELECT  ThucChayHopDongChiTietPRID ,
                    HopDongREF ,
                    ChietKhau ,
                    ThucChayHopDongChiTietPrREF ,
                    HopDongChiTietREF ,
                    DmHinhThucQuangCaoREF ,
                    DmSanPhamREF ,
                    DmWebsiteREF ,
                    GiaTien ,
                    SoLuong
            FROM    dbo.ThucChayHopDongChiTietPR
            WHERE   DeletedStatus <> 1
					AND HopDongREF = @pHopDongID
					AND DmSanPhamREF = @DmSanPhamREF
                    AND RecordStatus = 0
                    AND DmHinhThucQuangCaoREF <> 0
                    AND ThoiGianBatDau >= '2014-01-01'
                    AND ( CASE WHEN CreatedAt >= LastModifiedAt
                                THEN CONVERT(DATE, CreatedAt)
                                ELSE CONVERT(DATE, LastModifiedAt)
                            END ) <= @EndDate
                    ORDER BY LastModifiedAt   
        OPEN icursor;  

        FETCH NEXT FROM icursor   
		INTO @ThucChayHopDongChiTietPRID, @HopDongREF, @ChietKhau,
            @ThucChayHopDongChiTietPrREF, @HopDongChiTietREF,
            @DmHinhThucQuangCaoREF, @DmSanPhamREF, @DmWebsiteREF,
            @GiaTien, @SoLuong

        WHILE @@FETCH_STATUS = 0
            BEGIN  
                BEGIN
							INSERT  INTO dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_HopDong]
                            SELECT  @pHopDongID,*, @DmHinhThucQuangCaoREF, @DmSanPhamREF, (@GiaTien*@SoLuong*(100-@ChietKhau)/100) AS ThanhTienThucChay
                            FROM    [dbo].[fn_TC_Get_ThuThu_HopDongChiTietID_PR] (@ThucChayHopDongChiTietPRID,
                                                        @HopDongREF,
                                                        @ChietKhau,
                                                        @ThucChayHopDongChiTietPrREF,
                                                        @HopDongChiTietREF,
                                                        @DmHinhThucQuangCaoREF,
                                                        @DmSanPhamREF,
                                                        @DmWebsiteREF,
                                                        @GiaTien,
                                                        @SoLuong);

                END;
	 
                FETCH NEXT FROM icursor   
				INTO @ThucChayHopDongChiTietPRID, @HopDongREF,
                    @ChietKhau, @ThucChayHopDongChiTietPrREF,
                    @HopDongChiTietREF, @DmHinhThucQuangCaoREF,
                    @DmSanPhamREF, @DmWebsiteREF, @GiaTien, @SoLuong
            END;   
        CLOSE icursor;  
        DEALLOCATE icursor;  
 END;


```
