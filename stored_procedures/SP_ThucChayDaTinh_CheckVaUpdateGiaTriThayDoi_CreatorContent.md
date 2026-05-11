# Stored Procedure: `ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-25 16:35:24.837000
- **Ngày sửa cuối**: 2025-12-13 10:02:17.143000

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
	EXEC [ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_CreatorContent] '2021-06-19'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_CreatorContent]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @CONTRACT_NUMBER NVARCHAR(100)
		, @CONTRACT_ID INT
		, @CONTRACT_DETAIL_ID INT
		, @ISDELETED SMALLINT
		, @GhiChu_DoiTruThucChay NVARCHAR(500) = N''
		, @Ghichu_TinhLaiThucChay NVARCHAR(500) = N''
		, @NgayGioiHanTinh_HDCT DATETIME = '2021-10-01' --NGAY AP DUNG VIEC TINH CHO NHUNG HOPDONG DANH SO

	DECLARE @Table_ThucChay_CreatorContent TABLE
	(
		CONTRACT_ID int
		, CONTRACT_DETAIL_ID INT
		, SELL_MONEY_VND FLOAT
		, SELL_MONEY_VND_BF FLOAT
		, CHIETKHAU FLOAT
		, CHIETKHAU_BF FLOAT
		, DONGIA FLOAT
		, DONGIA_BF FLOAT
		, ISDELETED SMALLINT
	)
	--1. CHECK HOPDONGCHITET THAY DOI THANHTIEN VA BI XOA
	INSERT INTO @Table_ThucChay_CreatorContent
	(
		CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, SELL_MONEY_VND 
		, SELL_MONEY_VND_BF
		, CHIETKHAU
		, CHIETKHAU_BF
		, DONGIA
		, DONGIA_BF
		, ISDELETED 
	)
	--Check hop dong chi tiet thay doi
	--	Sản phẩm = Content Creator, ID=5184
	--- HTQC= Social Media, id=29
	SELECT tc.HopDongFK, tc.HopDongChiTietID
	, tc.ThanhTien
	, tcl.ThanhTien as thanhTien_bf
	, tc.ChietKhau
	, tcl.ChietKhau as chietkhau_bf
	, tc.DonGia
	, tcl.DonGia as dongia_bf
	, TC.DeletedStatus
	FROM
	(
		SELECT hdct.* FROM [dbo].HopDongChiTiet hdct
		INNER JOIN dbo.HopDong hd on hdct.HopDongFk = hd.HopDongID
		WHERE 1=1
		--AND hdct.DeletedStatus <> 1
		--AND hdct.DmLoaiREF = 29 --HAIDH LOAI DIEU KIEN NAY DO CHAY QUA NHIEU HINH THUC KHAC 13122025
		AND hdct.DmSanPhamREF = 5184
		AND convert(date,hdct.LastModifiedAt) = @NgayThucHien
		AND hd.NgayDanhSoHopDong >= @NgayGioiHanTinh_HDCT --TINH GIA TRI THAY DOI THEO NHUNG HOPDONG TINH THEO PP MOI 2021-10-01
	)TC
	OUTER APPLY
	(SELECT  TOP 1 tcl.HopDongChiTietREF, tcl.ThanhTien, tcl.ChietKhau, tcl.DonGia
	FROM  [dbo].HopDongChiTietLog TCL WHERE TCL.HopDongChiTietREF = tc.HopDongChiTietID
	AND convert(date,TCL.LastModifiedAt) < convert(date,tc.LastModifiedAt)
	order by tcl.LastModifiedAt desc
	)TCL
	WHERE (((ISNULL(TC.ThanhTien,0) <> ISNULL(TCL.ThanhTien,0))) 
		OR ((ISNULL(TC.ChietKhau,0) <> ISNULL(TCL.ChietKhau,0)))
		OR ((ISNULL(TC.DonGia,0) <> ISNULL(TCL.DonGia,0)))
		OR ( tc.DeletedStatus = 1)
	)
	AND TCL.HopDongChiTietREF IS NOT NULL

	--select * from @Table_ThucChay_CreatorContent

	DECLARE R_Cursor_CreatorContent CURSOR FOR 
	
	SELECT CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, ISDELETED 
	FROM @Table_ThucChay_CreatorContent
	ORDER BY CONTRACT_DETAIL_ID

	OPEN R_Cursor_CreatorContent

	-- Perform the first fetch.
	FETCH NEXT FROM R_Cursor_CreatorContent INTO  @CONTRACT_ID , @CONTRACT_DETAIL_ID 
		, @ISDELETED 
			
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @CONTRACT_NUMBER = ISNULL((SELECT TOP (1) hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @CONTRACT_ID ORDER BY hd.HopDongID),'')
		--THUC HIEN DOI TRU TOAN BO ORDER NAY
		SET @GhiChu_DoiTruThucChay = ''
		SET @Ghichu_TinhLaiThucChay = ''
		--HDCT BI XOA
		IF(@ISDELETED = 1)
		BEGIN
			--NEU TON TAI THUC CHAY VOI HOPDONGCHITIET
			IF(EXISTS(SELECT top (1) tcdt.HopDongChiTietREF FROM DBO.ThucChayDaTinh tcdt
			WHERE tcdt.HopDongId = @CONTRACT_ID
			AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
			ORDER BY tcdt.HopDongChiTietREF ))
			BEGIN
				--THUC HIEN DOI TRU TOAN BO
				SET @GhiChu_DoiTruThucChay = N'Doi Tru toan bo HDCT: ' + convert(nvarchar(100),@CONTRACT_DETAIL_ID) + N' do hdct CreatorContent bi huy'

				EXEC [dbo].[ThucChayDaTinh_DoiTru_ThanhTien_CreatorContent]
				@NgayGhiNhanThucChay				= @NgayThucHien,
				@HopDongREF							= @CONTRACT_ID,
				@HopDongChiTietREF					= @CONTRACT_DETAIL_ID,
				@ghiChuDoiTru						= @GhiChu_DoiTruThucChay

				----THUC HIEN UPDATE LAI KET QUA VAN HANH ??????
				--UPDATE dbo.AppKetQuaVanHanh_CreatorContent
				--SET RecordStatus = 0
				--WHERE HopDongBanRef = @CONTRACT_ID
				--AND PhanBoRef = @CONTRACT_DETAIL_ID
			END
		END
		--THAY DOI THANH TIEN
		ELSE
		BEGIN
			IF(EXISTS(SELECT top (1) t.CONTRACT_ID FROM @Table_ThucChay_CreatorContent t
			WHERE t.CONTRACT_ID = @CONTRACT_ID
			AND t.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
			AND ((t.CHIETKHAU <> t.CHIETKHAU_BF) OR (t.DONGIA <> t.DONGIA_BF))
			))
			BEGIN
				SET @GhiChu_DoiTruThucChay = N'Thay doi chietkhau or dongia '  + N' ,Doi tru CreatorContent cho hdct: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) 
				SET @Ghichu_TinhLaiThucChay = N'Thay doi chietkhau or dongia '  + N' ,Tinh lai CreatorContent cho hdct: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) 
				print @GhiChu_DoiTruThucChay
				EXEC [dbo].[sp_ThucChay_DoiTruVaTinhLai_CreatorContent]
				@pHopDongID = @CONTRACT_ID,
				@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
				@NgayGhiNhanThucChay = @NgayThucHien,
				@GhiChuDoiChu = @GhiChu_DoiTruThucChay,
				@GhiChuTinhLai = @Ghichu_TinhLaiThucChay
			END
			ELSE
			BEGIN
				IF(EXISTS(SELECT top (1) t.CONTRACT_ID FROM @Table_ThucChay_CreatorContent t
				WHERE t.CONTRACT_ID = @CONTRACT_ID
				AND t.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
				AND t.SELL_MONEY_VND > t.SELL_MONEY_VND_BF))
				BEGIN
					--HAIDH COMMENT DO CO TRUONG HOP HOPDONGCHITIET THAY DOI SOLUONG = 0 ROI THAY DOI TANG SL LAI KHONG TINH DUOC 13122025
					----NEU TON TAI THUC CHAY VOI HOPDONGCHITIET
					--IF(EXISTS(SELECT top (1) tcdt.HopDongChiTietREF FROM DBO.ThucChayDaTinh tcdt
					--WHERE tcdt.HopDongId = @CONTRACT_ID
					--AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
					--AND tcdt.NgayThucHien <= @NgayThucHien
					--AND tcdt.ThanhTienLechTreoHa <> 0
					--ORDER BY tcdt.NgayThucHien desc ))
					--BEGIN
					--	SET @GhiChu_DoiTruThucChay = N'Thay doi thanhtien '  + N' ,Doi tru CreatorContent cho hdct: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) 
					--	SET @Ghichu_TinhLaiThucChay = N'Thay doi thanhtien '  + N' ,Tinh lai CreatorContent cho hdct: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) 
					--	print @GhiChu_DoiTruThucChay
					--	EXEC [dbo].[sp_ThucChay_DoiTruVaTinhLai_CreatorContent]
					--	@pHopDongID = @CONTRACT_ID,
					--	@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
					--	@NgayGhiNhanThucChay = @NgayThucHien,
					--	@GhiChuDoiChu = @GhiChu_DoiTruThucChay,
					--	@GhiChuTinhLai = @Ghichu_TinhLaiThucChay
					--END

					SET @GhiChu_DoiTruThucChay = N'Thay doi thanhtien '  + N' ,Doi tru CreatorContent cho hdct: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) 
					SET @Ghichu_TinhLaiThucChay = N'Thay doi thanhtien '  + N' ,Tinh lai CreatorContent cho hdct: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) 
					print @GhiChu_DoiTruThucChay
					EXEC [dbo].[sp_ThucChay_DoiTruVaTinhLai_CreatorContent]
					@pHopDongID = @CONTRACT_ID,
					@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
					@NgayGhiNhanThucChay = @NgayThucHien,
					@GhiChuDoiChu = @GhiChu_DoiTruThucChay,
					@GhiChuTinhLai = @Ghichu_TinhLaiThucChay
				END
				ELSE
				--THANHTIEN HIEN TAI NHO HON THANHTIEN BF
				BEGIN
					DECLARE @SELL_MONEY_VND FLOAT = 0
					SET @SELL_MONEY_VND = ISNULL((SELECT TOP (1) tc.SELL_MONEY_VND FROM @Table_ThucChay_CreatorContent tc
					WHERE tc.CONTRACT_ID = @CONTRACT_ID
					AND tc.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID),0)

					IF(EXISTS(SELECT top (1) tcdt.HopDongChiTietREF FROM DBO.ThucChayDaTinh tcdt
					WHERE tcdt.HopDongId = @CONTRACT_ID
					AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
					AND tcdt.NgayThucHien <= @NgayThucHien
					GROUP BY tcdt.HopDongChiTietREF HAVING SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) > @SELL_MONEY_VND)
					)
					BEGIN
						SET @GhiChu_DoiTruThucChay = N'Thay doi thanhtien '  + N' ,Doi tru CreatorContent cho hdct: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) 
						SET @Ghichu_TinhLaiThucChay = N'Thay doi thanhtien '  + N' ,Tinh lai CreatorContent cho hdct: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) 
						print @GhiChu_DoiTruThucChay
						EXEC [dbo].[sp_ThucChay_DoiTruVaTinhLai_CreatorContent]
						@pHopDongID = @CONTRACT_ID,
						@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
						@NgayGhiNhanThucChay = @NgayThucHien,
						@GhiChuDoiChu = @GhiChu_DoiTruThucChay,
						@GhiChuTinhLai = @Ghichu_TinhLaiThucChay
					END
				END 
			END
			
		END


		FETCH NEXT FROM R_Cursor_CreatorContent INTO  @CONTRACT_ID , @CONTRACT_DETAIL_ID 
		, @ISDELETED 
	END

	CLOSE R_Cursor_CreatorContent
	DEALLOCATE R_Cursor_CreatorContent

	--2. CHECK KET QUA VAN HANH BI XOA
	EXEC [dbo].[ThucChayDaTinh_CheckKetQuaVanHanhXoa_CreatorContent]
	@NgayThucHien = @NgayThucHien
END

```
