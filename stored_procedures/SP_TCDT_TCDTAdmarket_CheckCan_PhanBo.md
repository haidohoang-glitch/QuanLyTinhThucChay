# Stored Procedure: `TCDT_TCDTAdmarket_CheckCan_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-03-02 10:42:40.397000
- **Ngày sửa cuối**: 2025-04-09 14:32:43.637000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Ngaythuchien` | `datetime(8)` | No |
| `@n2` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
 CREATE PROCEDURE [dbo].[TCDT_TCDTAdmarket_CheckCan_PhanBo]
    -- Add the parameters for the stored procedure here
    @Ngaythuchien DATETIME,
    @n2 DATETIME
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -----HopDong Kinh te----------------
-- check tổng tiền sản phẩm trả về 
SELECT NgayThucHien,dbo.FormatNumber(ISNULL(SUM(CONVERT(FLOAT,domain_tt_money))/1,0)) AS Thucchaysanpham FROM dbo.ThucChayAdmarket_PhanBo WHERE
NgayThucHien BETWEEN  @Ngaythuchien AND @n2
GROUP BY NgayThucHien
ORDER BY NgayThucHien DESC
-- thực chạy ghi nhận total = tiền sản phẩm trả về + yêu cầu ghi nhận KPI + TDGP
SELECT NgayThucHien, DBO.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi)) AS Tongthucchayghinhan
FROM dbo.ThucChayDaTinhAdmarket WHERE 1=1
 AND NgayThucHien BETWEEN  @Ngaythuchien AND @n2
AND DmHinhThucQuangCao<>42
GROUP BY NgayThucHien
ORDER BY NgayThucHien DESC 
 -- Thực chạy KPI, TDGP ghi nhận 
SELECT  CONVERT(DATE, CreatedAt) AS Ngaythuchien ,  dbo.FormatNumber(SUM(SoTienThayDoi)) AS TDGPvaNBo
FROM dbo.ThucChay_PerformanceBase_ThayDoi 
WHERE CONVERT(DATE, CreatedAt) BETWEEN  @Ngaythuchien AND @n2
      AND RecordStatus = 1
	 AND (LoaiGhiNhan=1
      OR (
            SoHopDong LIKE N'%NB%' 
            OR SoHopDong LIKE N'%NBDT%' 
            OR SoHopDong LIKE N'%NBNG%' 
            OR SoHopDong LIKE N'%S-NB%' 
            OR SoHopDong LIKE N'%C-NB%' 
            OR SoHopDong LIKE N'%TN%'
    ))
GROUP BY CONVERT(DATE, CreatedAt) 
ORDER BY Ngaythuchien DESC

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
               TenViTri 
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628 )
              AND NgayThucHien
              BETWEEN @Ngaythuchien AND @n2
                        AND DmHinhThucQuangCao <> 42
                           AND TenMaHopDong NOT IN
                  (
                      SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                  )
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri
       ) A
       full JOIN
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628 )
                  AND NgayThucHien
                  BETWEEN @Ngaythuchien AND @n2
                  AND TenMaHopDong NOT IN
                      (
                          SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                      )
                  AND DmHinhThucQuangCao <> 42
                     GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     TenViTri
               ) B
            ON A.DmSanPhamREF = B.DmSanPhamREF
               AND A.DmViTriREF = B.DmViTriREF
               AND A.TenViTri = B.TenViTri
    WHERE B.DmViTriREF IN ( 0, 1, 2, 3, 4 );



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
               TenViTri
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628 )
              AND NgayThucHien
              BETWEEN @Ngaythuchien AND @n2
              AND DmHinhThucQuangCao = 42
              AND TenMaHopDong NOT IN
                  (
                      SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                  ) 
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri
    ) A
      full JOIN		
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri 
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628)
                  AND NgayThucHien
                  BETWEEN @Ngaythuchien AND @n2
                  AND TenMaHopDong NOT IN
                      (
                          SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                      ) 
                  AND DmHinhThucQuangCao = 42
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     TenViTri
        ) B
            ON A.DmSanPhamREF = B.DmSanPhamREF
               AND A.DmViTriREF = B.DmViTriREF
               AND A.TenViTri = B.TenViTri;
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
               TenViTri
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628 )
              AND NgayThucHien
              BETWEEN @Ngaythuchien AND @n2
              AND TenMaHopDong NOT IN
                  (
                      SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                  ) 
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri
    ) A
     full  JOIN
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienKM + GiaTriKMThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri 
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628)
                  AND NgayThucHien
                  BETWEEN @Ngaythuchien AND @n2
                  AND TenMaHopDong NOT IN
                      (
                          SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                      ) 
					 GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     TenViTri
        ) B
            ON A.DmSanPhamREF = B.DmSanPhamREF
               AND A.DmViTriREF = B.DmViTriREF
               AND A.TenViTri = B.TenViTri;

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
               TenViTri 
        FROM dbo.ThucChayDaTinh
        WHERE DmSanPhamREF IN ( 144, 585, 628 )
              AND NgayThucHien
              BETWEEN @Ngaythuchien AND @n2
              AND TenMaHopDong IN
                  (
                      SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                  ) 
				  GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri
    ) A
     full   JOIN					
        (
            SELECT DmSanPhamREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                   DmViTriREF,
                   TenViTri 
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND DmSanPhamREF IN ( 144, 585, 628 )
                  AND NgayThucHien
                  BETWEEN @Ngaythuchien AND @n2
                  AND TenMaHopDong IN
                      (
                          SELECT MaLoaiHopDong FROM dbo.DmLoaiHopDongNoiBo WHERE DeletedStatus = 0
                      ) 
            GROUP BY DmSanPhamREF,
                     DmViTriREF,
                     TenViTri
        ) B
            ON A.DmSanPhamREF = B.DmSanPhamREF
               AND A.DmViTriREF = B.DmViTriREF
               AND A.TenViTri = B.TenViTri;


END;

```
