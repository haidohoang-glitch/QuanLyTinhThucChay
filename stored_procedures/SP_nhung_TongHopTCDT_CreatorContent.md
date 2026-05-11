# Stored Procedure: `nhung_TongHopTCDT_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:52:59.547000
- **Ngày sửa cuối**: 2026-03-06 16:52:59.547000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_TongHopTCDT_CreatorContent
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH hd AS ( 
        SELECT TOP 1
            HopDongChiTietID,
            ChietKhau,
            TenSanPham,
            CASE 
                WHEN ChietKhau = 100 THEN SoLuong * DonGia 
                ELSE ThanhTien 
            END AS ThanhtienHD_num
        FROM dbo.HopDongChiTiet
        WHERE HopDongChiTietID = @HopDongChiTietID
    ),

    sp AS (
        SELECT
            PhanBoRef,
            SUM(TRY_CONVERT(decimal(18,2), TcSoLuong))   AS Soluong_SP_num,
            SUM(TRY_CONVERT(decimal(18,2), TcThanhTien)) AS ThanhTien_SP_num,
            SUM(TRY_CONVERT(decimal(18,2), LaiLo))       AS ThanhtienLaiLo_SP_num
        FROM ABM_Data_ThucChay.dbo.AppKetQuaVanHanh_CreatorContent
        WHERE IsDeleted = 0
          AND PhanBoRef = @HopDongChiTietID
          AND TrangThai NOT IN (1,2,4)
        GROUP BY PhanBoRef
    ),

    tc AS (
        SELECT
            HopDongChiTietREF,
            SUM(TRY_CONVERT(decimal(18,2), SoLuongThucChay) + TRY_CONVERT(decimal(18,2), SoLuongThayDoi)) AS SoluongTC,
            SUM(TRY_CONVERT(decimal(18,2), ThanhTienSauTrietKhauThucChay) + TRY_CONVERT(decimal(18,2), GiaTriThayDoi)) AS ThanhtienTC_num,
            SUM(TRY_CONVERT(decimal(18,2), SoLuongThucChayKM) + TRY_CONVERT(decimal(18,2), SoLuongKMThayDoi)) AS SoluongKM,
            SUM(TRY_CONVERT(decimal(18,2), ThanhTienKM) + TRY_CONVERT(decimal(18,2), GiaTriKMThayDoi)) AS ThanhtienKm_num
        FROM dbo.ThucChayDaTinh
        WHERE HopDongChiTietREF = CAST(@HopDongChiTietID AS varchar(50))
        GROUP BY HopDongChiTietREF
    ),

    lai AS (
        SELECT
            HopDongChiTietREF,
            SUM(TRY_CONVERT(decimal(18,2), ThanhTienLaiThucChaySauCK) + TRY_CONVERT(decimal(18,2), GiaTriThayDoiLaiSauCK)) AS LaiTC_num,
            SUM(TRY_CONVERT(decimal(18,2), ThanhTienLaiThucChayKM)    + TRY_CONVERT(decimal(18,2), GiaTriKMLaiThayDoi))    AS LaiKm_num
        FROM dbo.ThucChayDaTinh_MuaNgoai
        WHERE HopDongChiTietREF = CAST(@HopDongChiTietID AS varchar(50))
        GROUP BY HopDongChiTietREF
    )

    SELECT
        hd.HopDongChiTietID,
        hd.TenSanPham,
        hd.ChietKhau,
        dbo.FormatNumber(COALESCE(hd.ThanhtienHD_num,0)) AS ThanhtienHD,

        dbo.FormatNumber(COALESCE(sp.Soluong_SP_num,0))  AS Soluong_SP,
        dbo.FormatNumber(COALESCE(sp.ThanhTien_SP_num,0)) AS ThanhTien_SP,
        dbo.FormatNumber(COALESCE(sp.ThanhtienLaiLo_SP_num,0)) AS ThanhtienLaiLo_SP,

        dbo.FormatNumber(
            CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.SoluongKM,0) ELSE COALESCE(tc.SoluongTC,0) END
        ) AS SoluongTC_ASD,

        dbo.FormatNumber(
            CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END
        ) AS ThanhtienTC_ASD,

        dbo.FormatNumber(
            CASE WHEN hd.ChietKhau = 100 THEN COALESCE(lai.LaiKm_num,0) ELSE COALESCE(lai.LaiTC_num,0) END
        ) AS Lai_ASD,

        (
            -- So HĐ
            CASE
                WHEN (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END) = COALESCE(hd.ThanhtienHD_num,0)
                    THEN N'HĐ: Đủ tiền'
                WHEN (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END) < COALESCE(hd.ThanhtienHD_num,0)
                    THEN N'HĐ: Thiếu ' + dbo.FormatNumber(
                            COALESCE(hd.ThanhtienHD_num,0) 
                            - (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END)
                         )
                ELSE N'HĐ: Vượt ' + dbo.FormatNumber(
                        (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END)
                        - COALESCE(hd.ThanhtienHD_num,0)
                     )
            END

            + N' | '

            -- So Lãi
            + CASE
                WHEN (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(lai.LaiKm_num,0) ELSE COALESCE(lai.LaiTC_num,0) END) = COALESCE(sp.ThanhtienLaiLo_SP_num,0)
                    THEN N'Lãi: Đủ'
                WHEN (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(lai.LaiKm_num,0) ELSE COALESCE(lai.LaiTC_num,0) END) < COALESCE(sp.ThanhtienLaiLo_SP_num,0)
                    THEN N'Lãi: Thiếu ' + dbo.FormatNumber(
                            COALESCE(sp.ThanhtienLaiLo_SP_num,0)
                            - (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(lai.LaiKm_num,0) ELSE COALESCE(lai.LaiTC_num,0) END)
                         )
                ELSE N'Lãi: Vượt ' + dbo.FormatNumber(
                        (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(lai.LaiKm_num,0) ELSE COALESCE(lai.LaiTC_num,0) END)
                        - COALESCE(sp.ThanhtienLaiLo_SP_num,0)
                     )
            END

            + N' | '

            -- So SP
            + CASE
                WHEN (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END) = COALESCE(sp.ThanhTien_SP_num,0)
                    THEN N'SP: Đủ tiền'
                WHEN (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END) < COALESCE(sp.ThanhTien_SP_num,0)
                    THEN N'SP: Thiếu ' + dbo.FormatNumber(
                            COALESCE(sp.ThanhTien_SP_num,0)
                            - (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END)
                         )
                ELSE N'SP: Vượt ' + dbo.FormatNumber(
                        (CASE WHEN hd.ChietKhau = 100 THEN COALESCE(tc.ThanhtienKm_num,0) ELSE COALESCE(tc.ThanhtienTC_num,0) END)
                        - COALESCE(sp.ThanhTien_SP_num,0)
                     )
            END
        ) AS GhiChu

    FROM hd
    LEFT JOIN sp  ON sp.PhanBoRef = hd.HopDongChiTietID
    LEFT JOIN tc  ON tc.HopDongChiTietREF = CAST(hd.HopDongChiTietID AS varchar(50))
    LEFT JOIN lai ON lai.HopDongChiTietREF = CAST(hd.HopDongChiTietID AS varchar(50));

END

```
