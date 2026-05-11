# Stored Procedure: `TCDT_TCDTAdmarket_CheckCan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-02-15 16:55:17.783000
- **Ngày sửa cuối**: 2026-03-18 08:25:20.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[TCDT_TCDTAdmarket_CheckCan]
    -- Add the parameters for the stored procedure here
    @NgayBatDau DATETIME,
    @NgayKetThuc DATETIME
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -----HopDong Kinh te----------------


    SELECT 'ADX_Quang_cao_PerBase' Loai,
		ISNULL( A.DmSanPhamREF,B.DmSanPhamREF) DmSanPhamREF,
		ISNULL( A.DmViTriREF,B.DmViTriREF) DmViTriREF,
		ISNULL(A.TenViTri,B.TenViTri) TenViTri,
		( ISNULL(A.tcdt,0) - ISNULL( B.tcdt,0)) AS lech
    FROM
    (
        SELECT DmSanPhamREF,
               ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
               DmViTriREF,
               TenViTri --,-- DonViTinh--,SoHopDong
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628, 337 )
              AND NgayThucHien
              BETWEEN @NgayBatDau AND @NgayKetThuc
              --and GhiChu = 'ThucChay_Insert_ThucChayDaTinh_Admatic_Adx'
              AND DmHinhThucQuangCao <> 42
              --AND DmSanPhamREF = 585 --AND DmViTriREF =1
              AND TenMaHopDong NOT IN
                  (
                      SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                  ) --('NB','S-NB','C-NB','NBDT','NBNG')  
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri
    --ORDER BY DmSanPhamREF, DmViTriREF	
    ) A
       full JOIN
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri --,-- DonViTinh--,SoHopDong
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628, 337 )
                  AND NgayThucHien
                  BETWEEN @NgayBatDau AND @NgayKetThuc
                  AND TenMaHopDong NOT IN
                      (
                          SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                      ) --('NB','S-NB','C-NB','NBDT','NBNG')  
                  -- and GhiChu = 'ThucChay_Insert_ThucChayDaTinh_Admatic_Adx'
                  AND DmHinhThucQuangCao <> 42
            -- AND DmSanPhamREF = 585-- AND DmViTriREF =1
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     TenViTri
        --ORDER BY DmSanPhamREF, DmViTriREF
        ) B
            ON A.DmSanPhamREF = B.DmSanPhamREF
               AND A.DmViTriREF = B.DmViTriREF
               AND A.TenViTri = B.TenViTri --02/12/2024 duongnt comment do sp không phát hiện lệch trường hợp cùng DmViTriREF nhưng TenViTri= rỗng 
    --WHERE B.DmViTriREF IN ( 0, 1, 2, 3, 4 ); --02/12/2024 duongnt comment do thực tế có các VitriID khác 



    SELECT 'ADX_Quang_cao_Admatic' Loai,
        ISNULL( A.DmSanPhamREF,B.DmSanPhamREF) DmSanPhamREF,
		ISNULL( A.DmViTriREF,B.DmViTriREF) DmViTriREF,
		ISNULL(A.TenViTri,B.TenViTri) TenViTri,
		( ISNULL(A.tcdt,0) - ISNULL( B.tcdt,0)) AS lech
    FROM
    (
        SELECT DmSanPhamREF,
               ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
               DmViTriREF,
               TenViTri --, DonViTinh--,SoHopDong
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628, 337 )
              AND NgayThucHien
              BETWEEN @NgayBatDau AND @NgayKetThuc
              --and GhiChu = 'ThucChay_Insert_ThucChayDaTinh_Admatic_Adx'
              AND DmHinhThucQuangCao = 42
              --AND DmSanPhamREF = 585 --AND DmViTriREF =1
              AND TenMaHopDong NOT IN
                  (
                      SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                  ) --('NB','S-NB','C-NB','NBDT','NBNG')  
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri
    ) A
      full JOIN
        --ORDER BY DmSanPhamREF, DmViTriREF		
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri --, DonViTinh--,SoHopDong
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628, 337 )
                  AND NgayThucHien
                  BETWEEN @NgayBatDau AND @NgayKetThuc
                  AND TenMaHopDong NOT IN
                      (
                          SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                      ) --('NB','S-NB','C-NB','NBDT','NBNG')  
                  -- and GhiChu = 'ThucChay_Insert_ThucChayDaTinh_Admatic_Adx'
                  AND DmHinhThucQuangCao = 42
            -- AND DmSanPhamREF = 585-- AND DmViTriREF =1
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     TenViTri
        ) B
            ON A.DmSanPhamREF = B.DmSanPhamREF
               AND A.DmViTriREF = B.DmViTriREF
              AND A.TenViTri = B.TenViTri; --02/12/2024 duongnt comment do sp không phát hiện lệch trường hợp cùng DmViTriREF nhưng TenViTri= rỗng 
    --and A.DonViTinh = B.DonViTinh



    --ORDER BY DmSanPhamREF, DmViTriREF
    -------------Khuyến mại--------------

    SELECT 'ADX_KhuyenMai_Per' Loai,
         ISNULL( A.DmSanPhamREF,B.DmSanPhamREF) DmSanPhamREF,
		ISNULL( A.DmViTriREF,B.DmViTriREF) DmViTriREF,
		ISNULL(A.TenViTri,B.TenViTri) TenViTri,
		( ISNULL(A.tcdt,0) - ISNULL( B.tcdt,0)) AS lech
    FROM
    (
        SELECT DmSanPhamREF,
               ROUND(SUM(ThanhTienKM + GiaTriKMThayDoi), 0) tcdt,
               DmViTriREF,
               TenViTri -- --DonViTinh--,SoHopDong
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628, 337 )
              AND NgayThucHien
              BETWEEN @NgayBatDau AND @NgayKetThuc
              --and GhiChu = 'ThucChay_Insert_ThucChayDaTinh_Admatic_Adx'
              --duongnt 16/05/2023 AND DmHinhThucQuangCao <> 42 
              --AND DmSanPhamREF = 585 --AND DmViTriREF =1
              AND TenMaHopDong NOT IN
                  (
                      SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                  ) --('NB','S-NB','C-NB','NBDT','NBNG')  
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri
    ) A
        --ORDER BY DmSanPhamREF, DmViTriREF	

     full  JOIN
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienKM + GiaTriKMThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri --, --DonViTinh--,SoHopDong
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628, 337 )
                  AND NgayThucHien
                  BETWEEN @NgayBatDau AND @NgayKetThuc
                  AND TenMaHopDong NOT IN
                      (
                          SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                      ) --('NB','S-NB','C-NB','NBDT','NBNG')  
            -- and GhiChu = 'ThucChay_Insert_ThucChayDaTinh_Admatic_Adx'
            --duongnt 16/05/2023 AND DmHinhThucQuangCao <> 42
            -- AND DmSanPhamREF = 585-- AND DmViTriREF =1
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     TenViTri
        ) B
            ON A.DmSanPhamREF = B.DmSanPhamREF
               AND A.DmViTriREF = B.DmViTriREF
               AND A.TenViTri = B.TenViTri; --02/12/2024 duongnt comment do sp không phát hiện lệch trường hợp cùng DmViTriREF nhưng TenViTri= rỗng 
    --ORDER BY DmSanPhamREF, DmViTriREF

    ----HopDong NB------------

    SELECT 'ADX_NoiBo_Per' Loai,
          ISNULL( A.DmSanPhamREF,B.DmSanPhamREF) DmSanPhamREF,
		ISNULL( A.DmViTriREF,B.DmViTriREF) DmViTriREF,
		ISNULL(A.TenViTri,B.TenViTri) TenViTri,
		( ISNULL(A.tcdt,0) - ISNULL( B.tcdt,0)) AS lech
    FROM
    (
        SELECT DmSanPhamREF,
               ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
               DmViTriREF,
               TenViTri --,-- DonViTinh--,SoHopDong
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628, 337 )
              AND NgayThucHien
              BETWEEN @NgayBatDau AND @NgayKetThuc
              --duongnt 16/05/2023 AND DmHinhThucQuangCao <> 42
              --AND DmSanPhamREF = 585 --AND DmViTriREF =1
              AND TenMaHopDong IN
                  (
                      SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                  ) --('NB','S-NB','C-NB','NBDT','NBNG')  
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri
    ) A
     full   JOIN
        --ORDER BY DmSanPhamREF, DmViTriREF						
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri --, ---DonViTinh--,SoHopDong
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628, 337 )
                  AND NgayThucHien
                  BETWEEN @NgayBatDau AND @NgayKetThuc
                  AND TenMaHopDong IN
                      (
                          SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                      ) --('NB','S-NB','C-NB','NBDT','NBNG')  
            --duongnt 16/05/2023 AND DmHinhThucQuangCao <> 42
            --AND DmSanPhamREF = 585 AND DmViTriREF =1
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     TenViTri
        ) B
            ON A.DmSanPhamREF = B.DmSanPhamREF
               AND A.DmViTriREF = B.DmViTriREF
               AND A.TenViTri = B.TenViTri; --02/12/2024 duongnt comment do sp không phát hiện lệch trường hợp cùng DmViTriREF nhưng TenViTri= rỗng 
--ORDER BY DmSanPhamREF, DmViTriREF


END;

```
