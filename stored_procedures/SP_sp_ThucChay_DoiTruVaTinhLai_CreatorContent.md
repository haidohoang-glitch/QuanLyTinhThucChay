# Stored Procedure: `sp_ThucChay_DoiTruVaTinhLai_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-25 16:29:34.333000
- **Ngày sửa cuối**: 2021-12-03 16:23:09.133000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pHopDongID` | `int(4)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@GhiChuDoiChu` | `nvarchar(2000)` | No |
| `@GhiChuTinhLai` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
 exec [dbo].[sp_ThucChay_DoiTruVaTinhLai_CreatorContent]
    @pHopDongID INT,
	@pHopDongChiTietID INT,
	@NgayGhiNhanThucChay DATETIME,
	@GhiChuDoiChu NVARCHAR(1000),
	@GhiChuTinhLai NVARCHAR(1000)
*/
CREATE PROCEDURE [dbo].[sp_ThucChay_DoiTruVaTinhLai_CreatorContent]
    @pHopDongID INT,
	@pHopDongChiTietID INT,
	@NgayGhiNhanThucChay DATETIME,
	@GhiChuDoiChu NVARCHAR(1000),
	@GhiChuTinhLai NVARCHAR(1000)
AS
    BEGIN

        DECLARE @NgayThucHien DATETIME , @NgayGioiHanTinh_HDCT DATETIME = '2021-10-01'
		, @Ghichu_DotChayHopDong NVARCHAR(200) = N'ThanhTien_CreatorContent'
		, @GhiChuDoiChu_MuaNgoai NVARCHAR(1000) = N''
		, @GhiChuTinhLai_MuaNgoai NVARCHAR(1000) = N''
		DECLARE @ThucTreo_CreatorContent_CanTinhNgay TABLE(
					AppKetQuaVanHanh_CreatorContent_id INT NOT NULL,
                    HopDongREF INT NOT NULL,
                    HopDongChiTietREF INT NULL ,
					ChietKhau FLOAT NULL,
                    GiaTien INT NOT NULL,
                    SoLuong INT NOT NULL,
					DonViTinh Nvarchar(100),
					ThanhTien FLOAT NOT NULL,
					LaiLo FLOAT NULL
					
		)
		SET @GhiChuDoiChu_MuaNgoai  = @Ghichu_DotChayHopDong + '-' + @GhiChuDoiChu
		SET @NgayThucHien = @NgayGhiNhanThucChay
		--THUC HIEN DOI TRU
		PRINT 'THCU HIEN DOI TRU'
		--1. DOI TRU THUCCHAYDATINH
		EXEC [dbo].[ThucChayDaTinh_DoiTru_ThanhTien_CreatorContent]
		@NgayGhiNhanThucChay				= @NgayGhiNhanThucChay,
		@HopDongREF							= @pHopDongID,
		@HopDongChiTietREF					= @pHopDongChiTietID,
		@ghiChuDoiTru						= @GhiChuDoiChu
		--2. DOI TRU THUCCHAYDATINH_MUANGOAI
		EXEC [dbo].[ThucChayDaTinh_MuaNgoai_DoiTru_ThanhTien_CreatorContent]
		@NgayGhiNhanThucChay				= @NgayGhiNhanThucChay,
		@HopDongREF							= @pHopDongID,
		@HopDongChiTietREF					= @pHopDongChiTietID,
		@ghiChu								= @GhiChuDoiChu_MuaNgoai

		--CAP NHAP TRANG THAI CUA AppKetQuaVanHanh_CreatorContent
		UPDATE ct
		SET ct.RecordStatus = 0
		FROM dbo.AppKetQuaVanHanh_CreatorContent ct
		WHERE ct.HopDongBanREF = @pHopDongID
		AND ct.PhanBoREF = @pHopDongChiTietID

		--THUC HIEN TINH LAI 
		DELETE FROM @ThucTreo_CreatorContent_CanTinhNgay
        DECLARE   @AppKetQuaVanHanh_CreatorContent_id INT = 0,
                @HopDongID INT = @pHopDongID,
                @ChietKhau FLOAT = 0,
                @HopDongChiTietID INT =@pHopDongChiTietID,
                @DonGia FLOAT =0,
                @SoLuongThucChay BIGINT = 0,
				@DonViTinhThucChay NVARCHAR(100) = '',
				@ThanhTienThucChaySauCK FLOAT = 0,
				@LaiLo FLOAT = 0

		--THUC HIEN INSERT DU LIEU THUCCHAYHOPDONGCHITIETPR CAN TINH NGAY
		INSERT INTO @ThucTreo_CreatorContent_CanTinhNgay
		(
			AppKetQuaVanHanh_CreatorContent_id,
			HopDongREF,
			HopDongChiTietREF,
			ChietKhau,
			GiaTien,
			SoLuong,
			DonViTinh,
			ThanhTien,
			LaiLo
		)
				
		SELECT tc.AppKetQuaVanHanh_CreatorContent_id,
                tc.HopDongBanREF,
                tc.PbChietKhau,
                tc.PhanBoREF,
                tc.TcDonGia,
                tc.TcSoLuong,
				tc.DonViTinh,
				ISNULL(tc.TcThanhTien,0) TcThanhTien,
				tc.LaiLo
				FROM
				(
				SELECT * FROM dbo.AppKetQuaVanHanh_CreatorContent tc
				WHERE   tc.IsDeleted <> 1
						--AND tc.RecordStatus = 0
						AND tc.TrangThai in (3,5,6,7,8)
						AND tc.PhanBoREF = @pHopDongChiTietID
						AND tc.HopDongBanREF =  @pHopDongID
				)tc INNER JOIN 
				(SELECT * FROM dbo.HopDong hd 
						WHERE hd.TrangThaiHopDong NOT IN (0,3)
						AND hd.NgayDanhSoHopDong >= @NgayGioiHanTinh_HDCT --pp mapping hdct tinh cho hd >=2021-10-01
				)hd ON tc.HopDongBanREF = hd.HopDongID
				ORDER BY tc.AppKetQuaVanHanh_CreatorContent_id 
        DECLARE icursor_ContentCreator CURSOR
        FOR
            SELECT distinct tc.AppKetQuaVanHanh_CreatorContent_id ,
            tc.HopDongREF ,
            tc.HopDongChiTietREF  ,
			tc.ChietKhau ,
            tc.GiaTien ,
            tc.SoLuong ,
			tc.DonViTinh,
			tc.ThanhTien, tc.LaiLo FROM @ThucTreo_CreatorContent_CanTinhNgay tc

        OPEN icursor_ContentCreator;  

        FETCH NEXT FROM icursor_ContentCreator INTO  @AppKetQuaVanHanh_CreatorContent_id ,
                    @HopDongID ,
                    @ChietKhau ,
                    @HopDongChiTietID ,
                    @DonGia ,
                    @SoLuongThucChay ,
					@DonViTinhThucChay ,
					@ThanhTienThucChaySauCK ,
					@LaiLo

        WHILE @@FETCH_STATUS = 0
            BEGIN  
					
			--KIEM TRA VIEC THUC CHAY BAN CO VUOT GIA TRI HOP DONG
			DECLARE @TongTienThucChayBanSCK FLOAT = 0,
			@TongTienThucChayMuaSCK FLOAT = 0,
			@TongTienLaiThucChaySCK FLOAT = 0,
			@FromDate DATETIME,
			@ToDate DATETIME,
			@ThanhTienThucChaySauCKSauCKThucChay FLOAT = 0,
			@ThanhTienThucChaySauCKHDCT FLOAT = 0,
			@ThucChayDaTinhID_op	NVARCHAR(50) = '',
			@ThucChayDaTinh_MuaNgoaiID_op BIGINT = 0,
			@TongThanhTienThucChayDaTinh_op FLOAT = 0,
			@TongThanhTienKMThucChayDaTinh_op FLOAT = 0
		
			SET @ThanhTienThucChaySauCKHDCT = ISNULL((SELECT TOP (1) IIF(hdct.chietkhau <> 100,hdct.ThanhTien,hdct.DonGia*hdct.SoLuong) FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID ORDER BY hdct.HopDongChiTietID),0)

			----1. INSERT VAO ThucChayDaTinh
			EXEC [dbo].[ThucChayDaTinh_TinhLai_ThanhTien_CreatorContent]
					@NgayThucHien						= @NgayThucHien,
					@AppKetQuaVanHanh_CreatorContent_id	= @AppKetQuaVanHanh_CreatorContent_id,
					@HopDongREF							= @HopDongID,
					@HopDongChiTietREF					= @HopDongChiTietID,
					@ChietKhau							= @ChietKhau,
					@DonGia								= @DonGia,
					@SoLuongThucChay					= @SoLuongThucChay,
					@DonViTinhThucChay					= @DonViTinhThucChay,
					@ThanhTienThucChaySauCK				= @ThanhTienThucChaySauCK,
					@ghiChu								= @GhiChuTinhLai,
					@ThucChayDaTinhID_output			= @ThucChayDaTinhID_op OUTPUT,
					@TongThanhTienThucChayDaTinh_output	= @TongThanhTienThucChayDaTinh_op OUTPUT,
					@TongThanhTienKMThucChayDaTinh_output	= @TongThanhTienKMThucChayDaTinh_op OUTPUT

				
			--2. INSERT VAO ThucChayDaTinh_MuaNgoai
			IF ( -- nếu tồn tại trên bảng ThucChayDaTinh , thì mới thực hiện tính trên bảng TCDT_MuaNgoai
					EXISTS(SELECT TOP (1) tcdt.HopDongID 
						FROM dbo.ThucChayDaTinh tcdt
						WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID
								AND tcdt.SoLuongDotChayBooking = @AppKetQuaVanHanh_CreatorContent_id 
								AND tcdt.NgayThucHien =  @NgayThucHien
								AND tcdt.ThucChayDaTinhID = @ThucChayDaTinhID_op
						ORDER BY HopDongID
					)
				)
			BEGIN
			
				--Xac dinh thuc chay ban co lech treo ha ko
				print 'tinh lai'
				IF(EXISTS(SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
						WHERE hdct.HopDongChiTietID = @HopDongChiTietID
						AND hdct.ChietKhau <> 100 
						ORDER BY hdct.HopDongChiTietID
					))
				BEGIN
					--NEU PHAT SINH LECH TREO HA
					IF(@TongThanhTienThucChayDaTinh_op < @ThanhTienThucChaySauCK)
					BEGIN
						SET @TongTienThucChayBanSCK = @TongThanhTienThucChayDaTinh_op
						SET @TongTienLaiThucChaySCK = @LaiLo
						SET @SoLuongThucChay = IIF(@TongTienLaiThucChaySCK <= 0 ,0 ,@TongTienThucChayBanSCK/@DonGia)
					END
					ELSE
					BEGIN
						SET @TongTienThucChayBanSCK = @ThanhTienThucChaySauCK
						SET @TongTienLaiThucChaySCK = @TongTienThucChayBanSCK - @TongTienThucChayMuaSCK
					END
				
				END
				--VOI TH LA KHUYEN MAI THI TA KO XET LECH TREO HA
				ELSE
				BEGIN
						SET @TongTienThucChayBanSCK = @ThanhTienThucChaySauCK
						SET @TongTienLaiThucChaySCK = @TongTienThucChayBanSCK - @TongTienThucChayMuaSCK
				END
						
				SET @TongTienThucChayMuaSCK = ISNULL((SELECT TOP (1) kq.ThanhTien FROM dbo.AppKetQuaVanHanh_CreatorContent kq
				WHERE kq.AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_id
				ORDER BY kq.AppKetQuaVanHanh_CreatorContent_id),0)

				--THUC HIEN INSERT GIA TRI CHENH LECH BAN MUA CUA CONTENT
				EXEC [dbo].[ThucChayDaTinh_MuaNgoai_TinhLai_ThanhTien_CreatorContent]
					@NgayThucHien						= @NgayThucHien,
					@AppKetQuaVanHanh_CreatorContent_id	= @AppKetQuaVanHanh_CreatorContent_id,
					@HopDongREF							= @HopDongID,
					@HopDongChiTietREF					= @HopDongChiTietID,
					@DonGiaTheoDonViTinh				= @DonGia,
					@DonViTinh							= @DonViTinhThucChay,
					@SoLuongThucChay					= @SoLuongThucChay,
					@TongTienThucChayBanSCK				= @ThanhTienThucChaySauCK,
					@TongTienThucChayMuaSCK				= @TongTienThucChayMuaSCK,
					@TongTienLaiThucChaySCK				= @LaiLo,
					@ghiChu								= @Ghichu_DotChayHopDong,
					@ThucChayDaTinh_MuaNgoai_ouput		= @ThucChayDaTinh_MuaNgoaiID_op OUTPUT

				--2. Update trang thai tinh thuc chay cua AppKetQuaVanHanh_CreatorContent 
				IF(EXISTS(SELECT top (1) tcdtm.ID FROM dbo.ThucChayDaTinh_MuaNgoai tcdtm WHERE tcdtm.ID = @ThucChayDaTinh_MuaNgoaiID_op
				AND tcdtm.HopDongREF = @HopDongID
				AND tcdtm.HopDongChiTietREF = @HopDongChiTietID
				AND tcdtm.NgayThucHien = @NgayThucHien ORDER BY tcdtm.ID))
				BEGIN
					UPDATE dbo.AppKetQuaVanHanh_CreatorContent
					SET RecordStatus = 1
					WHERE AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_id
					AND HopDongBanRef = @HopDongID
					AND PhanBoRef = @HopDongChiTietID

					--CAP NHAP TRANG THAI CUA TABLE INFOR CHO BEN CONTENT
				END
		END
        FETCH NEXT FROM icursor_ContentCreator INTO  @AppKetQuaVanHanh_CreatorContent_id ,
        @HopDongID ,
        @ChietKhau ,
        @HopDongChiTietID ,
        @DonGia ,
        @SoLuongThucChay ,
		@DonViTinhThucChay ,
		@ThanhTienThucChaySauCK ,
		@LaiLo
        END;   
    CLOSE icursor_ContentCreator;  
    DEALLOCATE icursor_ContentCreator;  
	DELETE FROM @ThucTreo_CreatorContent_CanTinhNgay;

END;

```
