# Stored Procedure: `ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_ThanhTien_GGFB_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-10-21 09:44:00.980000
- **Ngày sửa cuối**: 2024-10-25 11:56:19.120000

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
--DELETE	FROM dbo.ThucChayDaTinh_MuaNgoai 
--WHERE ThucChayMuaNgoaiChiTietREF = @ADS_Operating_Result_Map_OrderId
--AND HopDongREF = @HopDongID
--AND HopDongChiTietREF = @HopDongChiTietID
--AND (DmSanPhamREF in (306,423,5160,5188)
--	  OR DmViTriREF in (100093,100478,100774) )
--	  AND NgayThucHien = @NgayThucHien


	EXEC [dbo].[ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_ThanhTien_GGFB_dev]'2024-10-24'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_ThanhTien_GGFB_dev]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @CONTRACT_NUMBER NVARCHAR(100)
		, @CONTRACT_ID INT
		, @CONTRACT_DETAIL_ID INT
		, @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID INT
		, @OPERATING_ORDER_ID INT
		, @OPERATING_RESULT_ID INT
		, @ISDELETED SMALLINT
		, @CONTRACT_DETAIL_ID_LOG INT
		, @DATASOURCE NVARCHAR(100)
		, @DATATYPE INT
		, @IS_PROCESSED  SMALLINT
		, @GhiChu_DoiTruThucChay NVARCHAR(500) = N''
		, @Ghichu_TinhLaiThucChay NVARCHAR(500) = N''
		, @GhiChu NVARCHAR(1000) = N''

	DECLARE @Table_ThucChay_ThanhTien_GGFB TABLE
	(
		CONTRACT_ID int
		, CONTRACT_DETAIL_ID INT
		, ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID INT
		, OPERATING_ORDER_ID INT
		, OPERATING_RESULT_ID INT
		, SELL_MONEY_VND FLOAT
		, ISDELETED SMALLINT
		, SELL_MONEY_VND_LOGBF FLOAT
		, CONTRACT_DETAIL_ID_LOG INT
		, DATASOURCE NVARCHAR(100)
		, DATATYPE INT
		, IS_PROCESSED SMALLINT
	)

	INSERT INTO @Table_ThucChay_ThanhTien_GGFB
	(
		CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID 
		, OPERATING_ORDER_ID 
		, OPERATING_RESULT_ID 
		, SELL_MONEY_VND 
		, ISDELETED 
		, SELL_MONEY_VND_LOGBF 
		, CONTRACT_DETAIL_ID_LOG 
		, DATASOURCE 
		, DATATYPE 
		, IS_PROCESSED 
	)
	--chekc hop dong chi tiet thay doi
	SELECT tc.HopDongFK as Contract_Id, tc.HopDongChiTietID
	, 0 AS ADS_Operating_Result_Map_Order_Id
	, 0 as Operating_Order_Id, 0 as operating_Result_Id
	, tc.ThanhTien AS Sell_Money_VND
	, TC.DeletedStatus as  IsDeleted
	, ISNULL(tcl.ThanhTien,0) AS Sell_Money_VND_logbf
	, 0 AS  Contract_Detail_Id_LOG
	,'HopdongChiTiet' AS NGUON
	, (CASE WHEN ISNULL(TC.ThanhTien,0) <> ISNULL(TCL.ThanhTien,0) THEN 0
		ELSE 104
		END) AS TRUONGHOP
	, 0 IS_PROCESSED
	FROM
	(
		SELECT * FROM [dbo].HopDongChiTiet hdct
		WHERE 1=1
		AND hdct.DeletedStatus <> 1
		AND (hdct.DmSanPhamREF in (306,423,5188) OR DmViTriREF in (100093,100478,100774) )
		AND convert(date,hdct.LastModifiedAt) = @NgayThucHien
	)TC

	OUTER APPLY
	(SELECT  TOP 1 tcl.HopDongChiTietREF, tcl.ThanhTien
	FROM  [dbo].HopDongChiTietLog TCL WHERE TCL.HopDongChiTietREF = tc.HopDongChiTietID
	AND convert(date,TCL.LastModifiedAt) < convert(date,tc.LastModifiedAt)
	order by tcl.LastModifiedAt desc
	)TCL
	WHERE (ISNULL(TC.ThanhTien,0) <> ISNULL(TCL.ThanhTien,0))
	AND TCL.HopDongChiTietREF IS NOT NULL

	UNION
	--THONG TIN LOG CUA TABLE [ADS_Operating_Result_Map_Order]
	SELECT OD.Contract_Id, OD.Contract_Detail_Id, tc.Id AS ADS_Operating_Result_Map_Order_Id
	, TC.Operating_Order_Id, TC.operating_Result_Id
	, ISNULL(TC.Sell_Money_VND,0) AS Sell_Money_VND, TC.IsDeleted
	, ISNULL(tcl.Sell_Money_VND,0) AS Sell_Money_VND_logbf
	, OD.Contract_Detail_Id AS  Contract_Detail_Id_LOG
	,'ADS_Operating_Result_Map_Order' AS NGUON
	, (CASE WHEN TC.IsDeleted = 1 THEN 4
		WHEN ISNULL(TC.Sell_Money_VND,0) <> ISNULL(TCL.Sell_Money_VND,0) THEN 6
		ELSE 101
		END) AS TRUONGHOP
	, 0 IS_PROCESSED
	FROM
	(
		SELECT * FROM [dbo].[ADS_Operating_Result_Map_Order] TC
		WHERE 1=1
		AND ISNULL(tc.IsCaculatedActual,0) = 1
		AND (ISNULL(TC.Sell_Money_VND,0) <> 0)
		AND convert(date,TC.LastModificationTime) = @NgayThucHien
		--and tc.Operating_Order_Id = @OrderID
	)TC
	INNER JOIN 
			(SELECT OD.Contract_Id, OD.Contract_Number
					, OD.Contract_Detail_Id, OD.Units, OD.Id , OD.Money_Turnover
				FROM DBO.ADS_Operating_Order OD 
				WHERE 1=1
				AND OD.IsDeleted = 0
			) OD ON TC.Operating_Order_Id = OD.Id
	OUTER APPLY
	(SELECT  TOP 1 TCL.ADS_Operating_Result_Map_Order_Id, TCL.Id, tcl.Operating_Order_Id
	, tcl.Sell_Money_VND, tcl.LastModificationTime, tcl.Log_time 
	FROM  [dbo].[ADS_Operating_Result_Map_Order_Log] TCL WHERE TCL.ADS_Operating_Result_Map_Order_Id = TC.ID 
	AND TCL.LastModificationTime < TC.LastModificationTime
	order by tcl.LastModificationTime desc
	)TCL
	WHERE (TC.IsDeleted = 1 OR ISNULL(TC.Sell_Money_VND,0) <> ISNULL(TCL.Sell_Money_VND,0))
	AND tcl.ADS_Operating_Result_Map_Order_Id is not null

	--THONG TIN LOG CUA TABLE [ADS_Operating_Result_Quantity]
	UNION 
	SELECT OD.Contract_Id, OD.Contract_Detail_Id, tc.Id AS ADS_Operating_Result_Map_Order_Id
	, TC.Operating_Order_Id, 0 AS operating_Result_Id
	, ISNULL(TC.TotalMoney,0) AS Sell_Money_VND, TC.IsDeleted
	, ISNULL(tcl.TotalMoney,0) AS Sell_Money_VND_logbf
	, OD.Contract_Detail_Id AS Contract_Detail_Id_LOG
	,'ADS_Operating_Result_Quantity' AS NGUON
	, (CASE WHEN TC.IsDeleted = 1 THEN 5
		WHEN ISNULL(TC.TotalMoney,0) <> ISNULL(TCL.TotalMoney,0) THEN 7
		ELSE 102
		END) AS TRUONGHOP
	, 0 IS_PROCESSED
	FROM
	(
		SELECT * FROM [dbo].[ADS_Operating_Result_Quantity] TC
		WHERE 1=1
		AND ISNULL(tc.IsCalc_Result_Quantity,0) = 1
		AND (ISNULL(TC.TotalMoney,0) <> 0)
		AND convert(date,TC.LastModificationTime) = @NgayThucHien
		--and tc.Operating_Order_Id = @OrderID
	)TC
	INNER JOIN 
			(SELECT OD.Contract_Id, OD.Contract_Number
					, OD.Contract_Detail_Id, OD.Units, OD.Id , OD.Money_Turnover
				FROM DBO.ADS_Operating_Order OD 
				WHERE 1=1
				AND OD.IsDeleted = 0
			) OD ON TC.Operating_Order_Id = OD.Id
	OUTER APPLY
	(SELECT  TOP 1 TCL.ADS_Operating_Result_Quantity_Id, TCL.Id, tcl.Operating_Order_Id
	, tcl.TotalMoney, tcl.LastModificationTime, tcl.Log_time 
	FROM  [dbo].[ADS_Operating_Result_Quantity_Log] TCL WHERE TCL.ADS_Operating_Result_Quantity_Id = TC.ID 
	AND TCL.LastModificationTime < TC.LastModificationTime
	order by tcl.LastModificationTime desc
	)TCL
	WHERE (TC.IsDeleted = 1 OR ISNULL(TC.TotalMoney,0) <> ISNULL(TCL.TotalMoney,0))
	AND tcl.ADS_Operating_Result_Quantity_Id is not null

	--THONG TIN LOG CUA TABLE Operating_Order
	UNION
	SELECT OD.Contract_Id, OD.Contract_Detail_Id, 0 AS ADS_Operating_Result_Map_Order_Id
	, OD.ID AS Operating_Order_Id, 0 AS operating_Result_Id
	, ISNULL(OD.Money_Turnover,0) AS Sell_Money_VND, OD.IsDeleted
	, ISNULL(tcl.Money_Turnover,0) AS Sell_Money_VND_logbf
	, ISNULL(TCL.Contract_Detail_Id,0) AS Contract_Detail_Id_LOG
	, 'ADS_Operating_Order' AS NGUON
	, (CASE WHEN OD.IsDeleted = 1 THEN 1
		WHEN ISNULL(OD.Contract_Detail_Id,0) <> ISNULL(TCL.Contract_Detail_Id,0) THEN 2
		WHEN ISNULL(OD.Money_Turnover,0) <> ISNULL(TCL.Money_Turnover,0) THEN 3
		ELSE 100
		END) AS TRUONGHOP
	, 0 IS_PROCESSED
	FROM
	(SELECT ISNULL(OD.Contract_Id,0) Contract_Id, OD.Contract_Number, OD.Id AS Operating_Order_Id
			, ISNULL(OD.Contract_Detail_Id,0) Contract_Detail_Id, OD.Units, OD.Id , OD.Money_Turnover
			, OD.LastModificationTime
			, OD.IsDeleted
		FROM DBO.ADS_Operating_Order OD 
		WHERE 1=1
		AND CONVERT(DATE,OD.LastModificationTime) = @NgayThucHien
	)OD 
	OUTER APPLY
	(SELECT  TOP 1 TCL.ADS_Operating_Order_ID
	, tcl.Money_Turnover, tcl.LastModificationTime, tcl.Log_time , ISNULL(tcl.Contract_Detail_Id,0) Contract_Detail_Id
	FROM  [dbo].[ADS_Operating_Order_Log] TCL WHERE TCL.ADS_Operating_Order_ID = OD.Operating_Order_Id
	AND TCL.LastModificationTime < OD.LastModificationTime
	order by tcl.LastModificationTime desc
	)TCL
	WHERE (OD.IsDeleted = 1 OR ISNULL(OD.Money_Turnover,0) <> ISNULL(TCL.Money_Turnover,0) OR ISNULL(OD.Contract_Detail_Id,0) <> ISNULL(TCL.Contract_Detail_Id,0))
	AND TCL.ADS_Operating_Order_ID IS NOT NULL

	/*XAC DINH THU THU TU UU TIEN XL
	--0 THAY DOI THANH TIEN PHAN BO
	--1 ORDER BI XOA
	--2 ORDER BI THAY DOI THONG TIN HOPDONGCHITIET
	--3 ORDER BI THAY DOI NGAN SACH
	--4 ADS_Operating_Result_Map_Order BI XOA NEU KO THUOC ORDER BEN TREN
	--5 [ADS_Operating_Result_Quantity] BI XOA NEU KO THUOC ORDER BEN TREN
	--6 ADS_Operating_Result_Map_Order BI THAY DOI THONG TIN THUC CHAY NEU KO THUOC ORDER BEN TREN
	--7 ADS_Operating_Result_Quantity NEU KO THUOC ORDER BEN TREN
	*/

	--INSERT THONG TIN LOG HAIDH --10-06-2021
	INSERT INTO DBO.Table_ThucChay_ThanhTien_GGFB_log
	SELECT tt.*
	, @NgayThucHien AS NgayThucHien
	, GETDATE() AS CREATEDAT FROM @Table_ThucChay_ThanhTien_GGFB tt
	--	SELECT CONTRACT_ID 
	--	, CONTRACT_DETAIL_ID 
	--	, ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID 
	--	, OPERATING_ORDER_ID 
	--	, OPERATING_RESULT_ID 
	--	, ISDELETED 
	--	, CONTRACT_DETAIL_ID_LOG 
	--	, DATASOURCE 
	--	, DATATYPE 
	--	, IS_PROCESSED  
	--FROM @Table_ThucChay_ThanhTien_GGFB
	--where OPERATING_ORDER_ID = 164
	--ORDER BY DATATYPE ASC, OPERATING_ORDER_ID

	DECLARE R_Cursor_CheckUpdate_ggfb CURSOR FOR 
	
	SELECT CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID 
		, OPERATING_ORDER_ID 
		, OPERATING_RESULT_ID 
		, ISDELETED 
		, CONTRACT_DETAIL_ID_LOG 
		, DATASOURCE 
		, DATATYPE 
		, IS_PROCESSED  
	FROM @Table_ThucChay_ThanhTien_GGFB
	--where OPERATING_ORDER_ID = 164
	--AND ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = 4143
	ORDER BY DATATYPE ASC, OPERATING_ORDER_ID

	OPEN R_Cursor_CheckUpdate_ggfb

	-- Perform the first fetch.
	FETCH NEXT FROM R_Cursor_CheckUpdate_ggfb INTO  @CONTRACT_ID , @CONTRACT_DETAIL_ID 
		, @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID , @OPERATING_ORDER_ID 
		, @OPERATING_RESULT_ID , @ISDELETED , @CONTRACT_DETAIL_ID_LOG , @DATASOURCE 
		, @DATATYPE , @IS_PROCESSED  
			
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @CONTRACT_NUMBER = ISNULL((SELECT TOP (1) hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @CONTRACT_ID ORDER BY hd.HopDongID),'')
		--THUC HIEN DOI TRU TOAN BO ORDER NAY
		SET @GhiChu_DoiTruThucChay = N'TH: ' + CONVERT(NVARCHAR(50),@DATATYPE) + N' ,Doi tru thanhtien_GGFB cho HopDongChietTietID: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) + ' ,OPERATING_ORDER_ID: ' + CONVERT(NVARCHAR(100),@OPERATING_ORDER_ID)
		SET @Ghichu_TinhLaiThucChay = N'TH: ' + CONVERT(NVARCHAR(50),@DATATYPE) + N' ,Tinh lai thanhtien_GGFB cho HopDongChietTietID: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID) + ' ,OPERATING_ORDER_ID: ' + CONVERT(NVARCHAR(100),@OPERATING_ORDER_ID)
		SET @GhiChu = N'TH: ' + CONVERT(NVARCHAR(50),@DATATYPE) + N' ,HopDongChietTietID: ' + CONVERT(NVARCHAR(50),@CONTRACT_DETAIL_ID)

		print @GhiChu

		select @DATATYPE
		select @CONTRACT_ID
		select @CONTRACT_DETAIL_ID
		select @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		select @OPERATING_ORDER_ID
		select @OPERATING_RESULT_ID

		----TH CO THAY DOI THONG TIN THANHTIEN CUA PHAN BO
		--IF(@DATATYPE = 0)
		--BEGIN
		--	--PRINT @DATATYPE
		--	IF(EXISTS(SELECT TOP(1) tcdt.HopDongID FROM ThucChayDaTinh tcdt
		--		WHERE tcdt.HopDongID = @CONTRACT_ID
		--		AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
		--		AND (tcdt.DmSanPhamREF in (306,423,5160,5188)  OR tcdt.DmViTriREF in (100093,100478,100774))
		--		AND tcdt.DmSanPhamREF <> 585 --khac san pham Adx
		--		ORDER BY tcdt.HopDongID
		--		))
		--	BEGIN
		--		--thuc hien doi tru va tinh lai cho hopdongchitiet
		--		IF(NOT EXISTS(SELECT TOP (1) OPERATING_ORDER_ID FROM @Table_ThucChay_ThanhTien_GGFB TC
		--		WHERE (TC.DATATYPE IN (0) AND TC.IS_PROCESSED = 1)
		--		AND TC.CONTRACT_ID = @CONTRACT_ID
		--		AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--		ORDER BY TC.CONTRACT_DETAIL_ID ))
		--		BEGIN
		--			--PRINT 'CHO NAY CAN SUY NGHI THEM'
		--			EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_GGFB_GhiChu] 
		--			@pSoHopDong = @CONTRACT_NUMBER,
		--			@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@pDmSanPhamREF = 0,
		--			@NgayThucHien = @NgayThucHien,
		--			@GhiChu		= @GhiChu

		--			--CAP NHAP IS_PROCESSED = 1 NEU XU LY XONG
		--			UPDATE TC
		--			SET TC.IS_PROCESSED = 1 
		--			FROM @Table_ThucChay_ThanhTien_GGFB TC
		--			WHERE 1=1
		--			AND TC.CONTRACT_ID = @CONTRACT_ID
		--			AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--		END
		--	END
		--END
		--/*TH1 ORDER BI XOA*/
		--ELSE
		--IF(@DATATYPE = 1)
		--BEGIN
		--	--PRINT @DATATYPE
		--	--NEU DA TON TAI PHAT SINH THUC CHAY VOI ORDER
		--	IF(EXISTS(SELECT TOP(1) tcdt.HopDongID FROM ThucChayDaTinh tcdt
		--		WHERE tcdt.HopDongID = @CONTRACT_ID
		--		AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
		--		AND (tcdt.DmSanPhamREF in (306,423,5160,5188)  OR tcdt.DmViTriREF in (100093,100478,100774))
		--		AND tcdt.DmSanPhamREF <> 585 --khac san pham Adx
		--		AND tcdt.DmChienDichREF = @OPERATING_ORDER_ID
		--		ORDER BY tcdt.HopDongID
		--		))
		--	BEGIN
		--		--thuc hien doi tru va tinh lai cho hopdongchitiet
		--		IF(NOT EXISTS(SELECT TOP (1) OPERATING_ORDER_ID FROM @Table_ThucChay_ThanhTien_GGFB TC
		--		WHERE (TC.DATATYPE IN (1) AND TC.IS_PROCESSED = 1)
		--		AND TC.CONTRACT_ID = @CONTRACT_ID
		--		AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--		AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--		ORDER BY TC.OPERATING_ORDER_ID ))
		--		BEGIN
		--			--THUC HIEN DOI TRU THUCCHAYDATINH THEO NGAYTHUCHIEN
		--			EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_ORDER_ThanhTien_GGFB] 
		--			@NgayGhiNhanThucChay = @NgayThucHien,
		--			@HopDongID = @CONTRACT_ID,
		--			@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@Operating_Order_Id = @OPERATING_ORDER_ID,
		--			@GhiChu = @GhiChu_DoiTruThucChay

		--			--THUC HIEN DOI TRU THUCCHAYDATINH_MUANGOAI THEO NGAYTHUCHIEN
		--			EXEC [dbo].[ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_By_ORDER_ThanhTien_GGFB]
		--			@HopDongID = @CONTRACT_ID,
		--			@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@Operating_Order_Id = @OPERATING_ORDER_ID,
		--			@NgayGhiNhanThucChay = @NgayThucHien,
		--			@GhiChu = @GhiChu_DoiTruThucChay
		--			--UPDATE TRANG THAI
		--			UPDATE ADS_Operating_Result_Map_Order
		--			SET IsCaculatedActual = 0
		--			WHERE 1=1
		--			AND Operating_Order_Id = @Operating_Order_Id
		--			AND ISNULL(Sell_Money_VND,0) <> 0
		--			AND ISNULL(IsDeleted,0) = 0
		--			--UPDATE TRANG THAI
		--			UPDATE ADS_Operating_Result_Quantity
		--			SET IsCalc_Result_Quantity = 0
		--			WHERE 1=1
		--			AND Operating_Order_Id = @Operating_Order_Id
		--			AND [Status] = 2 --DA CHOT
		--			AND isnull(IsDeleted,0) = 0
		--			--CAP NHAP IS_PROCESSED = 1 NEU XU LY XONG
		--			UPDATE TC
		--			SET TC.IS_PROCESSED = 1 
		--			FROM @Table_ThucChay_ThanhTien_GGFB TC
		--			WHERE TC.DATATYPE = 1
		--			AND TC.CONTRACT_ID = @CONTRACT_ID
		--			AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--			AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--		END
		--	END
			
		--END

		--/*TH2 ORDER BI THAY DOI THONG TIN HOPDONGCHITIET*/
		--ELSE
		--IF(@DATATYPE = 2)
		--BEGIN
		--	--PRINT @DATATYPE
		--	--NEU KHONG TON TAI IS_PROCESSED = 1 CUA ORDER NAY VOI DATATYPE IN (1,2,3)
		--	IF(NOT EXISTS(SELECT TOP (1) OPERATING_ORDER_ID FROM @Table_ThucChay_ThanhTien_GGFB TC
		--		WHERE (TC.DATATYPE IN (1,2,3) AND TC.IS_PROCESSED = 1)
		--		AND TC.CONTRACT_ID = @CONTRACT_ID
		--		AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--		AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID ORDER BY OPERATING_ORDER_ID ))
		--	BEGIN
		--		--NEU DA TON TAI PHAT SINH THUC CHAY VOI CONTRACT_DETAIL_ID_LOG THI MOI THUC HIEN DOI TRU VA TINH LAI VOI CONTRACT_DETAIL_ID
		--		IF(EXISTS(SELECT TOP(1) tcdt.HopDongID FROM ThucChayDaTinh tcdt
		--		WHERE tcdt.HopDongID = @CONTRACT_ID
		--		AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID_LOG
		--		AND (tcdt.DmSanPhamREF in (306,423,5160,5188)  OR tcdt.DmViTriREF in (100093,100478,100774))
		--		AND tcdt.DmSanPhamREF <> 585 --khac san pham Adx
		--		AND tcdt.DmChienDichREF = @OPERATING_ORDER_ID
		--		ORDER BY tcdt.HopDongID
		--		))
		--		BEGIN
		--			--CHECK NEU CO LECH TREO HA THI THUC HIEN DOI TRU VA TINH LAI TOAN BO
		--			IF NOT(EXISTS(
		--						SELECT TOP(1) tcdt.HopDongChiTietREF FROM dbo.ThucChayDaTinh tcdt
		--									WHERE tcdt.HopDongID = @CONTRACT_ID
		--									AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
		--									AND tcdt.NgayThucHien <= @NgayThucHien
		--									AND (tcdt.ThanhTienLechTreoHa <> 0)
		--									ORDER BY tcdt.CreatedAt desc
		--						)
		--			)
		--			BEGIN
		--				--THUC HIEN DOI TRU THUCCHAYDATINH THEO NGAYTHUCHIEN
		--				EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_ORDER_ThanhTien_GGFB] 
		--				@NgayGhiNhanThucChay = @NgayThucHien,
		--				@HopDongID = @CONTRACT_ID,
		--				@HopDongChiTietID = @CONTRACT_DETAIL_ID_LOG,
		--				@Operating_Order_Id = @OPERATING_ORDER_ID,
		--				@GhiChu = @GhiChu_DoiTruThucChay

		--				--THUC HIEN DOI TRU THUCCHAYDATINH_MUANGOAI THEO NGAYTHUCHIEN
		--				EXEC [dbo].[ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_By_ORDER_ThanhTien_GGFB]
		--				@HopDongID = @CONTRACT_ID,
		--				@HopDongChiTietID = @CONTRACT_DETAIL_ID_LOG,
		--				@Operating_Order_Id = @OPERATING_ORDER_ID,
		--				@NgayGhiNhanThucChay = @NgayThucHien,
		--				@GhiChu = @GhiChu_DoiTruThucChay
					
		--				--UPDATE TRANG THAI
		--				UPDATE ADS_Operating_Result_Map_Order
		--				SET IsCaculatedActual = 0
		--				WHERE 1=1
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND ISNULL(Sell_Money_VND,0) <> 0
		--				AND ISNULL(IsDeleted,0) = 0
		--				--UPDATE TRANG THAI
		--				UPDATE ADS_Operating_Result_Quantity
		--				SET IsCalc_Result_Quantity = 0
		--				WHERE 1=1
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND [Status] = 2 --DA CHOT
		--				AND isnull(IsDeleted,0) = 0

		--				--THUC HIEN TINH LAI VOI CONTRACT_DETAIL_ID
		--				EXEC [dbo].[ThucChay_TinhLai_By_ORDER_ThanhTien_GGFB] 
		--				@pSoHopDong = @CONTRACT_NUMBER,
		--				@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@pOperating_Order_Id = @OPERATING_ORDER_ID,
		--				@NgayThucHien = @NgayThucHien,
		--				@Ghichu_TinhLaiThucChay = @Ghichu_TinhLaiThucChay
		--				--CAP NHAP IS_PROCESSED = 1 NEU XU LY XONG
		--				UPDATE TC
		--				SET TC.IS_PROCESSED = 1 
		--				FROM @Table_ThucChay_ThanhTien_GGFB TC
		--				WHERE 1=1 --TC.DATATYPE = 2
		--				AND TC.CONTRACT_ID = @CONTRACT_ID
		--				AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--				AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--			END
		--			--PHAT SINH LECH TREO HA THI THUC HIEN DOI TRU VA TINH LAI
		--			ELSE
		--			BEGIN
		--				--PRINT ''
		--				--THUC HIEN DOI TRU VA TINH LAI THEO CA HOPDONGCHITIET
		--				EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_GGFB_GhiChu] 
		--				@pSoHopDong = @CONTRACT_NUMBER,
		--				@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@pDmSanPhamREF = 772, --KHONG QUAN TAM DEN THAM SO NAY VI DOI TRU THEO HOPDONGCHITIET
		--				@NgayThucHien = @NgayThucHien,
		--				@GhiChu = @GhiChu

		--				--UPDATE TRANG THAI CHO CA HOPDONGCHITIET
		--				UPDATE TC
		--				SET TC.IS_PROCESSED = 1 
		--				FROM @Table_ThucChay_ThanhTien_GGFB TC
		--				WHERE 1=1 --TC.DATATYPE = 2
		--				AND TC.CONTRACT_ID = @CONTRACT_ID
		--				AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--				--AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--			END
					
		--		END

		--	END
			
		--END

		--/*TH3 ORDER BI THAY DOI NGAN SACH*/
		--ELSE
		--IF(@DATATYPE = 3)
		--BEGIN
		--	--PRINT @DATATYPE
		--	--NEU KHONG TON TAI IS_PROCESSED = 1 CUA ORDER NAY VOI DATATYPE IN (1,2,3)
		--	IF(NOT EXISTS(SELECT TOP (1) OPERATING_ORDER_ID FROM @Table_ThucChay_ThanhTien_GGFB TC
		--		WHERE (TC.DATATYPE IN (1,2,3) AND TC.IS_PROCESSED = 1)
		--		AND TC.CONTRACT_ID = @CONTRACT_ID
		--		AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--		AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID ORDER BY OPERATING_ORDER_ID ))
		--	BEGIN
		--		--NEU DA TON TAI PHAT SINH THUC CHAY VOI CONTRACT_DETAIL_ID THI MOI THUC HIEN DOI TRU VA TINH LAI
		--		IF(EXISTS(SELECT TOP(1) tcdt.HopDongID FROM ThucChayDaTinh tcdt
		--		WHERE tcdt.HopDongID = @CONTRACT_ID
		--		AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
		--		AND (tcdt.DmSanPhamREF in (306,423,5160,5188)  OR tcdt.DmViTriREF in (100093,100478,100774))
		--		AND tcdt.DmSanPhamREF <> 585 --khac san pham Adx
		--		AND tcdt.DmChienDichREF = @OPERATING_ORDER_ID
		--		ORDER BY tcdt.HopDongID
		--		))
		--		BEGIN
		--			--CHECK NEU CO LECH TREO HA THI THUC HIEN DOI TRU VA TINH LAI TOAN BO
		--			IF NOT(EXISTS(
		--						SELECT TOP(1) tcdt.HopDongChiTietREF FROM dbo.ThucChayDaTinh tcdt
		--									WHERE tcdt.HopDongID = @CONTRACT_ID
		--									AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
		--									AND tcdt.NgayThucHien <= @NgayThucHien
		--									AND (tcdt.ThanhTienLechTreoHa <> 0)
		--									ORDER BY tcdt.CreatedAt desc
		--						)
		--			)
		--			BEGIN
		--				--THUC HIEN DOI TRU THUCCHAYDATINH THEO NGAYTHUCHIEN
		--				EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_ORDER_ThanhTien_GGFB] 
		--				@NgayGhiNhanThucChay = @NgayThucHien,
		--				@HopDongID = @CONTRACT_ID,
		--				@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@Operating_Order_Id = @OPERATING_ORDER_ID,
		--				@GhiChu = @GhiChu_DoiTruThucChay

		--				--THUC HIEN DOI TRU THUCCHAYDATINH_MUANGOAI THEO NGAYTHUCHIEN
		--				EXEC [dbo].[ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_By_ORDER_ThanhTien_GGFB]
		--				@HopDongID = @CONTRACT_ID,
		--				@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@Operating_Order_Id = @OPERATING_ORDER_ID,
		--				@NgayGhiNhanThucChay = @NgayThucHien,
		--				@GhiChu = @GhiChu_DoiTruThucChay
					
		--					--UPDATE TRANG THAI
		--				UPDATE ADS_Operating_Result_Map_Order
		--				SET IsCaculatedActual = 0
		--				WHERE 1=1
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND ISNULL(Sell_Money_VND,0) <> 0
		--				AND ISNULL(IsDeleted,0) = 0
		--				--UPDATE TRANG THAI
		--				UPDATE ADS_Operating_Result_Quantity
		--				SET IsCalc_Result_Quantity = 0
		--				WHERE 1=1
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND [Status] = 2 --DA CHOT
		--				AND isnull(IsDeleted,0) = 0

		--				--THUC HIEN TINH LAI VOI CONTRACT_DETAIL_ID
		--				EXEC [dbo].[ThucChay_TinhLai_By_ORDER_ThanhTien_GGFB] 
		--				@pSoHopDong = @CONTRACT_NUMBER,
		--				@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@pOperating_Order_Id = @OPERATING_ORDER_ID,
		--				@NgayThucHien = @NgayThucHien,
		--				@Ghichu_TinhLaiThucChay = @Ghichu_TinhLaiThucChay
		--				--CAP NHAP IS_PROCESSED = 1 NEU XU LY XONG
		--				UPDATE TC
		--				SET TC.IS_PROCESSED = 1 
		--				FROM @Table_ThucChay_ThanhTien_GGFB TC
		--				WHERE 1=1 --TC.DATATYPE = 3
		--				AND TC.CONTRACT_ID = @CONTRACT_ID
		--				AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--				AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--			END
		--			ELSE
		--			BEGIN
		--				--THUC HIEN DOI TRU VA TINH LAI THEO CA HOPDONGCHITIET
		--				EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_GGFB_GhiChu] 
		--				@pSoHopDong = @CONTRACT_NUMBER,
		--				@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@pDmSanPhamREF = 772, --KHONG QUAN TAM DEN THAM SO NAY VI DOI TRU THEO HOPDONGCHITIET
		--				@NgayThucHien = @NgayThucHien,
		--				@GhiChu = @GhiChu

		--				--UPDATE TRANG THAI CHO CA HOPDONGCHITIET
		--				UPDATE TC
		--				SET TC.IS_PROCESSED = 1 
		--				FROM @Table_ThucChay_ThanhTien_GGFB TC
		--				WHERE 1=1 --TC.DATATYPE = 2
		--				AND TC.CONTRACT_ID = @CONTRACT_ID
		--				AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--				--AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--			END
					
		--		END
		--		--CAP NHAP IS_PROCESSED = 1 NEU XU LY XONG
		--	END
			
		--END

		--/*TH4 OR TH5 ADS_Operating_Result_Map_Order/[ADS_Operating_Result_Quantity] BI XOA NEU KO THUOC ORDER BEN TREN*/
		--ELSE
		--IF(@DATATYPE = 4 OR @DATATYPE = 5)
		--BEGIN
		--	--PRINT @DATATYPE
		--	--NEU KHONG TON TAI IS_PROCESSED =1 CỦA ORDER NAY VOI DATATYPE IN (1,2,3,4,5)
		--	IF(NOT EXISTS(SELECT TOP (1) OPERATING_ORDER_ID FROM @Table_ThucChay_ThanhTien_GGFB TC
		--		WHERE (TC.DATATYPE IN (1,2,3,4,5) AND TC.IS_PROCESSED = 1)
		--		AND TC.CONTRACT_ID = @CONTRACT_ID
		--		AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--		AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--		AND TC.ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID  
		--		ORDER BY OPERATING_ORDER_ID ))
		--	BEGIN
		--		--HAIDH COMMENT 01/03/2021
		--		--NEU DA CO LECH TREO HA -> THI THUC HIEN DOI TRU VA TINH LAI TOAN BO
		--		--NEU LECH TREO HA VOI
		--		IF (EXISTS(
		--						SELECT TOP(1) tcdt.HopDongChiTietREF FROM dbo.ThucChayDaTinh tcdt
		--														WHERE tcdt.HopDongID = @CONTRACT_ID
		--														AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
		--														--AND tcdt.DmChienDichREF = @OPERATING_ORDER_ID
		--														AND tcdt.NgayThucHien <= @NgayThucHien
		--														AND (tcdt.ThanhTienLechTreoHa <> 0)
		--														ORDER BY tcdt.CreatedAt desc
		--						)
		--		)
		--		BEGIN
		--			--PRINT THUC HIEN XU LY VOI LEHC TREO HA
		--			EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_GGFB] 
		--			@pSoHopDong = @CONTRACT_NUMBER,
		--			@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@pDmSanPhamREF = 0,
		--			@NgayThucHien = @NgayThucHien
		--		END
		--		ELSE
		--		BEGIN
		--			--NEU KHONG CO LECH TREO HA THI THOI
		--			--NEU KO TON TAI PHAT SINH LECH TREO HA THI DOI TRU VA TINH LUON VOI @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--			--THUC HIEN DOI TRU VOI ADS_Operating_Result_Map_Order_ID/ADS_Operating_Result_Quantity_ID NAY
		--			SET @GhiChu_DoiTruThucChay = @GhiChu_DoiTruThucChay + ', id=' + CONVERT(NVARCHAR(100),@ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID)
		--			EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_RESULT_ThanhTien_GGFB] 
		--			@NgayGhiNhanThucChay = @NgayThucHien,
		--			@HopDongID = @CONTRACT_ID,
		--			@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@Operating_Order_Id = @OPERATING_ORDER_ID,
		--			@ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID,
		--			@GhiChu = @GhiChu_DoiTruThucChay
		--			--
		--			EXEC [dbo].[ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_By_RESULT_ThanhTien_GGFB]
		--			@HopDongID = @CONTRACT_ID,
		--			@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@Operating_Order_Id = @OPERATING_ORDER_ID,
		--			@ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID,
		--			@NgayGhiNhanThucChay = @NgayThucHien,
		--			@GhiChu = @GhiChu_DoiTruThucChay
		--		END
				

		--		--CAP NHAP IS_PROCESSED =1 NEU XU LY XONG
		--		UPDATE TC
		--		SET TC.IS_PROCESSED = 1 
		--		FROM @Table_ThucChay_ThanhTien_GGFB TC
		--		WHERE (TC.DATATYPE = 4 OR TC.DATATYPE = 5)
		--		AND TC.CONTRACT_ID = @CONTRACT_ID
		--		AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--		AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--		AND TC.ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--	END

		--END

		--/*TH6 OR TH7 ADS_Operating_Result_Map_Order/ADS_Operating_Result_Quantity BI THAY DOI THONG TIN THUC CHAY NEU KO THUOC ORDER BEN TREN*/
		--ELSE
		--IF(@DATATYPE IN (6,7))
		--BEGIN
		--	--PRINT @DATATYPE
		--	--NEU KHONG TON TAI IS_PROCESSED = 1 CỦA ORDER NAY VOI DATATYPE IN (1,2,3)
		--	IF(NOT EXISTS(SELECT TOP (1) OPERATING_ORDER_ID FROM @Table_ThucChay_ThanhTien_GGFB TC
		--		WHERE (TC.DATATYPE IN (1,2,3,4,5,6,7) AND TC.IS_PROCESSED = 1)
		--		AND TC.CONTRACT_ID = @CONTRACT_ID
		--		AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--		AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID 
		--		AND TC.ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--		ORDER BY OPERATING_ORDER_ID ))
		--	BEGIN

		--		--NEU KO TON TAI PHAT SINH LECH TREO HA THI DOI TRU VA TINH LUON VOI @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--		--NEU LECH TREO HA VOI
		--		IF NOT(EXISTS(
		--						SELECT TOP(1) tcdt.HopDongChiTietREF FROM dbo.ThucChayDaTinh tcdt
		--														WHERE tcdt.HopDongID = @CONTRACT_ID
		--														AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
		--														--AND tcdt.DmChienDichREF = @OPERATING_ORDER_ID
		--														AND tcdt.NgayThucHien <= @NgayThucHien
		--														AND (tcdt.ThanhTienLechTreoHa <> 0)
		--														ORDER BY tcdt.CreatedAt desc
		--						)
		--			)
		--		BEGIN
		--			--THUC HIEN DOI TRU VA TINH LẠI VOI ADS_Operating_Result_Map_Order_ID/ADS_Operating_Result_Quantity_ID NÀY
		--			SET @GhiChu_DoiTruThucChay = @GhiChu_DoiTruThucChay +  ', id=' + CONVERT(NVARCHAR(100),@ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID)
		--			SET @Ghichu_TinhLaiThucChay = @Ghichu_TinhLaiThucChay +  ', id=' + CONVERT(NVARCHAR(100),@ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID)

		--			EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_RESULT_ThanhTien_GGFB] 
		--			@NgayGhiNhanThucChay = @NgayThucHien,
		--			@HopDongID = @CONTRACT_ID,
		--			@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@Operating_Order_Id = @OPERATING_ORDER_ID,
		--			@ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID,
		--			@GhiChu = @GhiChu_DoiTruThucChay
				
		--			--
		--			EXEC [dbo].[ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_By_RESULT_ThanhTien_GGFB]
		--			@HopDongID = @CONTRACT_ID,
		--			@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@Operating_Order_Id = @OPERATING_ORDER_ID,
		--			@ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID,
		--			@NgayGhiNhanThucChay = @NgayThucHien,
		--			@GhiChu = @GhiChu_DoiTruThucChay

		--			IF(@DATATYPE = 4)
		--			BEGIN
		--				UPDATE ADS_Operating_Result_Map_Order
		--				SET IsCaculatedActual = 0
		--				WHERE Id = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND ISNULL(Sell_Money_VND,0) <> 0
		--				AND ISNULL(IsDeleted,0) = 0
		--			END
		--			IF(@DATATYPE = 5)
		--			BEGIN
		--				--UPDATE TRANG THAI
		--				UPDATE ADS_Operating_Result_Quantity
		--				SET IsCalc_Result_Quantity = 0
		--				WHERE Id = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND [Status] = 2 --DA CHOT
		--				AND isnull(IsDeleted,0) = 0
		--			END
		--			--UPDATE TRANG THAI
		--			IF(@DATATYPE = 6)
		--			BEGIN
		--				UPDATE ADS_Operating_Result_Map_Order
		--				SET IsCaculatedActual = 0
		--				WHERE Id = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND ISNULL(Sell_Money_VND,0) <> 0
		--				AND ISNULL(IsDeleted,0) = 0
		--			END
		--			IF(@DATATYPE = 7)
		--			BEGIN
		--				--UPDATE TRANG THAI
		--				UPDATE ADS_Operating_Result_Quantity
		--				SET IsCalc_Result_Quantity = 0
		--				WHERE Id = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND [Status] = 2 --DA CHOT
		--				AND isnull(IsDeleted,0) = 0
		--			END
		--			--TINH LAI
		--			EXEC [dbo].[ThucChay_TinhLai_By_RESULT_ThanhTien_GGFB] 
		--			@pSoHopDong = @CONTRACT_NUMBER,
		--			@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--			@pOperating_Order_Id = @OPERATING_ORDER_ID,
		--			@ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID,
		--			@NgayThucHien = @NgayThucHien,
		--			@Ghichu_TinhLaiThucChay = @Ghichu_TinhLaiThucChay
		--			--CAP NHAP IS_PRCESSED = 1 NEU XU LY XONG
		--			UPDATE TC
		--			SET TC.IS_PROCESSED = 1 
		--			FROM @Table_ThucChay_ThanhTien_GGFB TC
		--			WHERE (TC.DATATYPE = 6 OR TC.DATATYPE = 7)
		--			AND TC.CONTRACT_ID = @CONTRACT_ID
		--			AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--			AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--			AND TC.ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID = @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID
		--		END
		--		--THUC HIEN TINH LAI CHO CA ORDER
		--		ELSE
		--		BEGIN
		--			--NEU TON TAI > 1 OPERATING_ORDER_ID TREN CONTRACT_DETAIL_ID
		--			IF EXISTS(
		--						SELECT HopDongChiTietREF, COUNT(DMCHIENDICHREF) SL FROM
		--							(
		--								SELECT DISTINCT tcdt.HopDongChiTietREF, DmChienDichREF 
		--									FROM dbo.ThucChayDaTinh tcdt
		--									WHERE tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID 
		--									AND tcdt.NgayThucHien <= @NgayThucHien
		--							)TCDT
		--							GROUP BY tcdt.HopDongChiTietREF HAVING COUNT(DmChienDichREF) >1
		--						)
		--			BEGIN
		--				--THUC HIEN DOI TRU VA TINH LAI THEO CA HOPDONGCHITIET
		--				EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_GGFB] 
		--				@pSoHopDong = @CONTRACT_NUMBER,
		--				@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@pDmSanPhamREF = 772, --KHONG QUAN TAM DEN THAM SO NAY VI DOI TRU THEO HOPDONGCHITIET
		--				@NgayThucHien = @NgayThucHien

		--				--UPDATE TRANG THAI CHO CA HOPDONGCHITIET
		--				--CAP NHAP IS_PRCESSED = 1 NEU XU LY XONG
		--				UPDATE TC
		--				SET TC.IS_PROCESSED = 1 
		--				FROM @Table_ThucChay_ThanhTien_GGFB TC
		--				WHERE (TC.DATATYPE = 6 OR TC.DATATYPE = 7)
		--				AND TC.CONTRACT_ID = @CONTRACT_ID
		--				AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--				--AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--			END
		--			ELSE
		--			BEGIN
		--				PRINT 'TINH LAI CHO CA ORDER'
		--				--THUC HIEN DOI TRU THUCCHAYDATINH THEO NGAYTHUCHIEN
		--				EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_ORDER_ThanhTien_GGFB] 
		--				@NgayGhiNhanThucChay = @NgayThucHien,
		--				@HopDongID = @CONTRACT_ID,
		--				@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@Operating_Order_Id = @OPERATING_ORDER_ID,
		--				@GhiChu = @GhiChu_DoiTruThucChay

		--				--THUC HIEN DOI TRU THUCCHAYDATINH_MUANGOAI THEO NGAYTHUCHIEN
		--				EXEC [dbo].[ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_By_ORDER_ThanhTien_GGFB]
		--				@HopDongID = @CONTRACT_ID,
		--				@HopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@Operating_Order_Id = @OPERATING_ORDER_ID,
		--				@NgayGhiNhanThucChay = @NgayThucHien,
		--				@GhiChu = @GhiChu_DoiTruThucChay
					
		--					--UPDATE TRANG THAI
		--				UPDATE ADS_Operating_Result_Map_Order
		--				SET IsCaculatedActual = 0
		--				WHERE 1=1
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND ISNULL(Sell_Money_VND,0) <> 0
		--				AND ISNULL(IsDeleted,0) = 0
		--				--UPDATE TRANG THAI
		--				UPDATE ADS_Operating_Result_Quantity
		--				SET IsCalc_Result_Quantity = 0
		--				WHERE 1=1
		--				AND Operating_Order_Id = @Operating_Order_Id
		--				AND [Status] = 2 --DA CHOT
		--				AND isnull(IsDeleted,0) = 0

		--				--THUC HIEN TINH LAI VOI CONTRACT_DETAIL_ID
		--				EXEC [dbo].[ThucChay_TinhLai_By_ORDER_ThanhTien_GGFB] 
		--				@pSoHopDong = @CONTRACT_NUMBER,
		--				@pHopDongChiTietID = @CONTRACT_DETAIL_ID,
		--				@pOperating_Order_Id = @OPERATING_ORDER_ID,
		--				@NgayThucHien = @NgayThucHien,
		--				@Ghichu_TinhLaiThucChay = @Ghichu_TinhLaiThucChay

		--				--CAP NHAP IS_PRCESSED = 1 NEU XU LY XONG
		--				UPDATE TC
		--				SET TC.IS_PROCESSED = 1 
		--				FROM @Table_ThucChay_ThanhTien_GGFB TC
		--				WHERE (TC.DATATYPE = 6 OR TC.DATATYPE = 7)
		--				AND TC.CONTRACT_ID = @CONTRACT_ID
		--				AND TC.CONTRACT_DETAIL_ID = @CONTRACT_DETAIL_ID
		--				AND TC.OPERATING_ORDER_ID = @OPERATING_ORDER_ID
		--			END
		--		END

		--	END 
			
		--END

		FETCH NEXT FROM R_Cursor_CheckUpdate_ggfb INTO  @CONTRACT_ID , @CONTRACT_DETAIL_ID 
		, @ADS_OPERATING_RESULT_MAP_ORDER_OR_QUANTITY_ID , @OPERATING_ORDER_ID 
		, @OPERATING_RESULT_ID , @ISDELETED , @CONTRACT_DETAIL_ID_LOG , @DATASOURCE 
		, @DATATYPE , @IS_PROCESSED  
	END

	CLOSE R_Cursor_CheckUpdate_ggfb
	DEALLOCATE R_Cursor_CheckUpdate_ggfb
END

```
