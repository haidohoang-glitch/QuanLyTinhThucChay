# Stored Procedure: `ThucChay_UpdateGTTDThucChayDaTinh_ChiPhiKhac_ThucTreoHuy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-01 15:15:15.877000
- **Ngày sửa cuối**: 2017-06-07 10:22:28.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateGTTDThucChayDaTinh_ChiPhiKhac_ThucTreoHuy]  '2017-06-01'
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_UpdateGTTDThucChayDaTinh_ChiPhiKhac_ThucTreoHuy] 
	@NgayThucHien DATETIME
AS
BEGIN
DECLARE @HopDongID INT , @HopDongChiTietID INT, @DmNhanHangREF NVARCHAR(50), @SoLuong INT, @DonGia INT
DECLARE @NgayGioiHanTinh DATETIME, @GiaTriThayDoi BIGINT =0, @SoLuongThayDoi BIGINT =0, @ChietKhau FLOAT, @Count_TCDT INT = 0
SET @NgayGioiHanTinh = '2013-01-01'

	DECLARE Cursor_chiphikhac CURSOR FOR
	
	SELECT C.HopDongFK, C.HopDongChiTietID, tchdt.DmNhanHangREF, C.SoLuong, C.DonGia, C.ChietKhau FROM
	(
		SELECT HopDongFK, HopDongChiTietID, DmSanPhamREF, DmLoaiREF, DmLoaiBannerREF, DmWebsiteREF 
		, SoLuong, DonGia, ChietKhau, ThanhTien 
		FROM HopDongChiTiet 
			WHERE DmSanPhamREF in 
							(--NHOM SP Chi phí--	
							242 -- Luot up	
							,241 -- Tinvip	
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
							,736 -- Chi phí công nghệ
						)
			AND DeletedStatus = 0 
			 AND NOT (DmLoaiREF = 13 or DmLoaiBannerREF = 18)	 --Khong tinh thuc chay cho HTQC Mua Ngoai
		
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd 
	    WHERE hd.TrangThaiHopDong <> 3
	    AND hd.DeletedStatus = 0
	 ) D on D.HopDongID = C.HopDongFK
	 INNER JOIN 
	(
		SELECT DmNhanHangREF, HopDongChiTietREF, HopDongREF FROM dbo.ThucChayHopDongChiTiet
		WHERE DeletedStatus = 1
		AND CONVERT(DATE,LastModifiedAt) = @NgayThucHien
	)tchdt ON C.HopDongChiTietID = tchdt.HopDongChiTietREF
	WHERE 1=1
	AND C.SoLuong >0	 
	AND C.DmWebsiteREF NOT IN (307,285) -- loai tru website Google, Facebook
	--AND C.HopDongChiTietID = 103876
	
	OPEN Cursor_chiphikhac
	FETCH NEXT FROM Cursor_chiphikhac INTO @HopDongID , @HopDongChiTietID , @DmNhanHangREF , @SoLuong , @DonGia, @ChietKhau
	WHILE @@FETCH_STATUS = 0
	BEGIN

		PRINT ' phat sinh vao'
		--Check da tinh thuc chay chua
		SET @Count_TCDT =
		(
			SELECT COUNT(HopDongID) FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @HopDongChiTietID
			AND NgayThucHien < @NgayThucHien
		)
		--Tinh gia tri thay doi
		IF(@Count_TCDT >0)
		BEGIN
			SET @GiaTriThayDoi = 1*@DonGia*(100-@ChietKhau)/100
			SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi,0)
			--tinh so luong thay doi
			SET @SoLuongThayDoi = 1
			--PRINT @ChietKhau
			PRINT 'tinh gia tri thay doi'
			EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinh_ChiPhiKhac] 	@NgayThucHien ,	@HopDongChiTietID ,	@DmNhanHangREF ,@GiaTriThayDoi ,@SoLuongThayDoi 
		END
		SET @GiaTriThayDoi = 0
		SET @SoLuongThayDoi = 0
		FETCH NEXT FROM Cursor_chiphikhac INTO @HopDongID , @HopDongChiTietID , @DmNhanHangREF , @SoLuong , @DonGia, @ChietKhau

	END
	CLOSE Cursor_chiphikhac
	DEALLOCATE Cursor_chiphikhac
END


```
