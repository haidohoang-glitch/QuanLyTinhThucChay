# Stored Procedure: `ThucChayDaTinh_CheckKetQuaVanHanhThayDoi_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-01-05 10:38:33.923000
- **Ngày sửa cuối**: 2024-08-29 15:52:11.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC [ThucChayDaTinh_CheckKetQuaVanHanhThayDoi_CreatorContent] @NgayThucHien = '2022-01-11'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_CheckKetQuaVanHanhThayDoi_CreatorContent]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @CONTRACT_NUMBER NVARCHAR(100)
		, @CONTRACT_ID INT
		, @CONTRACT_DETAIL_ID INT
		, @AppKetQuaVanHanh_CreatorContent_ID INT
		, @ISDELETED SMALLINT
		, @LaiLo FLOAT =0
		, @GhiChu_DoiTruThucChay NVARCHAR(500) = N''
		, @NgayGioiHanTinh_HDCT DATETIME = '2021-10-01'
	DECLARE @DonGiaTheoDonViTinh FLOAT = 0
			, @DonViTinh NVARCHAR(100)
			, @SoLuongThucChay BIGINT = 0
			, @TongTienThucChayMuaSCK FLOAT = 0
			, @TongTienThucChayBanSCK FLOAT = 0
			, @GhiChuTinhLai NVARCHAR(500) = ''
			, @ThucChayDaTinh_MuaNgoai_ouput_id BIGINT = 0

	DECLARE @Table_ThucChay_CreatorContent TABLE
	(
		CONTRACT_ID int
		, CONTRACT_DETAIL_ID INT
		, AppKetQuaVanHanh_CreatorContent_ID INT
		, ISDELETED SMALLINT
		, LaiLo FLOAT
		, DonGia FLOAT
		, SoluongThucChay BIGINT
		, DonViTinh NVARCHAR(100)
		, ThanhTienThucChayBan FLOAT
		, ThanhTienThucChayMua FLOAT
	)
	--1. CHECK AppKetQuaVanHanh_CreatorContent THAY DOI
	INSERT INTO @Table_ThucChay_CreatorContent
	(
		CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, AppKetQuaVanHanh_CreatorContent_ID
		, ISDELETED 
		, LaiLo
		, DonGia 
		, SoluongThucChay 
		, DonViTinh 
		, ThanhTienThucChayBan 
		, ThanhTienThucChayMua 
	)
	--Check hop dong chi tiet thay doi
	--	Sản phẩm = Content Creator, ID=5184
	--- HTQC= Social Media, id=29
	SELECT 
    tc.HopDongBanREF,
    tc.PhanBoREF,
	tc.AppKetQuaVanHanh_CreatorContent_id,
    tc.IsDeleted,
	ISNULL(tc.LaiLo,0) AS LaiLo,
	ISNULL(tc.TcDonGia,0),
	ISNULL(tc.TcSoLuong,0),
	ISNULL(tc.DonViTinh,''),
	ISNULL(tc.TcThanhTien,0) ,
	ISNULL(tc.ThanhTien,0)
	FROM
	(
		SELECT KQ.* FROM
		(
			SELECT T.* FROM dbo.AppKetQuaVanHanh_CreatorContent T
			WHERE   1=1
					AND ISNULL(T.PhanBoREF,0) <> 0
					AND T.TrangThai in (3,5,6,7,8)
					AND ( CASE WHEN T.CreationTime >= LastModificationTime THEN CONVERT(DATE, CreationTime)
								ELSE CONVERT(DATE, LastModificationTime)
							END ) = @NgayThucHien
		)KQ
		OUTER APPLY
		(SELECT  TOP 1 KQL.PhanBoRef, KQL.ThanhTien, KQL.ChietKhau, KQL.DonGia
		, KQL.LaiLo
		FROM  [dbo].AppKetQuaVanHanhHistory_CreatorContent KQL WHERE KQL.AppKetQuaVanHanh_CreatorContentRef = KQ.AppKetQuaVanHanh_CreatorContent_ID
		AND convert(date,KQL.LastModificationTime) < convert(date,KQ.LastModificationTime)
		order by KQL.LastModificationTime desc
		)KQL
		WHERE ((ISNULL(KQ.LaiLo,0) <> ISNULL(KQL.LaiLo,0)) OR (KQ.IsDeleted = 1))
				AND KQ.RecordStatus = 1 --da thuc hien tinh
	)tc INNER JOIN 
	(SELECT * FROM dbo.HopDong hd 
			WHERE hd.TrangThaiHopDong NOT IN (0,3)
			AND hd.NgayDanhSoHopDong >= @NgayGioiHanTinh_HDCT --pp mapping hdct tinh cho hd >=2021-10-01
	)hd ON tc.HopDongBanREF = hd.HopDongID

	DECLARE R_Cursor_KqvhCreatorContent CURSOR FOR 
	
	SELECT CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, AppKetQuaVanHanh_CreatorContent_ID
		, ISDELETED 
		, LaiLo
		, DonGia 
		, SoluongThucChay 
		, DonViTinh 
		, ThanhTienThucChayBan 
		, ThanhTienThucChayMua 
	FROM @Table_ThucChay_CreatorContent
	ORDER BY CONTRACT_DETAIL_ID

	OPEN R_Cursor_KqvhCreatorContent

	-- Perform the first fetch.
	FETCH NEXT FROM R_Cursor_KqvhCreatorContent INTO  @CONTRACT_ID , @CONTRACT_DETAIL_ID , @AppKetQuaVanHanh_CreatorContent_ID
		, @ISDELETED , @LaiLo,  @DonGiaTheoDonViTinh, @SoLuongThucChay , @DonViTinh  , @TongTienThucChayBanSCK , @TongTienThucChayMuaSCK 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		DECLARE @ThucChayDaTinhID_output NVARCHAR(100) = ''
		DECLARE @ThucChayDaTinh_MuaNgoai_ID_output BIGINT = 0
		SET @CONTRACT_NUMBER = ISNULL((SELECT TOP (1) hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @CONTRACT_ID ORDER BY hd.HopDongID),'')
		--THUC HIEN DOI TRU TOAN BO ORDER NAY
		SET @GhiChu_DoiTruThucChay = ''
		--KET QUA VAN HANH BI XOA
		IF(@ISDELETED = 1)
		BEGIN
			--NEU TON TAI THUC CHAY VOI HOPDONGCHITIET
			IF(EXISTS(SELECT top (1) tcdt.HopDongChiTietREF, tcdt.DotChayBooking FROM DBO.ThucChayDaTinh tcdt
			WHERE tcdt.HopDongId = @CONTRACT_ID
			AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
			AND tcdt.DotChayBooking = @AppKetQuaVanHanh_CreatorContent_ID
			GROUP BY  tcdt.HopDongChiTietREF, tcdt.DotChayBooking HAVING SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiatriThayDoi) <> 0
			OR SUM(tcdt.ThanhTienKM + tcdt.GiatriKMThayDoi) <> 0 ))
			BEGIN
				--THUC HIEN DOI TRU TOAN BO
				SET @GhiChu_DoiTruThucChay = N'Doi Tru toan bo KQVH: ' + convert(nvarchar(100),@AppKetQuaVanHanh_CreatorContent_ID) + N' do kqvh CreatorContent bi huy'

				EXEC [dbo].[ThucChayDaTinh_DoiTru_ThanhTien_CreatorContent_ByKetQuaVanHanhID]
				@NgayGhiNhanThucChay				= @NgayThucHien,
				@HopDongREF							= @CONTRACT_ID,
				@HopDongChiTietREF					= @CONTRACT_DETAIL_ID,
				@AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_ID,
				@ghiChuDoiTru						= @GhiChu_DoiTruThucChay,
				@ThucChayDaTinhID_op				= @ThucChayDaTinhID_output OUTPUT
				
				
			END
		END
		ELSE --THAY DOI LAI => THUC HIEN DOI TRU VA TINH LAI LAI (ThucChayDaTinh_MuaNgoai)
		BEGIN
			--PRINT 'VAO DAY'
			--NEU TON TAI THUC CHAY VOI HOPDONGCHITIET
			IF(EXISTS(SELECT top (1) tcdt.[ThucChayMuaNgoaiChiTietREF] FROM DBO.ThucChayDaTinh_MuaNgoai tcdt
			WHERE tcdt.[HopDongREF] = @CONTRACT_ID
			AND tcdt.[HopDongChiTietREF] = @CONTRACT_DETAIL_ID
			AND tcdt.[ThucChayMuaNgoaiChiTietREF] = @AppKetQuaVanHanh_CreatorContent_ID
			GROUP BY  tcdt.[ThucChayMuaNgoaiChiTietREF] HAVING SUM(ISNULL(tcdt.[ThanhTienLaiThucChaySauCK],0) + ISNULL(tcdt.[GiaTriThayDoiLaiSauCK],0)) <> @LaiLo
			OR SUM(tcdt.[ThanhTienLaiThucChayKM] + tcdt.[GiaTriKMLaiThayDoi]) <> 0 ))
			BEGIN
				--THUC HIEN DOI TRU TOAN BO
				PRINT 'VAO DAY DOI TRU LAI'
				SET @GhiChu_DoiTruThucChay = N'Doi Tru toan bo KQVH: ' + convert(nvarchar(100),@AppKetQuaVanHanh_CreatorContent_ID) + N' do kqvh CreatorContent thay doi lailo'

				EXEC [dbo].[ThucChayDaTinh_MuaNgoai_DoiTru_ThanhTien_CreatorContent_ThayDoiKQVH]
				@NgayGhiNhanThucChay				= @NgayThucHien,
				@HopDongREF							= @CONTRACT_ID,
				@HopDongChiTietREF					= @CONTRACT_DETAIL_ID,
				@AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_ID,
				@ghiChu								= @GhiChu_DoiTruThucChay,
				@ThucChayDaTinh_MuaNgoai_ouput		= @ThucChayDaTinh_MuaNgoai_ID_output OUTPUT

				SELECT @ThucChayDaTinh_MuaNgoai_ID_output

				IF(@ThucChayDaTinh_MuaNgoai_ID_output <> 0)
				BEGIN
					PRINT ' VAO TINH LAI LAI '
					--SELECT TOP (1)			@DonGiaTheoDonViTinh = tc.TcDonGia,
					--		@SoLuongThucChay = tc.TcSoLuong,
					--		@DonViTinh = tc.DonViTinh,
					--		@TongTienThucChayBanSCK = ISNULL(tc.TcThanhTien,0) ,
					--		@TongTienThucChayMuaSCK = ISNULL(tc.ThanhTien,0),
					--		@TongTienLaiThucChaySCK = ISNULL(tc.LaiLo,0)
					--FROM dbo.AppKetQuaVanHanh_CreatorContent tc
					--WHERE   tc.IsDeleted <> 1
					--AND tc.TrangThai in (3,5,6,7,8)
					--AND tc.PhanBoREF = @CONTRACT_DETAIL_ID
					--AND tc.HopDongBanREF =  @CONTRACT_ID
					--AND tc.AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_ID


					SET @DonGiaTheoDonViTinh = ISNULL(@DonGiaTheoDonViTinh,0)
					SET @DonViTinh = ISNULL(@DonViTinh,'')
					SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
					SET @TongTienThucChayBanSCK = ISNULL(@TongTienThucChayBanSCK,0)
					SET @TongTienThucChayMuaSCK = ISNULL(@TongTienThucChayMuaSCK,0)
					SET @LaiLo = ISNULL(@LaiLo,0)
					SET @GhiChuTinhLai =  N'Tinh lai cho KQVH: ' + convert(nvarchar(100),@AppKetQuaVanHanh_CreatorContent_ID) + N' do kqvh CreatorContent thay doi lailo'

					EXEC [dbo].[ThucChayDaTinh_MuaNgoai_TinhLai_ThanhTien_CreatorContent]
					@NgayThucHien						= @NgayThucHien,
					@AppKetQuaVanHanh_CreatorContent_id	= @AppKetQuaVanHanh_CreatorContent_ID,
					@HopDongREF							= @CONTRACT_ID,
					@HopDongChiTietREF					= @CONTRACT_DETAIL_ID,
					@DonGiaTheoDonViTinh				= @DonGiaTheoDonViTinh,
					@DonViTinh							= @DonViTinh,
					@SoLuongThucChay					= @SoLuongThucChay,
					@TongTienThucChayBanSCK				= @TongTienThucChayBanSCK,
					@TongTienThucChayMuaSCK				= @TongTienThucChayMuaSCK,
					@TongTienLaiThucChaySCK				= @LaiLo,
					@ghiChu								= @GhiChuTinhLai,
					@ThucChayDaTinh_MuaNgoai_ouput		= @ThucChayDaTinh_MuaNgoai_ouput_id OUTPUT

					IF (@ThucChayDaTinh_MuaNgoai_ouput_id <> 0) 
					BEGIN
						--UPDATE TRANG THAI DA TINH CHO BAN GHI
						UPDATE dbo.AppKetQuaVanHanh_CreatorContent
						SET RecordStatus = 1
						WHERE AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_ID
						AND HopDongBanRef = @CONTRACT_ID
						AND PhanBoRef = @CONTRACT_DETAIL_ID
					END
				END
			END
		END
	
	FETCH NEXT FROM R_Cursor_KqvhCreatorContent INTO  @CONTRACT_ID , @CONTRACT_DETAIL_ID , @AppKetQuaVanHanh_CreatorContent_ID
		, @ISDELETED , @LaiLo,  @DonGiaTheoDonViTinh, @SoLuongThucChay , @DonViTinh  , @TongTienThucChayBanSCK , @TongTienThucChayMuaSCK 
	END

	CLOSE R_Cursor_KqvhCreatorContent
	DEALLOCATE R_Cursor_KqvhCreatorContent



END

```
