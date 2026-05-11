# Stored Procedure: `sp_KSTC_CheckTCDT_PR_ByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-18 16:31:23.093000
- **Ngày sửa cuối**: 2021-06-11 15:50:47.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [sp_KSTC_CheckTCDT_PR_ByHopDongID] 1019636, 141
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_PR_ByHopDongID]
	-- Add the parameters for the stored procedure here
	@HopDongID INT,
	@DmSanPhamREF int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here

	--Khong KM
	SELECT N'Không KM'Loai, A.*, B.* FROM (
SELECT KhuyenMai, tchdctp.DmNhanHangREF, dbo.GetSoHopDongByID(tchdctp.HopDongREF) SoHopDong, 
HopDongREF, DmSanPhamREF,tchdctp.HopDongChiTietREF, CONVERT(NVARCHAR(50),ThucChayHopDongChiTietPRID) id,tchdctp.DeletedStatus, tchdctp.RecordStatus,  CONVERT(DATE,ThoiGianBatDau)ThoiGianBatDau,tchdctp.CreatedAt, tchdctp.LastModifiedAt,
tchdctp.TenWebsite, tchdctp.TenChuyenMuc,
tchdctp.SoLuong,tchdctp.GiaTien,tchdctp.ChietKhau,
(CASE WHEN tchdctp.DeletedStatus = 0 THEN (CONVERT(FLOAT, tchdctp.GiaTien) * tchdctp.SoLuong * (100-tchdctp.ChietKhau)/100) 
ELSE 0 END )TTSauCk ,tchdctp.Link, tchdctp.ThucChayHopDongChiTietPrREF ttid_cha
FROM dbo.ThucChayHopDongChiTietPR tchdctp left join DmSanPham sp on tchdctp.DmSanPhamREF = sp.DmSanPhamID WHERE 1=1
AND hopdongref =@HopDongID
and DmSanPhamREF = @DmSanPhamREF
and not (ChietKhau = 100 or isnull(KhuyenMai,0) = 1)
-- AND tchdctp.ThucChayHopDongChiTietPrID =538899

)A
full outer join 
(SELECT HopDongID, tcdt.DmSanPhamREF,tcdt.NhanHang,DotChayBooking, SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi)tcdt, SUM(ThanhTienKM+GiaTriKMThayDoi) tckm
FROM dbo.ThucChayDaTinh tcdt left join ThucChayHopDongChiTietPR treopr on convert(nvarchar(50),tcdt.DotChayBooking) = convert(nvarchar(50),treopr.ThucChayHopDongChiTietPRID)
WHERE tcdt.DmSanPhamREF IN (141,637,305) and not (treopr.ChietKhau = 100 or isnull(treopr.KhuyenMai,0) = 1)
AND NOT (DmLoaiBannerREF = 18 OR DmHinhThucQuangCao =13)
AND HopDongID =@HopDongID AND tcdt.DmSanPhamREF = @DmSanPhamREF
GROUP BY HopDongID, tcdt.DmSanPhamREF,DotChayBooking, tcdt.NhanHang
having (round(SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0) <>0 or round(SUM(ThanhTienKM+GiaTriKMThayDoi),0) <>0)
)B
ON A.HopDongREF = B.HopDongID

AND A.DmSanPhamREF = B.DmSanPhamREF
AND CONVERT(NVARCHAR(100),A.id) = B.DotChayBooking
WHERE 1=1  
AND( (
 (ABS(ISNULL(A.TTSauCk,0)- ISNULL(B.tcdt,0))>10 
 or B.tckm <> 0
)

or CONVERT(NVARCHAR(50),A.DmNhanHangREF)<>CONVERT(NVARCHAR(50),B.NhanHang)
) 
OR B.HopDongID IS NULL
)
ORDER BY HopDongREF desc-- a.LastModifiedAt DESC

-- KM
	SELECT N'KM'Loai, A.*, B.* FROM (
SELECT tchdctp.DmNhanHangREF, dbo.GetSoHopDongByID(tchdctp.HopDongREF) SoHopDong, 
HopDongREF, DmSanPhamREF,tchdctp.HopDongChiTietREF, CONVERT(NVARCHAR(50),ThucChayHopDongChiTietPRID) id,tchdctp.DeletedStatus, tchdctp.RecordStatus,  CONVERT(DATE,ThoiGianBatDau)ThoiGianBatDau,tchdctp.CreatedAt, tchdctp.LastModifiedAt,
tchdctp.TenWebsite, tchdctp.TenChuyenMuc,
tchdctp.SoLuong,tchdctp.GiaTien,tchdctp.ChietKhau,
(CASE WHEN tchdctp.DeletedStatus = 0 THEN (CONVERT(FLOAT, tchdctp.GiaTien) * tchdctp.SoLuong) 
ELSE 0 END )TTSauCk ,tchdctp.Link, tchdctp.ThucChayHopDongChiTietPrREF ttid_cha
FROM dbo.ThucChayHopDongChiTietPR tchdctp left join DmSanPham sp on tchdctp.DmSanPhamREF = sp.DmSanPhamID WHERE 1=1
AND hopdongref =@HopDongID
and DmSanPhamREF = @DmSanPhamREF
and (ChietKhau = 100 or KhuyenMai = 1)
 --AND tchdctp.ThucChayHopDongChiTietPrID =135313

)A
LEFT JOIN
(SELECT HopDongID, tcdt.DmSanPhamREF,tcdt.NhanHang,DotChayBooking, SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi)tcdt, SUM(ThanhTienKM+GiaTriKMThayDoi) tckm
FROM dbo.ThucChayDaTinh tcdt left join ThucChayHopDongChiTietPR treopr on convert(nvarchar(50),tcdt.DotChayBooking) = convert(nvarchar(50),treopr.ThucChayHopDongChiTietPRID)
WHERE tcdt.DmSanPhamREF IN (141,637,305) and (treopr.ChietKhau = 100 or isnull(treopr.KhuyenMai,0) = 1)
AND NOT (DmLoaiBannerREF = 18 OR DmHinhThucQuangCao =13)
AND HopDongID =@HopDongID AND tcdt.DmSanPhamREF = @DmSanPhamREF 
GROUP BY HopDongID, tcdt.DmSanPhamREF,DotChayBooking, tcdt.NhanHang
having (round(SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0) <>0 or round(SUM(ThanhTienKM+GiaTriKMThayDoi),0) <>0)
)B
ON A.HopDongREF = B.HopDongID

AND A.DmSanPhamREF = B.DmSanPhamREF
AND CONVERT(NVARCHAR(100),A.id) = B.DotChayBooking
WHERE 1=1  
AND ((
 (ABS(ISNULL(A.TTSauCk,0)- ISNULL(B.tckm,0))>10 
 or B.tcdt <> 0
)

or CONVERT(NVARCHAR(50),A.DmNhanHangREF)<>CONVERT(NVARCHAR(50),B.NhanHang)
) OR B.HopDongID IS NULL)
ORDER BY HopDongREF desc-- a.LastModifiedAt DESC
END

```
