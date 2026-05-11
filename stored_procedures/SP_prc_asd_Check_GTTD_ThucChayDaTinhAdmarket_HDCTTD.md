# Stored Procedure: `prc_asd_Check_GTTD_ThucChayDaTinhAdmarket_HDCTTD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-14 10:31:33.937000
- **Ngày sửa cuối**: 2021-06-14 14:43:21.287000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- exec [dbo].prc_asd_Check_GTTD_ThucChayDaTinhAdmarket_HDCTTD @NgayThucHien '2017-09-05'
-- =============================================
/*
	[dbo].[prc_asd_Check_GTTD_ThucChayDaTinhAdmarket_HDCTTD]  @NgayThucHien '2021-03-24'
*/

CREATE PROCEDURE [dbo].[prc_asd_Check_GTTD_ThucChayDaTinhAdmarket_HDCTTD]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	DECLARE @ThucChay_PerformanceBase_ThayDoi_ID INT
			  ,@HopDongID   BIGINT
			  ,@HopDongChitietID   BIGINT
			  ,@DmSanPhamID   INT
			  ,@TK_Admarket   NVARCHAR(100)
			  ,@Thanhtien FLOAT
			  ,@DeletedStatus SMALLINT
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	DECLARE @Table_HopDongChiTiet_Admarket TABLE
	(
		CONTRACT_ID int
		, CONTRACT_DETAIL_ID INT
		, PRODUCT_ID INT
		, TK_ADMARKET NVARCHAR(500)
		, SELL_MONEY_VND FLOAT
		, ISDELETED SMALLINT
	)
	--1. CHECK HOPDONGCHITET THAY DOI THANHTIEN VA BI XOA
	INSERT INTO @Table_HopDongChiTiet_Admarket
	(
		CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, PRODUCT_ID
		, TK_ADMARKET
		, SELL_MONEY_VND 
		, ISDELETED 
	)
	--Check hop dong chi tiet thay doi

	SELECT tc.HopDongFK, tc.HopDongChiTietID
	, tc.DmSanPhamREF
	, tc.tk_Admarket
	, tc.ThanhTien
	, TC.DeletedStatus
	FROM
	(
		SELECT * FROM [dbo].HopDongChiTiet hdct
		WHERE 1=1
		--AND hdct.DeletedStatus <> 1
		AND DmSanPhamREF in (585,628,144)
		AND DmLoaiREF <> 42
		AND convert(date,hdct.LastModifiedAt) = @NgayThucHien
	)TC
	OUTER APPLY
	(SELECT  TOP 1 tcl.HopDongChiTietREF, tcl.ThanhTien
	FROM  [dbo].HopDongChiTietLog TCL WHERE TCL.HopDongChiTietREF = tc.HopDongChiTietID
	AND convert(date,TCL.LastModifiedAt) < convert(date,tc.LastModifiedAt)
	order by tcl.LastModifiedAt desc
	)TCL
	WHERE (((ISNULL(TC.ThanhTien,0) <> ISNULL(TCL.ThanhTien,0))) OR ( tc.DeletedStatus = 1))
	AND TCL.HopDongChiTietREF IS NOT NULL

	DECLARE db_cursor_thaydoi CURSOR FOR  
		SELECT CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, PRODUCT_ID
		, TK_ADMARKET
		, SELL_MONEY_VND 
		, ISDELETED  FROM @Table_HopDongChiTiet_Admarket
	FETCH NEXT FROM db_cursor_thaydoi INTO @HopDongID ,@HopDongChitietID ,@DmSanPhamID,@TK_Admarket 
									,@ThanhTien, @DeletedStatus

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		DECLARE @ThanhTienThucChayDaTinh FLOAT = 0
		DECLARE @GiaTriThayDoi FLOAT = 0

		SET @ThanhTienThucChayDaTinh = ISNULL(
		 (SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
		   FROM ThucChayDaTinhAdmarket tcdt 
		   WHERE tcdt.HopDongID =  @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChitietID
		   AND tcdt.DmSanPhamREF = @DmSanPhamID AND tcdt.NgayThucHien <= @NgayThucHien
		   ),0)
		SET @GiaTriThayDoi = @ThanhTien - @ThanhTienThucChayDaTinh
		--NEU THUC CHAY TINH VUOI GIA TRI HOP DONG
		IF(@GiaTriThayDoi < 0)
		BEGIN
			--PRINT ''
			--3. Sp insert dữ liệu
			DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50)
			, @GhiChu NVARCHAR(max) =''
			, @v_ThucChayDaTinhID_output NVARCHAR(200)
			SET @DmWebsiteREF = 826
			SET @TenWebsite = '(Blanks)'
			SET @GhiChu = N'Update TCDT Admarket do thay doi thanhtien hdct:' + Convert(nvarchar(50),@HopDongChiTietID)

			EXEC [dbo].[prc_asd_Tinh_GTTD_ThucChayDaTinhAdmarket_HDCTTD]
			-- Add the parameters for the stored procedure here
			@NgayThucHien = @NgayThucHien, 
			@ThucChay_PerformanceBase_ThayDoi_ID = 0,
			@HopDongID = @HopDongID,
			@HopDongChiTietID = @HopDongChiTietID, 
			@DmSanPhamREF = @DmSanPhamID, 
			@DmWebsiteREF = @DmWebsiteREF,
			@TenWebsite = @TenWebsite,
			@TongThanhTienThucChayDaTinh = @ThanhTienThucChayDaTinh,
			@GiaTriThayDoi = @GiaTriThayDoi, 
			@GhiChu = @GhiChu,
			@ThucChayDaTinhID_output = @v_ThucChayDaTinhID_output OUTPUT
			
		END

		FETCH NEXT FROM db_cursor_thaydoi INTO @HopDongID ,@HopDongChitietID ,@DmSanPhamID,@TK_Admarket 
									,@ThanhTien, @DeletedStatus
	END   

	CLOSE db_cursor_thaydoi   
	DEALLOCATE db_cursor_thaydoi

END

```
