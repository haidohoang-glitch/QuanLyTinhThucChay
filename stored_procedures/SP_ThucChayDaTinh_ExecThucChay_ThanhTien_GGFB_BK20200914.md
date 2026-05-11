# Stored Procedure: `ThucChayDaTinh_ExecThucChay_ThanhTien_GGFB_BK20200914`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-09-14 10:44:15.063000
- **Ngày sửa cuối**: 2020-09-14 10:44:15.063000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChayDaTinh_ExecThucChay_ThanhTien_GGFB]  '2020-08-14'
EXEC [dbo].[ThucChayDaTinh_ExecThucChay_ThanhTien_GGFB]  '2020-09-01'

--DELETE	FROM dbo.ThucChayDaTinh_MuaNgoai 
--WHERE ThucChayMuaNgoaiChiTietREF = @ADS_Operating_Result_Map_OrderId
--AND HopDongREF = @HopDongID
--AND HopDongChiTietREF = @HopDongChiTietID
--AND (DmSanPhamREF in (306,423,5160,5188)
--	  OR DmViTriREF in (100093,100478) )
--	  AND NgayThucHien = @NgayThucHien
--	  AND DmChienDichREF = 2 --XOA THEO SAN LUONG CHOT
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExecThucChay_ThanhTien_GGFB_BK20200914]
	@NgayThucHien DATETIME
