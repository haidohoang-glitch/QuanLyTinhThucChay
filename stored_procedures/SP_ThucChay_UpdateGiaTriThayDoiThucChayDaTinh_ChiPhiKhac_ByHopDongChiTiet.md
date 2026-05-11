# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-04-13 16:10:49.410000
- **Ngày sửa cuối**: 2018-08-15 18:21:19.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac] '2014-08-05','2014-08-05'
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac_ByHopDongChiTiet]
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@HopDongChiTietREF INT
AS
BEGIN
	DECLARE	@HopDongREF INT,@SoHopDong NVARCHAR(50),@HopDongChiTietID INT
	DECLARE @SoLuongDotChayHD INT,@ThanhTienHDCT FLOAT
	DECLARE @NgayThucHien DATETIME
	set @NgayThucHien = @StartDate

	WHILE(Convert(date,@NgayThucHien) <= Convert(date,@EndDate))
	BEGIN
		PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
		DECLARE Record_Cursor CURSOR FOR 
	    
		SELECT a.HopDongID, a.SoHopDong, a.HopDongChiTietREF, a.SoLuong, a.ThanhTien FROM
		(
			SELECT tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF, tcdt.SoLuong, tcdt.ThanhTien
			  FROM ThucChayDaTinh tcdt
			WHERE Convert(date,tcdt.NgayThucHien) = @NgayThucHien
			AND tcdt.DmSanPhamREF IN 
								(--- NHOM SP TMDT --------------
							  242 -- Luot up	
							  ,241 -- Tin vip											
								--NHOM SP Chi phí--
							, 251 --Thiết kế, quản lý		
							, 252 --Hosting		
							, 253 --Chi phi khac		
							, 535 --Chi phí quản lý campaign		
							, 537 --Chi phí viết bài		
							, 538 --Chi phí thiết kế		
							, 539 --Chi phí dựng clip		
							, 540 --Chi phí sáng tạo		
							, 541 --Chi phí giải thưởng cuộc thi/ Contest		
							, 542 --Chi phí xây dưng microsite/ tab		
							, 555 --Chi phí trài trợ		
							, 556 --Hiệu đính		
							, 557 --Chèn Clip		
							, 558 --Chi phí viết bài		
							, 559 --Chi phí quay clip		
							, 560 --Chi phí sản xuất		
							, 561 -- Chi phí khảo sát thị trường online	
							, 635 -- Quản trị fanpage
							, 563  -- Forum Seeding	
							,631 -- facebook seeding
							,651 -- đăng tin fanpage
							,726 --Tư vấn viết đề án truyền thông
							,731 --KOL
							,730 --- Livestream
							,633
							,629
							,729
							,732 -- Content Network Sponsorship
							, 734
						)
			--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 2 --Đơn vị của hình thức Bài
			AND tcdt.DmWebsiteREF NOT IN (285,307) --loai tru phan bo co website GG,FB
			AND NOT (tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF in (17, 18))
			AND tcdt.HopDongID NOT IN (SELECT HopDongFK FROM hopdongchitiet WHERE DmSanPhamREF IN (306,423) AND DeletedStatus <> 1)
			AND tcdt.HopDongChiTietREF NOT IN (SELECT HopDongChiTietID
			                                     FROM ChiPhiKhac2014_Final WHERE IsThucChayDaTinh = 1)
		UNION ALL

			SELECT DISTINCT hd.HopDongID, hd.SoHopDong,hdct.HopDongChiTietID, hdct.SoLuong, hdct.ThanhTien FROM HopDongThayDoi hdtd
			INNER JOIN HopDong hd ON hdtd.HopDongFK = hd.HopDongID
			INNER JOIN HopDongChiTiet hdct ON hdct.HopDongFK = hdtd.HopDongFK
			WHERE convert(date,hdtd.NgayThayDoi) = @NgayThucHien
			AND hdct.DmSanPhamREF IN (--- NHOM SP TMDT --------------
							  242 -- Luot up
							  ,241 -- Tin vip												
						--NHOM SP Chi phí--
							, 251 --Thiết kế, quản lý		
							, 252 --Hosting		
							, 253 --Chi phi khac		
							, 535 --Chi phí quản lý campaign		
							, 537 --Chi phí viết bài		
							, 538 --Chi phí thiết kế		
							, 539 --Chi phí dựng clip		
							, 540 --Chi phí sáng tạo		
							, 541 --Chi phí giải thưởng cuộc thi/ Contest		
							, 542 --Chi phí xây dưng microsite/ tab		
							, 555 --Chi phí trài trợ		
							, 556 --Hiệu đính		
							, 557 --Chèn Clip		
							, 558 --Chi phí viết bài		
							, 559 --Chi phí quay clip		
							, 560 --Chi phí sản xuất		
							, 561 -- Chi phí khảo sát thị trường online	
							, 635 -- Quản trị fanpage
							, 563  -- Forum Seeding	
							,631 -- facebook seeding
							,651 -- đăng tin fanpage
							,726 --Tư vấn viết đề án truyền thông
							,731 --KOL
							,730 --- Livestream
							,633
							,629
							,729
							,732 -- Content Network Sponsorship
							,734
						)
			AND hd.TrangThaiHopDong <> 3
			AND hdct.DmWebsiteREF NOT IN (285,307) --loai tru phan bo co website GG,FB
			AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF in (17,18))
			--AND hdct.HopDongFK NOT IN (SELECT HopDongFK FROM hopdongchitiet WHERE DmSanPhamREF IN (306,423) AND DeletedStatus <> 1)
		
			--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh)  = 2 --Đơn vị của hình thức Bài
		)A
		WHERE A.HopDongChiTietREF = @HopDongChiTietREF
		ORDER BY a.SoHopDong, a.HopDongChiTietREF
	
		
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
				UPDATE ThucChayDaTinh
				SET
					GiaTriThayDoi = 0
				WHERE Convert(date,NgayThucHien) = @NgayThucHien
					AND HopDongID = @HopDongREF 
					AND SoHopDong = @SoHopDong
					AND HopDongChiTietREF = @HopDongChiTietID
					AND DmSanPhamREF IN (--- NHOM SP TMDT --------------
							  --NHOM SP Chi phí--	
							242 -- Luot up	
							,241 -- tin vip	
							, 251 --Thiết kế, quản lý		
							, 252 --Hosting		
							, 253 --Chi phi khac		
							, 535 --Chi phí quản lý campaign		
							, 537 --Chi phí viết bài		
							, 538 --Chi phí thiết kế		
							, 539 --Chi phí dựng clip		
							, 540 --Chi phí sáng tạo		
							, 541 --Chi phí giải thưởng cuộc thi/ Contest		
							, 542 --Chi phí xây dưng microsite/ tab		
							, 555 --Chi phí trài trợ		
							, 556 --Hiệu đính		
							, 557 --Chèn Clip		
							, 558 --Chi phí viết bài		
							, 559 --Chi phí quay clip		
							, 560 --Chi phí sản xuất		
							, 561 -- Chi phí khảo sát thị trường online	
							, 635 -- Quản trị fanpage
							, 563  -- Forum Seeding	
							,631 -- facebook seeding
							,651 -- đăng tin fanpage
							,726 --Tư vấn viết đề án truyền thông
							,731 --KOL
							,730 --- Livestream
							,633
							,629
							,729
							,732 -- Content Network Sponsorship
							,734
						)
				--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
				
				EXEC ThucChay_CheckHopDongCoThayDoi_ChiPhiKhac @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien
			FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		EXEC [ThucChay_CheckThucTreoThayDoi_ChiPhiKhac]	@NgayThucHien, '2013-01-01' 
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
	SELECT 2
END

	

--endregion


```
