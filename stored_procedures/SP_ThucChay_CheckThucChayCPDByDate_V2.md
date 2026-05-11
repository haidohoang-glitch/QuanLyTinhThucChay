# Stored Procedure: `ThucChay_CheckThucChayCPDByDate_V2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-27 11:12:36.833000
- **Ngày sửa cuối**: 2014-12-27 11:13:11.397000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayCPDByDate_V2]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	DELETE FROM ThucChay_CheckThucChayCPDDaily WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
	
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		DECLARE @curHopDongREF INT , @curHopDongChiTietREF INT 
		DECLARE hopdong_cursor CURSOR FOR SELECT Tempt.HopDongID, Tempt.HopDongChiTietREF FROM
			(		 
				SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF FROM ThucChayDaTinh tcdt 
				WHERE tcdt.NgayThucHien = @NgayThucHien
						AND tcdt.DmSanPhamREF IN (241,264,300,268,248,270,243,244,249,140, 228, 564, 549, 242,385)	
						AND tcdt.HopDongChiTietREF NOT IN (SELECT p.HopDongChiTietREF FROM ThucChay_CheckThucChayCPDDaily p
																WHERE p.CheckedStatus = 1 AND p.NgayThucHien = @NgayThucHien)
		     ) Tempt                     
		OPEN hopdong_cursor
		FETCH NEXT FROM hopdong_cursor
		INTO @curHopDongREF, @curHopDongChiTietREF		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT @curHopDongREF 
			PRINT @curHopDongChiTietREF
			----CHECK GIA TRI THỜI GIAN TRÊN HĐ VÀ SỐ LƯỢNG NGÀY ĐỢT CHẠY					
			INSERT INTO ThucChay_CheckThucChayCPDDaily		
			SELECT			
			@NgayThucHien, @curHopDongREF, tempt.SoHopDong, @curHopDongChiTietREF, tempt.DmSanPhamREF, tempt.TenSanPham
			, tempt.SoLuongHD, tempt.SoLuongDotChay
			, tempt.SoLuongThucChayTest
			, tempt.SoLuongChay_tcdt
			, tempt.DonGiaNgay
			, tempt.ThanhTien, tempt.TienThucChayTest, tempt.TienThucChay_tcdt
			, (tempt.TienThucChayTest - tempt.TienThucChay_tcdt) AS Lech 
			, 1
			, CASE WHEN (tempt.TienThucChayTest - tempt.TienThucChay_tcdt) NOT IN (0, 1,-1) 
					OR (tempt.SoLuongHD - tempt.SoLuongDotChay NOT IN (0,1,-1, 2,-2,3,-3,4,-4))
					OR (tempt.SoLuongThucChayTest <> tempt.SoLuongChay_tcdt)
					THEN 1				 
				ELSE 0 END
			, CASE 
				WHEN (tempt.TienThucChayTest - tempt.TienThucChay_tcdt) NOT IN (0, 1,-1) THEN N'Tiền thực chạy đã tính khác tiền thực chạy test tính' 
				WHEN (tempt.SoLuongHD - tempt.SoLuongDotChay NOT IN (0,1,-1, 2,-2,3,-3,4,-4)) THEN N'Số lượng ngày hợp đồng khác số lượng ngày đợt chạy'
				WHEN tempt.SoLuongThucChayTest <> tempt.SoLuongChay_tcdt THEN N'Số lượng thực chạy khác số lượng thực chạy test tính' 				 
				ELSE '' END
			, tempt.GhiChu
				 
			FROM
			(
				SELECT 
					A.SoHopDong
					, A.HopDongChiTietID
					, A.DmSanPhamREF
					, A.TenSanPham
					, A.SoLuongHD	
					, A.SoLuongDotChay
					, A.SoLuongThucChayTest
					, B.SoLuongChay_tcdt
					, A.DonGiaNgay
					, A.ThanhTien
					, ROUND(A.DonGiaNgay * A.SoLuongThucChayTest,0) TienThucChayTest				 
					, ISNULL(round(B.ThanhTienThucChay,0),0) AS TienThucChay_tcdt		
					, A.GhiChu	 
				FROM
				(		
					SELECT 
						hd.HopDongID
						, hd.SoHopDong
						, hdct.HopDongChiTietID
						, hdct.DmSanPhamREF
						, hdct.TenSanPham
						, dbo.ThucChay_GetSoLuong_DonViTinh(hdct.SoLuong, hdct.DonViTinh) AS SoLuongHD
						, ISNULL(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0) AS SoLuongDotChay
						, hdct.DonGia
						, CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia * hdct.SoLuong ELSE hdct.ThanhTien END ThanhTien
						, CASE
							WHEN hdct.IsKhuyenMai = 1 THEN (hdct.DonGia * hdct.SoLuong)/isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0) 
							ELSE hdct.ThanhTien/ isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0)  						 
						END	DonGiaNgay
						, CASE 
							WHEN ISNULL(dbo.ThucChay_GetSoLuongThucChayBooking_CPDDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien), 0) > 0 THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayBooking_CPDDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien), 0)
							ELSE ISNULL(dbo.ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien),0)
						END SoLuongThucChayTest		
						, hdct.GhiChu				
					FROM HopDong hd 
						INNER JOIN HopDongChiTiet hdct 
						ON hd.HopDongID = hdct.HopDongFK 
						AND hd.DeletedStatus = 0 AND hdct.DeletedStatus = 0
						AND hd.HopDongID = @curHopDongREF  
						AND hdct.HopDongChiTietID = @curHopDongChiTietREF
				) A FULL OUTER JOIN
				(
					SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
						, CASE WHEN tcdt.IsKhuyenMai = 0 THEN SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)
								ELSE SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi)  
							END SoLuongChay_tcdt				 
						, CASE WHEN tcdt.IsKhuyenMai = 0 THEN SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
								ELSE SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) 
							END ThanhTienThucChay
						FROM ThucChayDaTinh tcdt 
					WHERE tcdt.HopDongID = @curHopDongREF
						AND tcdt.HopDongChiTietREF = @curHopDongChiTietREF		
						AND tcdt.NgayThucHien <= @NgayThucHien											                               		
					GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.IsKhuyenMai
				)B ON A.HopDongID = B.HopDongID AND A.HopDongChiTietID = B.HopDongChiTietREF	
			) tempt	
					
			FETCH NEXT FROM hopdong_cursor
			INTO @curHopDongREF, @curHopDongChiTietREF		
		END 
		CLOSE hopdong_cursor;
		DEALLOCATE hopdong_cursor;	
		PRINT @NgayThucHien
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
	
	END	 

END

```