AS
BEGIN
	
	SET NOCOUNT ON;
    DECLARE	@NgayGioiHanTinh DATETIME = '2013-01-01',  --  tính thực chạy bắt đầu từ ngày 
	@Ghichu_DotChayHopDong NVARCHAR(100) =  N'ThanhTien_GGFB'
			
    DECLARE 
	 @ADS_Operating_Result_Map_OrderId INT -- id bảng map
	,@HopDongID INT				-- id hợp đồng
	,@HopDongChiTietID INT		-- id phân bổ
	,@Operating_Order_Id INT
	,@Operating_Result_Id INT
	,@Sell_Money_VND FLOAT
	,@Result BIGINT
	,@UNITS NVARCHAR(100)
	,@DuToanMua FLOAT
	,@Is_SanLuongChot SMALLINT = 0

	

	DECLARE thanhtien_ggfb_cursor CURSOR FOR
	--THONG TIN THUC CHAY HANG NGAY
	SELECT 
			TC.Id,
			TC.Operating_Order_Id,	
			TC.operating_Result_Id,	
			OD.Contract_Id, 
			OD.Contract_Detail_Id,
			ISNULL(TC.Sell_Money_VND,0) AS Sell_Money_VND, --thuc chay ban
			ISNULL(TC.Result,0) AS Result, --soluong
			OD.UNITS, --don gia
			0 AS DuToanMua, --ngan sach ban
			1 AS IS_SANLUONGCHOT --1: TINH THEO SO LUONG THUC TE PHAT SINH, 2: TINH THEO SAN LUONG CHOT
	FROM (
			SELECT * FROM [dbo].[ADS_Operating_Result_Map_Order] TC
			WHERE isnull(TC.IsCaculatedActual, 0) = 0
				  AND TC.IsDeleted = 0
				  AND (ISNULL(TC.Sell_Money_VND,0) <> 0)
				  AND CONVERT(DATE,TC.LastModificationTime) = @NgayThucHien
		 )TC
	INNER JOIN DBO.ADS_Operating_Order OD ON TC.Operating_Order_Id = OD.Id
	INNER JOIN (SELECT HDCT.HopDongFK, HDCT.HopDongChiTietID, HDCT.DeletedStatus FROM dbo.HopDongChiTiet hdct WHERE HDCT.DeletedStatus = 0) hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
	AND OD.Contract_Id = hdct.HopDongFK
	--THONG TIN THUC CHAY THEO SAN LUONG
	UNION
	SELECT TC.[Id],
      TC.[Operating_Order_Id], 
	  0 AS operating_Result_Id,
	  OD.Contract_Id, 
	  OD.Contract_Detail_Id,
	  ISNULL(TC.[TotalMoney],0) AS Sell_Money_VND, --thuc chay ban
	  ISNULL(TC.[Quantity],0) AS Result, --soluong
	  ISNULL(OD.UNITS,'') AS UNITS, --don gia
      0 AS DuToanMua,
	  2 AS IS_SANLUONGCHOT --1: TINH THEO SO LUONG THUC TE PHAT SINH, 2: TINH THEO SAN LUONG CHOT
	FROM 
	(
		SELECT * FROM [dbo].[ADS_Operating_Result_Quantity] TC
		WHERE TC.Status = 2 --DA CHOT
		AND TC.IsCalc_Result_Quantity = 0 --CHUA TINH THUC CHAY
		AND isnull(TC.IsDeleted,0) = 0
		AND CONVERT(DATE,TC.LastModificationTime) = @NgayThucHien
	) TC
	INNER JOIN DBO.ADS_Operating_Order OD ON TC.Operating_Order_Id = OD.Id
	INNER JOIN (SELECT HDCT.HopDongFK, HDCT.HopDongChiTietID, HDCT.DeletedStatus 
			FROM dbo.HopDongChiTiet hdct WHERE HDCT.DeletedStatus = 0) hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
	AND OD.Contract_Id = hdct.HopDongFK

	OPEN thanhtien_ggfb_cursor
	FETCH NEXT FROM thanhtien_ggfb_cursor 
	INTO  @ADS_Operating_Result_Map_OrderId , @Operating_Order_Id, @Operating_Result_Id,
		  @HopDongID, @HopDongChiTietID, @Sell_Money_VND, @Result, @UNITS, @DuToanMua, @Is_SanLuongChot
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--KIEM TRA VIEC THUC CHAY BAN CO VUOT GIA TRI HOP DONG
		DECLARE @DonGiaTheoDonViTinh FLOAT = 0,
		@SoLuongThucChay BIGINT = 0,
		@TongTienThucChayBanSCK FLOAT = 0,
		@TongTienThucChayMuaSCK FLOAT = 0,
		@TongTienLaiThucChaySCK FLOAT = 0,
		@FromDate DATETIME,
		@ToDate DATETIME,
		--@TongTienLechTreoHa FLOAT = 0,
		@ThanhTienSauTrietKhauThucChay FLOAT = 0

		SET @Result = IIF(@Result = 0,1,@Result)
		SET @UNITS = IIF(@UNITS = '',N'GÓI',@UNITS)
		--CHECK TINH THEO SOLUONG THUC TE PHAT SINH HAY SAN LUONG CHOT
		IF(@Is_SanLuongChot = 1)
		BEGIN
			--1. INSERT VAO ThucChayDaTinh
			EXEC [dbo].[ThucChayDaTinh_InsertThucChay_ThanhTien_GGFB]
					@NgayThucHien						= @NgayThucHien,
					@ADS_Operating_Result_Map_OrderId	= @ADS_Operating_Result_Map_OrderId,
					@HopDongREF							= @HopDongID,
					@HopDongChiTietREF					= @HopDongChiTietID,
					@ghiChu								= @Ghichu_DotChayHopDong

			--2. INSERT VAO ThucChayDaTinh_MuaNgoai
			IF ( -- nếu tồn tại trên bảng ThucChayDaTinh , thì mới thực hiện tính trên bảng TCDT_MuaNgoai
				 EXISTS(SELECT TOP (1) HopDongID 
						FROM dbo.ThucChayDaTinh 
						WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
							  AND SoLuongDotChayBooking = @ADS_Operating_Result_Map_OrderId 
							  AND NgayThucHien =  @NgayThucHien
						ORDER BY HopDongID
					)
				)
			BEGIN
			

				SET @DonGiaTheoDonViTinh = @Sell_Money_VND/@Result
				SET @UNITS	= dbo.FormatDonViTinh_ThanhTien_GGFB(@UNITS)
				SET @TongTienThucChayMuaSCK = ISNULL((SELECT TOP (1) isnull(TCC.Total_Money_VND,0) FROM DBO.ADS_Operating_Result TCC WHERE TCC.ID = @Operating_Result_Id ORDER BY TCC.ID),0)

				--Xac dinh thuc chay ban co lech treo ha ko
				IF(EXISTS(SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
						WHERE hdct.HopDongChiTietID = @HopDongChiTietID
						AND hdct.ChietKhau <> 100 
						ORDER BY hdct.HopDongChiTietID
					))
				BEGIN
					SET @ThanhTienSauTrietKhauThucChay = (SELECT TOP(1) (tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)  FROM dbo.ThucChayDaTinh tcdt
															WHERE tcdt.HopDongID = @HopDongID
															AND tcdt.HopDongChiTietREF = @HopDongChiTietID
															AND tcdt.SoLuongDotChayBooking = @ADS_Operating_Result_Map_OrderId
															AND tcdt.NgayThucHien = @NgayThucHien
															AND (tcdt.ThanhTienSauTrietKhauThucChay +  tcdt.GiaTriThayDoi < @Sell_Money_VND)
														    ORDER BY tcdt.CreatedAt desc)
					IF(@ThanhTienSauTrietKhauThucChay IS NOT NULL)
					BEGIN
						SET @TongTienThucChayBanSCK = @ThanhTienSauTrietKhauThucChay
						SET @TongTienLaiThucChaySCK = @TongTienThucChayBanSCK - @TongTienThucChayMuaSCK
						SET @SoLuongThucChay = IIF(@TongTienLaiThucChaySCK <= 0 ,0 ,@TongTienThucChayBanSCK/@DonGiaTheoDonViTinh)
					END
					ELSE
					BEGIN
						SET @TongTienThucChayBanSCK = @Sell_Money_VND
						SET @TongTienLaiThucChaySCK = @TongTienThucChayBanSCK - @TongTienThucChayMuaSCK
						SET @SoLuongThucChay = @Result
					END
				
				END
				--VOI TH LA KHUYEN MAI THI TA KO XET LECH TREO HA
				ELSE
				BEGIN
						SET @TongTienThucChayBanSCK = @Sell_Money_VND
						SET @TongTienLaiThucChaySCK = @TongTienThucChayBanSCK - @TongTienThucChayMuaSCK
						--SET @SoLuongThucChay = IIF(@DonGiaTheoDonViTinh= 0, 0 ,@TongTienLaiThucChaySCK/@DonGiaTheoDonViTinh)
						SET @SoLuongThucChay =  @Result
				END

				--THUC HIEN INSERT GIA TRI CHENH LECH BAN MUA CUA GGFB
				EXEC [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLai_ThanhTien_GGFB]
					@NgayThucHien						= @NgayThucHien,
					@ADS_Operating_Result_Map_OrderId  	= @ADS_Operating_Result_Map_OrderId,
					@HopDongREF							= @HopDongID,
					@HopDongChiTietREF					= @HopDongChiTietID,
					@DonGiaTheoDonViTinh				= @DonGiaTheoDonViTinh,
					@DonViTinh							= @UNITS,
					@SoLuongThucChay					= @SoLuongThucChay,
					@TongTienThucChayBanSCK				= @TongTienThucChayBanSCK,
					@TongTienThucChayMuaSCK				= @TongTienThucChayMuaSCK,
					@TongTienLaiThucChaySCK				= @TongTienLaiThucChaySCK,
					@TongTienDuToanMuaSauCK				= @DuToanMua,
					@ghiChu								= @Ghichu_DotChayHopDong

				--2. Update trang thai tinh thuc chay cua ThucChayMuaNgoaiChiTiet 
				UPDATE dbo.[ADS_Operating_Result_Map_Order]
				SET IsCaculatedActual = 1
				WHERE Id = @ADS_Operating_Result_Map_OrderId
			END

		END
		ELSE
			IF(@Is_SanLuongChot = 2)
			BEGIN
				SET @Ghichu_DotChayHopDong =  N'ThanhTien_GGFB_Chot'
				--1. INSERT VAO ThucChayDaTinh
				EXEC [dbo].[ThucChayDaTinh_InsertThucChaySanLuongChot_ThanhTien_GGFB]
						@NgayThucHien						= @NgayThucHien,
						@ADS_Operating_Result_QuantityId	= @ADS_Operating_Result_Map_OrderId,
						@HopDongREF							= @HopDongID,
						@HopDongChiTietREF					= @HopDongChiTietID,
						@ghiChu								= @Ghichu_DotChayHopDong

				--2. INSERT VAO ThucChayDaTinh_MuaNgoai
				IF ( -- nếu tồn tại trên bảng ThucChayDaTinh , thì mới thực hiện tính trên bảng TCDT_MuaNgoai
					 EXISTS(SELECT TOP (1) HopDongID 
							FROM dbo.ThucChayDaTinh 
							WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
								  AND SoLuongDotChayBooking = @ADS_Operating_Result_Map_OrderId 
								  AND NgayThucHien =  @NgayThucHien
							ORDER BY HopDongID
						)
					)
				BEGIN
			

					SET @DonGiaTheoDonViTinh = @Sell_Money_VND/@Result
					SET @UNITS	= dbo.FormatDonViTinh_ThanhTien_GGFB(@UNITS)

					SELECT @FromDate = TC.fromdate, @ToDate = TC.toDate FROM [dbo].[ADS_Operating_Result_Quantity] TC
					WHERE TC.ID = @ADS_Operating_Result_Map_OrderId
					
					SET @FromDate = ISNULL(@FromDate,'1900-01-01')
					SET @ToDate = ISNULL(@ToDate,'1900-01-01')

					--CHO NAY CAN PHAI CHECK LAI DU LIEU THUC TE PHAT SINH : HAIDH ??????????????????
					SET @TongTienThucChayMuaSCK = 
					( 
						 SELECT SUM(RS.Total_Money_VND) --TONG TIEN MUA SAU CHIET KHAU
						  FROM [dbo].[ADS_Operating_Result_Map_Order] MP
						  INNER JOIN [dbo].[ADS_Operating_Result]  RS ON MP.operating_Result_Id = RS.Id
						  WHERE MP.Operating_Order_Id = @Operating_Order_Id
						  AND RS.Date_result BETWEEN @FromDate AND @ToDate
					 )

					--Xac dinh thuc chay ban co lech treo ha ko
					IF(EXISTS(SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
							WHERE hdct.HopDongChiTietID = @HopDongChiTietID
							AND hdct.ChietKhau <> 100 
							ORDER BY hdct.HopDongChiTietID
						))
					BEGIN
						SET @ThanhTienSauTrietKhauThucChay = (SELECT TOP(1) tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi FROM dbo.ThucChayDaTinh tcdt
																WHERE tcdt.HopDongID = @HopDongID
																AND tcdt.HopDongChiTietREF = @HopDongChiTietID
																AND tcdt.SoLuongDotChayBooking = @ADS_Operating_Result_Map_OrderId
																AND tcdt.NgayThucHien = @NgayThucHien
																AND (tcdt.ThanhTienSauTrietKhauThucChay + TCDT.GiaTriThayDoi < @Sell_Money_VND)
																ORDER BY tcdt.CreatedAt desc)
						IF(@ThanhTienSauTrietKhauThucChay IS NOT NULL)
						BEGIN
							SET @TongTienThucChayBanSCK = @ThanhTienSauTrietKhauThucChay
							SET @TongTienLaiThucChaySCK = @TongTienThucChayBanSCK - @TongTienThucChayMuaSCK
							SET @SoLuongThucChay = IIF(@TongTienLaiThucChaySCK <= 0 ,0 ,@TongTienThucChayBanSCK/@DonGiaTheoDonViTinh)
						END
						ELSE
						BEGIN
							SET @TongTienThucChayBanSCK = @Sell_Money_VND
							SET @TongTienLaiThucChaySCK = @TongTienThucChayBanSCK - @TongTienThucChayMuaSCK
							SET @SoLuongThucChay = @Result
						END
				
					END
					--VOI TH LA KHUYEN MAI THI TA KO XET LECH TREO HA
					ELSE
					BEGIN
							SET @TongTienThucChayBanSCK = @Sell_Money_VND
							SET @TongTienLaiThucChaySCK = @TongTienThucChayBanSCK - @TongTienThucChayMuaSCK
							SET @SoLuongThucChay = @Result
					END

					--THUC HIEN INSERT GIA TRI CHENH LECH BAN MUA CUA GGFB
					EXEC [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLai_SanLuongChot_ThanhTien_GGFB]
						@NgayThucHien						= @NgayThucHien,
						@ADS_Operating_Result_Map_OrderId  	= @ADS_Operating_Result_Map_OrderId,
						@HopDongREF							= @HopDongID,
						@HopDongChiTietREF					= @HopDongChiTietID,
						@DonGiaTheoDonViTinh				= @DonGiaTheoDonViTinh,
						@DonViTinh							= @UNITS,
						@SoLuongThucChay					= @SoLuongThucChay,
						@TongTienThucChayBanSCK				= @TongTienThucChayBanSCK,
						@TongTienThucChayMuaSCK				= @TongTienThucChayMuaSCK,
						@TongTienLaiThucChaySCK				= @TongTienLaiThucChaySCK,
						@TongTienDuToanMuaSauCK				= @DuToanMua,
						@ghiChu								= @Ghichu_DotChayHopDong

					--2. Update trang thai tinh thuc chay cua ThucChayMuaNgoaiChiTiet 
					UPDATE dbo.[ADS_Operating_Result_Quantity]
					SET [IsCalc_Result_Quantity] = 1
					WHERE Id = @ADS_Operating_Result_Map_OrderId
				END

			END
		
	FETCH NEXT FROM thanhtien_ggfb_cursor 
	INTO  @ADS_Operating_Result_Map_OrderId , @Operating_Order_Id,@Operating_Result_Id,
		  @HopDongID, @HopDongChiTietID, @Sell_Money_VND, @Result, @UNITS, @DuToanMua, @Is_SanLuongChot
	END
	
	CLOSE thanhtien_ggfb_cursor
	DEALLOCATE thanhtien_ggfb_cursor
    
    SELECT 1
END


```
