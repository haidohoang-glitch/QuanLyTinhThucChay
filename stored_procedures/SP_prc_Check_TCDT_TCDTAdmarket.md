# Stored Procedure: `prc_Check_TCDT_TCDTAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-04-28 15:18:45.230000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien1` | `date(3)` | No |
| `@ngayThucHien2` | `date(3)` | No |

## Definition (Source Code)

```sql


CREATE PROC [dbo].[prc_Check_TCDT_TCDTAdmarket]
    @ngayThucHien1 DATE = NULL,
    @ngayThucHien2 DATE = NULL
AS

BEGIN
    SET NOCOUNT ON;

    SELECT a.DmSanPhamREF AS tcdt_DmSanPhamREF,
           a.tcdt,
           a.DmViTriREF,
           a.TenViTri,
           --a.DonViTinh,
           b.DmSanPhamREF AS tcdtAdmarket_DmSanPhamREF,
           b.tcdt,
           b.DmViTriREF,
           b.TenViTri,
           --b.DonViTinh,
           ROUND(a.tcdt - b.tcdt, 0) AS ChenhLech
    FROM
    (
        SELECT DmSanPhamREF,
               ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
               DmViTriREF,
               TenViTri
               --,DonViTinh 
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628, 337 )
              AND NgayThucHien
              BETWEEN @ngayThucHien1 AND @ngayThucHien2
              AND DmHinhThucQuangCao <> 42
              AND TenMaHopDong NOT IN (SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus=0)
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 --DonViTinh,
                 TenViTri
    ) a
        JOIN
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri
				   --,DonViTinh 
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628, 337 )
                  AND NgayThucHien
                  BETWEEN @ngayThucHien1 AND @ngayThucHien2
                  AND TenMaHopDong NOT IN ( SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus=0 )
                  AND DmHinhThucQuangCao <> 42
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     --DonViTinh,
                     TenViTri
        ) b
            ON a.DmSanPhamREF = b.DmSanPhamREF
               AND a.DmViTriREF = b.DmViTriREF
               AND a.TenViTri = b.TenViTri
    ORDER BY a.DmSanPhamREF,
             a.DmViTriREF;
			 --a.DonViTinh;



    SELECT a.DmSanPhamREF AS tcdt_DmSanPhamREF,
           a.tcdt,
           a.DmViTriREF,
           a.TenViTri,
           --a.DonViTinh,
           b.DmSanPhamREF AS tcdtAdmarket_DmSanPhamREF,
           b.tcdt,
           b.DmViTriREF,
           b.TenViTri,
           --b.DonViTinh,
           ROUND(a.tcdt - b.tcdt, 0) AS ChenhLech
    FROM
    (
        SELECT DmSanPhamREF,
               ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
               DmViTriREF,
               TenViTri
			   --,DonViTinh
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628, 337 )
              AND NgayThucHien
              BETWEEN @ngayThucHien1 AND @ngayThucHien2
              AND DmHinhThucQuangCao = 42
              AND TenMaHopDong NOT IN ( SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus=0 )
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 --DonViTinh,
                 TenViTri
    ) a
        JOIN
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri
				   --,DonViTinh 
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628, 337 )
                  AND NgayThucHien
                  BETWEEN @ngayThucHien1 AND @ngayThucHien2
                  AND TenMaHopDong NOT IN ( SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus=0 )
                  AND DmHinhThucQuangCao = 42
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     --DonViTinh,
                     TenViTri
        ) b
            ON a.DmSanPhamREF = b.DmSanPhamREF
               --AND a.DonViTinh = b.DonViTinh
    ORDER BY a.DmSanPhamREF,
             a.DmViTriREF;
			 --a.DonViTinh;



    SELECT a.DmSanPhamREF AS tcdt_DmSanPhamREF,
           a.tcdt,
           a.DmViTriREF,
           a.TenViTri,
           --a.DonViTinh,
           b.DmSanPhamREF AS tcdtAdmarket_DmSanPhamREF,
           b.tcdt,
           b.DmViTriREF,
           b.TenViTri,
           --b.DonViTinh,
           ROUND(a.tcdt - b.tcdt, 0) AS ChenhLech
    FROM
    (
        SELECT DmSanPhamREF,
               ROUND(SUM(ThanhTienKM + GiaTriKMThayDoi), 0) tcdt,
               DmViTriREF,
               TenViTri
			   --,DonViTinh
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628, 337 )
              AND NgayThucHien
              BETWEEN @ngayThucHien1 AND @ngayThucHien2
              AND DmHinhThucQuangCao <> 42
              AND TenMaHopDong NOT IN ( SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus=0 )
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 --DonViTinh,
                 TenViTri
    ) a
        JOIN
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienKM + GiaTriKMThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri
				   --,DonViTinh
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628, 337 )
                  AND NgayThucHien
                  BETWEEN @ngayThucHien1 AND @ngayThucHien2
                  AND TenMaHopDong NOT IN (SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus=0 )
                  AND DmHinhThucQuangCao <> 42
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     --DonViTinh,
                     TenViTri
        ) b
            ON a.DmSanPhamREF = b.DmSanPhamREF
               AND a.DmViTriREF = b.DmViTriREF
               AND a.TenViTri = b.TenViTri
    ORDER BY a.DmSanPhamREF,
             a.DmViTriREF;
			 --a.DonViTinh;


    SELECT a.DmSanPhamREF AS tcdt_DmSanPhamREF,
           a.tcdt,
           a.DmViTriREF,
           a.TenViTri,
           --a.DonViTinh,
           b.DmSanPhamREF AS tcdtAdmarket_DmSanPhamREF,
           b.tcdt,
           b.DmViTriREF,
           b.TenViTri,
           --b.DonViTinh,
           ROUND(a.tcdt - b.tcdt, 0) AS ChenhLech
    FROM
    (
        SELECT DmSanPhamREF,
               ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
               DmViTriREF,
               TenViTri
			   --,DonViTinh
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628, 337 )
              AND NgayThucHien
              BETWEEN @ngayThucHien1 AND @ngayThucHien2
              AND DmHinhThucQuangCao <> 42
              AND TenMaHopDong IN ( SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus=0)
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 --DonViTinh,
                 TenViTri
    ) a
        JOIN
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri
				   --,DonViTinh
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628, 337 )
                  AND NgayThucHien
                  BETWEEN @ngayThucHien1 AND @ngayThucHien2
                  AND TenMaHopDong IN (SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus=0 )
                  AND DmHinhThucQuangCao <> 42
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     --DonViTinh,
                     TenViTri
        ) b
            ON a.DmSanPhamREF = b.DmSanPhamREF
               AND a.DmViTriREF = b.DmViTriREF
               AND a.TenViTri = b.TenViTri
    ORDER BY a.DmSanPhamREF,
             a.DmViTriREF;
			 --a.DonViTinh;


END;


```
