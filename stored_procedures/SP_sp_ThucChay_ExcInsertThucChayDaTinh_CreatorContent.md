# Stored Procedure: `sp_ThucChay_ExcInsertThucChayDaTinh_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-25 16:32:57.780000
- **Ngày sửa cuối**: 2025-10-02 10:32:44.733000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@piHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
 exec [dbo].[sp_ThucChay_ExcInsertThucChayDaTinh_CreatorContent] '2025-09-29' ,'2025-09-30' , 1066883
*/
CREATE PROCEDURE [dbo].[sp_ThucChay_ExcInsertThucChayDaTinh_CreatorContent]
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @piHopDongID INT = NULL
AS
    BEGIN

        DECLARE @NgayThucHien DATETIME , @NgayGioiHanTinh_HDCT DATETIME = '2021-10-01'
		, @Ghichu_DotChayHopDong NVARCHAR(200) = N'ThanhTien_CreatorContent'
		, @GhiChuThucChayDaTinh NVARCHAR(200) = N'Tinh sp_ThucChay_ExcInsertThucChayDaTinh_CreatorContent'
		
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
        SET @NgayThucHien = CONVERT(DATE, @StartDate);

	
        WHILE ( @NgayThucHien <= @EndDate )
        BEGIN
				  DELETE FROM @ThucTreo_CreatorContent_CanTinhNgay
                 DECLARE   @AppKetQuaVanHanh_CreatorContent_id INT = 0,
                           @HopDongID INT = 0,
                           @ChietKhau FLOAT = 0,
                           @HopDongChiTietID INT =0,
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
									AND ISNULL(tc.PhanBoREF,0) <> 0
									AND tc.RecordStatus = 0
									AND tc.TrangThai in (3,5,6,7,8)
									AND ( CASE WHEN tc.CreationTime >= LastModificationTime THEN CONVERT(DATE, CreationTime)
												ELSE CONVERT(DATE, LastModificationTime)
											END ) = @NgayThucHien
									AND ( @piHopDongID IS NULL OR tc.HopDongBanREF = @piHopDongID )
							)tc INNER JOIN 
							(SELECT * FROM dbo.HopDong hd 
									WHERE hd.TrangThaiHopDong NOT IN (0,3)
									AND hd.NgayDanhSoHopDong >= @NgayGioiHanTinh_HDCT --pp mapping hdct tinh cho hd >=2021-09-20
							)hd ON tc.HopDongBanREF = hd.HopDongID
					UNION 
					SELECT  ct.AppKetQuaVanHanh_CreatorContent_id,
                           ct.HopDongBanREF,
                           ct.PbChietKhau,
                           ct.PhanBoREF,
                           ct.TcDonGia,
                           ct.TcSoLuong,
						   ct.DonViTinh,
						   ISNULL(ct.TcThanhTien,0) TcThanhTien,
						   ct.LaiLo
                    FROM    (SELECT * FROM dbo.AppKetQuaVanHanh_CreatorContent ct
								WHERE ct.IsDeleted <> 1
								AND ct.RecordStatus = 0
								AND ct.TrangThai in (3,5,6,7,8)
								AND ct.CreationTime < @NgayThucHien
								AND ( @piHopDongID IS NULL OR ct.HopDongBanREF = @piHopDongID )
							)ct
							INNER JOIN 
							(SELECT * FROM dbo.HopDong hd 
								WHERE hd.NgayDanhSoHopDong >=@NgayGioiHanTinh_HDCT  --pp mapping hdct tinh cho hd >=2021-09-20
								AND hd.TrangThaiHopDong NOT IN (0,3)
								AND CONVERT(DATE, hd.LastModifiedAt) = @NgayThucHien
							)hd ON ct.HopDongBanREF = hd.HopDongID


				--SELECT * FROM @ThucTreo_CreatorContent_CanTinhNgay

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
					
					--SELECT * FROM @ThucTreo_CreatorContent_CanTinhNgay  T
					--WHERE T.HopDongChiTietREF = 761619


					--KIEM TRA VIEC THUC CHAY BAN CO VUOT GIA TRI HOP DONG
					DECLARE @TongTienThucChayBanSCK FLOAT = 0,
					@TongTienThucChayMuaSCK FLOAT = 0,
					@TongTienLaiThucChaySCK FLOAT = 0,
					@FromDate DATETIME,
					@ToDate DATETIME,
					@ThanhTienThucChaySauCKSauCKThucChay FLOAT = 0,
					--@ThanhTienThucChaySauCKHDCT FLOAT = 0,
					@ThucChayDaTinhID_op	NVARCHAR(50) = '',
					@ThucChayDaTinh_MuaNgoaiID_op BIGINT = 0,
					@TongThanhTienThucChayDaTinh_op FLOAT = 0,
					@TongThanhTienKMThucChayDaTinh_op FLOAT = 0
		
					--SET @ThanhTienThucChaySauCKHDCT = ISNULL((SELECT TOP (1) IIF(hdct.chietkhau <> 100,hdct.ThanhTien,hdct.DonGia*hdct.SoLuong) FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID ORDER BY hdct.HopDongChiTietID),0)

					----1. INSERT VAO ThucChayDaTinh
					EXEC [dbo].[ThucChayDaTinh_InsertThucChay_ThanhTien_CreatorContent]
							@NgayThucHien						= @NgayThucHien,
							@AppKetQuaVanHanh_CreatorContent_id	= @AppKetQuaVanHanh_CreatorContent_id,
							@HopDongREF							= @HopDongID,
							@HopDongChiTietREF					= @HopDongChiTietID,
							@ChietKhau							= @ChietKhau,
							@DonGia								= @DonGia,
							@SoLuongThucChay					= @SoLuongThucChay,
							@DonViTinhThucChay					= @DonViTinhThucChay,
							@ThanhTienThucChaySauCK				= @ThanhTienThucChaySauCK,
							@ghiChu								= @GhiChuThucChayDaTinh,
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

						--print 'ThucChayDaTinh_MuaNgoai_InsertThucChayLai_ThanhTien_CreatorContent'
						--THUC HIEN INSERT GIA TRI CHENH LECH BAN MUA CUA CREATORCONTENT
						EXEC [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLai_ThanhTien_CreatorContent]
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

						--print @ThucChayDaTinh_MuaNgoaiID_op

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

        SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien);	
        END; 	 

END;

```
