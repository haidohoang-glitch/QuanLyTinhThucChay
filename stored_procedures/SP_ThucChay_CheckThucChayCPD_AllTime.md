# Stored Procedure: `ThucChay_CheckThucChayCPD_AllTime`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-23 09:45:45.410000
- **Ngày sửa cuối**: 2015-04-02 17:42:31.843000

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
--EXEC CheckThucChayCPD_AllTime '2014-09-22'

--SELECT * FROM dbo.GetListHopDongCheck('2014-09-21') 
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayCPD_AllTime]
		--@ListHopDongID NVARCHAR(MAX)
		@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Table TABLE (
		NgayThucHien DATETIME
		, HopDongREF INT
		, SoHopDong NVARCHAR(50)
		, HopDongChiTietID INT 		
		, TienThucChaySauCK FLOAT
		, ThanhTien FLOAT
		, TienThucChay_tcdt FLOAT
		, TienLech FLOAT	
	)
		
	DECLARE @curHopDongREF INT , @curHopDongChiTietREF INT 
	DECLARE hopdong_cursor CURSOR FOR SELECT * FROM dbo.GetListHopDongCheck(@NgayThucHien) 
	                           
	OPEN hopdong_cursor
	FETCH NEXT FROM hopdong_cursor INTO @curHopDongREF, @curHopDongChiTietREF	
	WHILE @@FETCH_STATUS = 0
	BEGIN		
		INSERT INTO @Table		
		SELECT
			@NgayThucHien
			, @curHopDongREF
			, tempt.SoHopDong
			, tempt.HopDongChiTietID			
			, tempt.TienThucChaySauCK
			, tempt.ThanhTien
			, tempt.TienThucChay_tcdt
			, (tempt.TienThucChaySauCK - tempt.TienThucChay_tcdt)			
		FROM
		(
			SELECT 
				A.SoHopDong
				, A.HopDongChiTietID
				, A.TenSanPham
				, A.TenWebsite
				, A.SoLuongMua
				, A.SoLuongThucChay_DotChay	
				, A.SoLuongThucChay_KhongDotChay
				, A.ThanhTien
				, CASE 
				WHEN ISNULL(A.SoLuongThucChay_DotChay, 0) > 0 THEN  ROUND(A.DonGiaNgay*A.SoLuongThucChay_DotChay,0) 
				ELSE ROUND(A.DonGiaNgay*A.SoLuongThucChay_KhongDotChay,0)
				END TienThucChaySauCK
				, ISNULL(round(B.ThanhTienThucChay,0),0) AS TienThucChay_tcdt			
			FROM
			(
				SELECT 
					hd.HopDongID
					, hd.SoHopDong
					, hdct.HopDongChiTietID
					, hdct.TenSanPham
					, hdct.TenWebsite
					, hdct.SoLuong
					, hdct.DonViTinh
					, isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0) AS SoLuongMua
					, hdct.DonGia
					, hdct.ThanhTien
					, hdct.ThanhTien/ isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0) AS DonGiaNgay
					, dbo.ThucChay_GetSoLuongThucChayBooking_CPDDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien) AS SoLuongThucChay_DotChay
					, dbo.ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien) AS SoLuongThucChay_KhongDotChay		
				FROM HopDong hd 
					INNER JOIN HopDongChiTiet hdct 
					ON hd.HopDongID = hdct.HopDongFK 
					AND hd.DeletedStatus = 0 AND hdct.DeletedStatus = 0
					AND hd.HopDongID = @curHopDongREF  
					AND hdct.HopDongChiTietID = @curHopDongChiTietREF						
				WHERE hdct.DmSanPhamREF IN (140, 228, 241, 564, 549, 385, 
										264,300,268,248,270,243,244,249)	
					AND hdct.DmLoaiREF <> 13				
			) A FULL OUTER JOIN
			(
				SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhTienThucChay
				FROM ThucChayDaTinh tcdt 
					WHERE tcdt.HopDongID = @curHopDongREF
					AND tcdt.HopDongChiTietREF = @curHopDongChiTietREF	
					AND tcdt.DmSanPhamREF IN (140, 228, 241, 564, 549, 385, 
											264,300,268,248,270,243,244,249)															                               		
					AND tcdt.NgayThucHien <= @NgayThucHien
					AND tcdt.DmHinhThucQuangCao <> 13
				GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF				
			)B ON A.HopDongID = B.HopDongID AND A.HopDongChiTietID = B.HopDongChiTietREF
		) tempt	
			
		FETCH NEXT FROM hopdong_cursor
		INTO @curHopDongREF, @curHopDongChiTietREF		
	END 
	CLOSE hopdong_cursor;
	DEALLOCATE hopdong_cursor;	
	
	SELECT * FROM @Table t WHERE t.TienLech <> 0 OR t.ThanhTien - t.TienThucChay_tcdt < 0
END

--EXEC CheckThucChayCPD_AllTime '2014-10-01'

```
