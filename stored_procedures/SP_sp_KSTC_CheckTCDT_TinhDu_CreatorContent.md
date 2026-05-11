# Stored Procedure: `sp_KSTC_CheckTCDT_TinhDu_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-04-21 17:27:30.153000
- **Ngày sửa cuối**: 2023-12-04 14:08:45.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_TinhDu_CreatorContent] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
-- check tính đủ KQVH

SELECT A.HopDongBanRef,A.PhanBoRef,dbo.FormatNumber(A.TienTT) AS TienTT,
       B.SoHopDong,B.HopDongID,B.HopDongChiTietREF,B.DmSanPhamREF,dbo.FormatNumber(B.[ThucChay]),
       Cast(A.TienTT AS DECIMAL(18,0)) - Cast(B.ThucChay AS DECIMAL(18,0)) AS [LechTT-TC]
FROM
(
    SELECT a.HopDongBanRef,
           a.PhanBoRef,
           SUM(a.TcThanhTien) TienTT
    FROM ABM_Data_ThucChay.dbo.AppKetQuaVanHanh_CreatorContent a
        JOIN ABM_Data_ThucChay.dbo.HopDong b
            ON b.HopDongID = a.HopDongBanRef
    WHERE TrangThai NOT IN ( 1, 2, 4 )
          AND IsDeleted = 0
          AND CONVERT(DATE, b.NgayDanhSoHopDong) >= '2021-10-01'
		    AND a.PhanBoRef  NOT IN (654498,654499,654500) --Linhvt phan bo hd cu vuot co confirm
    GROUP BY a.HopDongBanRef,
             a.PhanBoRef
) A
    FULL OUTER JOIN
    (
        SELECT a.SoHopDong,
               a.HopDongID,
               a.HopDongChiTietREF,
               a.DmSanPhamREF,
               SUM(a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi) AS [ThucChay]
        FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh a
            JOIN ABM_Data_ThucChay.dbo.HopDong b
                ON b.HopDongID = a.HopDongID
        WHERE NOT (
                      DmHinhThucQuangCao = 13
                      OR DmLoaiBannerREF = 18
                  )
              AND DotChayHopDong <> 'ThanhTien_GGFB'
              AND DotChayHopDong <> 'ThanhTien_GGFB_chot'
              AND DmSanPhamREF = 5184
              AND CONVERT(DATE, b.NgayDanhSoHopDong) >= '2021-10-01'
              AND a.NgayThucHien <= @NgayThucHien
			  AND a.HopDongChiTietREF  NOT IN (654498,654499,654500) --Linhvt phan bo hd cu vuot co confirm
        GROUP BY a.SoHopDong,
                 a.HopDongID,
                 a.HopDongChiTietREF,
                 a.DmSanPhamREF
    ) B
        ON A.PhanBoRef = B.HopDongChiTietREF
WHERE 1 = 1 AND ((Cast(A.TienTT AS DECIMAL(18,0))-Cast(B.ThucChay AS DECIMAL(18,0)))<>0 OR (Cast(A.TienTT AS DECIMAL(18,0)) - CAST(B.ThucChay AS DECIMAL(18,0))) IS NULL) -- and a.PhanBoRef=666220


-- check tính đủ lãi theo treo
DECLARE @tbl TABLE
(
	AppKetQuaVanHanh_CreatorContent_id INT,
	HopDongBanRef INT,
	HopDongChiTietREF INT,
	PbThanhTien INT,
	TcThanhTien NVARCHAR(20),
	LaiLo INT,
	LaiDaTinh INT,
	ChenhLech INT
)

INSERT INTO @tbl
(
    AppKetQuaVanHanh_CreatorContent_id,
    HopDongBanRef,
    HopDongChiTietREF,
    PbThanhTien,
    TcThanhTien,
    LaiLo,
    LaiDaTinh,
    ChenhLech
)
SELECT a.AppKetQuaVanHanh_CreatorContent_id,
       a.HopDongBanRef,
       b.HopDongChiTietREF,
       a.PbThanhTien,
       dbo.FormatNumber(a.TcThanhTien),
       a.LaiLo,
       SUM(b.ThanhTienLaiThucChaySauCK + b.GiaTriThayDoiLaiSauCK) LaiDaTinh,
       a.LaiLo - SUM(b.ThanhTienLaiThucChaySauCK + b.GiaTriThayDoiLaiSauCK) ChenhLech
FROM dbo.AppKetQuaVanHanh_CreatorContent a
    JOIN dbo.ThucChayDaTinh_MuaNgoai b
        ON b.ThucChayMuaNgoaiChiTietREF = a.AppKetQuaVanHanh_CreatorContent_id
WHERE b.DmSanPhamREF = 5184
      AND CONVERT(DATE, b.NgayDanhSoHopDong) >= '2021-10-01'
      AND NOT (DmLoaiBannerREF = 18)
      AND a.IsDeleted = 0
      AND a.RecordStatus = 1
	  AND  a.AppKetQuaVanHanh_CreatorContent_id  NOT IN (9480,9815) --Linhvt loai kqvh bi xoa
GROUP BY a.AppKetQuaVanHanh_CreatorContent_id,
         a.HopDongBanRef,
         b.HopDongChiTietREF,
         a.PbThanhTien,
         a.TcThanhTien,
         a.LaiLo
--HAVING a.LaiLo - SUM(b.ThanhTienLaiThucChaySauCK + b.GiaTriThayDoiLaiSauCK) <> 0

SELECT * FROM @tbl
WHERE (ChenhLech <> 0 OR ChenhLech IS NULL) AND ( LaiLo IS NOT NULL OR LaiDaTinh IS NOT NULL OR ChenhLech IS NOT NULL)

END

```
