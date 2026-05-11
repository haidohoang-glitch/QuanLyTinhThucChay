# Stored Procedure: `ThucChay_CheckThucChayCPDByDate_V3`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-18 12:24:11.617000
- **Ngày sửa cuối**: 2018-10-15 10:18:17.247000

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
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayCPDByDate_V3]
	@NgayThucHien DATETIME
AS
BEGIN
	
	DELETE FROM CheckThucChayCPD_Daily WHERE NgayThucHien = @NgayThucHien

	INSERT INTO CheckThucChayCPD_Daily 
	SELECT
		@NgayThucHien AS NgayThucHien,
		*
		, CASE WHEN A.StatusChecked = 1 THEN N'Thực chạy tính thiếu'
		WHEN A.StatusChecked = 2 THEN N'Giá trị thời gian khác số lượng ngày đợt chạy'
		WHEN A.StatusChecked = 3 THEN N'Số lượng thực chạy khác số lượng thực chạy test tính'
		WHEN A.StatusChecked = 4 THEN N'Tiền thực chạy khác tiền thực chạy test tính'
		WHEN A.StatusChecked = 5 THEN N'HĐ có lịch chạy nhưng chưa có thực treo, ko có thực chạy'
		WHEN A.StatusChecked = 6 THEN N'HĐ ko có lịch chạy nhưng có thực treo, ko có thực chạy'
		WHEN A.StatusChecked = 7 THEN N'HĐ ko có lịch chạy, ko có thực treo nhưng có thực chạy'
	END GhiChu
	FROM
	(
	SELECT
		HD.HopDongID AS HopDongID_hd, HD.SoHopDong AS SoHopDong_hd , HD.HopDongChiTietID AS HopDongChiTietID_hd , HD.TenSanPham, HD.TenWebsite AS TenWebsite_hd, HD.ThanhTien, HD.ThanhTienKM, HD.SoLuongHD, HD.SLDotChayHD
		, ThucTreo.HopDongREF AS HopDongREF_thuctreo, ThucTreo.SoHopDong AS SoHopDong_thuctreo, ThucTreo.HopDongChiTietREF AS HopDongChiTietREF_tt 	
		, TC.HopDongID AS HopDongID_tcdt, TC.SoHopDong AS SoHopDong_tcdt , TC.HopDongChiTietREF AS HopDongChiTietREF_tcdt, TC.TenWebsite AS TenWebsite_tcdt, TC.SLChay, TC.SLKM
		, ThucTreo.SoLuongChay_Test
		, Tc.TienThucChay, TC.TienKM
		, ROUND(HD.DonGiaNgay * ThucTreo.SoLuongChay_Test,0) AS TienThucChay_Test
		, (ISNULL(TC.TienThucChay,0) + ISNULL(TC.TienKM,0)) - ISNULL(ROUND(HD.DonGiaNgay * ThucTreo.SoLuongChay_Test,0),0) AS LechTienThucChay
		, CASE WHEN HD.HopDongChiTietID IS NOT NULL AND ThucTreo.HopDongChiTietREF IS NOT NULL AND TC.HopDongChiTietREF IS NULL THEN 1
		WHEN HD.SoLuongHD <> HD.SLDotChayHD THEN 2
		WHEN TC.SLChay + TC.SLKM <> ThucTreo.SoLuongChay_Test THEN 3
		WHEN (ISNULL(TC.TienThucChay,0) + ISNULL(TC.TienKM,0)) <> ISNULL(ROUND(HD.DonGiaNgay * ThucTreo.SoLuongChay_Test,0),0) THEN 4
		WHEN HD.HopDongChiTietID IS NOT NULL AND ThucTreo.HopDongChiTietREF IS NULL AND TC.HopDongChiTietREF IS NULL THEN 5 
		WHEN HD.HopDongChiTietID IS NULL AND ThucTreo.HopDongChiTietREF IS NOT NULL AND TC.HopDongChiTietREF IS NULL THEN 6
		WHEN HD.HopDongChiTietID IS NULL AND ThucTreo.HopDongChiTietREF IS NULL AND TC.HopDongChiTietREF IS NOT NULL THEN 7 
		ELSE 0 END StatusChecked	
	FROM 
	(	
		SELECT hd.HopDongID, hd.SoHopDong, hdct.HopDongChiTietID, hdct.TenSanPham , hdct.DmSanPhamREF
			, hdct.TenWebsite
			, CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia* hdct.SoLuong ELSE 0 END ThanhTienKM 
			, hdct.ThanhTien
			, dchdct.BookingREF
			, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc
			, CASE WHEN hdct.ThanhTien = 0 THEN (hdct.DonGia * hdct.SoLuong)/isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0) 
				ELSE hdct.ThanhTien/isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0) END DonGiaNgay
			, dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID) AS SLDotChayHD
			, ISNULL(dbo.ThucChay_GetSoLuong_DonViTinh(hdct.SoLuong, hdct.DonViTinh),0) AS SoLuongHD		
		FROM HopDong hd	
			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK 
												AND hd.TrangThaiHopDong <> 3 AND hdct.DeletedStatus = 0  
			LEFT JOIN DotChayHopDongChiTiet dchdct ON hdct.HopDongChiTietID = dchdct.HopDongChiTietREF 
													AND hdct.HopDongFK = dchdct.HopDongREF 
													AND dchdct.DeletedStatus = 0
		WHERE @NgayThucHien BETWEEN dchdct.ThoiGianBatDau AND dchdct.ThoiGianKetThuc	
			AND hdct.DmSanPhamREF IN (140, 228, 564, 549 -- CPD
										, 241, 242, 243, 244, 248, 249, 264, 268, 270, 300, 385, 5005, 5006 -- TMĐT	
									  ) 
			AND hdct.DmLoaiREF <> 13	
	) HD
	FULL OUTER JOIN 
	(
		SELECT tchdct.HopDongREF
			, dbo.GetSoHopDongByID(tchdct.HopDongREF) AS SoHopDong
			, tchdct.HopDongChiTietREF
			, COUNT(DISTINCT HopDongChiTietREF) AS SoLuongChay_Test
		FROM ThucChayHopDongChiTiet tchdct 
		WHERE  
			tchdct.HopDongChiTietREF IN ( 
					SELECT hdct.HopDongChiTietID
					FROM HopDongChiTiet hdct INNER JOIN HopDong hd2 ON hd2.HopDongID = hdct.HopDongFK AND hd2.TrangThaiHopDong <> 3 
					WHERE hdct.DmSanPhamREF IN (140, 228, 564, 549 -- CPD
										, 241, 242, 243, 244, 248, 249, 264, 268, 270, 300, 385, 5005, 5006, 5007 -- TMĐT	
					)
					AND hdct.DmLoaiREF <> 13 
					AND hdct.DeletedStatus = 0						
			)
			AND @NgayThucHien BETWEEN tchdct.ThoiGianBatDau AND tchdct.ThoiGianKetThuc
			AND tchdct.DeletedStatus = 0
		GROUP BY tchdct.HopDongREF, tchdct.HopDongChiTietREF, tchdct.BookingREF
	) ThucTreo ON ThucTreo.HopDongREF = HD.HopDongID AND HD.HopDongChiTietID = ThucTreo.HopDongChiTietREF
	FULL OUTER JOIN 
	(
		SELECT tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF
			, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.TenWebsite
			, SUM(tcdt.SoLuongThucChay+ tcdt.SoLuongThayDoi) AS SLChay
			, SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS SLKM
			, ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0) AS TienThucChay
			, ROUND(SUM(tcdt.ThanhTienKM),0) AS TienKM 
		FROM ThucChayDaTinh tcdt 
		WHERE tcdt.DmSanPhamREF IN  (140, 228, 564, 549 -- CPD
										, 241, 242, 243, 244, 248, 249, 264, 268, 270, 300 ,  385, 5005, 5006, 5007-- TMĐT	
				)
			AND tcdt.DmHinhThucQuangCao <> 13
			AND tcdt.NgayThucHien = @NgayThucHien	
		GROUP BY tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF
			, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.TenWebsite
	) TC ON HD.HopDongID = TC.HopDongID AND HD.HopDongChiTietID = TC.HopDongChiTietREF
	)A


	ORDER BY A.HopDongID_hd asc
	
	
END

```
