# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac_BK`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-23 17:49:06.300000
- **Ngày sửa cuối**: 2014-11-19 12:25:02.963000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac_BK]
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
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
			AND tcdt.DmSanPhamREF IN (--- NHOM SP TMDT --------------
										242 -- Luot up
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
										)
			--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 2 --Đơn vị của hình thức Bài
		UNION

			SELECT DISTINCT hd.HopDongID, hd.SoHopDong,hdct.HopDongChiTietID, hdct.SoLuong, hdct.ThanhTien FROM HopDongThayDoi hdtd
			INNER JOIN HopDong hd ON hdtd.HopDongFK = hd.HopDongID
			INNER JOIN HopDongChiTiet hdct ON hdct.HopDongFK = hdtd.HopDongFK
			WHERE convert(date,hdtd.NgayThayDoi) = @NgayThucHien
			AND hdct.DmSanPhamREF IN (--- NHOM SP TMDT --------------
										242 -- Luot up										
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
										)
			AND hd.TrangThaiHopDong <> 3
			--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh)  = 2 --Đơn vị của hình thức Bài
		)A
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
											242 -- Luot up
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
