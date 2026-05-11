# Stored Procedure: `prc_asd_CheckGTTDChiPhi_With_HopDong_ThangDuGP_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-02-07 15:30:53.600000
- **Ngày sửa cuối**: 2023-02-07 16:00:00.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Thuc hien check gia tri thay doi cua cac san pham chi phi co gia tri ThangDuGP co thuc hien doi tru day du ko??>
--Thuc hien doi tru day du tren ThucChayDaTinh, ThucChayDaTinh_MuaNgoai
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2017-09-05'
-- =============================================
/*
	[dbo].[prc_asd_CheckGTTDChiPhi_With_HopDong_ThangDuGP_dev]
	@NgayThucHien = '2023-02-06'
*/

CREATE PROCEDURE [dbo].[prc_asd_CheckGTTDChiPhi_With_HopDong_ThangDuGP_dev]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	--SET NOCOUNT ON added to prevent extra result sets from
	--interfering with SELECT statements.
	SET NOCOUNT ON;
	--Neu co GiaTriThayDoi <>0 cua ThangDuGP tren table ThucChayDaTinh ngay NgayThucHien va tongthanhtienTCDT= 0 
	--thi thuc hien doi tru tren ThucChayDaTinh_MuaNgoai -> cap nhat 
	--recordStatus, lydo của table [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong]
	--check neu tien ThangDuGP +TongThanhTienThucChay <= ThanhTien thi thuc hien tinh tiep
	DECLARE   @SoHopDong NVARCHAR(100) = ''
			  ,@HopDongID   BIGINT
			  ,@HopDongChitietID   BIGINT
			  ,@DmSanPhamID   INT
			  ,@ThucChay_PerformanceBase_ThayDoi_ID   INT --SoLuongDotChayBooking
			  ,@TongthanhtienTCDT FLOAT = 0
			  ,@Dolechgiatri FLOAT = 1
			  ,@GhiChu_TCDTM NVARCHAR(500) = N''
			  ,@v_ThucChayDaTinh_MuaNgoai_ID_output BIGINT =0

	DECLARE @ThucChayDaTinh_ChiPhi_ThangDuGP TABLE(
				SoHopDong NVARCHAR(100)
			  ,HopDongID   BIGINT
			  ,HopDongChitietID   BIGINT
			  ,DmSanPhamID   INT
			  ,ThucChay_PerformanceBase_ThayDoi_ID   INT --SoLuongDotChayBooking
			  )

	INSERT INTO @ThucChayDaTinh_ChiPhi_ThangDuGP
	(
		SoHopDong
		, HopDongID   
		,HopDongChitietID   
		,DmSanPhamID   
		,ThucChay_PerformanceBase_ThayDoi_ID   
	)

	SELECT  DISTINCT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.SoLuongDotChayBooking
	FROM dbo.ThucChayDaTinh tcdt
	WHERE tcdt.NgayThucHien = @NgayThucHien
	AND tcdt.DmChienDichREF = 3 --Ghi nhan cho ThangDuGP
	AND tcdt.GiaTriThayDoi <> 0
	AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = tcdt.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
						AND NOT ( tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF in (18))
						and tcdt.HopDongChiTietREF = 676781
	--DIEU KIEN NHOM SAN PHAM CHI PHI

	DECLARE db_cur_CP_ThangDuCP CURSOR FOR  
	
	SELECT	SoHopDong
				,HopDongID   
				,HopDongChitietID   
				,DmSanPhamID   
				,ThucChay_PerformanceBase_ThayDoi_ID   
	FROM @ThucChayDaTinh_ChiPhi_ThangDuGP
		
	OPEN db_cur_CP_ThangDuCP   
	FETCH NEXT FROM db_cur_CP_ThangDuCP INTO  @SoHopDong, @HopDongID ,@HopDongChitietID ,@DmSanPhamID ,@ThucChay_PerformanceBase_ThayDoi_ID    

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		DECLARE @ThanhTien FLOAT = 0
		, @TongThanhTienThucChay FLOAT = 0
		, @TienThangDuGP FLOAT = 0
		, @TK_Admarket NVARCHAR(100) = ''
		, @DmViTriID INT = 0

		SET @TongthanhtienTCDT = ISNULL((SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
			FROM dbo.ThucChayDaTinh tcdt
			WHERE tcdt.NgayThucHien <= @NgayThucHien
			AND tcdt.HopDongID = @HopDongID
			AND tcdt.HopDongChiTietREF = @HopDongChitietID
			AND tcdt.DmSanPhamREF = @DmSanPhamID
			AND tcdt.SoLuongDotChayBooking = @ThucChay_PerformanceBase_ThayDoi_ID
			AND tcdt.DmChienDichREF = 3 --Ghi nhan cho ThangDuGP
		),0)
		print @TongthanhtienTCDT
		print @ThucChay_PerformanceBase_ThayDoi_ID
		IF(ROUND(@TongthanhtienTCDT,0)= 0)
		BEGIN
			--Neu ton tai gia tri thuc chay cua ThangDuGP tren table ThucChayDaTinh_MuaNgoai thi thuc hien doi tru
			IF(EXISTS(SELECT top (1) tcdt.HopdongChiTietREF, tcdt.ThucChayMuaNgoaiChiTietREF
			FROM dbo.ThucChayDaTinh_MuaNgoai tcdt
			WHERE tcdt.NgayThucHien < @NgayThucHien
			AND tcdt.HopDongREF = @HopDongID
			AND tcdt.HopDongChiTietREF = @HopDongChitietID
			AND tcdt.DmSanPhamREF = @DmSanPhamID
			AND tcdt.ThucChayMuaNgoaiChiTietREF = @ThucChay_PerformanceBase_ThayDoi_ID
			AND tcdt.DmChienDichREF = 3 --Ghi nhan cho ThangDuGP
			group by tcdt.HopDongChiTietREF, tcdt.ThucChayMuaNgoaiChiTietREF HAVING ROUND(SUM(tcdt.ThanhtienlaithucchaysauCK + tcdt.GiatrithaydoilaiSauCK),0) <> 0
			))
			BEGIN
				SET @GhiChu_TCDTM = N'Đối trừ ThangDuGP,HopDongChiTietID =' + CONVERT(NVARCHAR(10),@HopDongChitietID)
				+ N' , @ThucChay_PerformanceBase_ThayDoi_ID= '+ CONVERT(NVARCHAR(10),@ThucChay_PerformanceBase_ThayDoi_ID)
				print @GhiChu_TCDTM
				
				--1.THUC HIEN DOI TRU TOAN BO CHO THUCCHAYDATINH_MUANGOAI
				EXEC [dbo].[ThucChay_DoiTruGTTDThucChayDaTinh_MuaNgoai_With_HopDong_ThangDuGP]
				-- Add the parameters for the stored procedure here
				@NgayThucHien = @NgayThucHien, 
				@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID,
				@HopDongID = @HopDongID,
				@HopDongChiTietID = @HopDongChitietID, 
				@DmSanPhamREF = @DmSanPhamID, 
				@GhiChu = @GhiChu_TCDTM,
				@ThucChayDaTinh_MuaNgoai_ID_output = @v_ThucChayDaTinh_MuaNgoai_ID_output OUTPUT

				print @v_ThucChayDaTinh_MuaNgoai_ID_output

				IF(@v_ThucChayDaTinh_MuaNgoai_ID_output <> 0)
				BEGIN
					--2.THUC HIEN UPDATE TRANG THAI BAN GHI CHO TABLE [ThucChay_PerformanceBase_ThayDoi_HopDong] VA CAP NHAP LYDO
					UPDATE tc
					SET tc.RecordStatus = 0
					, tc.LyDoLoi = N'Thay đổi gia trị hopdong, nên đối trừ để check tính lại'
					FROM [ThucChay_PerformanceBase_ThayDoi_HopDong] tc
					WHERE tc.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
					AND tc.HopDongID = @HopDongID
					AND tc.HopDongChiTietID = @HopDongChitietID
					
					---HAIDH COMMENT BO VIEC TINH LẠI THEO NHU THONG NHAT VOI THAO 07/02/2023
					--print 'done'
					--SET @ThanhTien = ISNULL((SELECT top (1) hdct.ThanhTien FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChitietID),0)
					--SET @TongThanhTienThucChay = ISNULL((SELECT sum(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) 
					--							FROM dbo.ThucChayDaTinh tcdt 
					--							WHERE tcdt.HopDongChiTietREF = @HopDongChitietID
					--							AND tcdt.DmSanPhamREF = @DmSanPhamID
					--							AND tcdt.NgayThucHien <= @NgayThucHien),0)
					-- SELECT TOP 1 @TienThangDuGP = tc.TienThucChay_GhiNhan 
					-- , @TK_Admarket = tc.[TK_Admarket]
					-- , @DmViTriID	= tc.[DmViTriID]
					-- FROM dbo.[ThucChay_PerformanceBase_ThayDoi_HopDong] tc 
					--							WHERE tc.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
					--							AND tc.HopDongID = @HopDongID
					--							AND tc.HopDongChiTietID = @HopDongChitietID

					----3. NEU THANH TIEN ThangDuGP + TongThanhTienThucChayPB <= ThanhTien
					--IF(@TongThanhTienThucChay + @TienThangDuGP <= @ThanhTien)
					--BEGIN
					--	--3.1 Thuc hien tinh tiep cho ThangDuGP
					--	--3.2 Cap nhap trang thai ban ghi cho table [ThucChay_PerformanceBase_ThayDoi_HopDong] VA CAP NHAP LYDO
					--	print 'tinh tiep'
					--	EXEC [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_Admarket_ThangDuGP]
					--	@NgayThucHien = @NgayThucHien
					--	,@SoHopDong = @SoHopDong
					--	,@HopDongID = @HopDongID
					--	,@HopDongChitietID = @HopDongChitietID
					--	,@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
					--	,@DmSanPhamID = @DmSanPhamID
					--	,@TK_Admarket = @TK_Admarket
					--	,@DmViTriID = @DmViTriID
					--	,@TienThucChay_GhiNhan = @TienThangDuGP
						
					--END
					
				END
				
			END
		END
		FETCH NEXT FROM db_cur_CP_ThangDuCP INTO  @SoHopDong, @HopDongID ,@HopDongChitietID ,@DmSanPhamID ,@ThucChay_PerformanceBase_ThayDoi_ID 
	END   

	CLOSE db_cur_CP_ThangDuCP   
	DEALLOCATE db_cur_CP_ThangDuCP

END

```
