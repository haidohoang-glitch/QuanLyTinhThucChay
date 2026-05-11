# Stored Procedure: `sp_KSTC_CheckTCDTCreatorContent_ChiPhi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-04-04 11:57:00.803000
- **Ngày sửa cuối**: 2024-04-12 14:03:39.357000

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
CREATE PROCEDURE  [dbo].[sp_KSTC_CheckTCDTCreatorContent_ChiPhi]
	-- Add the parameters for the stored procedure here
	 @NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here

SELECT ttdt.SoHopDong,
       ttdt.HopDongID,
       ttdt.HopDongChiTietREF,
       ttdt.NhanHang,
       ttdt.TenSanPham,
       ttdt.DmSanPhamREF,
       dbo.FormatNumber(A.ThanhTienTreo_CCN) ThanhTienTreo_CCN,
       dbo.FormatNumber(A.ThanhTienTreo_CCĐ) ThanhTienTreo_CCĐ,
       dbo.FormatNumber(A.ThanhTienTreo_CPN) ThanhTienTreo_CPN,
       dbo.FormatNumber(A.ThanhTienTreo_CPĐ) ThanhTienTreo_CPĐ,
       dbo.FormatNumber(ttdt.ThanhTienTC) ThanhTienTC,
       (SUM(A.ThanhTienTreo_CCN - A.ThanhTienTreo_CPN)) AS ChenhlechTreo_CC_CPN,
       (SUM(A.ThanhTienTreo_CCĐ - A.ThanhTienTreo_CPĐ)) AS ChenhlechTreo_CC_CPĐ,
       (SUM(A.ThanhTienTreo_CPĐ - ttdt.ThanhTienTC)) AS ChenhlechTC_CPĐ
FROM
(
    SELECT ttcc.PhanBo1,
           ttcc.ThanhTienTreo_CCN,
           ttcc.ThanhTienTreo_CCĐ,
           tccp.ThanhTienTreo_CPN,
           tccp.ThanhTienTreo_CPĐ
    FROM
    (
   SELECT (nvh.PhanBoRef) PhanBo1,
               (kqvh.PhanBoRef) PhanBo2,
               SUM(nvh.TcThanhTien) ThanhTienTreo_CCN,
               SUM(kqvh.TcThanhTien) ThanhTienTreo_CCĐ
        FROM ASDAG2.AbpZeroDb_SanPham_CreatorContent.dbo.AppKetQuaVanHanh nvh
            FULL JOIN ABM_Data_ThucChay.dbo.AppKetQuaVanHanh_CreatorContent kqvh
                ON kqvh.PhanBoRef = nvh.PhanBoRef
                   AND nvh.Id = kqvh.AppKetQuaVanHanh_CreatorContent_id
			FULL JOIN dbo.HopDong  hd
			    ON hd.HopDongID=nvh.HopDongBanRef
        WHERE nvh.TrangThai NOT IN ( 1, 2, 4 )
              AND nvh.IsDeleted = 0
              AND nvh.PhanBoRef NOT IN ( 654497,654498,654499,654500,686379,660869 --gỡ vượt CF
			,676467,652992,680642,664375,699911,664617,660890,--chuyen DMsanphanREF
			688572,672660-- chuyen mua ngoai
			)
              AND CONVERT(DATE, nvh.LastModificationTime) <=  @NgayThucHien
			  AND SUBSTRING(hd.SoHopDong, LEN(hd.SoHopDong) - 1, 2) >= 22-- lấy các hđ >=2022
        GROUP BY nvh.PhanBoRef,
                 kqvh.PhanBoRef
    ) ttcc
        INNER JOIN
        --- thuc treo Chi phi
        (
            SELECT ncp.Contract_Detail_Id,
                   tchdctp.HopDongChiTietREF,
                   SUM(ncp.TotalMoney) ThanhTienTreo_CPN,
                   SUM(tchdctp.ThanhTien) ThanhTienTreo_CPĐ
            FROM ASDAG2.ThucTreo.dbo.ThucTreo_ChiPhi ncp
                FULL JOIN ThucChayHopDongChiTiet tchdctp
                    ON ncp.Id = tchdctp.ThucChayHopDongChiTietID
                       AND tchdctp.HopDongChiTietREF = ncp.Contract_Detail_Id
				FULL JOIN dbo.HopDong hd
				    ON ncp.Contract_Id=hd.HopDongID
            WHERE ncp.Contract_Detail_Id  NOT IN ( 654497,654498,654499,654500,686379,660869 --gỡ vượt CF
			,676467,652992,680642,664375,699911,664617,660890,--chuyen DMsanphanREF
			688572,672660-- chuyen mua ngoai
			)
                  AND ncp.DeletedStatus = 0
                  AND CONVERT(DATE, ncp.LastModifiedAt) <=   @NgayThucHien
				  AND SUBSTRING(hd.SoHopDong, LEN(hd.SoHopDong) - 1, 2) >= 22-- lấy các hđ >=2022
            GROUP BY ncp.Contract_Detail_Id,
                     tchdctp.HopDongChiTietREF
        ) tccp
            ON tccp.Contract_Detail_Id = ttcc.PhanBo1
               AND tccp.HopDongChiTietREF = ttcc.PhanBo2
) A
    FULL JOIN
    -- check thuc chay da tinh 
    (
        SELECT SoHopDong,
               HopDongID,
               HopDongChiTietREF,
               NhanHang,
               TenSanPham,
               DmSanPhamREF,
               SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienTC
        FROM dbo.ThucChayDaTinh
        WHERE HopDongChiTietREF  NOT IN ( 654497,654498,654499,654500,686379,660869 --gỡ vượt CF
			,676467,652992,680642,664375,699911,664617,660890,--chuyen DMsanphanREF
			688572,672660-- chuyen mua ngoai-
			)
              AND NgayThucHien <=  @NgayThucHien
			  AND SoHopDong <> N'-'
			  AND SoHopDong <> N'NB'
			  AND SUBSTRING(SoHopDong, LEN(SoHopDong) - 1, 2) >= 22-- lấy các hđ >=2022
        GROUP BY SoHopDong,
                 HopDongID,
                 HopDongChiTietREF,
                 NhanHang,
                 TenSanPham,
                 DmSanPhamREF
    ) ttdt
        ON A.PhanBo1 = ttdt.HopDongChiTietREF
WHERE (A.ThanhTienTreo_CPĐ - ttdt.ThanhTienTC) <> 0
      OR (A.ThanhTienTreo_CCĐ - A.ThanhTienTreo_CPĐ) <> 0
      OR A.ThanhTienTreo_CCN - A.ThanhTienTreo_CPN <> 0
	  --AND SUBSTRING(ttdt.SoHopDong, LEN(ttdt.SoHopDong) - 1, 2) >= 22-- lấy các hđ >=2022
GROUP BY ttdt.SoHopDong,
         ttdt.HopDongID,
         ttdt.HopDongChiTietREF,
         ttdt.NhanHang,
         ttdt.TenSanPham,
         ttdt.DmSanPhamREF,
         ThanhTienTreo_CCN,
         ThanhTienTreo_CCĐ,
         ThanhTienTreo_CPN,
         ThanhTienTreo_CPĐ,
         ThanhTienTC;
END

```
