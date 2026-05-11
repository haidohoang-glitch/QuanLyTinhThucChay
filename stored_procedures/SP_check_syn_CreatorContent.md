# Stored Procedure: `check_syn_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-04-27 11:24:42.173000
- **Ngày sửa cuối**: 2022-04-27 11:24:42.173000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[check_syn_CreatorContent]
AS
BEGIN
    SELECT A.*,
           B.*
    FROM
    (
        SELECT a.Id,
               a.HopDongBanRef,
               a.PhanBoRef,
               a.PbSoLuong,
               a.pbDonGia,
               a.PbChietKhau,
               a.PbThanhTien,
               a.TcSoLuong,
               a.TcDonGia,
               a.TcThanhTien,
               a.DonGia,
               a.ChietKhau,
               a.ThanhTien,
               a.IsDeleted,
               a.TrangThai,
               a.CreationTime,
               a.LastModificationTime
        FROM ASDAG2.AbpZeroDb_SanPham_CreatorContent.dbo.AppKetQuaVanHanh a
            JOIN ASDAG2.CONTRACT.dbo.CONTRACTS b
                ON a.HopDongBanRef = b.ID
        WHERE CONVERT(DATE, b.INDEXED_DATE) >= '2021-10-01'
              AND a.TrangThai NOT IN ( 1, 2, 4 )
              AND IsDeleted = 0
              AND a.CreationTime < CONVERT(DATE, GETDATE())
    ) A
        FULL OUTER JOIN
        (
            SELECT a.AppKetQuaVanHanh_CreatorContent_id,
                   a.HopDongBanRef,
                   a.PhanBoRef,
                   a.PbSoLuong,
                   a.PbChietKhau,
                   a.pbDonGia,
                   a.PbThanhTien,
                   a.TcSoLuong,
                   a.TcDonGia,
                   a.TcThanhTien,
                   a.DonGia,
                   a.ChietKhau,
                   a.ThanhTien,
                   a.IsDeleted,
                   a.TrangThai,
                   a.CreationTime,
                   a.LastModificationTime
            FROM ABM_Data_ThucChay.dbo.AppKetQuaVanHanh_CreatorContent a
                JOIN ABM_Data_ThucChay.dbo.HopDong b
                    ON b.HopDongID = a.HopDongBanRef
            WHERE TrangThai NOT IN ( 1, 2, 4 )
                  AND IsDeleted = 0
                  AND CONVERT(DATE, b.NgayDanhSoHopDong) >= '2021-10-01'
                  AND a.CreationTime < CONVERT(DATE, GETDATE())
        ) B
            ON A.Id = B.AppKetQuaVanHanh_CreatorContent_id
    WHERE A.Id IS NULL
          OR B.AppKetQuaVanHanh_CreatorContent_id IS NULL
          OR A.HopDongBanRef <> B.HopDongBanRef
          OR A.PhanBoRef <> B.PhanBoRef
          OR A.PbSoLuong <> B.PbSoLuong
          OR A.pbDonGia <> B.pbDonGia
          OR A.PbChietKhau <> B.PbChietKhau
          OR A.TcSoLuong <> B.TcSoLuong
          OR A.TcDonGia <> B.TcDonGia
          OR A.TcThanhTien <> B.TcThanhTien
          OR A.DonGia <> B.DonGia
          OR A.ChietKhau <> B.ChietKhau
          OR A.ThanhTien <> B.ThanhTien
          OR A.TrangThai <> B.TrangThai
    ORDER BY A.LastModificationTime,
             B.LastModificationTime DESC;
END;
```
