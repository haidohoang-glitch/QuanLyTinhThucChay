# Stored Procedure: `KiemTra_DaTinh_PR_TinhDungDu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 10:30:01.337000
- **Ngày sửa cuối**: 2016-12-05 11:12:53

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--[KiemTra_DaTinh_PR_TinhDungDu] '2016-01-01','2016-12-31'
CREATE PROCEDURE [dbo].[KiemTra_DaTinh_PR_TinhDungDu] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME
AS
    BEGIN
	

        SELECT  A.* ,
                B.*
        FROM    ( SELECT    HopDongREF ,
                            dbo.GetSoHopDongByID(tt.HopDongREF) shd ,
                            DmSanPhamREF ,
                            ( CASE WHEN hd.TrangThaiHopDong = 3 THEN 0
                                   ELSE SUM(CONVERT(FLOAT, GiaTien * SoLuong)
                                            * ( 100 - ChietKhau ) / 100)
                              END ) tt
                  FROM      dbo.ThucChayHopDongChiTietPR tt
                            INNER JOIN HopDong hd ON hd.HopDongID = tt.HopDongREF
                  WHERE     ThoiGianBatDau >= @StartDate
                            AND tt.DeletedStatus = 0
                            AND tt.LastModifiedAt >= @StartDate
                            AND tt.CreatedAt < DATEADD(DAY, 1, @EndDate)
                            AND NOT ( tt.CreatedAt >= @StartDate
                                      AND ChietKhau <> 100
                                      AND DmSanPhamREF NOT IN ( 141, 637, 305 )
                                    )
                            AND tt.DmHinhThucQuangCaoREF <> 13
--AND tt.HopDongREF =45488
GROUP BY                    HopDongREF ,
                            DmSanPhamREF ,
                            hd.TrangThaiHopDong
                ) A
                LEFT JOIN ( SELECT  tc.HopDongID ,
                                    tc.DmSanPhamREF ,
                                    SUM(ThanhTienSauTrietKhauThucChay
                                        + GiaTriThayDoi) tc ,
                                    tc.SoHopDong
                            FROM    dbo.ThucChayDaTinh tc
                            WHERE   DmSanPhamREF IN ( 141, 637, 305 )
                                    AND tc.TrangThaiHopDong <> 3
                                    AND NOT ( tc.DmHinhThucQuangCao = 13
                                              OR tc.DmLoaiBannerREF = 18
                                            )
                            GROUP BY tc.HopDongID ,
                                    tc.DmSanPhamREF ,
                                    tc.SoHopDong
                          ) B ON A.HopDongREF = B.HopDongID
                                 AND A.DmSanPhamREF = B.DmSanPhamREF
        WHERE   1 = 1
                AND ( ISNULL(A.tt, 0) <> ISNULL(B.tc, 0)
                      OR A.HopDongREF IS NULL
                      OR B.HopDongID IS NULL
                    )
        ORDER BY A.DmSanPhamREF ,
                A.HopDongREF

    END

```
