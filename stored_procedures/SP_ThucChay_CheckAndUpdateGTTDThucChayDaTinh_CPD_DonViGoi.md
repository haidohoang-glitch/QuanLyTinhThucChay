# Stored Procedure: `ThucChay_CheckAndUpdateGTTDThucChayDaTinh_CPD_DonViGoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-10-10 11:53:11.080000
- **Ngày sửa cuối**: 2024-08-21 16:22:03.703000

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

CREATE  PROCEDURE [dbo].[ThucChay_CheckAndUpdateGTTDThucChayDaTinh_CPD_DonViGoi] 
	@NgayThucHien DATETIME
AS
BEGIN

	DECLARE  @NgayDanhSo_GioiHan DATETIME , @TongThanhTienThucChay FLOAT = 0
	SET @NgayDanhSo_GioiHan = '2022-01-01'
	DECLARE @HopDongID INT, @HopDongChiTietID INT
		, @ThanhTien FLOAT, @ThanhTien_BF FLOAT
		, @ChietKhau FLOAT, @ChietKhau_BF FLOAT
		, @DonGia FLOAT, @DonGia_BF FLOAT
		, @DeletedStatus SMALLINT
		, @SoLuong BIGINT
		, @GhiChu NVARCHAR(500)
	DECLARE @ChietKhauBF FLOAT, @NgaythuchienBF DATETIME, @ChietKhauHT FLOAT

	--1. Xác định danh mục hdct thay đổi 
	DECLARE db_cursor_CPD_TD_Goi CURSOR FOR  
	SELECT tc.HopDongFK, tc.HopDongChiTietID
		, tc.ThanhTien
		, tcl.ThanhTien as thanhTien_bf
		, tc.ChietKhau
		, tcl.ChietKhau as chietkhau_bf
		, tc.DonGia
		, tcl.DonGia as dongia_bf
		, TC.DeletedStatus
		, tc.SoLuong
	FROM
		(
			SELECT hdct.* FROM [dbo].HopDongChiTiet hdct
			INNER JOIN dbo.HopDong hd on hdct.HopDongFk = hd.HopDongID
			WHERE 1=1
			AND  hdct.DmSanPhamREF in (140,228,564,549,5082)
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 5  
			AND hdct.DeletedStatus = 0
			AND hdct.DmLoaiBannerREF NOT IN (17,18)
			AND hdct.DmLoaiREF <> 13  
			AND CONVERT(DATE,hdct.LastModifiedAt)  = CONVERT(DATE,@NgayThucHien)
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

	OPEN db_cursor_CPD_TD_Goi   
	FETCH NEXT FROM db_cursor_CPD_TD_Goi INTO  @HopDongID , @HopDongChiTietID , @ThanhTien , @ThanhTien_BF 
			, @ChietKhau , @ChietKhau_BF , @DonGia , @DonGia_BF , @DeletedStatus , @SoLuong

	--2. đối trừ
	WHILE @@FETCH_STATUS = 0   
		BEGIN 
			DECLARE @ThucChayDaTinhID_output  NVARCHAR(100) = ''
			DECLARE @ThucChayDaTinhID_output_TL NVARCHAR(100) = N''
			--SELECT 'dbo.ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ThaydoiKM_CPDDonvigoi' as SP, @HopDongChiTietID as HopdongchitietID
			
			SELECT  @ChietKhauHT = hdct.ChietKhau
			FROM HopDongChiTiet hdct
			WHERE hdct.HopDongChiTietID = @HopDongChiTietID

			SELECT TOP 1 @NgaythuchienBF = ngaythuchien
			FROM ThucChayDaTinh
			WHERE HopDongChiTietREF = @HopDongChiTietID and
				  Ngaythuchien < @Ngaythuchien 
			ORDER BY Ngaythuchien desc

			--print (N'NgaythuchienBF')
			--print (@NgaythuchienBF)

			SET @ChietKhauBF = isnull([dbo].[ThucChay_GetChietkhauDatinh](@NgaythuchienBF, @HopDongChiTietID), @ChietKhauHT)

			--print (N'Chiet khấu HT')
			--print (@ChietkhauHT)
			--print (N'Chiet khấu BF')
			--print (@ChietkhauBF)

			IF @ChietKhauHT = 100 OR @ChietKhauBF = 100
			BEGIN
				IF(@DeletedStatus = 1) 
				BEGIN
					EXEC ThucChay_DoitruGiamDoThayDoiKhuyenMai_CPDDonviGoi 
						@NgayThucHien = @NgayThucHien,
						@HopDongChitietID = @HopDongChiTietID,
						@GhiChu = @GhiChu,
						@ThucChayDaTinhID_op = @ThucChayDaTinhID_output OUTPUT
				END
				ELSE
					BEGIN
						EXEC ThucChay_DoitruGiamDoThayDoiKhuyenMai_CPDDonviGoi 
							@NgayThucHien = @NgayThucHien,
							@HopDongChitietID = @HopDongChiTietID,
							@GhiChu = @GhiChu,
							@ThucChayDaTinhID_op = @ThucChayDaTinhID_output OUTPUT

						EXEC [ThucChay_TinhLaiDothaydoikhuyenmai_CPD_DonViGoi]
								@NgayThucHien = @NgayThucHien,
								@HopDongChitietID = @HopDongChiTietID,
								@GhiChu = @GhiChu,
								@ThucChayDaTinhID_op = @ThucChayDaTinhID_output_TL OUTPUT
					END
			END
			ELSE
			BEGIN
				IF(@DeletedStatus = 1) 
				BEGIN
					-- nếu đã tính trước đó thì mới đối trừ
					IF(EXISTS(  SELECT  tcdt.HopDongChiTietREF 
								FROM dbo.ThucChayDaTinh tcdt
								WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
										AND tcdt.NgayThucHien <= @NgayThucHien
								GROUP BY tcdt.HopDongChiTietREF 
								HAVING SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) <> 0
										OR SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) <> 0))
					BEGIN
							SET @GhiChu = N'Đối trừ CPD DonViGoi do huy HopDongChiTietID = ' + CONVERT(NVARCHAR(20),@HopDongChiTietID)
							EXEC [dbo].[ThucChay_DoiTruGiamThucChayDaTinh_CPD_DonViGoi_ByHopDongChiTiet] 
							@NgayThucHien = @NgayThucHien,
							@HopDongChitietID = @HopDongChiTietID,
							@GhiChu = @GhiChu,
							@ThucChayDaTinhID_op = @ThucChayDaTinhID_output OUTPUT
					END
				END
				ELSE
					BEGIN
						-- nếu đã tính trước đó thì mới đối trừ, tính lại
						IF(EXISTS(  SELECT  tcdt.HopDongChiTietREF 
									FROM dbo.ThucChayDaTinh tcdt
									WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
											AND tcdt.NgayThucHien <= @NgayThucHien
									GROUP BY tcdt.HopDongChiTietREF 
									HAVING SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) <> 0
											OR SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) <> 0))
						BEGIN
								SET @GhiChu = N'Đối trừ CPD DonViGoi do thay doi gia tri HopDongChiTietID = ' + CONVERT(NVARCHAR(20),@HopDongChiTietID)
								EXEC [dbo].[ThucChay_DoiTruGiamThucChayDaTinh_CPD_DonViGoi_ByHopDongChiTiet] 
								@NgayThucHien = @NgayThucHien,
								@HopDongChitietID = @HopDongChiTietID,
								@GhiChu = @GhiChu,
								@ThucChayDaTinhID_op = @ThucChayDaTinhID_output OUTPUT

								UPDATE tc
								SET tc.RecordStatus = 0 
								FROM dbo.ThucChayHopDongChiTiet tc
								WHERE tc.HopDongChiTietREF = @HopDongChiTietID

								SET @GhiChu = N'Tính lại CPD DonViGoi do thay doi gia tri HopDongChiTietID = ' + CONVERT(NVARCHAR(20),@HopDongChiTietID)
								EXEC [ThucChay_TinhLaiDothaydoikhuyenmai_CPD_DonViGoi]
										@NgayThucHien = @NgayThucHien,
										@HopDongChitietID = @HopDongChiTietID,
										@GhiChu = @GhiChu,
										@ThucChayDaTinhID_op = @ThucChayDaTinhID_output_TL OUTPUT

								UPDATE tc
								SET tc.RecordStatus = 1 
								FROM dbo.ThucChayHopDongChiTiet tc
								WHERE tc.HopDongChiTietREF = @HopDongChiTietID
						END
					END
			END
	
			FETCH NEXT FROM db_cursor_CPD_TD_Goi INTO  @HopDongID , @HopDongChiTietID , @ThanhTien , @ThanhTien_BF 
			, @ChietKhau , @ChietKhau_BF , @DonGia , @DonGia_BF , @DeletedStatus , @SoLuong
		END   
	CLOSE db_cursor_CPD_TD_Goi   
	DEALLOCATE db_cursor_CPD_TD_Goi

	
END

```
